---
layout: post
title: My Home Assistant Setup - Part 1
slug: my-home-assistant-setup
status: published
date: 2024-02-14 09:11:56 +0000
author: Ron
excerpt: 'I use Home Assistant for quite some years now, started to run it on a Raspberry
  Pi, a NUC, later went for Home Assistant Blue, and recently bought a Home Assistant
  Yellow, specially for the built-in radio''s and faster Raspberry CM4 module. https://www.raspberrypi.com/documentation/computers/compute-module.html


  I could move over my installation vie the backup-restore method, but I want to document
  things, clean up unused code, and maybe improve older integrations. (by adding unique
  id''s, Config '
feature_image: /assets/images/2024/02/200921211689844881.2508.jpg
ghost_id: 65cc82d8e7fddf00012febb9
ghost_url: https://cyberjunky.nl/my-home-assistant-setup/
---

{% raw %}
I use Home Assistant for quite some years now, started to run it on a Raspberry Pi, a NUC, later went for Home Assistant Blue, and recently bought a Home Assistant Yellow, specially for the built-in radio's and faster Raspberry CM4 module. <https://www.raspberrypi.com/documentation/computers/compute-module.html>

I could move over my installation vie the backup-restore method, but I want to document things, clean up unused code, and maybe improve older integrations. (by adding unique id's, Config Flows etc)

So here a list in no order with all my notes, code snippets and instructions.

### The Home Assistant Yellow

Get yours here... <https://www.home-assistant.io/blog/2021/09/13/home-assistant-yellow/>

I added a WD Blue SN570 NVMe SSD

![](/assets/images/2022/11/PXL_20221012_170907869.jpg)![](/assets/images/2022/11/PXL_20221013_065307207.jpg)

After boot up, create user account, set basics like name, timezone, currency etc.  
Then go to Storage settings and move data to new drive by selecting option from the meatball/kebab menu.

### Zones

Created zones for work and home addresses, they will be used to see if the home is occupied.

### Rooms

Created the rooms I need.

![](/assets/images/2022/11/image.png)

### Add-ons

I installed the following add-ons, most of them are straightforward to install.

![](/assets/images/2022/11/image-7.png)

### Add-on DSMR-Reader

Logs my utility meter readings (more on this configuration later) add this repository to add-ons: https://github.com/sanderdw/hassio-addons/

```
WEBSERVER: Ingress
DSMRREADER_ADMIN_USER: admin
DSMRREADER_ADMIN_PASSWORD: <secret>
DJANGO_DATABASE_NAME: dsmrreader
DJANGO_DATABASE_USER: postgres
DJANGO_DATABASE_PASSWORD: <secret>
DJANGO_DATABASE_HOST: 77b2833f-timescaledb
DJANGO_DATABASE_PORT: "5432"
DSMRREADER_REMOTE_DATALOGGER_MODE: standalone
DSMRREADER_REMOTE_DATALOGGER_API_HOSTS: http(s)://<YOUR_DSMR_HOST>:<PORT>
DSMRREADER_REMOTE_DATALOGGER_API_KEYS: <YOUR_API_KEY>
DSMRREADER_REMOTE_DATALOGGER_SERIAL_PORT: /dev/ttyUSB1
DSMRREADER_REMOTE_DATALOGGER_INPUT_METHOD: serial
DSMRREADER_REMOTE_DATALOGGER_SERIAL_BAUDRATE: "115200"
DSMRREADER_REMOTE_DATALOGGER_NETWORK_HOST: x.x.x.x
DSMRREADER_REMOTE_DATALOGGER_NETWORK_PORT: x
DSMRREADER_REMOTE_DATALOGGER_SLEEP: "0.5"
DSMRREADER_LOGLEVEL: ERROR
DJANGO_FORCE_SCRIPT_NAME: ""
DJANGO_STATIC_URL: static/
```

### Add-on TimeScaleDB

Is the PostgreSQL database engine used by DSMR-Reader, I also store Home Assistant data in a PostgreSQL database instead of the default SQLite. Add this repository to get this and the pgAdmin4 management tool: https://github.com/Expaso/hassos-addons

```
databases:
  - homeassistant
  - dsmrreader
timescale_enabled:
  - homeassistant
  - dsmrreader
timescaledb:
  telemetry: basic
  maxmemory: 512MB
  maxcpus: 4
max_connections: 20
system_packages: []
init_commands: []
retry_upgrade: false
```

### Add-on WireGuard

Handy VPN tool.

```
peers:
  - addresses:
      - 172.27.xx.x
    allowed_ips: []
    client_allowed_ips: []
    name: <secret>
server:
  addresses:
    - 172.27.xx.x
  dns: []
  host: <secret url>
```

### Add-on ESPHome

Nice platform to program and control ESP board and other devices.

### Add-on Studio Code Server

Great editor, including syntax checks and variable lookup amoung other useful features.

### Packages

I choose to use the 'packages' way of organizing the .yaml files to configure home assistant.

Create a directory 'packages' inside /config, this will hold all .yaml files.

```
# Load config from packages directory
homeassistant:
  packages: !include_dir_named packages
```

*The file secrets.yaml* will hold all credentials and other sensitive values.

### Added via yaml

Twitter Notify  
Huisbot  
HVC  
WAQI  
Workday  
Twitch

### Added via GUI

Google Maps Reistijd

*Reistijd van Huis naar Werk  
Reistijd van Werk naar Huis*

Created Google Distance Matrix API, add API key to *secrets.yaml*  
Disable Automatic Polling  
Added automation to only poll during weekdays

Buienradar  
Ring  
Broadcom IR  
 *RMMINI-TELECOM-SICHUAN-50-9b-18 2.4Ghz WiFi*  
Vervaldatum Certificaat  
Maan  
KNX  
SQL

### Added via HACS

HVC Groep  
PowerCalc  
Arpscan Device Tracker Component  
iPhone Device Tracker  
Toon Climate  
Toon Boilerstats  
Toon Smartmeter  
Garmin Connect
{% endraw %}
