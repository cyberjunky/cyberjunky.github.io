---
layout: post
title: Omnik Inverter serial sensor for Home Assistant
slug: omnik-inverter-serial-sensor-for-home-assistant
status: published
date: 2019-01-06 19:13:00 +0000
tags:
- wemo
- arduino
- sensor
- home-assistant
- omnik
category: wemo
author: Ron
excerpt: 'For a long time I wanted to disconnect my Omnik Inverter from my WiFi network
  and stop uploading it''s data to the Omnik portal https://www.omnikportal.com/


  The Omnik inverter also couldn''t connect to the Meraki AP I have, it showed an
  empty SSID for the MAC addresses, (it probably didn''t understand the multiple SSID
  broadcast-ed from one AP) so I had to enable a separate Wifi network via my FRITZ!Box
  just to get it connected. And I also queried the Omnik for it''s data using Omnik-Stats-Logger
  ('
feature_image: /assets/images/2019/01/photo.jpg
ghost_id: 65cc82d8e7fddf00012feb86
ghost_url: https://cyberjunky.nl/omnik-inverter-serial-sensor-for-home-assistant/
---

For a long time I wanted to disconnect my Omnik Inverter from my WiFi network and stop uploading it's data to the Omnik portal <https://www.omnikportal.com/>

The Omnik inverter also couldn't connect to the Meraki AP I have, it showed an empty SSID for the MAC addresses, (it probably didn't understand the multiple SSID broadcast-ed from one AP) so I had to enable a separate Wifi network via my FRITZ!Box just to get it connected. And I also queried the Omnik for it's data using Omnik-Stats-Logger (<https://github.com/Woutrrr/Omnik-Data-Logger>) sending the data to PVoutput, and then downloading it back into Home Assistant. ;P

I could have had enabled the MQTT output of Omnik-Stats-Logger, but then I still have the WiFi connect and data upload concerns. I took a more direct approach, after looking at the following projects.

<https://www.curioustimo.nl/2017/11/28/esp32-omniksol-solar-pv-to-mqtt-gateway/>  
<https://www.instructables.com/id/Omnik-Inverter-Off-Its-Cloud-and-on-My-MQTT/>

I came with the idea that I want to created a sensor using a WEMOS D1 mini and a OLED 64x48 pixel shield (which I had in stock) and let it connect to my Omnik AP over WiFi and as direct as possible to Home Assistant.

I merged the code from above links to one version, and stripped out all MQTT stuff, and added OLED display code to have some visual status info. I also added a status value (Offline/Online) and the ID of the inverter.

The WiFi side of the WEMOS connects to the Omnik WiFi card which is set to AP mode, and has strong credentials, isolating it from my WiFi/LAN network.

The USB port of the WEMOS is plugged into my Home Assistant server, serving JSON data on it's serial port which is read by a Serial Sensor <https://www.home-assistant.io/components/sensor.serial/>

The Serial Sensor code of HA seems very smart, it recognizes the JSON data automatically, and stores the fields as it's attributes.

You can find my Arduino code here: <https://github.com/cyberjunky/wemosomnikserialsensor/>

Open the Arduino code in Arduino IDE and change the name of Omnik AP with your own usually this is "AP\_<SERIALNO>" also enter your passphrase and your serial number. The last one is used to calculate the Magic String to query the inverter.

Before compiling the code using Arduino IDE you need to install the following libraries:

- ArduinJson library from <https://github.com/bblanchon/ArduinoJson>
- OLED library from <https://www.arduinolibraries.info/libraries/adafruit-ssd1306-wemos-mini-oled> (if you also use the 64x48 display which is a unusual dimension it seems)
- Adafruit GFX library from <https://github.com/adafruit/Adafruit-GFX-Library>

All by simply 'Include .ZIP library'

And install Wemos D1 board support:

- Wemos D1 by Entering <https://arduino.esp8266.com/stable/package_esp8266com_index.json> into Additional Board, and installing esp8266 by SparkFun Electronics from Boards Manager

This is the sensor configuration I use with Home Assistant:

