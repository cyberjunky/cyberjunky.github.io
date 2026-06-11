---
layout: post
title: Installing Debian 9 image for Beagle Bone Black Cape KNX 1-Wire
slug: building-image-for-beagle-bone-black
status: published
date: 2019-04-01 19:22:25 +0000
tags:
- linux
- knx
- beaglebone
category: linux
author: Ron
excerpt: "Installation commands and log for building your own image with KNX and 1-wire\
  \ support.\n\n\nInstall and configure the 1-wire daemon\n\n# Download base image:\
  \ \nhttps://rcn-ee.net/rootfs/2018-09-11/flasher/BBB-eMMC-flasher-debian-9.5-console-armhf-2018-09-11-2gb.img.xz\n\
  \n# Write to 2GB micro sd card\nhttps://learn.adafruit.com/beaglebone-black-installing-operating-systems/flashing-the-beaglebone-black\n\
  \n# Look for bbgw's IP address in DHCP and login using SSH\nssh 192.168.178.122\
  \ \n\nUser: debian\nPassword: t"
feature_image: /assets/images/2019/04/IBBCape-KOE-Produktbild.jpg
ghost_id: 65cc82d8e7fddf00012feb8d
ghost_url: https://cyberjunky.nl/building-image-for-beagle-bone-black/
---

{% raw %}
Installation commands and log for building your own image with KNX and 1-wire support.

## Install and configure the 1-wire daemon

```
# Download base image: 
https://rcn-ee.net/rootfs/2018-09-11/flasher/BBB-eMMC-flasher-debian-9.5-console-armhf-2018-09-11-2gb.img.xz

# Write to 2GB micro sd card
https://learn.adafruit.com/beaglebone-black-installing-operating-systems/flashing-the-beaglebone-black

# Look for bbgw's IP address in DHCP and login using SSH
ssh 192.168.178.122 

User: debian
Password: temppwd

$ sudo passwd root
$ root

$ useradd ron --home/home/ron -c /bin/bash
$ passwd ron

# Logout/in
$ userdel --remove debian

cat update.sh
#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoclean
sudo apt-get clean
sudo apt-get autoremove
> ~/.bash_history
history -c
dpkg -l | awk '/^rc/ {print $2}' | xargs sudo dpkg --purge

./update/sh

# Rename hostname
In /etc/hosts and /etc/hostname „arm“ replace „bbbgw“

$ sudo dpkg-reconfigure locales
$ sudo reboot

$ dpkg-reconfigure tzdata

# Install 1-wire daemon
$ apt-get install owserver owhttpd
$ sudo vi /etc/owfs.conf
Replace lines „FAKE“ with
server: i2c = dev/i2c-2:0
server: i2c = dev/i2c-3:0
server: i2c = dev/i2c-4:0
server: i2c = dev/i2c-5:0

$ sudo service --status-all
 [ + ]  acpid
 [ - ]  alsa-utils
 [ + ]  apache-htcacheclean
 [ + ]  apache2
 [ + ]  avahi-daemon
 [ + ]  bluetooth
 [ + ]  connman
 [ - ]  console-setup.sh
 [ + ]  cpufrequtils
 [ + ]  cron
 [ - ]  cryptdisks
 [ - ]  cryptdisks-early
 [ + ]  dbus
 [ + ]  dnsmasq
 [ + ]  dundee
 [ + ]  fake-hwclock
 [ + ]  haveged
 [ - ]  hostapd
 [ - ]  hwclock.sh
 [ - ]  keyboard-setup.sh
 [ + ]  kmod
 [ - ]  knxd
 [ + ]  loadcpufreq
 [ - ]  networking
 [ + ]  ofono
 [ + ]  owhttpd
 [ + ]  owserver
 [ - ]  pppd-dns
 [ + ]  procps
 [ - ]  rsync
 [ + ]  rsyslog
 [ + ]  ssh
 [ - ]  sudo
 [ + ]  udev
 [ - ]  udhcpd

# Reboot

# Browse to http://IP:2121 click „bus.0“ you should see the onboard Temperature sensor „28.xxxxxxx“
```

![](/assets/images/2020/09/1-wire.png)

## Install and configure the Knxd daemon for KNX support

