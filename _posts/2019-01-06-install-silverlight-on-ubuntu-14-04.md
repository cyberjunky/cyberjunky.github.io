---
layout: post
title: Install Silverlight on Ubuntu 14.04
slug: install-silverlight-on-ubuntu-14-04
status: published
date: 2019-01-06 11:14:14 +0000
tags:
- ubuntu
category: ubuntu
author: Ron
excerpt: "Ok, sometimes you can't go around a Microsoft product because a crappy\n\
  \nsite is written in Silverlight and you can't go without it.\n\nThese steps install\
  \ a modified version of Wine and configure it so that\n\nthe site which I needed.\n\
  \nSoftware called Magister used on a School website to monitor childrens\n\nprogress\
  \ worked oke for me on Ubuntu 14.04\n\n\n  $ sudo apt-get install python-software-properties\n\
  \  $ sudo add-apt-repository ppa:pipelight/stable\n  $ sudo apt-get update\n  $\
  \ sudo apt-get install p"
ghost_id: 65cc82d8e7fddf00012feb73
ghost_url: https://cyberjunky.nl/install-silverlight-on-ubuntu-14-04/
---

{% raw %}
Ok, sometimes you can't go around a Microsoft product because a crappy  
site is written in Silverlight and you can't go without it.  
These steps install a modified version of Wine and configure it so that  
the site which I needed.  
Software called Magister used on a School website to monitor childrens  
progress worked oke for me on Ubuntu 14.04

```
  $ sudo apt-get install python-software-properties
  $ sudo add-apt-repository ppa:pipelight/stable
  $ sudo apt-get update
  $ sudo apt-get install pipelight
  $ sudo pipelight-plugin --update
```

```
For system wide setting:
```

```
  $ sudo pipelight-plugin --enable silverlight
```

```
For current user only:
```

```
  $ pipelight-plugin --enable silverlight
```

Please note that only Firefox browser will work, since Chrome version  
>34 doesn't support the NSAPI anymore which this plugin uses.
{% endraw %}