```
sensor:
  - platform: serial
    name: "Omnik Sensor"
    serial_port: /dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0
    baudrate: 9600

  - platform: template
    sensors:
      omnik_sensor_inverter_status:
        friendly_name: 'Inverter Status'
        value_template: '{{ states.sensor.omnik_sensor.attributes["Status"] }}'
      omnik_sensor_inverter_id:
        friendly_name: 'Inverter ID'
        value_template: '{{ states.sensor.omnik_sensor.attributes["ID"] }}'
      omnik_sensor_power_generation:
        friendly_name: 'Huidige Levering'
        value_template: '{{ states.sensor.omnik_sensor.attributes["PowerAC"] }}'
        unit_of_measurement: 'Watt'
      omnik_sensor_voltageac:
        friendly_name: 'Voltage AC'
        value_template: '{{ states.sensor.omnik_sensor.attributes["VoltageAC"] }}'
        unit_of_measurement: 'Volt'
      omnik_sensor_currentac:
        friendly_name: 'Stroom AC'
        value_template: '{{ states.sensor.omnik_sensor.attributes["CurrentAC"] }}'
        unit_of_measurement: 'A'
      omnik_sensor_frequency:
        friendly_name: 'Frequentie AC'
        value_template: '{{ states.sensor.omnik_sensor.attributes["FrequencyAC"] }}'
        unit_of_measurement: 'Hz'
      omnik_sensor_energy_generation_today:
        friendly_name: 'Gegenereerd Vandaag'
        value_template: '{{ states.sensor.omnik_sensor.attributes["EnergyToday"] }}'
        unit_of_measurement: 'Wh'
      omnik_sensor_energy_generation_total:
        friendly_name: 'Totaal Gegenereerd'
        value_template: '{{ states.sensor.omnik_sensor.attributes["TotalEnergy"] }}'
        unit_of_measurement: 'kWh'
      omnik_sensor_voltagepv:
        friendly_name: 'Voltage Paneel'
        value_template: '{{ states.sensor.omnik_sensor.attributes["PVVoltageDC"] }}'
        unit_of_measurement: 'Volt'
      omnik_sensor_currentpv:
        friendly_name: 'Stroom Paneel'
        value_template: '{{ states.sensor.omnik_sensor.attributes["PVCurrentDC"] }}'
        unit_of_measurement: 'A'
      omnik_sensor_temperature:
        friendly_name: 'Temperatuur Inverter'
        value_template: '{{ states.sensor.omnik_sensor.attributes["Temperature"] }}'
        unit_of_measurement: '°C'
      omnik_sensor_total_hours:
        friendly_name: 'Totaal Uren'
        value_template: '{{ states.sensor.omnik_sensor.attributes["TotalHours"] }}'
        unit_of_measurement: 'Uur'

homeassistant:
  customize:
    sensor.energy_consumption:
      hidden: true
    sensor.energy_using:
      hidden: true
    sensor.omnik_sensor_inverter_status:
      icon: mdi:flash-circle
    sensor.omnik_sensor_inverter_id:
      icon: mdi:label
    sensor.omnik_sensor_power_generation:
      icon: mdi:solar-power
    sensor.omnik_sensor_voltageac:
      icon: mdi:current-ac
    sensor.omnik_sensor_currentac:
      icon: mdi:current-ac
    sensor.omnik_sensor_frequency:
      icon: mdi:current-ac
    sensor.omnik_sensor_energy_generation_today:
      icon: mdi:calendar-today
    sensor.omnik_sensor_voltagepv:
      icon: mdi:current-dc
    sensor.omnik_sensor_currentpv:
      icon: mdi:current-dc
    sensor.omnik_sensor_temperature:
      icon: mdi:temperature-celsius
    sensor.omnik_sensor_total_hours:
      icon: mdi:clock-outline

group:
  solar:
   name: 'Omnik Inverter'
   entities:
     - sensor.omnik_sensor_inverter_status
     - sensor.omnik_sensor_inverter_id
     - sensor.omnik_sensor_power_generation
     - sensor.omnik_sensor_voltageac
     - sensor.omnik_sensor_currentac
     - sensor.omnik_sensor_frequency
     - sensor.omnik_sensor_energy_generation_today
     - sensor.omnik_sensor_energy_generation_total
     - sensor.omnik_sensor_voltagepv
     - sensor.omnik_sensor_currentpv
     - sensor.omnik_sensor_temperature
     - sensor.omnik_sensor_total_hours
```

This results in these cards with information:

![](/assets/images/2019/01/inverter_online.png)

![](/assets/images/2019/01/inverter_offline.png)

![](/assets/images/2019/01/omniksensor_attrib.png)

![](/assets/images/2019/01/generation.png)

When the inverter is offline (at night) it's still pushing data to home-assistant, but only the stats, the live data is left out.

I still upload the data to PVOutput.org but now using home-assistant automation. I upload used power along with it as well. (taken from my toon\_smartmeter custom component)

```
automation:
- alias: 'Upload Omnik data en verbruik naar PVOutput.org'
  trigger:
    - platform: time
      minutes: '/5'
      seconds: 00
  action:
    - service: rest_command.pvoutput_addstatus


rest_command:
  pvoutput_addstatus:
    url: "https://pvoutput.org/service/r2/addstatus.jsp?sid=XXXXX&key=XXXXXXXXXXXXXXXXXXXXXXXXXXX&d={{now().strftime('%Y%m%d&t=%H:%M')}}&v2={{states.sensor.omnik_sensor_power_generation.state|int}}&v4={{states.sensor.stroom_verbruik.state|int}}&v5={{states.sensor.omnik_sensor_temperature.state|float}}&v6={{states.sensor.omnik_sensor_voltagepv.state|float}}"
```

Resources:

- <https://wiki.wemos.cc/products:d1:d1_mini>
- <https://www.dennisdeal.com/products/wemosr-0-66-inch-oled-shield-for-wemos-d1-mini-64x48-iic-i2c-compatible>
- <https://www.home-assistant.io/components/sensor.serial/>