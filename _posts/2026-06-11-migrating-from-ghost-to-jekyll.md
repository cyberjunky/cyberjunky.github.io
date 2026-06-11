---
layout: post
title: "Migrating a Ghost blog to Jekyll on GitHub Pages"
slug: migrating-from-ghost-to-jekyll
date: 2026-06-11 12:00:00 +0000
tags:
  - jekyll
  - ghost
  - github-pages
  - python
category: meta
author: Ron
excerpt: "A small Python toolkit that exports a whole Ghost blog through the Admin API and turns it into a static Jekyll site that GitHub Pages builds and serves for free. Code included as a download."
---

I moved this blog off [Ghost](https://ghost.org/) and onto a plain
[Jekyll](https://jekyllrb.com/) site hosted on GitHub Pages. No server to keep
running, no database, no monthly bill — just Markdown files and images in a git
repo that GitHub builds automatically.

To do it cleanly I wrote a small Python script that talks to the **Ghost Admin
API** and writes out a ready-to-publish Jekyll site: posts, pages, tags,
authors, and every image, all re-linked locally.

**Grab the whole toolkit here:**
👉 [**ghost-to-jekyll-toolkit.zip**]({{ "/assets/downloads/ghost-to-jekyll-toolkit.zip" | relative_url }})

The zip contains the converter (`ghost_to_jekyll.py`), a Jekyll scaffold
(`_config.yml`, `Gemfile`, `index.html`), a GitHub Actions deploy workflow, and
a `README.md`.

## What it produces

```text
_posts/YYYY-MM-DD-<slug>.md   published posts (Markdown + YAML front matter)
_drafts/<slug>.md             draft posts
_pages/<slug>.md              static pages
assets/images/...             every image, downloaded and re-linked locally
_data/authors.yml             author metadata
_data/tags.yml                tag metadata
```

## How it works

Ghost's Admin API uses a short-lived JWT signed from your `id:secret` API key.
The script builds that token, pages through every resource, converts each post's
HTML to Markdown, and downloads every `/content/images/...` URL it finds:

```python
def _token(self) -> str:
    iat = int(dt.datetime.now(dt.timezone.utc).timestamp())
    return jwt.encode(
        {"iat": iat, "exp": iat + 5 * 60, "aud": "/admin/"},
        bytes.fromhex(self.secret),
        algorithm="HS256",
        headers={"alg": "HS256", "typ": "JWT", "kid": self.key_id},
    )
```

Credentials are read from a git-ignored `.env`, so your API key never lands in
the repo.

## Step-by-step

### 1. Get a Ghost Admin API key

In Ghost Admin: **Settings → Integrations → Add custom integration**. Copy the
**Admin API Key** (format `<id>:<hex-secret>`).

### 2. Configure and run

```bash
cp .env.example .env          # then set GHOST_API_URL and GHOST_ADMIN_API_KEY
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python ghost_to_jekyll.py --dry-run   # confirm the connection, see counts
python ghost_to_jekyll.py             # do the real conversion
```

### 3. Preview locally

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000
```

### 4. Push and publish

```bash
git init && git branch -M main
git add . && git commit -m "Migrate blog from Ghost to Jekyll"
git remote add origin https://github.com/<you>/<you>.github.io.git
git push -u origin main
```

Then in the repo: **Settings → Pages → Source → GitHub Actions**. Every push to
`main` rebuilds and redeploys the site.

## Caveats

- Complex Ghost cards (galleries, embeds, bookmark cards) convert best-effort —
  spot-check a few posts.
- Members/paywall content, code injection, and newsletter settings have no
  static equivalent and aren't migrated.
- Re-running is safe: existing images are skipped and content files are
  overwritten with the latest from Ghost.

That's the whole thing. The download has everything you need to repeat it on
your own blog.
