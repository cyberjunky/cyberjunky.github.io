---
layout: post
title: Updating rooted Toon 5.9.6
slug: updating-rooted-toon-5-9-6
status: published
date: 2019-09-27 11:25:48 +0000
tags:
- toon
category: toon
author: Ron
excerpt: 'Excerpt of latest Toon update.


  # cd /root


  Get correct resource files:

  # wget http://qutility.nl/resourcefiles/resources-qb2-5.9.6.zip

  --2019-08-15 15:34:37--  http://qutility.nl/resourcefiles/resources-qb2-5.9.6.zip

  Resolving qutility.nl... 54.38.183.159

  Connecting to qutility.nl|54.38.183.159|:80... connected.

  HTTP request sent, awaiting response... 200 OK

  Length: 2796681 (2.7M) [application/zip]

  Saving to: `resources-qb2-5.9.6.zip''


  100%[======================================================'
feature_image: /assets/images/2020/08/TOON-Logo_reg_mark_ORANGE-rgb.png
ghost_id: 65cc82d8e7fddf00012feb91
ghost_url: https://cyberjunky.nl/updating-rooted-toon-5-9-6/
---

Excerpt of latest Toon update.

```
# cd /root

Get correct resource files:
# wget http://qutility.nl/resourcefiles/resources-qb2-5.9.6.zip
--2019-08-15 15:34:37--  http://qutility.nl/resourcefiles/resources-qb2-5.9.6.zip
Resolving qutility.nl... 54.38.183.159
Connecting to qutility.nl|54.38.183.159|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2796681 (2.7M) [application/zip]
Saving to: `resources-qb2-5.9.6.zip'

100%[==============================================================================================>] 2,796,681   2.83M/s   in 0.9s    

2019-08-15 15:34:38 (2.83 MB/s) - `resources-qb2-5.9.6.zip' saved [2796681/2796681]

Install resource files:
# cp /root/*.rcc /qmf/qml

Get latest toonstore app:
# wget http://files.domoticaforum.eu/uploads/Toon/apps/toonstore-3.0.2/toonstore_3.0.2-r0_qb2.ipk
--2019-08-15 15:37:20--  http://files.domoticaforum.eu/uploads/Toon/apps/toonstore-3.0.2/toonstore_3.0.2-r0_qb2.ipk
Resolving files.domoticaforum.eu... 80.101.79.154
Connecting to files.domoticaforum.eu|80.101.79.154|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 42856 (42K) [application/vnd.android.package-archive]
Saving to: `toonstore_3.0.2-r0_qb2.ipk'

100%[==============================================================================================>] 42,856      --.-K/s   in 0.1s    

2019-08-15 15:37:20 (438 KB/s) - `toonstore_3.0.2-r0_qb2.ipk' saved [42856/42856]

Remove toonstore app:
# opkg remove toonstore
Removing package toonstore from root...
Executing post-rm script for toonstore-2.1.4 ...
Removing stale link /HCBv2/qml/apps/toonstore ...
Removing settings files ...
Restoring original keyring ... 
Restoring original hosts file ... 
Restoring original project file ...
Restarting http server ...

Install toonstore app:
# opkg install toonstore_3.0.2-r0_qb2.ipk 
Installing toonstore (3.0.2-r0) to root...
Executing pre-install script for toonstore-3.0.2
New installation of toonstore.
Backing up public keyring ...
Backing up /etc/hosts ...
Editing /etc/hosts to enable toonstore ...
hcb_config process ID now: 704
Restarting hcb_config ...
Waiting for 3 seconds ...
hcb_config process ID now: 23660
Creating backup for /qmf/etc/qmf_release.xml ...
Patching /qmf/etc/qmf_release.xml for 403-forbidden error ...
Restarting http server ...
Cleaning garbage....
rm: can't remove '/HCBv2/qml/apps/toonstore/*.qmlc': No such file or directory
rm: can't remove '/HCBv2/qml/apps/toonstore/*.jsc': No such file or directory
rm: can't remove '/HCBv2/qml/apps/toonstore/*.txt': No such file or directory
ToonStore pre-install script completed ...
Configuring toonstore.
Executing post-install script for toonstore-3.0.2 ...
Writing app version number to /HCBv2/qml/apps/toonstore-3.0.2/version.txt ...
Adding toonstore key to opkg keyring ...
OK
This is a Toon 1
No settings to be restored
Creating symbolic link /HCBv2/qml/apps/toonstore to /HCBv2/qml/apps/toonstore-3.0.2
Firmware version 5 or greater detected, changing app for firmware compatibility...
Posting message ...
skipped update request of tsc scripts

Disable VPN:
# vi /etc/inittab

#ovpn:2345:respawn:/usr/sbin/openvpn --config /etc/openvpn/vpn.conf --verb 0 >/dev/null 2>&1

Supress warning:
# vi /HCBv2/qml/apps/internetSettings/InternetSettingsApp.qml

Change NTP server:
# vi /etc/chrony.conf:

#server time.quby.nl minpoll 8
server www.nist.gov minpoll 8

#initstepslew 30 time.quby.nl
initstepslew 30 www.nist.gov

Change ping server:
# cat /etc/hosts
# <persistent /etc/hosts content can be added to /etc/hosts.template file>
127.0.0.1		localhost.localdomain		localhost		eneco-001-002209
127.0.0.1  feed.hae.int  feed

Disable whitelist:
# vi /qmf/etc/qmf_release.xml                                   
                <enforceWhitelist>0</enforceWhitelist>        

Enable stuff:
# vi /etc/config/config_happ_scsync.xml

     <visibility>0</visibility><StartDate>1381708800</StartDate><EndDate>-1</EndDate><Status>IN_SUPPLY</Status><ProductVariant>Toon</ProductVariant
# killall happ_scsync && killall qt-gui

# reboot
```

Tweak SSH parameters to be able to copy files:

```
$ scp -oKexAlgorithms=+diffie-hellman-group1-sha1 x11vnc_0.9.13-r0_qb2.ipk root@192.168.x.y:/root
```