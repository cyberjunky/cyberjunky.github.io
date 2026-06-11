---
layout: post
title: Change Color Gamma on Ubuntu
slug: change-color-gamma-on-ubuntu
status: published
date: 2019-01-06 11:06:29 +0000
tags:
- ubuntu
category: ubuntu
author: Ron
excerpt: "\n\n\nInstall xgamma-gui:\n\n\n    $ git clone https://github.com/dfc643/xgamma-gui.git\n\
  \    $ cd xgamma-gui\n\n\n\nAdd to Makefile:\n\n\n    CONFIG += qt\n    QT += gui\n\
  \n    $ qmake && make && make install\n    $ ./XgammaGui\n\n"
ghost_id: 65cc82d8e7fddf00012feb68
ghost_url: https://cyberjunky.nl/change-color-gamma-on-ubuntu/
---

![xgamma](/assets/images/2019/01/xgamma.png)

Install xgamma-gui:

```
    $ git clone https://github.com/dfc643/xgamma-gui.git
    $ cd xgamma-gui
```

Add to Makefile:

```
    CONFIG += qt
    QT += gui

    $ qmake && make && make install
    $ ./XgammaGui
```