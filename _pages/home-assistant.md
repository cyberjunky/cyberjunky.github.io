---
layout: default
title: Home Assistant
permalink: /home-assistant/
---

<div class="container post-grid-wrap">
<h1 style="margin-bottom:1.5rem">Home Assistant</h1>

{% assign ha_posts = site.posts | where: "category", "home-assistant" %}

{% if ha_posts.size > 0 %}
<ul class="post-grid">
  {% for post in ha_posts %}
    {% assign badge = post.category | default: post.tags[0] %}
    <li class="post-card">
      <a class="post-card-link" href="{{ post.url | relative_url }}">
        <div class="post-card-img-wrap">
          {% if post.feature_image %}
            <img class="post-card-img" src="{{ post.feature_image | relative_url }}"
                 alt="{{ post.title | escape }}" loading="lazy" />
          {% else %}
            <div class="post-card-img post-card-img--placeholder"></div>
          {% endif %}
          {% if badge %}<span class="post-card-badge">{{ badge | upcase | replace: "-", " " }}</span>{% endif %}
        </div>
        <div class="post-card-body">
          <h2 class="post-card-title">{{ post.title | escape }}</h2>
          {% if post.excerpt %}
            <p class="post-card-excerpt">{{ post.excerpt | strip_html | truncate: 130 }}</p>
          {% endif %}
          <footer class="post-card-meta">
            <span class="meta-date">{{ post.date | date: "%-d %b %Y" }}</span>
          </footer>
        </div>
      </a>
    </li>
  {% endfor %}
</ul>
{% else %}
<p>No Home Assistant posts yet.</p>
{% endif %}
</div>
