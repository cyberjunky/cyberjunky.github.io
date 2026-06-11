---
layout: post
title: Examining AVM FRITZ!Box firmware
slug: examining-avm-fritz
status: published
date: 2020-03-20 06:56:02 +0000
tags:
- hacks
- fritz!box
category: hacks
author: Ron
excerpt: "Some steps too take a closer look to AVM's firmware\n\n$ mkdir ~/Firmware;\
  \ cd ~/Firmware\n$ wget https://download.avm.de/fritzbox/fritzbox-7590/other/fritz.os/FRITZ.Box_7590-07.13.image\n\
  \n$ sudo apt install binwalk\n\n$ ls\nFRITZ.Box_7590-07.13.image\n$ binwalk --signature\
  \ --term FRITZ.Box_7590-07.13.image \n\nDECIMAL       HEXADECIMAL     DESCRIPTION\n\
  --------------------------------------------------------------------------------\n\
  0             0x0             POSIX tar archive (GNU)\n\n\n$ tar xvf FRITZ.Box"
feature_image: /assets/images/2020/03/7950.jpg
ghost_id: 65cc82d8e7fddf00012feb9c
ghost_url: https://cyberjunky.nl/examining-avm-fritz/
---

{% raw %}
Some steps too take a closer look to AVM's firmware

```
$ mkdir ~/Firmware; cd ~/Firmware
$ wget https://download.avm.de/fritzbox/fritzbox-7590/other/fritz.os/FRITZ.Box_7590-07.13.image

$ sudo apt install binwalk

$ ls
FRITZ.Box_7590-07.13.image
$ binwalk --signature --term FRITZ.Box_7590-07.13.image 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             POSIX tar archive (GNU)


$ tar xvf FRITZ.Box_7590-07.13.image
./var/
./var/install
./var/regelex
./var/tmp/
./var/tmp/kernel.image
./var/tmp/filesystem.image
./var/info.txt
./var/content
./var/version
./var/chksum
./var/urladerupdate
./var/signature


$ cd tmp/
$ binwalk --signature --term kernel.image 

DECIMAL       HEXADECIMAL     DESCRIPTION
------------------------------------------------------------------------------------------------------------------------------------------------------
4753479       0x488847        LZMA compressed data, properties: 0x5B, dictionary size: 0 bytes, uncompressed size: 2152784640 bytes


ron@laptop-dell:~/Desktop/Firmware/var/tmp$ binwalk --signature --term filesystem.image 

DECIMAL       HEXADECIMAL     DESCRIPTION
------------------------------------------------------------------------------------------------------------------------------------------------------
0             0x0             Squashfs filesystem, big endian, version 4.0, compression:xz, size: 24002361 bytes, 3836 inodes, blocksize: 65536
                              bytes, created: 1970-10-05 19:19:21

$ binwalk --extract --quiet filesystem.image
WARNING: Extractor.execute failed to run external extractor 'sasquatch -p 1 -le -d 'squashfs-root' '%e'': [Errno 2] No such file or directory: 'sasquatch': 'sasquatch', 'sasquatch -p 1 -le -d 'squashfs-root' '%e'' might not be installed correctly

WARNING: Extractor.execute failed to run external extractor 'sasquatch -p 1 -be -d 'squashfs-root' '%e'': [Errno 2] No such file or directory: 'sasquatch': 'sasquatch', 'sasquatch -p 1 -be -d 'squashfs-root' '%e'' might not be installed correctly

$ git clone https://github.com/devttys0/sasquatch
$ cd sasquatch
$ ./build.sh
..

$ mkdir -p /usr/local/bin
$ cp sasquatch /usr/local/bin

$ binwalk --extract --quiet filesystem.image 
$ ls
filesystem.image  _filesystem.image-0.extracted  _filesystem.image.extracted  kernel.image
```

‌
{% endraw %}
