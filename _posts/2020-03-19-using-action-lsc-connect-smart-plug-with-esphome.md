---
layout: post
title: Using LSC Smart Connect's Power Plug with ESPHome
slug: using-action-lsc-connect-smart-plug-with-esphome
status: published
date: 2020-03-19 07:29:57 +0000
tags:
- esphome
- home-assistant
- hack
category: esphome
author: Ron
excerpt: "In this post I describe the steps needed to prepare a LSC Smart Connect\
  \ power plug -sold by Action- for use with Home Assistant/ESPHome. I simply gathered\
  \ instructions I found on the web.\n\nYou need to be able to solder thin copper\
  \ wires on the Smart Plug's circuit board. All steps are at your own risk!\n\n 1.\
  \ Open the plug by undoing the two small screws at the bottom. There are two internal\
  \ plastic clips on the opposite side. You now see the small ESP board standing upright,\
  \ this is the TYWE3L mo"
feature_image: /assets/images/2019/09/smartplug.jpeg
ghost_id: 65cc82d8e7fddf00012feb92
ghost_url: https://cyberjunky.nl/using-action-lsc-connect-smart-plug-with-esphome/
---

In this post I describe the steps needed to prepare a LSC Smart Connect power plug -sold by Action- for use with Home Assistant/ESPHome. I simply gathered instructions I found on the web.

You need to be able to solder thin copper wires on the Smart Plug's circuit board. All steps are at your own risk!

1. Open the plug by undoing the two small screws at the bottom. There are two internal plastic clips on the opposite side. You now see the small ESP board standing upright, this is the TYWE3L module, see it's datasheet below under resources. The connections are as follows:

![](/assets/images/2019/10/connectmodule.png)

So TX en RX are the two middle ones from the six connections on the board. 3v3 is at bottom left, make sure that your FTDI module is set to 3v3 VCC because this plug get its power from the FDTI, powered by mains would be to dangerous. (The Action LED strip with 12V can be flashed using it's own power)

Module <-> FTDI-dapter  
3V3 <-> VCC  
GND <-> GND  
RX <-> TX  
TX <-> RX  
I00 <-> GND (only during boot)

Create a new device config inside your ESPhome installation with this configuration and compile the binary.

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

switch:
  - platform: gpio
    pin: 12
    name: "ESP switch"
    id: relay
    on_turn_on:
      - switch.turn_on: blue_led
    on_turn_off:
      - switch.turn_off: blue_led
  
  - platform: gpio
    pin: 
      number: GPIO04
      inverted: yes
    id: blue_led
    internal: yes
    
binary_sensor:
  - platform: gpio
    pin:
      number: GPIO14
      inverted: True
    name: "ESP Switch Button"
    on_press: 
      then:
        - switch.toggle: relay
    internal: yes    
    ```
```