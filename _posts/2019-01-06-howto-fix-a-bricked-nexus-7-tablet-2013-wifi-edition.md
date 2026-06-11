---
layout: post
title: Howto fix a bricked Nexus 7 tablet (2013 WiFi edition)
slug: howto-fix-a-bricked-nexus-7-tablet-2013-wifi-edition
status: published
date: 2019-01-06 11:12:50 +0000
tags:
- fixes
- android
category: fixes
author: Ron
excerpt: "Make sure you have latest SDK platform tools installed and have\n\ndownloaded\
  \ and unpack correct image fot your tablet.\n\n\nThese proceed with these steps:\n\
  \n\n    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot devices\n    08554881\
  \    fastboot\n    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot erase\
  \ boot\n    erasing 'boot'...\n    OKAY [  0.034s]\n    finished. total time: 0.034s\n\
  \n    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot erase cache\n    ********\
  \ Did you mean to fastb"
ghost_id: 65cc82d8e7fddf00012feb70
ghost_url: https://cyberjunky.nl/howto-fix-a-bricked-nexus-7-tablet-2013-wifi-edition/
---

{% raw %}
Make sure you have latest SDK platform tools installed and have  
downloaded and unpack correct image fot your tablet.

These proceed with these steps:

```
    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot devices
    08554881    fastboot
    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot erase boot
    erasing 'boot'...
    OKAY [  0.034s]
    finished. total time: 0.034s

    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot erase cache
    ******** Did you mean to fastboot format this partition?
    erasing 'cache'...
    OKAY [  0.359s]
    finished. total time: 0.359s

    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot erase recovery
    erasing 'recovery'...
    OKAY [  0.032s]
    finished. total time: 0.032s

    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot erase system
    ******** Did you mean to fastboot format this partition?
    erasing 'system'...
    OKAY [  1.103s]
    finished. total time: 1.103s

    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot erase userdata
    ******** Did you mean to fastboot format this partition?
    erasing 'userdata'...
    OKAY [ 17.426s]
    finished. total time: 17.426s
    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ 

    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot flash bootloader ~/Desktop/nexus/razor-lrx22g/bootloader-flo-flo-04.04.img
    sending 'bootloader' (3911 KB)...
    OKAY [  0.163s]
    writing 'bootloader'...
    OKAY [  1.573s]
    finished. total time: 1.737s

    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot reboot-bootloader
    rebooting into bootloader...
    OKAY [  0.005s]
    finished. total time: 0.156s

    ron@ron-ubuntu:~/Android/Sdk/platform-tools$ ./fastboot -w update ~/Desktop/nexus/razor-lrx22g/image-razor-lrx22g.zip
    archive does not contain 'boot.sig'
    archive does not contain 'recovery.sig'
    archive does not contain 'system.sig'
    archive does not contain 'vendor.img'
    Creating filesystem with parameters:
        Size: 28856791040
        Block size: 4096
        Blocks per group: 32768
        Inodes per group: 8192
        Inode size: 256
        Journal blocks: 32768
        Label: 
        Blocks: 7045115
        Block groups: 215
        Reserved block group size: 1024
    Created filesystem with 11/1761280 inodes and 154578/7045115 blocks
    Creating filesystem with parameters:
        Size: 587202560
        Block size: 4096
        Blocks per group: 32768
        Inodes per group: 7168
        Inode size: 256
        Journal blocks: 2240
        Label: 
        Blocks: 143360
        Block groups: 5
        Reserved block group size: 39
    Created filesystem with 11/35840 inodes and 4616/143360 blocks
    --------------------------------------------
    Bootloader Version...: FLO-04.04
    Baseband Version.....: none
    Serial Number........: 08554881
    --------------------------------------------
    checking product...
    OKAY [  0.003s]
    checking version-bootloader...
    OKAY [  0.004s]
    sending 'boot' (7182 KB)...
    OKAY [  0.289s]
    writing 'boot'...
    OKAY [  0.298s]
    sending 'recovery' (7768 KB)...
    OKAY [  0.311s]
    writing 'recovery'...
    OKAY [  0.300s]
    erasing 'system'...
    OKAY [  0.653s]
    sending 'system' (799293 KB)...
    OKAY [ 31.303s]
    writing 'system'...
```

Fixed!

Resource:

<http://forums.androidcentral.com/google-nexus-7-2012-rooting-roms-hacks/191477-guide-nexus-7-factory-image-restore.html>
{% endraw %}
