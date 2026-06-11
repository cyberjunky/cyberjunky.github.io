---
layout: post
title: Move TTN Kickstarter LORA Gateway to V3 network
slug: move-ttn-gateway-to-v3
status: published
date: 2021-06-25 14:27:44 +0000
tags:
- thethingsnetwork
- lora
- ttn
category: thethingsnetwork
author: Ron
excerpt: "Finally had some time to move my TTN gateway from V2 to V2 network. Here\
  \ are the steps and screenshots.\n\nPrerequisites:\n- Running v1.08 gateway firmware\
  \ (beta)\n- User account for TTN console (Community Edition)\n\nVisit https://www.thethingsindustries.com/docs/download/\
  \ for the options\n\n 1. Create a gateway in V3.\n    a. Visit https://eu1.cloud.thethings.network/console/gateways/add\
  \ if you live in Europe.\n    b. Give the gateway a name. (Gateway ID)\n    c. Choose\
  \ the frequency plan 'Europe 863-870"
feature_image: /assets/images/2021/06/Screenshot-from-2021-06-25-14-40-26.png
ghost_id: 65cc82d8e7fddf00012febb7
ghost_url: https://cyberjunky.nl/move-ttn-gateway-to-v3/
---

Finally had some time to move my TTN gateway from V2 to V2 network. Here are the steps and screenshots.  
  
Prerequisites:  
- Running v1.08 gateway firmware (beta)  
- User account for TTN console (Community Edition)  
  
Visit <https://www.thethingsindustries.com/docs/download/> for the options

1. Create a gateway in V3.  
   a. Visit <https://eu1.cloud.thethings.network/console/gateways/add> if you live in Europe.  
   b. Give the gateway a name. (Gateway ID)  
   c. Choose the frequency plan 'Europe 863-870 MHz (SF9 for RX2 - recommended)' I'm a Dutch guy.  
   d. Save
2. Goto V3 gateway API Settings  
   a. Select Add API key  
   b. Provide a name  
   c. Select 'Grant Individual Rights'  
   d. Choose 'Link as Gateway to a Gateway Server for traffic exchange, i.e. write uplink and read downlink  
   e. Generate API key  
   f.  Copy key to clipboard and store safely, you can only look at it now.  
   g. Click 'I have copied the key'
3. Now we need to enter the new settings inside of the gateway  
   a. Power cycle gateway with holding the pink reset button inside for 5 seconds.  
   b. Browse to it's local website to fill in the gateway settings (I use wired LAN, so I skip the WLAN part)  
   c. In Account server field replace <https://account.thethingsnetwork.org> with the URL from V3 <https://eu1.cloud.thethings.network/>  
   d. At Gateway Key fill in the API key from 2f.  
   e. Save

After creation the new gateway show 'Disconnected':

![](/assets/images/2021/06/Screenshot-from-2021-06-25-14-39-57.png)

Filling in the new settings:

![](/assets/images/2021/06/Screenshot-from-2021-06-25-14-40-56.png)

The gateway will now restart and connect to the new V3 enviroment:

![](/assets/images/2021/06/Screenshot-from-2021-06-25-14-40-26-1.png)

A few moments later you will see it online, if all goes well:

![](/assets/images/2021/06/Screenshot-from-2021-06-25-14-41-44.png)

Success!