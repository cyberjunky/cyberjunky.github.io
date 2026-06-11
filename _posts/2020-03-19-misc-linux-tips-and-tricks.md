---
layout: post
title: Misc Linux tips and tricks
slug: misc-linux-tips-and-tricks
status: published
date: 2020-03-19 20:32:20 +0000
tags:
- linux
category: linux
author: Ron
excerpt: 'R Studio Data Recovery doesn''t start with:

  /usr/local/R-Studio/bin/R-Studio: error while loading shared libraries: librs_linux_r.so:
  cannot open shared object file: No such file or directory


  $ sudo vi /etc/ld.so.conf.d/rstudio.conf

  /usr/local/R-Studio/lib


  Change words in multiple docs:


  $ grep -rl ''Tcphost'' ./ | sudo xargs sed -i ''s/Tcphost/TCP Host/g''

  $ grep -rl ''Tcpport'' ./ | sudo xargs sed -i ''s/Tcpport/TCP Port/g''


  Mount a VDI disk image:


  $ sudo modprobe nbd max_part=16

  $ sudo qemu-nbd -c'
feature_image: /assets/images/2020/03/linuxtux.png
ghost_id: 65cc82d8e7fddf00012feb99
ghost_url: https://cyberjunky.nl/misc-linux-tips-and-tricks/
---

**R Studio Data Recovery doesn't start with:**  
*/usr/local/R-Studio/bin/R-Studio: error while loading shared libraries: librs\_linux\_r.so: cannot open shared object file: No such file or directory*

```
$ sudo vi /etc/ld.so.conf.d/rstudio.conf
/usr/local/R-Studio/lib
```

**Change words in multiple docs:**

```
$ grep -rl 'Tcphost' ./ | sudo xargs sed -i 's/Tcphost/TCP Host/g'
$ grep -rl 'Tcpport' ./ | sudo xargs sed -i 's/Tcpport/TCP Port/g'
```

**Mount a VDI disk image:**

```
$ sudo modprobe nbd max_part=16
$ sudo qemu-nbd -c /dev/nbd0 ./home-logger.vdi
```

```
$ ls -lh /dev/nbd0*
<this lists all the partitions in the vdi>
```

Choose which of the partitions you want to mount (eg 1st partition), then:

```
$ sudo mount /dev/nbd0p1 /mnt
```

When done, unmount it:

```
$ sudo qemu-nbd -d /dev/nbd0
```

**Remove forbidden characters from files (for Samba share):**

```
SERVER> find . | perl -l -ne '/^([\000-\177]|[\300-\337][\200-\277]|[\340-\357][\200-\277]{2}|[\360-\367][\200-\277]{3}|[\370-\373][\200-\27
7]{4}|[\374-\375][\200-\277]{5})*$/ or print'

./HP EliteBook 2530p/tonymacx86 Forum � View topic - HP EliteBook 2530P install almost fully working.url
./MQTT/Search � mosquitto � GitHub.url
./MQTT/pubsubclient-PubSubClient-PubSubClient.cpp at master � knolleary-pubsubclient � GitHub.url
./PIC/Ethernet PIC PIC18 PIC24 PIC18F67J60 MikroPascal custom software YO2LIO Microcontrollers � Buy Products.url
./Security/How I cracked my neighbor�s WiFi password without breaking a sweat - Ars Technica.url
./Synology NAS/Wordpress/Darren Monahan � Updating WordPress on a Synology.url
./Synology NAS/Wordpress/Synology usage series 16- Install WordPress on Diskstation � blog.deadcode.net.url
./Synology NAS/Wordpress/WordPress � WordPress SEO by Yoast � WordPress Plugins.url
./Synology NAS/Wordpress/WordPress � Support � WordPress SEO by Yoast 1.2.7.8 on Synology DSM 4,1.url
./Dogm Displays/Blau macht gl�cklich! � www.ledhilfe.de - LED Forum.url
./Dogm Displays/Electronics-Lab.com Blog � firmware.url
./Dogm Displays/Library f�r EA-DOGM Grafikdisplays inkl. Font-Generator - Mikrocontroller.net.url
./Dogm Displays/PIC18 � Circuits@Home.url
./SmartMeter P1/rhekkers (Robert Hekkers) � GitHub.url
./SmartMeter P1/rhekkers-P1_Publisher � GitHub.url
./mFI/Ubiquiti mFi � Home Automation Monitoring and Control - Automated Home.url
./iBoard/� LCD screen for the RPi JeeLabs.url
./Raspberry Pi/Raspberry Kiosk - 06 - Installing a 10� Touch Screen on the Raspberry.url
./mBed/meterbed/MQTTClient_RFID_on_mbed-main.cpp at master � yilun-MQTTClient_RFID_on_mbed � GitHub.url
./mBed/meterbed/Andrew Hazelden's Blog � Monitoring A Solar Hot Water System Over the Internet.url
```