---
layout: post
title: Push TOON P1 data to DSMR Reader
slug: push-toon-p1-data-to-dsmr-on-docker
status: published
date: 2019-01-22 15:34:57 +0000
tags:
- solar
- slimme meter
- toon
- dsmr
category: solar
author: Ron
excerpt: 'I wanted to see what DSMR reader can tell from my power and gas usage over
  time, and also to get an insight in the costs. This until I have build a dashboard
  with the same functionality with Grafana.


  But I have no P1 reader other than TOON''s meteradapter which data I already read
  via http for Home Assistant and PVOutput. I could Home Assistant push data to DSMR,
  but instead to safe time I created a small Python script which I call every 10 seconds.


  Install dsmr-docker via docker-compose.yml by'
feature_image: /assets/images/2019/01/landisgyr.png
ghost_id: 65cc82d8e7fddf00012feb8a
ghost_url: https://cyberjunky.nl/push-toon-p1-data-to-dsmr-on-docker/
---

{% raw %}
I wanted to see what DSMR reader can tell from my power and gas usage over time, and also to get an insight in the costs. This until I have build a dashboard with the same functionality with Grafana.

But I have no P1 reader other than TOON's meteradapter which data I already read via http for Home Assistant and PVOutput. I could Home Assistant push data to DSMR, but instead to safe time I created a small Python script which I call every 10 seconds.

Install dsmr-docker via docker-compose.yml by adding these lines and running docker-compose up -d

```
  dsmrdb:
    image: postgres:10.5-alpine
    container_name: dsmrdb
    volumes:
      - dsmrdb:/var/lib/postgresql/data
      - dsmrdb_backups:/dsmr/backups
    restart: always
    labels:
      - com.centurylinklabs.watchtower.enable=true
    environment:
      - POSTGRES_USER=dsmrreader
      - POSTGRES_PASSWORD=dsmrreader
      - POSTGRES_DB=dsmrreader

  dsmr:
    image: xirixiz/dsmr-reader-docker
    container_name: dsmr
    depends_on:
      - dsmrdb
    cap_add:
      - NET_ADMIN
    links:
      - dsmrdb
    restart: always
    labels:
      - com.centurylinklabs.watchtower.enable=true
    environment:
      - DB_HOST=dsmrdb
      - DSMR_USER=admin
      - DSMR_EMAIL=admin@localhost.nl
      - DSMR_PASSWORD=admin
      - VIRTUAL_HOST=localhost
    ports:
      - 7777:80
      - 7779:443

volumes:
  ...
  dsmrdb:
  dsmrdb_backups:
```

Then browse to <IP>:7777 and enable the API, and copy you AUTH KEY.

![](/assets/images/2019/01/apiauth.png)

Create this script, fill in your IP address for your TOON and DSMR server, and the AUTH KEY you copied.

```
#!/usr/bin/python

import requests
import json
import time
import datetime

energy = requests.get('http://<YOUR TOON IP>:10080/hdrv_zwave?action=getDevices.json', timeout=5).json()

electricity_delivered_1 = float(energy["dev_3.5"]["CurrentElectricityQuantity"])/1000
electricity_returned_1 = float(energy["dev_3.6"]["CurrentElectricityQuantity"])/1000
electricity_delivered_2 = float(energy["dev_3.3"]["CurrentElectricityQuantity"])/1000
electricity_returned_2 = float(energy["dev_3.4"]["CurrentElectricityQuantity"])/1000
electricity_currently_delivered = float(energy["dev_3.5"]["CurrentElectricityFlow"])/1000 + float(energy["dev_3.3"]["CurrentElectricityFlow"])/1000
electricity_currently_returned = float(energy["dev_3.4"]["CurrentElectricityFlow"])/1000 + float(energy["dev_3.6"]["CurrentElectricityFlow"])/1000
timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
extra_device_timestamp = timestamp
extra_device_delivered = float(energy["dev_3.1"]["CurrentGasQuantity"])/1000

#print(extra_device_delivered)
#print(extra_device_timestamp)
#print(electricity_delivered_1)
#print(electricity_delivered_2)
#print(electricity_returned_1)
#print(electricity_returned_2)
#print(electricity_currently_delivered)
#print(electricity_currently_returned)
#print(timestamp)

response = requests.post(
    'http://<YOUR DSMR IP>:7777/api/v2/datalogger/dsmrreading',
    headers={'X-AUTHKEY': '<YOUR AUTH KEY>'},
    data={
        'electricity_currently_delivered': electricity_currently_delivered,
        'electricity_currently_returned': electricity_currently_returned,
        'electricity_delivered_1': electricity_delivered_1,
        'electricity_delivered_2': electricity_delivered_2,
        'electricity_returned_1': electricity_returned_1,
        'electricity_returned_2': electricity_returned_2,
        'timestamp': timestamp,
        'extra_device_timestamp': extra_device_timestamp,
        'extra_device_delivered': extra_device_delivered,
    }
)

#if response.status_code != 201:
#    print('Error: {}'.format(response.text))
#else:
#    print('Created: {}'.format(json.loads(response.text)))
```

It may be needed to adapt the dev\_x\_x entries to yours, just enable the print command and check the output.

Create a cronjob by adding a crontab entry like this:

```
* * * * * ( sleep 10 ; /usr/bin/python /home/docker/scripts/pushreading.py )
```

After a few minutes the dashboard should show you your usage

![](/assets/images/2019/01/dashboard.png)

Disable MQTT since I don't use it and to prevent these log entries:

```
2019-01-23 07:26:24,370 INFO spawned: 'dsmr_mqtt' with pid 40
2019-01-23 07:26:25,390 INFO success: dsmr_mqtt entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)
2019-01-23 07:27:25,725 INFO exited: dsmr_mqtt (exit status 1; not expected)
2019-01-23 07:27:26,078 INFO spawned: 'dsmr_mqtt' with pid 42
2019-01-23 07:27:27,101 INFO success: dsmr_mqtt entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)
```

```
$ vi /etc/supervisor.d/supervisord.ini
[program:dsmr_mqtt]
command=/bin/nice -n 15 python3 -u /dsmr/manage.py dsmr_mqtt
pidfile=/var/tmp/dsmrreader--%(program_name)s.pid
autostart=false
autorestart=false
```

Restart container
{% endraw %}
