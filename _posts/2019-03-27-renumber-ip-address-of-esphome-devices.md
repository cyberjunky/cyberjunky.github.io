---
layout: post
title: Renumbering static IP address of ESPHome node
slug: renumber-ip-address-of-esphome-devices
status: published
date: 2019-03-27 15:27:14 +0000
tags:
- home-assistant-addon esphome
category: home-assistant-addon esphome
author: Ron
excerpt: "I had my network IP address range renamed because of an ISP change, and\
  \ forgot to change the static IP's of my ESPHome nodes before the switch.\n\nThese\
  \ are the steps to re-program them using the same server.\n\nFirst change the static\
  \ IP address settings in the node's config, and add another field with the old IP\
  \ address called 'use_address'\n\nwifi:\n  ssid: !secret wifi_ssid\n  password:\
  \ !secret wifi_password\n  use_address: 192.168.178.112\n\n  manual_ip:\n    static_ip:\
  \ 192.168.2.112\n    gateway: 192.1"
feature_image: /assets/images/2019/03/esphome.png
ghost_id: 65cc82d8e7fddf00012feb8c
ghost_url: https://cyberjunky.nl/renumber-ip-address-of-esphome-devices/
---

{% raw %}
I had my network IP address range renamed because of an ISP change, and forgot to change the static IP's of my ESPHome nodes before the switch.

These are the steps to re-program them using the same server.

First change the static IP address settings in the node's config, and add another field with the old IP address called 'use\_address'

```
wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  use_address: 192.168.178.112

  manual_ip:
    static_ip: 192.168.2.112
    gateway: 192.168.2.1
    subnet: 255.255.255.0
```

Then add an IP address (alias) from the old range to your Home Assistant server's Ethernet interface, mine is called 'enp2s0', this is for Ubuntu. Check if node can be reached on old address.

```
$ sudo ifconfig enp2s0:0 192.168.178.10 up
$ ping 192.168.178.112
PING 192.168.178.112 (192.168.178.112) 56(84) bytes of data.
64 bytes from 192.168.178.112: icmp_seq=1 ttl=255 time=11.8 ms
```

Then compile and upload the program the node using OTA. The node should get the new IP address after the reboot.

Remove 'use\_address' field from config and re-program, remove IP address alias from server.

```
$ sudo ifconfig enp2s0:0 192.168.178.10 down
```
{% endraw %}
