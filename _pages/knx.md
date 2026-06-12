---
layout: default
title: KNX
slug: knx
permalink: /knx/
feature_image: /assets/images/2020/03/index.png
ghost_id: 65cc82d8e7fddf00012feb9d
---
<div class="container post-grid-wrap">
  <h1 style="margin-bottom:1.5rem">KNX</h1>

  {% assign knx_posts = site.tags["knx"] %}
  {% if knx_posts.size > 0 %}
  <ul class="post-grid">
    {% for post in knx_posts %}
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
            {% if badge %}
              <span class="post-card-badge">{{ badge | upcase | replace: "-", " " }}</span>
            {% endif %}
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
  <p>No KNX posts yet.</p>
  {% endif %}
</div>
