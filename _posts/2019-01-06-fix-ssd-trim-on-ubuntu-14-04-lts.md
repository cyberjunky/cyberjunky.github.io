---
layout: post
title: Fix SSD Trim on Ubuntu 14.04 LTS
slug: fix-ssd-trim-on-ubuntu-14-04-lts
status: published
date: 2019-01-06 11:10:43 +0000
tags:
- ubuntu
- ssd
category: ubuntu
author: Ron
excerpt: 'In Ubuntu 14.04 LTS SSD Trim is enabled by default.


  That''s nice and all, so I thought, nothing to do here but I found out


  it doesn''t work when you use LUKS crypt partitions, it''s a bug.



  Here the steps to fix it, please make backups of important files before


  doing this!!


  Note it only runs on Intel and Samsung SSD drives, see bottom of page


  why.



  First check if you have the same problems as me:



  $ sudo fstrim /

  fstrim: /: FITRIM ioctl failed: Inappropriate ioctl for device




  Check what d'
ghost_id: 65cc82d8e7fddf00012feb6d
ghost_url: https://cyberjunky.nl/fix-ssd-trim-on-ubuntu-14-04-lts/
---

{% raw %}
In Ubuntu 14.04 LTS SSD Trim is enabled by default.  
That's nice and all, so I thought, nothing to do here but I found out  
it doesn't work when you use LUKS crypt partitions, it's a bug.

Here the steps to fix it, please make backups of important files before  
doing this!!  
Note it only runs on Intel and Samsung SSD drives, see bottom of page  
why.

First check if you have the same problems as me:

```
$ sudo fstrim /
fstrim: /: FITRIM ioctl failed: Inappropriate ioctl for device
```

Check what dmsetup gives:

```
$ sudo dmsetup table 
sda5_crypt: 0 233934848 crypt aes-xts-plain64 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 0 8:5 4096 1
```

The reason for above error is the missing 'allow\_discards' at the end.

How to fix, open this file:

```
$ sudo vi /usr/share/initramfs-tools/scripts/local-top/cryptroot
```

```
        cryptrootdev=""
        cryptdiscard=""
        CRYPTTAB_OPTIONS=""
```

Change cryptdiscard value to:

```
        cryptdiscard="yes"
```

Write changes to your initrd:

```
$ sudo update-initramfs -u
$ sudo reboot
```

Check:

```
$ sudo dmsetup table
[sudo] password for ron: 
sda5_crypt: 0 233934848 crypt aes-xts-plain64 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 0 8:5 4096 1 allow_discards
```

You can also check if SSD trim is enabled by using lsblk:

```
$ lsblk -D
NAME                           DISC-ALN DISC-GRAN DISC-MAX DISC-ZERO
sda                                   0      512B       2G         0
├─sda1                                0      512B       2G         0
├─sda2                                0      512B       2G         0
└─sda5                                0      512B       2G         0
  └─sda5_crypt (dm-0)                 0      512B       2G         0
    ├─ubuntu--vg-root (dm-1)          0      512B       2G         0
    └─ubuntu--vg-swap_1 (dm-2)        0      512B       2G         0
sdb                                   0      512B       2G         0
```

If both values DISC-GRAN and DISC-MAX are >0, it's fine.

Now run fstrim again, please note that because it never worked on my SSD  
it run >10 minutes to catch up, running it again took 35 seconds ;-)

```
$ sudo fstrim -v /
/: 72480993280 bytes were trimmed
```

Wow that's 67.5GB while the drive is 120GB total.

```
[    1.395347] ata1.00: ATA-9: INTEL SSDSC2CW120A3, 400i, max UDMA/133
[    1.405488] scsi 0:0:0:0: Direct-Access     ATA      INTEL SSDSC2CW12 400i PQ: 0 ANSI: 5
```

Ubuntu 14.04 has a default configured weekly crontab job which starts  
'fstrim-all', so I leave it like this.

There is a warning inside the cronjob file btw:

```
$ sudo tail -n 6 /etc/cron.weekly/fstrim

# This only runs on Intel and Samsung SSDs by default, as some SSDs with faulty
# firmware may encounter data loss problems when running fstrim under high I/O
# load (e. g.  https://launchpad.net/bugs/1259829). You can append the
# --no-model-check option here to disable the vendor check and run fstrim on
# all SSD drives.
exec fstrim-all
```
{% endraw %}
