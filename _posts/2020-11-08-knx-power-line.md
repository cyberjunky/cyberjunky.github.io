---
layout: post
title: KNX with a power-line IP backbone
slug: knx-power-line
status: published
date: 2020-11-08 15:30:18 +0000
tags:
- knx
- ets
- powerline
- fritz!box
category: knx
author: Ron
excerpt: 'Like I wrote here I wanted to see if I could connect my Shed with KNX via
  power-line since I have no means of getting the KNX data bus there, and KNX RF doesn''t
  support extending a line over KNX RF. (Yet, I don''t know what ETS6 brings)


  I could have done all with KNX-RF(+) devices, but there are no KNX RF weather stations.


  So I started to created a test installation, also for enhancing my practical KNX
  knowledge about bus types.


  I knew I needed to replace my IP gateway with two IP routers, so '
feature_image: /assets/images/2020/11/title.png
ghost_id: 65cc82d8e7fddf00012febad
ghost_url: https://cyberjunky.nl/knx-power-line/
---

{% raw %}
Like I wrote [here](https://cyberjunky.nl/updating-a-gira-2167-00-ip-router/) I wanted to see if I could connect my Shed with KNX via power-line since I have no means of getting the KNX data bus there, and KNX RF doesn't support extending a line over KNX RF. (Yet, I don't know what ETS6 brings)

I could have done all with KNX-RF(+) devices, but there are no KNX RF weather stations.

So I started to created a test installation, also for enhancing my practical KNX knowledge about bus types.

I knew I needed to replace my IP gateway with two IP routers, so I bought two secondhand GIRA 2671 00 routers (index 04 and 10), flashed them both with the latest firmware, factory reset and configured them.

![](/assets/images/2020/11/iprouters.png)

So I now needed to configure an IP backbone, on the KNX Module E course and exam IP backbones were only mentioned briefly, not practical.

This is what I did to get it to work.

First in Topology set backbone ('Hooflijn') type to IP (most of the time this is already the case), I changed the default multicast address from 224.0.0.31 to another one in that range, since I read issues when using the default one together with FRITZ!box devices. This address is automatically used by the IP routers below (you cannot change this setting there)

Created 'IP Woonhuis' line and set type to IP as well, choosing one of the GIRA IP routers in LAN (called 'KNX/IP Router') as bus connector.

Created 'IP Schuur' line, with same settings but choosing the other GIRA IP router in LAN (called 'GIRA KNX/IP router') as the bus connector.

I enabled filtering (normal) on both IP -> Bus and Bus -> IP settings.  
Remember if you change and addresses or add devices behind any of the IP routers you need to Download them as well to update their filter tables.

The GIRA 2671 00 routers support 'reliable communication', mainly for connections over WLAN I guess, but I enabled the setting on both IP routers anyway.

This is what it looks like:

![](/assets/images/2020/11/schuur.png)

![](/assets/images/2020/11/toplogy.png)

![](/assets/images/2020/11/woonhuis.png)

![](/assets/images/2020/11/hoofdlijn-1.png)

I first tested with both routers connected to same network switch, then I had a look at the FRITZ!Powerline 510E modules I bought, they are one of the cheapest and only do 100Mbit, but this is more than enough for extending a 9600 baud bus ;-)

When I bought them I didn't know that they integrate so well in the rest of the FRITZ! products, they become part of the network Mesh and you can even update the firmware via the FRITZ!box GUI, which I did. I had to pair them again afterwards. (simply pressing the  'Security' button)

They encrypt the data communication using AES-128-Bit, so that's nice.

![](/assets/images/2020/11/powerline-1.png)

I plugged in the remote KNX installation (I also needed an extra KNX power supply) and everything is working fine, and reliable!

![](/assets/images/2020/11/powerline-module.jpg)![](/assets/images/2020/11/PXL_20201108_135337848.jpg)

You also see the infamous SIEMENS data-rails 190 5WG1-190-8AB02 in action (well actually you can't see it because it's covered by all the modules), but all SIEMENS devices are connected to the KNX bus by using it, the REG 191/01 5WG1 191–5AB01 module is used to get the IP router connected to that rail, and the weather-station will use it also later, saves on wiring though.

**Note: this setup is fine for an residential hobbyist, but not for industrial or commercial purposes.**
{% endraw %}
