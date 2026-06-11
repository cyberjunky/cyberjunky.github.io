---
layout: post
title: Invert Window Sensor state for ABB EnOcean Gateway
slug: invert-window-sensor-state-for-abb-enocean-gateway
status: published
date: 2020-09-22 17:09:10 +0000
tags:
- knx
- enocean
- home-assistant
category: knx
author: Ron
excerpt: 'I use a ABB EnOcean EG/A32.2.1 EnOcean to KNX Gateway, a wonderful device,
  but I ran into an issue where a Eltako FTKE door window sensor (F6-10-00) reported
  0 - Close; 1 - Open

  And an STM 250 window sensor (D5-00-01) reports 1 = Closed; 0 -  Open.


  So Home Assistant sees Window Open when magnet contact closed and visa versa.


  Not wanting to fiddle with Home Assistant code this time, but it turns out that
  after pairing the EnOcean contact you get two status_contacts, one enabled and one
  disabled'
feature_image: /assets/images/2020/09/gateway.jpg
ghost_id: 65cc82d8e7fddf00012feba3
ghost_url: https://cyberjunky.nl/invert-window-sensor-state-for-abb-enocean-gateway/
---

I use a ABB EnOcean EG/A32.2.1 EnOcean to KNX Gateway, a wonderful device, but I ran into an issue where a Eltako FTKE door window sensor (F6-10-00) reported 0 - Close; 1 - Open  
And an STM 250 window sensor (D5-00-01) reports 1 = Closed; 0 -  Open.

So Home Assistant sees Window Open when magnet contact closed and visa versa.

Not wanting to fiddle with Home Assistant code this time, but it turns out that after pairing the EnOcean contact you get two status\_contacts, one enabled and one disabled, if you switch them around you have a device with inverted values, happy days!

![](/assets/images/2020/09/EnOcean-Contacts.PNG)![](/assets/images/2020/09/EnOcean-Values.PNG)

The first is with inverted instance enabled, the last the default.