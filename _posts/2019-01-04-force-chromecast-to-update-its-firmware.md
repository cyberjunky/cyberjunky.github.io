---
layout: post
title: Force Chromecast to update it's firmware
slug: force-chromecast-to-update-its-firmware
status: published
date: 2019-01-04 10:54:01 +0000
author: Ron
excerpt: 'I noticed that some of my Google Chromecasts were on an older firmware version.


  You can force a reboot and update with this command: (insert own IP address)


  $ curl -X POST -H "Content-Type: application/json" -d ''{"params": "ota foreground"}''
  http://<YOUR IP>:8008/setup/reboot -v

  Note: Unnecessary use of -X or --request, POST is already inferred.

  *   Trying <YOUR IP>...

  * TCP_NODELAY set

  * Connected to <YOUR IP> (192.168.178.113) port 8008 (#0)

  > POST /setup/reboot HTTP/1.1

  > Host: <YOUR IP>:80'
ghost_id: 65cc82d8e7fddf00012feb66
ghost_url: https://cyberjunky.nl/force-chromecast-to-update-its-firmware/
---

{% raw %}
I noticed that some of my Google Chromecasts were on an older firmware version.

You can force a reboot and update with this command: (insert own IP address)

```
$ curl -X POST -H "Content-Type: application/json" -d '{"params": "ota foreground"}' http://<YOUR IP>:8008/setup/reboot -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying <YOUR IP>...
* TCP_NODELAY set
* Connected to <YOUR IP> (192.168.178.113) port 8008 (#0)
> POST /setup/reboot HTTP/1.1
> Host: <YOUR IP>:8008
> User-Agent: curl/7.58.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 28
> 
* upload completely sent off: 28 out of 28 bytes
< HTTP/1.1 200 OK
< Access-Control-Allow-Headers:Content-Type
< Cache-Control:no-cache
< Content-Length:0
< 
* Connection #0 to host <YOUR IP> left intact
```
{% endraw %}
