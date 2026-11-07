---
layout: post
title: Mount Samba share on Ubuntu
date: 2020-03-18 10:52:29 +0000
author: Ron
excerpt: '$ sudo apt install cifs-utils

  $ sudo mkdir /mnt/<mountpoint>

  $ sudo mount -t cifs -o user=<user> //<server>/<share> /mnt/<mountpoint>

  '
---

{% raw %}
```
$ sudo apt install cifs-utils
$ sudo mkdir /mnt/<mountpoint>
$ sudo mount -t cifs -o user=<user> //<server>/<share> /mnt/<mountpoint>
```
{% endraw %}
