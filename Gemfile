source "https://rubygems.org"

# The site is built by .github/workflows/jekyll.yml with plain Jekyll, so the
# heavyweight `github-pages` meta-gem (pinned to Jekyll 3.x) is not needed.
#
# Local preview:
#   bundle config set --local path vendor/bundle
#   bundle install
#   bundle exec jekyll serve --livereload
gem "jekyll", "~> 4.4"

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
  gem "jekyll-paginate"
end

# `jekyll serve` needs these on Ruby 3.x
gem "webrick"
gem "csv"
gem "base64"
gem "bigdecimal"
