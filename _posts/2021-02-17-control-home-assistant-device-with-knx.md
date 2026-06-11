---
layout: post
title: Control Home Assistant devices with KNX group addresses
slug: control-home-assistant-device-with-knx
status: published
date: 2021-02-17 16:23:23 +0000
tags:
- knx
- home-assistant
category: knx
author: Ron
excerpt: "Had to look up some posts before I got it working, so this is a note to\
  \ myself.\n\nFirst you need to allow the KNX Group Addresses you want to trigger\
  \ on to hit Home Assistants event bus, in this example 0/0/1.\n\nknx:\n  fire_event:\
  \ true\n  fire_event_filter: [\"0/0/1\"]\n\nCorrection: 'fire_event' is deprecated.\n\
  \nThis is the correct syntax:\n\n  knx:\n    event_filter: [\"0/0/1\", \"1/0/13\"\
  ]\n\nAfter a restart you can check if the GA is visible on the bus when triggered,\
  \ open HA's developer menu, events, and ty"
feature_image: /assets/images/2021/02/knx.png
ghost_id: 65cc82d8e7fddf00012febb2
ghost_url: https://cyberjunky.nl/control-home-assistant-device-with-knx/
---

{% raw %}
Had to look up some posts before I got it working, so this is a note to myself.

First you need to allow the KNX Group Addresses you want to trigger on to hit Home Assistants event bus, in this example 0/0/1.

```
knx:
  fire_event: true
  fire_event_filter: ["0/0/1"]
```

***Correction: 'fire\_event' is deprecated.***

![](/assets/images/2021/02/eventfiltermsg.png)

This is the correct syntax:

```
  knx:
    event_filter: ["0/0/1", "1/0/13"]
```

After a restart you can check if the GA is visible on the bus when triggered, open HA's developer menu, events, and type 'knx\_event' as event and 'listen', then generated the GA transmit, press key or whatever is generating it.

![](/assets/images/2021/02/knx_event.png)

You see it contains 'data.data' with value 0 (off in this case), so we create an automation for that.

```
  - alias: "Alles Uit"
    trigger:
      platform: event
      event_type: knx_event
    condition:
      condition: template
      value_template: >
        {{ trigger.event.data.destination == '0/0/1' and trigger.event.data.data == 0 }}
    action:
      - service: light.turn_off
        data:
          entity_id: light.hobbykamer_ledstrip
```

If you want to react on more Group Addresses, you can use choose in your automation's, like so:

```
  - alias: "Trigger on KNX events"
    trigger:
      platform: event
      event_type: knx_event
    condition: []
    action:
      - choose:
          - conditions:
              - condition: template
                value_template: >-
                  {{ trigger.event.data.destination == '0/0/1' and trigger.event.data.data == 0 }}
            sequence:
              - service: light.turn_off
                data: {}
                entity_id: light.hobbykamer_ledstrip
          - conditions:
              - condition: template
                value_template: >-
                  {{ trigger.event.data.destination == '1/0/13' and trigger.event.data.data == 1 }}
            sequence:
              - service: light.turn_on
                data: {}
                entity_id: light.hobbykamer_ledstrip
          - conditions:
              - condition: template
                value_template: >-
                  {{ trigger.event.data.destination == '1/0/13' and trigger.event.data.data == 0 }}
            sequence:
              - service: light.turn_off
                data: {}
                entity_id: light.hobbykamer_ledstrip
```

It will switch off the non-KNX light 'hobbykamer\_ledstrip' when it sees a 'All Off' event on the bus, and you can toggle it on and off with another button. (using GA '1/0/13', in this case sent from a Gira RF taster)
{% endraw %}
