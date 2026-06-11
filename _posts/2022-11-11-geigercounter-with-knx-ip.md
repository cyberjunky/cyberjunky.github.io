---
layout: post
title: Geigercounter with KNX IP
slug: geigercounter-with-knx-ip
status: published
date: 2022-11-11 14:21:48 +0000
author: Ron
excerpt: 'Having a KNX IP backbone with IP routers working I wanted to see if I can
  build some DIY sensors using it, and check if this is a stable solution for non-critical
  use cases.


  After building a module using ESPHome, I thought of converting it using KNX IP (ie.
  broadcast over WiFi to a broadcast address to report sensor values)


  Install Arduino IDE if not done yet.


  Go to https://www.arduino.cc/en/software and download version for your OS.


  On Linux do not install via sudo apt install Arduino, it''s'
feature_image: /assets/images/2022/11/geigercounter.jpeg
ghost_id: 65cc82d8e7fddf00012febae
ghost_url: https://cyberjunky.nl/geigercounter-with-knx-ip/
---

Having a KNX IP backbone with IP routers working I wanted to see if I can build some DIY sensors using it, and check if this is a stable solution for non-critical use cases.

After building a module using ESPHome, I thought of converting it using KNX IP (ie. broadcast over WiFi to a broadcast address to report sensor values)

Install Arduino IDE if not done yet.

Go to <https://www.arduino.cc/en/software> and download version for your OS.

On Linux do not install via *sudo apt install Arduino*, it's old!

Unpack the archive and run *sudo ./install.sh* from it.

Next, open Arduino IDE and go to [File => Preferences]. A dialog box appears. In this box, an additional board manager URL text box is present.

- Copy and paste the following URL into the box and click OK to download the packages.
- <http://arduino.esp8266.com/stable/package_esp8266com_index.json>
- Go to board manager and look for esp8266, install it.
- Then select board Wemo D1 from the board's menu.

Now we need to install the esp-knx-ip library.

Go to the GitHub page and under releases download the zip, I have version <https://github.com/envy/esp-knx-ip/archive/0.4.0.zip>

[envy/esp-knx-ip

A KNX/IP library for the ESP8266 with Arduino. Contribute to envy/esp-knx-ip development by creating an account on GitHub.

![](https://github.githubassets.com/favicons/favicon.svg)GitHubenvy

![](https://avatars0.githubusercontent.com/u/241552?s=400&v=4)](https://github.com/envy/esp-knx-ip)

- Open Sketch menu Library menu, select Include Library and Add .ZIP Library
- Select downloaded archive

Do the same with the ESP8266 library from here, <https://github.com/esp8266/Arduino/releases/download/2.7.4/esp8266-2.7.4.zip>

- Open Boards manager and install *esp8266*

[esp8266/Arduino

ESP8266 core for Arduino. Contribute to esp8266/Arduino development by creating an account on GitHub.

![](https://github.githubassets.com/favicons/favicon.svg)GitHubesp8266

![](https://avatars0.githubusercontent.com/u/8943775?s=400&v=4)](https://github.com/esp8266/Arduino)