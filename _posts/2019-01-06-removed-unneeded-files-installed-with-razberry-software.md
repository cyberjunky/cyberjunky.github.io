---
layout: post
title: Removed unneeded files installed with Razberry software
slug: removed-unneeded-files-installed-with-razberry-software
status: published
date: 2019-01-06 11:18:51 +0000
tags:
- rasberry-pi
- razberry
- z-wave
category: rasberry-pi
author: Ron
excerpt: "Steps on how to remove Razberry bloated/unneeded files:\n\n\nCloud connect\
  \ stuff:\n\n\n    # /etc/init.d/zbw_connect stop\n    # rm -rf /etc/zbw\n    # rm\
  \ -rf /var/webif\n\n\n\nMongoose:\n\n\n    # /etc/init.d/mongoose stop\n    # rm\
  \ /etc/init.d/mongoose\n    # rm -rf /etc/mongoose\n    # rm /usr/sbin/mongoose\n\
  \n"
ghost_id: 65cc82d8e7fddf00012feb7a
ghost_url: https://cyberjunky.nl/removed-unneeded-files-installed-with-razberry-software/
---

{% raw %}
Steps on how to remove Razberry bloated/unneeded files:

Cloud connect stuff:

```
    # /etc/init.d/zbw_connect stop
    # rm -rf /etc/zbw
    # rm -rf /var/webif
```

Mongoose:

```
    # /etc/init.d/mongoose stop
    # rm /etc/init.d/mongoose
    # rm -rf /etc/mongoose
    # rm /usr/sbin/mongoose
```
{% endraw %}
