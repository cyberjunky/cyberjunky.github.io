---
layout: post
title: GitHub MFA on Ubuntu CLI
slug: github-mfa-on-ubuntu-cli
status: published
date: 2020-11-08 16:48:16 +0000
tags:
- mfa
- ubuntu
- github
category: mfa
author: Ron
excerpt: 'Install and compile the Gnome Keyring development


  $ sudo apt-get install libgnome-keyring-dev

  $ sudo make --directory=/usr/share/doc/git/contrib/credential/gnome-keyring

  $ git config --global credential.helper /usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring'
feature_image: /assets/images/2020/11/2fa.PNG
ghost_id: 65cc82d8e7fddf00012feb9e
ghost_url: https://cyberjunky.nl/github-mfa-on-ubuntu-cli/
---

{% raw %}
Install and compile the Gnome Keyring development

```
$ sudo apt-get install libgnome-keyring-dev
$ sudo make --directory=/usr/share/doc/git/contrib/credential/gnome-keyring
$ git config --global credential.helper /usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring
```
{% endraw %}
