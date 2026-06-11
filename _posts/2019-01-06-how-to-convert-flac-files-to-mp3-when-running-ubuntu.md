---
layout: post
title: How to convert FLAC files to MP3 when running Ubuntu
slug: how-to-convert-flac-files-to-mp3-when-running-ubuntu
status: published
date: 2019-01-06 11:12:00 +0000
tags:
- ubuntu
category: ubuntu
author: Ron
excerpt: "$ sudo apt-get install flac lame \n$ for f in *.flac; do flac -cd \"$f\"\
  \ | lame -b 320 - \"${f%.*}\".mp3; done\n\n"
ghost_id: 65cc82d8e7fddf00012feb6f
ghost_url: https://cyberjunky.nl/how-to-convert-flac-files-to-mp3-when-running-ubuntu/
---

{% raw %}
```
$ sudo apt-get install flac lame 
$ for f in *.flac; do flac -cd "$f" | lame -b 320 - "${f%.*}".mp3; done
```
{% endraw %}
