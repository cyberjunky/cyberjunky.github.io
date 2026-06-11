---
layout: post
title: '''All On/Off'' only switch Off for KNX Central Group Address'
slug: all-off-only-switch-for-knx-central-group-address
status: published
date: 2020-09-22 16:45:59 +0000
tags:
- knx
- home-assistant
category: knx
author: Ron
excerpt: "I had an issue where i have an All On/Off Central group address in KNX but\
  \ I didn't want to be able to do a Switch On All for a switch from Home Assistant.\n\
  \nI came up with a template switch like this:\n\nknx:\n   switch:\n      - name:\
  \ 'Alles Uit/Aan'\n        address: '0/0/1'\n\n\n\nswitch:\n - platform: template\n\
  \   switches:\n     alles_uit:\n       friendly_name: \"Alles Uit\"\n       value_template:\
  \ \"{{ is_state('switch.alles_uit_aan', 'off') }}\"\n       turn_on:\n         service:\
  \ switch.turn_off\n         d"
feature_image: /assets/images/2020/09/7297401.jpg
ghost_id: 65cc82d8e7fddf00012feba2
ghost_url: https://cyberjunky.nl/all-off-only-switch-for-knx-central-group-address/
---

{% raw %}
I had an issue where i have an All On/Off Central group address in KNX but I didn't want to be able to do a Switch On All for a switch from Home Assistant.

I came up with a template switch like this:

```
knx:
   switch:
      - name: 'Alles Uit/Aan'
        address: '0/0/1'
```

```
switch:
 - platform: template
   switches:
     alles_uit:
       friendly_name: "Alles Uit"
       value_template: "{{ is_state('switch.alles_uit_aan', 'off') }}"
       turn_on:
         service: switch.turn_off
         data:
           entity_id: switch.alles_uit_aan
       turn_off:
         service: switch.turn_off
         data:
           entity_id: switch.alles_uit_aan
```
{% endraw %}
