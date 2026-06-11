---
layout: post
title: Quick webserver for Toon Home Assistant development
slug: quick-webserver-for-toon-home-assistent-development
status: published
date: 2023-12-23 17:42:30 +0000
author: Ron
excerpt: "import http.server\nimport socketserver\nfrom http import HTTPStatus\n\n\
  class MyServer(http.server.SimpleHTTPRequestHandler):\n    \n    def do_GET(self):\n\
  \        \n        # toon_smartmeter\n        if self.path == '/hdrv_zwave?action=getDevices.json':\n\
  \            filename = \"getDevices.json\"\n        # toon_climate\n        elif\
  \ self.path == '/happ_thermstat?action=getThermostatInfo':\n            filename\
  \ = \"getThermostatInfo.json\"\n        \n        if self.path:\n            try:\n\
  \                f = open"
feature_image: /assets/images/2024/02/maxresdefault.jpg
ghost_id: 65cc82d8e7fddf00012febbb
ghost_url: https://cyberjunky.nl/quick-webserver-for-toon-home-assistent-development/
---

{% raw %}
```
import http.server
import socketserver
from http import HTTPStatus

class MyServer(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        
        # toon_smartmeter
        if self.path == '/hdrv_zwave?action=getDevices.json':
            filename = "getDevices.json"
        # toon_climate
        elif self.path == '/happ_thermstat?action=getThermostatInfo':
            filename = "getThermostatInfo.json"
        
        if self.path:
            try:
                f = open(filename, 'rb')
            except OSError:
                self.send_error(HTTPStatus.NOT_FOUND, "File not found")
                return None

            self.send_response(200)
            self.send_header("Content-type", "text/javascript")
            self.end_headers()

            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()
        else:
            super().do_GET()

# Main
handler_object = MyServer
PORT = 8080

print(f'Started listening on port {PORT}')

try:
    socketserver.TCPServer.allow_reuse_address = True
    my_server = socketserver.TCPServer(("", PORT), handler_object)
    my_server.serve_forever()

finally:
    print('Closing')
    my_server.server_close()
```
{% endraw %}
