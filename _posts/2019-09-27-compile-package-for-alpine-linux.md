---
layout: post
title: Compile package for Alpine Linux
slug: compile-package-for-alpine-linux
status: published
date: 2019-09-27 11:26:14 +0000
author: Ron
excerpt: 'Install Alpine Linux inside Virtual Box using this image, assign to DVD
  device, set network adapter to bridged, boot it, and login with root


  Then start the setup script


  # setup-alpine



  Walk through script:


  Keyboard layout: us

  Keyboard variants: us

  Networking eth0, bridge, dhcp

  Root password

  Timezone: Europe/Amsterdam

  HTTP/FTP, proxy none [enter]

  NTP client: chrony [enter]

  Mirror: f (fastest)

  SSH server: openssh [enter]

  Disk(s): sda, how: sys, continue: y

  Shutdown live cd using poweroff comma'
feature_image: /assets/images/2019/04/alogo.png
ghost_id: 65cc82d8e7fddf00012feb90
ghost_url: https://cyberjunky.nl/compile-package-for-alpine-linux/
---

{% raw %}
Install Alpine Linux inside Virtual Box using [this image](https://wiki.alpinelinux.org/wiki/Install_Alpine_on_VirtualBox), assign to DVD device, set network adapter to bridged, boot it, and login with root

Then start the setup script

```
# setup-alpine
```

![](/assets/images/2019/04/boot.png)

Walk through script:

Keyboard layout: us  
Keyboard variants: us  
Networking eth0, bridge, dhcp  
Root password  
Timezone: Europe/Amsterdam  
HTTP/FTP, proxy none [enter]  
NTP client: chrony [enter]  
Mirror: f (fastest)  
SSH server: openssh [enter]  
Disk(s): sda, how: sys, continue: y  
Shutdown live cd using *poweroff* command and remove DVD image, restart VM.

![](/assets/images/2019/04/booted-1.png)

Install needed environment:

```
# apk add alpine-sdk
# adduser <yourusername>
# cat <<EOF >/etc/sudoers.d/<yourusername>
  <yourusername> ALL=(ALL) ALL'
  EOF
```

Now logout of the root account, and login as <yourusername>. From here on everything can be done in a normal user account, and operations that require superuser privileges can be done with sudo.

Define git settings and clone aports repository:

```
$ git config --global user.name "Your Full Name"
$ git config --global user.email "your@email.address"
$ git clone git://git.alpinelinux.org/aports
$ sudo vi /etc/abuild.conf
```

Most of the defaults can be left alone, unless you are developing for a custom platform, in which case the comments in the file should guide you. The one field to edit is PACKAGER, so that you can get credit (or blame) for packages you create, and uncomment MAINTAINER.

Use 'abuild -r' command to install dependency packages automatically.

```
$ sudo addgroup <yourusername> abuild
```

We also need to prepare the location where the build process caches files when they are downloaded. By default this is /var/cache/distfiles/. To create this directory and ensure that it is write-able, enter the following commands:

```
$ sudo mkdir -p /var/cache/distfiles
$ sudo chmod a+w /var/cache/distfiles
$ abuild-keygen -a -i
```

I want to build arp-scan for Alpine Linux 3.9, so I followed these steps:

```
$ newapkbuild arp-scan
```

Resources:  
<https://wiki.alpinelinux.org/wiki/Install_Alpine_on_VirtualBox>  
<https://wiki.alpinelinux.org/wiki/Installation#Installation_Handbook>  
<https://wiki.alpinelinux.org/wiki/Alpine_Linux_Init_System>  
<https://wiki.alpinelinux.org/wiki/Creating_an_Alpine_package#Setup_your_system_and_account>
{% endraw %}
