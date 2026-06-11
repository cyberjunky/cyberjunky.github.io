---
layout: post
title: Reflashing my LG Chromebase back to ChromeOS
slug: reflashing-my-lg-chromebase-back-to-chromeos
status: published
date: 2020-03-19 13:49:03 +0000
tags:
- ubuntu
- chromeos
category: ubuntu
author: Ron
excerpt: 'With a lot of effort (back then when not much was known) I flashed my LG
  Chromebase (22CV241) to use Coreboot and installed Ubuntu 14.04 LTS on it.


  For a while I wanted to reinstalled ChromeOS since I used it for email and viewing
  YouTube/Twitch only. But since I didn''t saved the original BIOS file I couldn''t.


  Until I came across mrchromebox''s script which appeared to download the BIOS from
  the web, and low and behold it worked.


  These are the steps.


  Since I already ran Ubuntu on it, I could '
feature_image: /assets/images/2020/03/chrome_icon.png
ghost_id: 65cc82d8e7fddf00012feb98
ghost_url: https://cyberjunky.nl/reflashing-my-lg-chromebase-back-to-chromeos/
---

{% raw %}
With a lot of effort (back then when not much was known) I flashed my LG Chromebase (22CV241) to use Coreboot and installed Ubuntu 14.04 LTS on it.

For a while I wanted to reinstalled ChromeOS since I used it for email and viewing YouTube/Twitch only. But since I didn't saved the original BIOS file I couldn't.

Until I came across mrchromebox's script which appeared to download the BIOS from the web, and low and behold it worked.

These are the steps.

Since I already ran Ubuntu on it, I could just download the script and run it:

```
$ cd ~; curl -L -O http://mrchromebox.tech/firmware-util.sh; sudo bash firmware-util.sh
```

It looks like this:

![](/assets/images/2020/03/script.png)

I didn't reboot yet but used the following steps to create the Chromebook Recovery Utility to create a USB restore stick.

```
$ curl https://dl.google.com/dl/edgedl/chromeos/recovery/linux_recovery.sh
$ chmod +x linux_recovery.sh 
$ sudo bash linux_recovery.sh

======================================================================
This tool is in maintenance mode.
Try the new Chromebook Recovery Utility on Chrome OS, Windows, or Mac.
For more information, visit http://www.google.com/chromeos/recovery.
======================================================================

Working in /tmp/tmp.crosrec/
Downloading config file from https://dl.google.com/dl/edgedl/chromeos/recovery/recovery.conf

If you know the Model string displayed at the recovery screen,
type some or all of it; otherwise just press Enter: MONROE

This may take a few minutes to print the full list...

There are up to 249 recovery images to choose from:

0 - <quit>
113 - LG Chromebase (22CB25S)
  channel:  stable-channel
  pattern:   ^MONROE .4.*
114 - LG Chromebase (22CV241)
  channel:  stable-channel
  pattern:   ^MONROE .[23].*

Please select a recovery image to download: 114

ERROR:  There is not enough free space in /tmp/tmp.crosrec (it has 1606MB, we need 2829MB).

Please free up some space on that filesystem, or specify a temporary directory
on the commandline like so:

  WORKDIR=/path/to/some/dir  linux_recovery.sh

ron@ron-chromebase:~/Downloads$ df -k
Filesystem     1K-blocks    Used Available Use% Mounted on
udev             4046444       4   4046440   1% /dev
tmpfs             811580    1232    810348   1% /run
/dev/dm-0        6815456 4802424   1643780  75% /
```

Uh oh, not enough space.. I fixed it using the dpigs tool:

```
$ sudo apt install debian-goodies
$ dpigs -H
 176.1M firefox
 156.2M thunderbird
 149.2M linux-image-extra-3.16.0-77-generic
 149.1M linux-image-extra-3.16.0-30-generic
 149.0M linux-image-extra-3.16.0-45-generic
 121.2M linux-firmware
 119.1M liboxideqtcore0
 111.0M libreoffice-core
  72.6M libreoffice-common
  61.6M linux-headers-3.16.0-77
```

