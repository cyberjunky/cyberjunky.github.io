---
layout: post
title: Docker Monitor sensor for Home Assistant
slug: docker-monitor-sensor-for-home-assistant
status: published
date: 2019-01-21 20:54:28 +0000
tags:
- home-assistant
- custom_components
- docker
category: home-assistant
author: Ron
excerpt: "Found an interesting custom component sensor called docker_monitor.py here.\n\
  But since I use Hass.io it couldn't open docker's UNIX socket, this post describes\
  \ how to enable and use the TCP based API instead.\n\nCopy docker_monitor.py to\
  \ your custom_components/sensor directory, create a sensor in your home assistant\
  \ config like so, and define the containers you want to monitor.\n\n  - platform:\
  \ docker_monitor\n    host: tcp://192.168.179.10:2375\n    containers:\n      -\
  \ homeassistant\n      - hassio_sup"
feature_image: /assets/images/2019/01/docker_version-1.png
ghost_id: 65cc82d8e7fddf00012feb89
ghost_url: https://cyberjunky.nl/docker-monitor-sensor-for-home-assistant/
---

{% raw %}
Found an interesting custom component sensor called docker\_monitor.py [here](https://gist.github.com/Sanderhuisman/e609a99682854d9f880f8334b7194558).  
But since I use Hass.io it couldn't open docker's UNIX socket, this post describes how to enable and use the TCP based API instead.

Copy docker\_monitor.py to your custom\_components/sensor directory, create a sensor in your home assistant config like so, and define the containers you want to monitor.

```
  - platform: docker_monitor
    host: tcp://192.168.179.10:2375
    containers:
      - homeassistant
      - hassio_supervisor
      - portainer
      - watchtower
    monitored_conditions:
      - utilization_version
      - container_status
      - container_memory_usage
      - container_memory_percentage_usage
      - container_cpu_percentage_usage
```

To enable docker's TCP API do this:

```
$ sudo vi /lib/systemd/system/docker.service
```

Change ExecStart line to:

```
ExecStart=/usr/bin/docker daemon -H fd:// -H tcp://0.0.0.0
```

Reload systemd and restart docker service

```
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker.service
```

Check if it's listening on port 2375

```
$ ss -ntl|grep 2375
LISTEN     0      128         :::2375                    :::*
```

Restart your Home Assistant

I have these groups defined:

```
Docker Monitor:
  - sensor.docker_version
  - sensor.docker_hassio_supervisor_status
  - sensor.docker_hassio_supervisor_cpu_use
  - sensor.docker_hassio_supervisor_memory_use
  - sensor.docker_hassio_supervisor_memory_use_percent
  - sensor.docker_homeassistant_status
  - sensor.docker_homeassistant_cpu_use
  - sensor.docker_homeassistant_memory_use
  - sensor.docker_homeassistant_memory_use_percent
  - sensor.docker_portainer_status
  - sensor.docker_portainer_cpu_use
  - sensor.docker_portainer_memory_use
  - sensor.docker_portainer_memory_use_percent
  - sensor.docker_watchtower_status
  - sensor.docker_watchtower_cpu_use
  - sensor.docker_watchtower_memory_use
  - sensor.docker_watchtower_memory_use_percent
```

Customization:

```
  sensor.docker_version:
    friendly_name: 'Docker Version'
  sensor.docker_hassio_supervisor_status:
    friendly_name: 'Hass.io Status'
  sensor.docker_hassio_supervisor_cpu_use:
    friendly_name: 'Hass.io CPU Usage'
  sensor.docker_hassio_supervisor_memory_use:
    friendly_name: 'Hass.io Memory Usage'
  sensor.docker_hassio_supervisor_memory_use_percent:
    friendly_name: 'Hass.io Memory %'
  sensor.docker_homeassistant_status:
    friendly_name: 'Home Assistant Status'
  sensor.docker_homeassistant_cpu_use:
    friendly_name: 'Home Assistant CPU Usage'
  sensor.docker_homeassistant_memory_use:
    friendly_name: 'Home Assistant Memory Usage'
  sensor.docker_homeassistant_memory_use_percent:
    friendly_name: 'Home Assistant Memory %'
  sensor.docker_portainer_status:
    friendly_name: 'Portainer Status'
  sensor.docker_portainer_cpu_use:
    friendly_name: 'Portainer CPU Usage'
  sensor.docker_portainer_memory_use:
    friendly_name: 'Portainer Memory Usage'
  sensor.docker_portainer_memory_use_percent:
    friendly_name: 'Portainer Memory %'
  sensor.docker_watchtower_status:
    friendly_name: 'Watchtower Status'
  sensor.docker_watchtower_cpu_use:
    friendly_name: 'Watchtower CPU Usage'
  sensor.docker_watchtower_memory_use:
    friendly_name: 'Watchtower Memory Usage'
  sensor.docker_watchtower_memory_use_percent:
    friendly_name: 'Watchtower Memory %'
```

![](/assets/images/2019/01/docker_monitor.png)

![](/assets/images/2019/01/docker_version.png)

![](/assets/images/2019/01/docker_usage.png)

Resources:  
<https://gathering.tweakers.net/forum/list_message/57718722#57718722>  
<https://docker-py.readthedocs.io/en/stable/client.html>
{% endraw %}
