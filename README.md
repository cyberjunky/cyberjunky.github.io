# Ghost → Jekyll (GitHub Pages) migration

Converts a Ghost blog — posts, pages, tags, authors, and all images — into a
static [Jekyll](https://jekyllrb.com/) site that GitHub Pages builds and serves
automatically (no custom CI required).

## What you get

```
_posts/YYYY-MM-DD-<slug>.md   published posts (Markdown + YAML front matter)
_drafts/<slug>.md             draft posts
_pages/<slug>.md              static pages
assets/images/...             every image, downloaded and re-linked locally
_data/authors.yml             author metadata
_data/tags.yml                tag metadata
_config.yml, Gemfile, index.html, .gitignore   Jekyll scaffold
```

## 1. Get a Ghost Admin API key

In Ghost Admin: **Settings → Integrations → Add custom integration**. Copy the
**Admin API Key** — it looks like `651a...:9f8c...` (`<id>:<hex-secret>`).

## 2. Configure credentials

```bash
cp .env.example .env
# edit .env and set GHOST_API_URL and GHOST_ADMIN_API_KEY
```

The script reads these from `.env` (or your shell environment). `.env` is
git-ignored, so the secret never gets committed.

## 3. Run the converter

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt

python ghost_to_jekyll.py            # writes into the current directory
python ghost_to_jekyll.py --dry-run  # fetch + report counts, write nothing
```

## 4. Preview locally (optional)

```bash
bundle install
bundle exec jekyll serve
# open http://localhost:4000
```

## 5. Publish to GitHub Pages

```bash
git init
git add .
git commit -m "Migrate blog from Ghost to Jekyll"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```

Then in the GitHub repo: **Settings → Pages → Build and deployment → Source:
GitHub Actions**.

This repo ships a workflow at `.github/workflows/jekyll.yml`. On every push to
`main` it runs `bundle install` + `jekyll build` (so all the `Gemfile` plugins
work, not just GitHub's built-in safe-mode set) and deploys the result. Watch
progress under the repo's **Actions** tab.

- **User/org site** (`<you>.github.io` repo): leave `baseurl` empty in
  `_config.yml`. The workflow injects the correct base path automatically.
- **Project site** (`<you>.github.io/<repo>`): the workflow passes the right
  `--baseurl` at build time, so you don't have to hardcode it.

## Creating and editing posts

### Write a new post

1. Create a file in `_posts/` named `YYYY-MM-DD-your-slug.md`.
2. Add YAML front matter at the top:

```yaml
---
layout: post
title: "Your Post Title"
date: 2026-06-12 10:00:00 +0000
tags:
  - home-assistant
  - knx
category: home-assistant        # shown as the badge on the card
author: Ron
excerpt: "One or two sentence summary shown in the post card."
feature_image: /assets/images/your-image.jpg   # optional, shown at top of post
---

Your post content here in Markdown.
```

3. Put images in `assets/images/` and reference as `/assets/images/filename.jpg`.
4. If your content contains `{{ }}` or `{% %}` (e.g. Home Assistant templates),
   wrap those sections in `{% raw %}` / `{% endraw %}` so Jekyll doesn't try to
   process them as Liquid.

### Edit an existing post

Open the file in `_posts/` in any text editor and edit the Markdown body or
front matter. The filename date sets the publish date on the home page list.

### Preview locally before publishing

```bash
bundle exec jekyll serve
# open http://localhost:4000
```

Edits are reflected on save without restarting (except `_config.yml` changes).

### Publish

```bash
git add _posts/YYYY-MM-DD-your-slug.md assets/images/...
git commit -m "Add post: your post title"
git push
```

GitHub Actions picks up the push, builds, and deploys in ~60 seconds. Watch
progress at `https://github.com/cyberjunky/cyberjunky.github.io/actions`.

### Drafts

Save unfinished posts in `_drafts/your-slug.md` (no date in filename). They
build locally with `bundle exec jekyll serve --drafts` but are never deployed.

## Notes & limitations

- Edit `title`, `description`, `url`, and `baseurl` in `_config.yml`.
- Post HTML is converted to Markdown with `markdownify`. Complex Ghost cards
  (galleries, embeds, bookmark cards) become best-effort HTML/Markdown — spot
  check a few posts.
- Re-running is safe: images already on disk are skipped, content files are
  overwritten with the latest from Ghost.
- Ghost code injection, members/paywall content, and newsletter settings are
  **not** migrated (no static equivalent).
- The default theme is `minima`. Swap `theme:` in `_config.yml` for any
  GitHub-Pages-supported theme, or vendor a `_layouts/` directory for full
  control.