```
# Install knxd 

$ sudo apt-get install git-core build-essential fakeroot debhelper libusb-1.0 libsystemd-dev dh-systemd libev-dev libfmt3-dev 
$ git clone https://github.com/knxd/knxd.git

$ cd knxd
$ dpkg-buildpackage -b -uc

$ cd ..
$ sudo dpkg -i knxd_*.deb knxd-tools_*.deb
---
Selecting previously unselected package knxd.
(Reading database ... 32886 files and directories currently installed.)
Preparing to unpack knxd_0.14.25-1_armhf.deb ...
Unpacking knxd (0.14.25-1) ...
Selecting previously unselected package knxd-tools.
Preparing to unpack knxd-tools_0.14.25-1_armhf.deb ...
Unpacking knxd-tools (0.14.25-1) ...
Setting up knxd (0.14.25-1) ...
Adding group `knxd' (GID 114) ...
Done.
Adding system user `knxd' (UID 109) ...
Adding new user `knxd' (UID 109) with group `knxd' ...
Creating home directory `/var/lib/knxd' ...
Created symlink /etc/systemd/system/multi-user.target.wants/knxd.service ? /lib/systemd/system/knxd.service.
Created symlink /etc/systemd/system/network-online.target.wants/knxd.service ? /lib/systemd/system/knxd.service.
Created symlink /etc/systemd/system/sockets.target.wants/knxd.socket ? /lib/systemd/system/knxd.socket.
Setting up knxd-tools (0.14.25-1) ...
Processing triggers for systemd (232-25+deb9u4) ...
Processing triggers for libc-bin (2.24-11+deb9u3) ...
---

Set static ip
$ vi /etc/network/interfaces
# The primary network interface
iface eth0 inet static
    address 192.168.178.14
    netmask 255.255.255.0
    gateway 192.168.178.1
    dns-nameservers 192.168.178.1
    post-up route add -net 224.0.23.12 netmask 255.255.255.255 eth0
    pre-down route del -net 224.0.23.12 netmask 255.255.255.255 eth0

$ update-rc.d -f dhcpd remove

org
/usr/bin/eibd -e 1.1.0 -c -S -D -i -T –tpuarts-disch-reset –tpuarts-ack-all-group -t0123 -u –pid-file=/var/run/eibd.pid tpuarts:/dev/ttyO2

ini
–daemon=/var/log/eibd.log -D -T -R -S -i -u -t1023 –eibaddr=1.1.128 usb:1:4:1:0:0?

You can create the content of the ini file by running the following command. Change everything after knxd_args to your own settings:
/usr/lib/knxd_args -e1.1.65 -E1.1.66:8 -i -u -b tpuarts:/dev/ttyO2 -D -R -T -S


/usr/lib/knxd_args -e1.1.65 -E1.1.66:8 -i -u -b tpuarts:/dev/ttyO2 -D -R -T -S
[A.tcp]
server = knxd_tcp
systemd-ignore = true
[B.unix]
server = knxd_unix
systemd-ignore = true
[C.tpuarts]
device = /dev/ttyO2
driver = tpuart
[debug-server]
name = mcast:knxd
[main]
addr = 1.1.65
client-addrs = 1.1.66:8
connections = A.tcp,B.unix,C.tpuarts,server
systemd = systemd
[server]
debug = debug-server
discover = true
router = router
server = ets_router
tunnel = tunnel

Give permission to knxd
$ sudo usermod -a -G tty knxd
$ sudo usermod -a -G dialout knxd

#KNXD_OPTS="-e 1.1.0 -c -S -D -i -T –tpuarts-disch-reset –tpuarts-ack-all-group -t0123 -u –pid-file=/var/run/eibd.pid tpuarts:/dev/ttyO2"
#KNXD_OPTS="-e 0.0.0 -c --no-tunnel-client-queuing  tpuarts:/dev/ttyO2 -D -R -T -S"
#KNXD_OPTS="-e 0.0.1 -E 0.0.2:8 -u /tmp/eib -b ip:"


Works with debug
[A.tpuarts]
debug = debug-A.tpuarts
device = /dev/ttyO2
driver = tpuart
[debug-A.tpuarts]
error-level = 0x9
trace-mask = 0x3ff
[debug-server]
name = mcast:knxd
[main]
addr = 0.0.1
client-addrs = 0.0.2:8
connections = server,A.tpuarts
systemd = systemd
[server]
debug = debug-server
discover = true
router = router
server = ets_router
tunnel = tunnel

$ sudo vi /etc/udev/rules.d/70-knxd.rules
ACTION=="add", SUBSYSTEM=="tty", KERNELS="ttyS2", SYMLINK+="knx1", OWNER="knxd"

$ udevadm control --reload-rules && udevadm trigger

Change the knxd.ini for knxd.conf ile according to your needs. The interface is /dev/ttyKNX1 from now on!
To restart udev: udevadm control --reload-rules && udevadm trigger
See if /dev/ttyKNX1 is available and linking to /dev/ttyAMA0. If not, reboot and/or retry the steps above or just change the entry "ttyKNX1" to "ttyAMA0" accordingly. Actually it doesn't matter too much.

Restart knxd:
$ sudo systemctl stop knxd.socket
$ sudo systemctl stop knxd.service
$ sudo systemctl start knxd.socket
$ sudo systemctl start knxd.service

Debug

$ knxd -e 0.0.1 -E 0.0.2:8 -D -T -R -S -f9 -t1023 -b tpuarts:/dev/ttyS2

Update knxd:
$ rm knxd*.deb
$ cd knxd
$ git pull
$ dpkg-buildpackage -b -uc
$ cd ..
$ sudo dpkg -i knxd_*.deb knxd-tools_*.deb
```
{% endraw %}