Remove the biggest packages (leaving the newest kernel there ofcourse), after freeing up enough space I re-ran the recovery script.. it went on like this:

```
Downloading image zipfile from https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_12739.94.0_monroe_recovery_stable-channel_mp-v2.bin.zip

...
I found 2 USB drives.  We need one with at least 2215MB capacity.

0 - <quit>

1 - Use /dev/sdb 7747MB Kingston DataTraveler 102

2 - Use /dev/sdc 1039MB Kingston DataTraveler II+


Tell me what to do (or just press Enter to scan again): 1

Is this the device you want to put the recovery image on?

  /dev/sdb 7747MB Kingston DataTraveler 102

You must enter 'YES' (all uppercase) to continue: YES


I'm really going to erase this device. This will permanently ERASE
whatever you may have on that drive. You won't be able to undo it.

  /dev/sdb 7747MB Kingston DataTraveler 102

If you're sure that's correct, enter 'DoIt' now (case is important): 

If you're sure that's correct, enter 'DoIt' now (case is important): DoIt


Installing the recovery image


unmounting...
copying... (this may take several minutes)


Installing the recovery image


unmounting...
copying... (this may take several minutes)
553+1 records in
554+0 records out
2323644416 bytes (2,3 GB) copied, 982,197 s, 2,4 MB/s


Done. Remove the USB drive and insert it in your Chrome notebook.


Shall I remove the temporary files now? [y/n]
```

Rebooted with the recovery USB inserted and restored the ChromeOS by following the steps on-screen.

All fine it booted ChromeOS, but I could get it out of developer mode using SPACE BAR, because of this error:

"WARNING: TONORM prohibited by GBB  FORCE\_DEV\_SWITCH\_ON"

If you try to boot with it set you'll see the dev mode screen, but pressing spacebar will cause a  beep and this message.

To get back to normal behavior I did this:  
\* Boot into developer mode  
\* Switch to console shell (Ctrl-Alt-F2)  
\* Login as root and run this command:

```
# /usr/share/vboot/bin/set_gbb_flags.sh 0
```

It looks like this, so even though I got a lot of warnings it worked, and I could enable the Check OS settings again upon next boot.

![](/assets/images/2020/03/dev_mode_flags.jpg)

WARNING: It deletes locally saved data and settings, you have to setup your ChromeOS from start.

![](/assets/images/2020/03/front_board.JPG)

![](/assets/images/2020/03/possible_wp_screw.JPG)

![](/assets/images/2020/03/winbond_spi_chip.JPG)

![](/assets/images/2020/03/rear_of_main_board.JPG)

Some internal pictures of the unit

Resources:

[MrChromebox.tech

MrChromebox.tech : Custom coreboot firmware and firmware utilities for your Chromebook/Chromebox

![](https://www.paypalobjects.com/en_US/i/scr/pixel.gif)](https://mrchromebox.tech/)[Recover your Chromebook - Chromebook Help

When your Chromebook’s operating system (OS) isn’t working properly, you can recover it. Recovery is removing and reinstalling the OS.Note: If you’re using your Chromebook at work or school, a

Chromebook Help

![](https://lh3.googleusercontent.com/-20NuyB0WC36P5OvH-HnVwgMQlIRx47n0At3ZLRZuU2UIuXpsDZVhrsFJMW5DQkQVQU=w18-h18)](https://support.google.com/chromebook/answer/1080595?hl=en)[LG Chromebase 22CV241-W : Chromebase 22″ Class (21.5″ Diagonal) | LG USA

Get information on the LG Chromebase 22CV241-W. Find pictures, reviews, and tech specs for the LG Chromebase 22CV241-W Chromebase 22″ Class (21.5″ Diagonal)

![](https://www.lg.com/lg5-common/favicons/228x228.png)LG USAHojoMojo

![](https://www.lg.com/us/images/monitors/chromebase-22cv241-w/gallery/large01.jpg)](https://www.lg.com/us/desktops-all-in-one-computers/lg-Chromebase-22CV241-W-all-in-one-computer)
{% endraw %}
