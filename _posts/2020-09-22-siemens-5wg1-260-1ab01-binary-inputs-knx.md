---
layout: post
title: SIEMENS 5WG1 260-1AB01 Binary Inputs
slug: siemens-5wg1-260-1ab01-binary-inputs-knx
status: published
date: 2020-09-22 17:56:55 +0000
tags:
- knx
- siemens
category: knx
author: Ron
excerpt: 'I needed binary inputs which could handle 230 Volt and simply have the option
  to send On, Off or Toggle to a Group Address using standard light switches with
  rocker-  and push switches. (for a good user experience)


  I came across a batch of old SIEMENS N260 4-fold binary inputs, for 10 Euro each,
  so I bought them,


  Just before placing the order I noticed that they have no KNX connector but use
  a data-rail connection, upon request I got a free piece of data-rail (5WG1190-8AB03)
  with it.


  Problem '
feature_image: /assets/images/2020/09/s-l16004.jpg
ghost_id: 65cc82d8e7fddf00012feba5
ghost_url: https://cyberjunky.nl/siemens-5wg1-260-1ab01-binary-inputs-knx/
---

I needed binary inputs which could handle 230 Volt and simply have the option to send On, Off or Toggle to a Group Address using standard light switches with rocker-  and push switches. (for a good user experience)

I came across a batch of old SIEMENS N260 4-fold binary inputs, for 10 Euro each, so I bought them,

Just before placing the order I noticed that they have no KNX connector but use a data-rail connection, upon request I got a free piece of data-rail (5WG1190-8AB03) with it.

Problem solved and I could also connect other adjacent SIEMENS modules at the same time.

Looking for the KNX application to load into ETS5 I noticed there are 4 different versions.

![](/assets/images/2020/09/n260appl.PNG)

Long story short; I experimented with the 'On/off/toggle/Dim/Shutter' version for a long time, and I couldn't select a toggle option so it didn't do what I wanted, bad buy.

But today I again fiddled with them and tried the 'On/off/toggle/cycl' firmware, and low and behold I could just disable the cyclic sending part and the toggle works perfectly, and if I add the Central GA for 'All On/Off' to the object states stay synced nicely!

![](/assets/images/2020/09/n260params.PNG)

Parameters for rocker switch toggle functionality

![](/assets/images/2020/09/n260paramspush.PNG)

Parameters for push button toggle functionality