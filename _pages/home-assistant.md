---
layout: page
title: Home Assistant
slug: home-assistant
permalink: /home-assistant/
---

{% assign ha_posts = site.posts | where_exp: "post", "post.tags contains 'home-assistant' or post.category == 'home-assistant'" %}

{% if ha_posts.size > 0 %}
<ul class="post-grid" style="margin-top:1.5rem">
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
