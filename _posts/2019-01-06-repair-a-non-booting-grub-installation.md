---
layout: post
title: Repair a non booting GRUB installation
slug: repair-a-non-booting-grub-installation
status: published
date: 2019-01-06 11:19:23 +0000
tags:
- linux
category: linux
author: Ron
excerpt: "Today I had to fix two issues with my computer not booting through grub\n\
  \nbootloader.\n\nOne of the reasons was a failed installation of Ubuntu due to using\
  \ an\n\nUSB stick with a corrupt image on it.\n\n\nA little Google query found a\
  \ page with info about boot-repair,\n\ndescribing a great tool to fix grub boot\
  \ problems.\n\n\nI used the 2nd option, simply boot into a live Ubuntu installation\
  \ and\n\nrun these two commands.\n\nThen follow the steps given.\n\n\nhttps://help.ubuntu.com/community/Boot-Repair\n\
  \n\n    $ su"
ghost_id: 65cc82d8e7fddf00012feb7b
ghost_url: https://cyberjunky.nl/repair-a-non-booting-grub-installation/
---

{% raw %}
Today I had to fix two issues with my computer not booting through grub  
bootloader.  
One of the reasons was a failed installation of Ubuntu due to using an  
USB stick with a corrupt image on it.

A little Google query found a page with info about boot-repair,  
describing a great tool to fix grub boot problems.

I used the 2nd option, simply boot into a live Ubuntu installation and  
run these two commands.  
Then follow the steps given.

<https://help.ubuntu.com/community/Boot-Repair>

```
    $ sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt-get update
    $ sudo apt-get install -y boot-repair && boot-repair
```
{% endraw %}
