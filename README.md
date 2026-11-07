[![Deploy][deploy-shield]][deploy]
[![GitHub Activity][commits-shield]][commits]
[![Last Commit][last-commit-shield]][commits]
![Project Maintenance][maintenance-shield]

[![Donate via PayPal](https://img.shields.io/badge/Donate-PayPal-blue.svg?style=for-the-badge&logo=paypal)](https://www.paypal.me/cyberjunkynl/)
[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor-GitHub-red.svg?style=for-the-badge&logo=github)](https://github.com/sponsors/cyberjunky)

# CyberJunky's Blog

Source of [cyberjunky.nl](https://cyberjunky.nl), a personal tech blog about home automation, Home Assistant, KNX, solar power, electronics and whatever else lands on the workbench.

## About

The site is a static [Jekyll](https://jekyllrb.com/) site hosted on GitHub Pages. No server, no database, no subscription. Posts are plain Markdown files with YAML front matter, and a GitHub Actions workflow builds and deploys the site on every push to `main`.

Features:

- Custom layouts with light/dark mode, post cards with feature images and category badges
- Client-side search over all posts (`/search/`)
- Tag archive (`/tags/`) and topic pages for Home Assistant, KNX and Solar Power
- RSS feed, sitemap and SEO tags via Jekyll plugins

The blog was migrated from Ghost with [ghost-to-jekyll](https://github.com/cyberjunky/ghost-to-jekyll), a small Python toolkit that lives in its own repo.

## Site Structure

```
_posts/YYYY-MM-DD-<slug>.md   published posts (URL becomes /<slug>/)
_drafts/<slug>.md             unpublished drafts
_pages/<slug>.md              static pages (about, topic archives, search, tags)
_layouts/                     default, home, page and post templates
assets/main.scss              all styling (light + dark theme)
assets/images/                post and page images
search.json                   search index generated at build time
_config.yml                   site settings, plugins, navigation order
.github/workflows/jekyll.yml  build and deploy workflow
```

## Writing a Post

1. Create `_posts/YYYY-MM-DD-your-slug.md`. The filename sets the date and the URL.
2. Add front matter:

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
excerpt: "One or two sentence summary shown on the post card and in search."
feature_image: /assets/images/your-image.jpg   # optional, shown at top of post
---
```

3. Write the body in Markdown. Put images in `assets/images/` and reference them as `/assets/images/filename.jpg`.
4. If the content contains `{{ }}` or `{% %}` (Home Assistant templates for example), wrap those sections in `{% raw %}` / `{% endraw %}` so Jekyll does not try to render them.

Drafts go in `_drafts/` without a date in the filename. They are built locally with `--drafts` and never deployed.

## Preview Locally

Requires Ruby 3.x and Bundler.

```bash
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --livereload --drafts
# open http://localhost:4000
```

Or without installing Ruby:

```bash
docker run --rm -it -p 4000:4000 -v "$PWD:/work" -w /work -e BUNDLE_PATH=/work/vendor/bundle ruby:3.3 \
  bash -c "bundle install && bundle exec jekyll serve --host 0.0.0.0 --drafts"
```

Edits are reflected on save, except changes to `_config.yml` which need a restart.

## Publishing

```bash
git add _posts/YYYY-MM-DD-your-slug.md assets/images/...
git commit -m "Add post: your post title"
git push
```

The workflow in `.github/workflows/jekyll.yml` picks up the push, builds the site and deploys it in about a minute. Editing a file in the GitHub web editor triggers the same build. Progress is visible under the [Actions](https://github.com/cyberjunky/cyberjunky.github.io/actions) tab.

## Development

- Dependencies (gems and GitHub Actions) are kept current by Dependabot, see `.github/dependabot.yml`.
- `Gemfile.lock` is committed so the CI build uses the same gem versions as a local build.
- Styling lives in a single `assets/main.scss`; colours are CSS custom properties defined per theme at the top of that file.

## 💖 Support This Project

If you find this blog useful, please consider supporting its continued upkeep:

### 🌟 Ways to Support

- **⭐ Star this repository** - Help others discover the blog
- **💰 Financial Support** - Contribute to hosting and development costs
- **🐛 Report Issues** - Found a broken link or an outdated post? Open an issue
- **📖 Spread the Word** - Share posts you found useful

### 💳 Financial Support Options

[![Donate via PayPal](https://img.shields.io/badge/Donate-PayPal-blue.svg?style=for-the-badge&logo=paypal)](https://www.paypal.me/cyberjunkynl/)
[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor-GitHub-red.svg?style=for-the-badge&logo=github)](https://github.com/sponsors/cyberjunky)

**Why Support?**
- Keeps the blog and the open-source projects behind it actively maintained
- Enables more write-ups and faster fixes
- Supports infrastructure costs (domain, testing, AI, CI/CD)
- Shows appreciation for the hours that go into each post

Every contribution, no matter the size, makes a difference and is greatly appreciated! 🙏

[deploy-shield]: https://img.shields.io/github/actions/workflow/status/cyberjunky/cyberjunky.github.io/jekyll.yml?branch=main&style=for-the-badge&label=deploy
[deploy]: https://github.com/cyberjunky/cyberjunky.github.io/actions/workflows/jekyll.yml
[commits-shield]: https://img.shields.io/github/commit-activity/y/cyberjunky/cyberjunky.github.io.svg?style=for-the-badge
[last-commit-shield]: https://img.shields.io/github/last-commit/cyberjunky/cyberjunky.github.io.svg?style=for-the-badge
[commits]: https://github.com/cyberjunky/cyberjunky.github.io/commits/main
[maintenance-shield]: https://img.shields.io/badge/maintainer-cyberjunky-blue.svg?style=for-the-badge
