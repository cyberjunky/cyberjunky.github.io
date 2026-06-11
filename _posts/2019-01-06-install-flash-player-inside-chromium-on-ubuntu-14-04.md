---
layout: post
title: Install Flash player inside Chromium on Ubuntu 14.04
slug: install-flash-player-inside-chromium-on-ubuntu-14-04
status: published
date: 2019-01-06 11:13:19 +0000
tags:
- ubuntu
- chrome
category: ubuntu
author: Ron
excerpt: "Chromium on Ubuntu 14.04 doesn't use Netscape plugin API anymore, it\n\n\
  simply not there.\n\nThe Chrome browser has support for Flash, so the following\
  \ steps\n\ndownload Chrome, extract it's Flashplayer and install it for Chromium.\n\
  \n\nYou need to reboot your computer after installing to activate it, or\n\nkill\
  \ all running chromium-browser processes.\n\nWe need to install the Pepper Flash\
  \ player installer.\n\n\n   $ sudo apt-get install pepperflashplugin-nonfree\n \
  \  $ sudo update-pepperflashplugin-nonfree --ins"
ghost_id: 65cc82d8e7fddf00012feb71
ghost_url: https://cyberjunky.nl/install-flash-player-inside-chromium-on-ubuntu-14-04/
---

{% raw %}
Chromium on Ubuntu 14.04 doesn't use Netscape plugin API anymore, it  
simply not there.  
The Chrome browser has support for Flash, so the following steps  
download Chrome, extract it's Flashplayer and install it for Chromium.

You need to reboot your computer after installing to activate it, or  
kill all running chromium-browser processes.  
We need to install the Pepper Flash player installer.

```
   $ sudo apt-get install pepperflashplugin-nonfree
   $ sudo update-pepperflashplugin-nonfree --install
```

If you want to uninstall it for some reason, use

```
   $ sudo update-pepperflashplugin-nonfree --uninstall
```
{% endraw %}
