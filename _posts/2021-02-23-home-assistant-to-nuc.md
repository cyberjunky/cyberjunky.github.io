---
layout: post
title: Home Assistant OS on a Intel NUC
slug: home-assistant-to-nuc
status: published
date: 2021-02-23 15:06:45 +0000
tags:
- home-assistant
- home server
- NUC
category: home-assistant
author: Ron
excerpt: 'My D.I.Y. i3 board running Ubuntu 18 and Docker with Supervised HA for a
  long became unsupported, and in unhealthy state according to Hass.io, so I was looking
  at a Intel NUC to test running Home Assistant OS with add-ons only. And possibly
  create a add-on or two if needed.



  Hardware


  Browsing the web at Black Friday I came across this NUC on sale rather cheap.

  So I bought the following for around 300 Euro:

  - Intel NUC Kit NUC8i3BEK i3-8109U

  - SSD 1TB WD Blue M.2

  - Lexar 16GB 2666MHz RAM


  Mount'
feature_image: /assets/images/2021/02/nuc.png
ghost_id: 65cc82d8e7fddf00012febaf
ghost_url: https://cyberjunky.nl/home-assistant-to-nuc/
---

My D.I.Y. i3 board running Ubuntu 18 and Docker with Supervised HA for a long became unsupported, and in unhealthy state according to Hass.io, so I was looking at a Intel NUC to test running Home Assistant OS with add-ons only. And possibly create a add-on or two if needed.

### Hardware

Browsing the web at Black Friday I came across this NUC on sale rather cheap.  
So I bought the following for around 300 Euro:  
- Intel NUC Kit NUC8i3BEK i3-8109U  
- SSD 1TB WD Blue M.2  
- Lexar 16GB 2666MHz RAM

Mounted the RAM and the SSD inside the NUC

### BIOS

Switched on and pressed F2 to enter BIOS to check it's version.  
*Intel Desktop Board NUC8BEB  
BIOS Version: BECFL357.86A.0076.2019.1127.1452 (not kidding)  
Processor: Intel(R) Core(TM) i3-8109U CPU @ 3.00GHz*  
  
So it has the latest BIOS already running <https://downloadcenter.intel.com/download/29959/BIOS-Update-BECFL357-86A-?wapkw=NUC8i3BEK>

I left all settings at default for now, except 'After Power Failure', which I set to 'Power On'.

### Install Home Assistant OS via Debian live

I downloaded Debian 10 live install ISO

<https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-10.6.0-amd64-standard.iso>

Burned it on an 2GB USB stick with Rufus.  
Booted from USB stick.

### Stable Branch

```
$ sudo passwd
$ sudo su

# wget https://github.com/home-assistant/operating-system/releases/download/4.18/hassos_intel-nuc-4.18.img.gz

# dmesg|grep sd

# zcat hassos_intel-nuc-4.18.img.gz | dd bs=16k of=/dev/sda

# reboot

login: root
ha > login
ip addr
```

### Development Branch

```
$ sudo passwd
$ sudo su

# wget https://github.com/home-assistant/operating-system/releases/download/5.6/hassos_intel-nuc-5.6.img.xz

# dmesg|grep sd

# xz -d hassos_intel-nuc-5.6.img.xz
# dd if=hassos_intel-nuc-5.6.img of=/dev/sda

# reboot

login: root
ha > login
ip addr
```

You should get a login screen on http://ip address:8123 after booting.

I installed the following add-ons:

![](/assets/images/2021/02/addons.png)

NOTE: I enabled Fast Boot but wasn't able to enter the BIOS setup afterwards via F2, fix it like this: Switch on the NUC by holding the power button for 3 seconds then the Power menu should be shown, press F3 to disable Fast Boot.