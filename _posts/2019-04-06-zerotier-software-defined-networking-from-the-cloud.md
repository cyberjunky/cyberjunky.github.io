---
layout: post
title: ZeroTier One SDN from the cloud
slug: zerotier-software-defined-networking-from-the-cloud
status: published
date: 2019-04-06 15:44:58 +0000
tags:
- sdn
- vpn
- hass.io add-on
category: sdn
author: Ron
excerpt: 'I never heard of ZeroTier One until Frenck created a Hass.io Add-on for
  it.


  To start using it, first create a free ZeroTier One account and create a network
  to get the network-id needed for the add-on settings, then install the add-on, fill
  in the network-id and start it. Check log for succesful startup.


  It should show up as connected device in the network settings. Authorise the connected
  device, and install the ZeroTier One client on the computer from which you want
  to connect to the home ne'
feature_image: /assets/images/2019/04/zt.png
ghost_id: 65cc82d8e7fddf00012feb8f
ghost_url: https://cyberjunky.nl/zerotier-software-defined-networking-from-the-cloud/
---

{% raw %}
I never heard of [ZeroTier One](https://www.zerotier.com/) until Frenck created a [Hass.io Add-on](https://github.com/hassio-addons/addon-zerotier) for it.

To start using it, first create a free ZeroTier One account and create a network to get the network-id needed for the add-on settings, then install the add-on, fill in the network-id and start it. Check log for succesful startup.

It should show up as connected device in the network settings. Authorise the connected device, and install the ZeroTier One client on the computer from which you want to connect to the home network. Create and enter an API token, and the network-id, also authorize the device in your ZeroTier One Admin portal.

NOTE: I had to restart my Windows instance before it showed the connected network stats in the ZeroTier One client.

You should now be able to ping the remote IP address and login to your Hass.io instance.
{% endraw %}
