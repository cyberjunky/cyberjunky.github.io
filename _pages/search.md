---
layout: default
title: Search
permalink: /search/
---
<div class="container search-wrap">
  <h1 class="search-heading">Search</h1>

  <div class="search-bar">
    <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
         fill="none" stroke="currentColor" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
    <input id="search-input" class="search-input" type="search"
           placeholder="Search posts…" autocomplete="off" autofocus />
  </div>

  <p id="search-count" class="search-count" hidden></p>
  <ul id="search-results" class="post-grid search-results"></ul>
  <p id="search-empty"  class="search-empty"  hidden>No posts found.</p>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/lunr.js/2.3.9/lunr.min.js"
        integrity="sha512-4SpMJ6pBm7PYMvHPMOB6PpVB+i4FJPHv6YuPnqPbGhWC8EhQ5lF0c0lCRuI6CJrF9VFJqUk6EaQ2wW2cpQFw=="
        crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script>
(function () {
  var input   = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  var count   = document.getElementById('search-count');
  var empty   = document.getElementById('search-empty');
  var idx, posts;

  // Pre-fill query from URL param ?q=...
  var params = new URLSearchParams(window.location.search);
  var initial = params.get('q') || '';

  fetch('{{ "/search.json" | relative_url }}')
    .then(function(r) { return r.json(); })
    .then(function(data) {
      posts = data;
      idx = lunr(function () {
        this.ref('url');
        this.field('title',    { boost: 10 });
        this.field('category', { boost: 5  });
        this.field('tags',     { boost: 5  });
        this.field('excerpt',  { boost: 3  });
        this.field('content');
        data.forEach(function (p) { this.add(p); }, this);
      });
      if (initial) {
        input.value = initial;
        doSearch(initial);
      }
    })
    .catch(function(e) { console.error('Search index load failed:', e); });

  input.addEventListener('input', function () {
    doSearch(this.value.trim());
    // Keep URL in sync so the query is bookmarkable/shareable.
    var url = new URL(window.location);
    if (this.value.trim()) {
      url.searchParams.set('q', this.value.trim());
    } else {
      url.searchParams.delete('q');
    }
    history.replaceState(null, '', url);
  });

  function doSearch(q) {
    results.innerHTML = '';
    count.hidden = true;
    empty.hidden = true;

    if (!q || q.length < 2) return;

    var hits;
    try {
      // Try exact first, then wildcard.
      hits = idx.search(q);
      if (!hits.length) hits = idx.search(q + '*');
    } catch(e) {
      hits = [];
    }

    if (!hits.length) { empty.hidden = false; return; }

    count.textContent = hits.length + ' result' + (hits.length === 1 ? '' : 's');
    count.hidden = false;

    var map = {};
    posts.forEach(function(p) { map[p.url] = p; });

    hits.forEach(function (h) {
      var p = map[h.ref];
      if (!p) return;
      var badge = p.category
        ? '<span class="post-card-badge">' + p.category.replace(/-/g,' ').toUpperCase() + '</span>'
        : '';
      var li = document.createElement('li');
      li.className = 'post-card';
      li.innerHTML =
        '<a class="post-card-link" href="' + p.url + '">' +
          '<div class="post-card-img-wrap">' +
            '<div class="post-card-img post-card-img--placeholder"></div>' +
            badge +
          '</div>' +
          '<div class="post-card-body">' +
            '<h2 class="post-card-title">' + escHtml(p.title) + '</h2>' +
            '<p class="post-card-excerpt">' + escHtml(p.excerpt) + '</p>' +
            '<footer class="post-card-meta">' +
              '<span class="meta-date">' + escHtml(p.date) + '</span>' +
            '</footer>' +
          '</div>' +
        '</a>';
      results.appendChild(li);
    });
  }

  function escHtml(s) {
    return String(s)
      .replace(/&/g,'&amp;').replace(/</g,'&lt;')
      .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }
})();
</script>
