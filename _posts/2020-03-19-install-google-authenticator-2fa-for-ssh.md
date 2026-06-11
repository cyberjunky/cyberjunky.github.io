---
layout: post
title: Enable Google Authenticator 2FA for SSH
slug: install-google-authenticator-2fa-for-ssh
status: published
date: 2020-03-19 21:00:58 +0000
tags:
- linux
- google
category: linux
author: Ron
excerpt: 'Ubuntu:


  $ sudo apt-get install libpam-google-authenticator


  Debian:


  $ sudo apt-get install libqrencode3

  $ wget http://ftp.us.debian.org/debian/pool/main/g/google-authenticator/libpam-google-authenticator_20191231-1_amd64.deb

  $ sudo dpkg -i libpam-google-authenticator_20191231-1_amd64.deb


  Configure:


  $ google-authenticator


  $ sudo vi /etc/pam.d/sshd

  Add to the bottom:

  auth required pam_google_authenticator.so


  $ sudo vi /etc/ssh/sshd_config

  Set ChallengeResponseAuthentication yes


  $ sudo /etc/'
feature_image: /assets/images/2020/03/google-authenticator.png
ghost_id: 65cc82d8e7fddf00012feb9b
ghost_url: https://cyberjunky.nl/install-google-authenticator-2fa-for-ssh/
---

Ubuntu:

```
$ sudo apt-get install libpam-google-authenticator
```

Debian:

```
$ sudo apt-get install libqrencode3
$ wget http://ftp.us.debian.org/debian/pool/main/g/google-authenticator/libpam-google-authenticator_20191231-1_amd64.deb
$ sudo dpkg -i libpam-google-authenticator_20191231-1_amd64.deb
```

Configure:

```
$ google-authenticator

$ sudo vi /etc/pam.d/sshd
Add to the bottom:
auth required pam_google_authenticator.so

$ sudo vi /etc/ssh/sshd_config
Set ChallengeResponseAuthentication yes

$ sudo /etc/init.d/ssh restart
```