---
layout: post
title: ESPHome revised AKA native API
slug: esphome-revised-aka-native-api
status: published
date: 2019-01-10 19:29:05 +0000
tags:
- arduino
- home-assistant
- wemo
- home-assistant-addon esphome
category: arduino
author: Ron
excerpt: 'ESPhomeyaml was already a great add-on for Home Assistant, you could program,
  compile and flash an ESP node just from your browser. And if you wanted to update
  it, you just compiled it again and used OTA flashing, auto-reboot node and up again.


  It uses MQTT to communicate with Home Assistant. Point was I only ran MQTT broker
  for that purpose, all other devices were connected via another binding. So it was
  nice to see that ESPhomeyaml version 1.10.0 (now called ESPHome btw) now has it''s
  own nati'
feature_image: /assets/images/2019/01/esphomelogo.png
ghost_id: 65cc82d8e7fddf00012feb87
ghost_url: https://cyberjunky.nl/esphome-revised-aka-native-api/
---

{% raw %}
ESPhomeyaml was already a great add-on for Home Assistant, you could program, compile and flash an ESP node just from your browser. And if you wanted to update it, you just compiled it again and used OTA flashing, auto-reboot node and up again.

It uses MQTT to communicate with Home Assistant. Point was I only ran MQTT broker for that purpose, all other devices were connected via another binding. So it was nice to see that ESPhomeyaml version 1.10.0 (now called ESPHome btw) now has it's own native API for Home Assistant.

The nodes report directly to the add-on on port 6053.

I used [this guide](https://esphomelib.com/esphomeyaml/components/api.html#api-mqtt-to-native) to migrate away from MQTT, the sensors were named the same at the old ones.

It's stable for half a day already, so I could remove the MQTT broker add-on afterwards.

I'm running a WEMOS D1 mini with 4 Dallas temperature sensors connected, to monitor the water temperatures going from an to the CV (central heating)

With [this sensor](https://esphomelib.com/esphomeyaml/components/dallas.html) defined in this code:

```
esphomeyaml:
  name: espcv
  platform: ESP8266
  board: d1_mini

wifi:
  ssid: 'MySSID'
  password: 'MyPassphrase'

 # Optional manual IP
  manual_ip:
    static_ip: 192.168.x.y
    gateway: 192.168.x.1
    subnet: 255.255.255.0

api:

# Enable logging
# logger:

ota:
  password: 'MyOTAPasswd'

dallas:
  - pin: GPIO2
  
sensor:
- platform: dallas
  address: 0xC3000801C04CBE10
  name: "Tap Kraan Temperatuur"
- platform: dallas
  address: 0xE0000802D086C510
  name: "CV Aanvoer Temperatuur"
- platform: dallas
  address: 0x55000802D0D39110
  name: "CV Retour Temperatuur"
- platform: dallas
  address: 0x86000802CFB91010
  name: "Tap Douche Temperatuur"
```

```
group:
  CV Ketel:
    view: false
    entities:
      - sensor.cv_aanvoer_temperatuur
      - sensor.cv_retour_temperatuur
      - sensor.tap_douche_temperatuur
      - sensor.tap_kraan_temperatuur
```

![](/assets/images/2019/01/cvesp.png)

![](/assets/images/2019/01/cvespgraph.png)

![](/assets/images/2019/01/esphome.PNG)

Because of this native support you can also use native Home Assistant services from the nodes itself!

```
# In some trigger
on_...:
  # Simple
  - homeassistant.service:
      service: notify.html5
      data:
        title: Button was pressed
  # With templates and variables
  - homeassistant.service:
      service: notify.html5
      data:
        title: New Humidity
      data_template:
        message: The humidity is {{ my_variable }}%.
      variables:
        my_variable: |-
          return id(my_sensor).state;
```

Resources:

- <https://esphomelib.com/index.html>
- <https://esphomelib.com/esphomeyaml/components/sensor/dallas.html>
{% endraw %}
