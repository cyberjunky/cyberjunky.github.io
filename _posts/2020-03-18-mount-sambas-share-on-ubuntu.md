---
layout: post
title: Mount Samba share on Ubuntu
slug: mount-sambas-share-on-ubuntu
status: published
date: 2020-03-18 10:52:29 +0000
author: Ron
excerpt: '$ sudo apt install cifs-utils

  $ sudo mkdir /mnt/<mountpoint>

  $ sudo mount -t cifs -o user=<user> //<server>/<share> /mnt/<mountpoint>

  '
ghost_id: 65cc82d8e7fddf00012feb95
ghost_url: https://cyberjunky.nl/mount-sambas-share-on-ubuntu/
---

{% raw %}
```
$ sudo apt install cifs-utils
$ sudo mkdir /mnt/<mountpoint>
$ sudo mount -t cifs -o user=<user> //<server>/<share> /mnt/<mountpoint>
```
{% endraw %}
