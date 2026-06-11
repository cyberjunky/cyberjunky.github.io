---
layout: post
title: Geigercounter with ESPHome
slug: geigercounter-with-esphome
status: published
date: 2020-03-19 15:12:34 +0000
tags:
- esphome
- home-assistant
category: esphome
author: Ron
excerpt: "I had this Geiger counter DIY Kit for Arduino laying around for a long time\
  \ and decided to connect it to my Home Assistant installation using ESPHome.\n\n\
  I'm using a Wemos D1 mini, even though the counter works at 5V and the IO pins accept\
  \ a max. voltage of 3.2V it works and hasn't damage the input. (disclaimer)\n\n\
  Connect the pins as follows:\n\n\n\n\nWemos D1\nGeigercounter\n\n\n\n\nGND\nGND\n\
  \n\n5V\n5V\n\n\nD2 (GPIO4)\nINT\n\n\n\n\n\nesphome:\n  name: <YOURPLUGNAME>\n  platform:\
  \ ESP8266\n  board: esp01_1m\n\nwifi:\n  ssid: \"<WI"
feature_image: /assets/images/2020/03/radiation-detector-arduino-kit.jpg
ghost_id: 65cc82d8e7fddf00012feb97
ghost_url: https://cyberjunky.nl/geigercounter-with-esphome/
---

I had this Geiger counter DIY Kit for Arduino laying around for a long time and decided to connect it to my Home Assistant installation using ESPHome.

I'm using a Wemos D1 mini, even though the counter works at 5V and the IO pins accept a max. voltage of 3.2V it works and hasn't damage the input. (disclaimer)

Connect the pins as follows:

| Wemos D1 | Geigercounter |
| --- | --- |
| GND | GND |
| 5V | 5V |
| D2 (GPIO4) | INT |

![](/assets/images/2020/03/Lolin-D1-Mini-V3-1-0-Wemos-Wifi-Internet-Van-Dingen-Development-Board-Gebaseerd-ESP8266-4.jpg_q50.jpg)

```
esphome:
  name: <YOURPLUGNAME>
  platform: ESP8266
  board: esp01_1m

wifi:
  ssid: "<WIFISSID>"
  password: "<WIFIPASSWORD>"

# Enable logging
logger:

# Enable Home Assistant API
api:
  password: "<YOURPASSWORD>"

ota:
  password: "<YOURPASSWORD>"

sensor:
  - platform: pulse_counter
    pin: GPIO4
    name: "Geiger Counter"
    update_interval: 15s
    unit_of_measurement: 'μSv/h'
    filters:
      - multiply: 0.006315
      # https://github.com/radhoo/uradmonitor_kit1/issues/16
```

Above the code for the ESPHome node, after compile and upload, auto discover it using integrations and define a Lovelace entry like so:

```
              - type: entities
                entities:
                  - entity: sensor.geiger_counter
```

![](/assets/images/2020/03/geiger.png)

Resources:

[Geiger Counter Radiation Detector DIY Kit Arduino Compatible ver. 3.00 | RH Electronics

Radiation Detector DIY Kit ver. 3.00The third edition of our Nuclear Radiation DIY Detector Kit. Arduino compatible kit. Easy assembly for beginners. Support many popular 400V and 500V Geiger Tubes. The kit has several improvements in compare to previously sold second editions. The package comes wit…

![](https://static.wixstatic.com/media/e43988_d2c34975cd2048adb17f0b189d801c60~mv2.jpg/v1/fill/w_32%2Ch_32%2Clg_1%2Cusm_0.66_1.00_0.01/e43988_d2c34975cd2048adb17f0b189d801c60~mv2.jpg)RH ElectronicsRHElectronics

![](https://static.wixstatic.com/media/e43988_c1b267bf11984739b2471428541fd3fc~mv2.jpg/v1/fit/w_500,h_500,q_90/file.jpg)](https://www.rhelectronics.store/radiation-detector-geiger-counter-diy-kit-second-edition)

<https://wiki.wemos.cc/products:d1:d1_mini>