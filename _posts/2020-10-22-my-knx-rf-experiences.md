---
layout: post
title: My KNX RF experiences so far
slug: my-knx-rf-experiences
status: published
date: 2020-10-22 13:56:03 +0000
tags:
- knx
- rf
- ets
category: knx
author: Ron
excerpt: 'I have some sections in my house where it''s impossible to get the green
  lifeline aka the KNX Cable to reach.


  So I started to investigate the possibility of using KNX RF for those locations.
  Since it''s rather new (in KNX terms) there are already several types of KNX RF,
  I needed to find out what works together and note it down.


  Standards KNX RF, KNX RF Ready, KNX Multi, KNX RF+, mostly backwards compatible.



  KNX RF


  For retro-fit/residential, works standalone or with other media, repeater func'
feature_image: /assets/images/2020/10/RF-LK00102.png
ghost_id: 65cc82d8e7fddf00012febab
ghost_url: https://cyberjunky.nl/my-knx-rf-experiences/
---

I have some sections in my house where it's impossible to get the green lifeline aka the KNX Cable to reach.

So I started to investigate the possibility of using KNX RF for those locations. Since it's rather new (in KNX terms) there are already several types of KNX RF, I needed to find out what works together and note it down.

Standards KNX RF, KNX RF Ready, KNX Multi, KNX RF+, mostly backwards compatible.

### KNX RF

For retro-fit/residential, works standalone or with other media, repeater functionality for bigger environments, bi- and unidirectional, uses 868 MHz band.

### KNX RF 1.1 (2000)

One channel (F1)  
Short preamble  
No new certifications

### KNX RF Ready (2004)

One channel same F1 frequency  
Longer preamble  
Replaces KNX RF 1.1

### KNX RF Multi (2012)

Supports 'RF Ready'  
Has frequency agility (5 frequencies), in other words it can quickly switch channels when congestion is detected, listen before talking.  
Supports fast and slow modes  
3 fast channels F1, F2, F3 and 2 slow channels S1 and S2  
Fast acknowledge from up to 64 devices with retry if not successful, and repeaters (re-transmitters).

All these features make the KNX RF Multi very reliable and robust wireless protocol for building control applications.

### KNX RF+

Supports System Mode so you can program it completely with ETS5  
Not many devices support it yet (MDT) Backwards compatible.

### Unidirectional devices

Can either only send or receive  
Send a telegram immediately if required.  
Because of duty cycle of only 1%, collisions are rare  
Only sending devices are mainly battery operated sensors or detectors, hand-held or wall mounted transmitters, binary inputs and door/window contacts are examples.

### Bidirectional devices

Can both send and received, so they can be sensors and actuators at the same time.  
They check whether the radio channel is free before sending.  
If channel is occupied the device waits until it's free and then sends the telegram.

### Domain Addresses

RF devices send their domain address (this is 6 bytes long, allocated by ETS), only devices learned in of linked to this address can talk to each other, they got the same domain address when programmed.  
The range can be extended with 2 repeaters

TDLR; The GIRA 5103 00 works fine together with the MDT RF+ Line Coupler

### My devices

MDT RF-LK001.02 RF+ Line Coupler

GIRA 5103 00 Tastsensor 3fach

MDT RF-AKK1ST.01 Socket

MDT RF-AKK1UP.01

### MDT RF+ Line Coupler

Nothing much to say about this device, connect it to the KNX Line and place it somewhere high, or unobstructed. Since it's a line coupler it gets an x.x.0 address.

Below some settings, I disabled the filter to start with.  
Have enabled it now, remember with every device you add to or change on the RF line you have to program the Line Coupler too, so it's filter table gets updated.  
See more below for a handy ETS APP called 'MDT RF+ Range Check'

### GIRA 5103 00 Tastsensor 3fach

So knowing what you need to buy for this product line is a quest on it's own, it consists of so many parts, and the combinations (design) are endless.  
They even created an [App](https://partner.gira.com/nl_NL/schalterprogramme/designkonfigurator.html), so you can design and see how it looks on your wall using VR.

I use these parts for the first buttons:

GIRA 2133 03 Wippenset  System 55 3fach Clear White  
GIRA 0211410 E3 abdeckrahmen 1fach Alpine White  
GIRA 5103 00 RF Tastsensor 3fach  
GIRA 533900 Montageplattenset System 55

![](/assets/images/2020/10/gira-bodemplset-533900-2.jpg)

![](/assets/images/2020/10/gira-e3-afdekraam-0211410-1.jpg)

![](/assets/images/2020/10/gira-tastsensor-3fach-510300-1.jpg)

![](/assets/images/2020/10/gira-wippenset-3fach-213303-1.jpg)

![](/assets/images/2020/10/PXL_20201020_143034892-1.jpg)

One major drawback is that when you program it with ETS5 you always have to press the program button, even with partial downloads, I guess it's by design, to save battery, or not implemented in RF protocol.

The program button is located in the middle of the lowest rocker, between the text 'Bureau Lamp' and 'Alles Uit' which means you have to pry the wip loose and fold over the paper label, arggg..

### MDT RF-AKK1ST.01 Socket

I had to open one of them because something was loose inside, a small piece of plastic.

![](/assets/images/2020/10/PXL_20201020_141852801.jpg)

![](/assets/images/2020/10/PXL_20201020_142118840.jpg)

![](/assets/images/2020/10/PXL_20201020_142140380.jpg)

If you program them they do a switch off/on cycle, which can be unwanted behavior for some connected appliances. Other than that they work fine.

### MDT RF-AKK1UP.01

Not looked at yet.

### MDT RF+ Range Check App

To check the signal strength of the connected KNX RF devices a free ETS APP can be downloaded and used with the MDT RF+ Line Coupler.

![](/assets/images/2020/10/range.png)

![](/assets/images/2020/10/range2.png)

![](/assets/images/2020/10/range3.png)

![](/assets/images/2020/10/range4-1.png)