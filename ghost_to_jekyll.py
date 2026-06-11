#!/usr/bin/env python3
"""
ghost_to_jekyll.py
==================

Export an entire Ghost blog (posts, pages, tags, authors and images) through the
Ghost **Admin API** and turn it into a GitHub-Pages-ready **Jekyll** site.

What it produces
----------------
    _posts/YYYY-MM-DD-<slug>.md      published posts (Markdown + YAML front matter)
    _drafts/<slug>.md                draft posts
    _pages/<slug>.md                 static pages (with permalink)
    assets/images/...                every image referenced by the content,
                                     downloaded locally and re-linked
    _data/authors.yml                author metadata
    _data/tags.yml                   tag metadata

Authentication
--------------
Reads two values, from the environment or a local ``.env`` file:

    GHOST_API_URL          e.g. https://your-blog.com   (no trailing /ghost)
    GHOST_ADMIN_API_KEY    the Admin API key in the form  <id>:<hex-secret>

Get the key from Ghost Admin -> Settings -> Integrations -> Add custom
integration -> copy the "Admin API Key".

Usage
-----
    pip install -r requirements.txt
    # put credentials in .env (see .env.example), then:
    python ghost_to_jekyll.py
    # or override the output dir:
    python ghost_to_jekyll.py --output .  --version v5.0

Run with --dry-run to fetch and report counts without writing files.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path
from typing import Any, Iterable

try:
    import jwt
    import requests
    import yaml
    from markdownify import markdownify as md
except ImportError as exc:  # pragma: no cover
    sys.exit(
        f"Missing dependency: {exc.name}. Run:  pip install -r requirements.txt"
    )

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass  # .env support is optional


# --------------------------------------------------------------------------- #
# Ghost Admin API client
# --------------------------------------------------------------------------- #
class GhostAdminClient:
    """Minimal Ghost Admin API client with JWT auth and pagination."""

    def __init__(self, base_url: str, admin_key: str, api_version: str = "v5.0"):
        self.base_url = base_url.rstrip("/")
        self.api_version = api_version
        if ":" not in admin_key:
            sys.exit("GHOST_ADMIN_API_KEY must look like '<id>:<hex-secret>'.")
        self.key_id, self.secret = admin_key.split(":", 1)
        self.session = requests.Session()

    def _token(self) -> str:
        iat = int(dt.datetime.now(dt.timezone.utc).timestamp())
        return jwt.encode(
            {"iat": iat, "exp": iat + 5 * 60, "aud": "/admin/"},
            bytes.fromhex(self.secret),
            algorithm="HS256",
            headers={"alg": "HS256", "typ": "JWT", "kid": self.key_id},
        )

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Ghost {self._token()}",
            "Accept-Version": self.api_version,
        }

    def fetch_all(self, resource: str, **params: Any) -> list[dict]:
        """Fetch every page of a paginated Admin API resource."""
        url = f"{self.base_url}/ghost/api/admin/{resource}/"
        out: list[dict] = []
        page = 1
        while True:
            q = {"page": page, "limit": 100, **params}
            resp = self.session.get(url, headers=self._headers(), params=q, timeout=60)
            if resp.status_code != 200:
                sys.exit(
                    f"Ghost API error {resp.status_code} on {resource} "
                    f"page {page}: {resp.text[:300]}"
                )
            data = resp.json()
            out.extend(data.get(resource, []))
            pagination = data.get("meta", {}).get("pagination", {})
            if not pagination or page >= (pagination.get("pages") or 1):
                break
            page += 1
        return out


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def parse_ghost_date(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    # Ghost returns ISO 8601 with milliseconds + Z, e.g. 2023-01-15T10:30:00.000Z
    cleaned = value.replace("Z", "+00:00")
    try:
        return dt.datetime.fromisoformat(cleaned)
    except ValueError:
        return None


def front_matter(data: dict) -> str:
    """Serialise a dict to a YAML front-matter block."""
    # Drop empty values so the front matter stays tidy.
    clean = {k: v for k, v in data.items() if v not in (None, "", [], {})}
    body = yaml.safe_dump(clean, allow_unicode=True, sort_keys=False, default_flow_style=False)
    return f"---\n{body}---\n\n"


# --------------------------------------------------------------------------- #
# Image handling
# --------------------------------------------------------------------------- #
class ImageDownloader:
    """Downloads Ghost content images and maps remote URLs -> local Jekyll paths."""

    def __init__(self, site_url: str, assets_dir: Path, client: GhostAdminClient):
        self.site_url = site_url.rstrip("/")
        self.assets_dir = assets_dir
        self.client = client
        self.map: dict[str, str] = {}  # remote url -> /assets/images/...
        # Match absolute (this site) or root-relative /content/images/... URLs.
        self.pattern = re.compile(
            r'(?:' + re.escape(self.site_url) + r')?/content/images/[^\s"\'\)\]]+'
        )

    def _local_for(self, url: str) -> tuple[str, Path]:
        rel = url.split("/content/images/", 1)[1]
        web_path = f"/assets/images/{rel}"
        disk_path = self.assets_dir / rel
        return web_path, disk_path

    def _download(self, url: str, disk_path: Path) -> bool:
        if disk_path.exists() and disk_path.stat().st_size > 0:
            return True
        abs_url = url if url.startswith("http") else f"{self.site_url}{url}"
        try:
            resp = requests.get(abs_url, timeout=120)
            if resp.status_code in (401, 403):
                # Private site? retry with admin auth.
                resp = requests.get(abs_url, headers=self.client._headers(), timeout=120)
            resp.raise_for_status()
        except requests.RequestException as exc:
            print(f"  ! failed to download {abs_url}: {exc}", file=sys.stderr)
            return False
        disk_path.parent.mkdir(parents=True, exist_ok=True)
        disk_path.write_bytes(resp.content)
        return True

    def harvest(self, *texts: str | None) -> None:
        """Find every content-image URL in the given strings and download it."""
        for text in texts:
            if not text:
                continue
            for url in self.pattern.findall(text):
                if url in self.map:
                    continue
                web_path, disk_path = self._local_for(url)
                if self._download(url, disk_path):
                    self.map[url] = web_path

    def rewrite(self, text: str | None) -> str | None:
        """Replace remote image URLs with their local paths."""
        if not text:
            return text
        # Replace longest URLs first to avoid partial overlaps.
        for url in sorted(self.map, key=len, reverse=True):
            text = text.replace(url, self.map[url])
        return text


# --------------------------------------------------------------------------- #
# Conversion
# --------------------------------------------------------------------------- #
def html_to_markdown(html: str | None) -> str:
    if not html:
        return ""
    return md(html, heading_style="ATX", bullets="-", strip=["script", "style"]).strip()


def build_document(item: dict, kind: str, images: ImageDownloader) -> tuple[str, str]:
    """Return (relative_path, file_contents) for a post or page."""
    published = parse_ghost_date(item.get("published_at"))
    created = parse_ghost_date(item.get("created_at"))
    updated = parse_ghost_date(item.get("updated_at"))
    date = published or created or updated
    slug = item.get("slug") or "untitled"

    tags = [t["name"] for t in item.get("tags", []) if not t.get("name", "").startswith("#")]
    authors = [a["name"] for a in item.get("authors", [])]
    primary_author = (item.get("primary_author") or {}).get("name")
    primary_tag = (item.get("primary_tag") or {}).get("name")

    fm: dict[str, Any] = {
        "layout": "page" if kind == "page" else "post",
        "title": item.get("title"),
        "slug": slug,
        "status": item.get("status"),
    }
    if date:
        fm["date"] = date.strftime("%Y-%m-%d %H:%M:%S %z") or date.strftime("%Y-%m-%d %H:%M:%S")
    if kind == "page":
        fm["permalink"] = f"/{slug}/"
    if kind == "post":
        fm["tags"] = tags
        if primary_tag:
            fm["category"] = primary_tag
    fm["author"] = primary_author or (authors[0] if authors else None)
    fm["authors"] = authors if len(authors) > 1 else None
    fm["excerpt"] = item.get("custom_excerpt") or item.get("excerpt")
    fm["feature_image"] = images.rewrite(item.get("feature_image"))
    fm["feature_image_alt"] = item.get("feature_image_alt")
    fm["featured"] = item.get("featured") or None
    fm["ghost_id"] = item.get("id")
    fm["ghost_url"] = item.get("url")

    body = images.rewrite(html_to_markdown(item.get("html"))) or ""
    # Migrated content often contains {{ ... }} and {% ... %} (e.g. Home
    # Assistant / Jinja2 / Ansible snippets) that are identical to Jekyll's
    # Liquid syntax. Without this, Jekyll tries to *execute* them and the build
    # fails ("Unknown tag", "Expected end_of_string"). Wrapping the body in raw
    # tells Liquid to leave it alone; Markdown still renders normally.
    if body.strip():
        body = "{% raw %}\n" + body + "\n{% endraw %}"
    contents = front_matter(fm) + body

    if kind == "page":
        rel = f"_pages/{slug}.md"
    elif item.get("status") == "published" and date:
        rel = f"_posts/{date.strftime('%Y-%m-%d')}-{slug}.md"
    else:
        rel = f"_drafts/{slug}.md"
    return rel, contents


def write_data_files(out: Path, tags: list[dict], authors: list[dict]) -> None:
    data_dir = out / "_data"
    data_dir.mkdir(parents=True, exist_ok=True)
    tag_data = [
        {
            "name": t.get("name"),
            "slug": t.get("slug"),
            "description": t.get("description"),
            "feature_image": t.get("feature_image"),
        }
        for t in tags
        if not (t.get("name") or "").startswith("#")
    ]
    author_data = [
        {
            "name": a.get("name"),
            "slug": a.get("slug"),
            "bio": a.get("bio"),
            "profile_image": a.get("profile_image"),
            "website": a.get("website"),
            "twitter": a.get("twitter"),
        }
        for a in authors
    ]
    (data_dir / "tags.yml").write_text(
        yaml.safe_dump(tag_data, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    (data_dir / "authors.yml").write_text(
        yaml.safe_dump(author_data, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a Ghost blog to a Jekyll site.")
    parser.add_argument("--output", default=".", help="Output directory (default: current).")
    parser.add_argument("--version", default="v5.0", help="Ghost Accept-Version header.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch only; write nothing.")
    args = parser.parse_args()

    site_url = os.environ.get("GHOST_API_URL", "").strip()
    admin_key = os.environ.get("GHOST_ADMIN_API_KEY", "").strip()
    if not site_url or not admin_key:
        sys.exit(
            "Set GHOST_API_URL and GHOST_ADMIN_API_KEY (env vars or .env file). "
            "See .env.example."
        )

    out = Path(args.output).resolve()
    assets_dir = out / "assets" / "images"

    client = GhostAdminClient(site_url, admin_key, args.version)

    print(f"Connecting to {site_url} ...")
    posts = client.fetch_all("posts", formats="html", include="tags,authors")
    pages = client.fetch_all("pages", formats="html", include="tags,authors")
    tags = client.fetch_all("tags")
    authors = client.fetch_all("users")
    print(
        f"Fetched {len(posts)} posts, {len(pages)} pages, "
        f"{len(tags)} tags, {len(authors)} authors."
    )

    if args.dry_run:
        print("Dry run complete — no files written.")
        return

    images = ImageDownloader(site_url, assets_dir, client)

    print("Downloading images ...")
    for item in (*posts, *pages):
        images.harvest(item.get("html"), item.get("feature_image"))
    images.harvest(*(t.get("feature_image") for t in tags))
    images.harvest(*(a.get("profile_image") for a in authors))
    print(f"Downloaded {len(images.map)} images into {assets_dir}.")

    written = 0
    for item in posts:
        rel, contents = build_document(item, "post", images)
        path = out / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents, encoding="utf-8")
        written += 1
    for item in pages:
        rel, contents = build_document(item, "page", images)
        path = out / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents, encoding="utf-8")
        written += 1

    write_data_files(out, tags, authors)

    print(f"Wrote {written} content files to {out}.")
    print("Done. Review the output, then commit & push to GitHub.")


if __name__ == "__main__":
    main()
