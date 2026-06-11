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
