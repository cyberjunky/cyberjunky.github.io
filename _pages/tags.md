---
layout: default
title: Tags
slug: tags
permalink: /tags/
ghost_id: 65cc82d8e7fddf00012feba9
---
<div class="container page-wrap">
  <h1>Tags</h1>

  {% assign all_tags = site.posts | map: "tags" | join: "," | split: "," | uniq | sort %}

  <div class="tag-index">
    {% for tag in all_tags %}
      {% unless tag == "" %}
        {% assign tag_posts = site.tags[tag] %}
        <a class="tag-index-item" href="#tag-{{ tag | slugify }}">
          {{ tag }} <span class="tag-count">{{ tag_posts.size }}</span>
        </a>
      {% endunless %}
    {% endfor %}
  </div>

  <hr class="tags-divider">

  {% for tag in all_tags %}
    {% unless tag == "" %}
      {% assign tag_posts = site.tags[tag] %}
      <section id="tag-{{ tag | slugify }}" class="tag-section">
        <h2 class="tag-section-title">#{{ tag }}</h2>
        <ul class="tag-post-list">
          {% for post in tag_posts %}
          <li class="tag-post-item">
            <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
            <span class="meta-date">{{ post.date | date: "%-d %b %Y" }}</span>
          </li>
          {% endfor %}
        </ul>
      </section>
    {% endunless %}
  {% endfor %}
</div>
