---
layout: post
title: Open MS .URL shortcuts on Ubuntu
slug: open-ms-url-shortcuts-on-ubuntu
status: published
date: 2019-01-06 11:17:16 +0000
tags:
- ubuntu
category: ubuntu
author: Ron
excerpt: 'We need to create a wrapper script and associate the file type with it.



  $ sudo vi /usr/bin/open-url.sh


  #!/bin/sh

  # opens Windows .URL files in your default browser

  # requires: xdg-open sed grep xargs

  sed ''s/^BASEURL=/URL=/'' "$1" | grep -m 1 ''^URL='' | sed ''s/^URL=//'' | sed ''s/\r//''
  | xargs xdg-open




  $ sudo chmod +x /usr/bin/open-url.sh




  Now we can associate .URL files with the script. This might be the hard


  part.



  $ cp /usr/share/applications/chromium-browser.desktop ~/.local/share/appli'
ghost_id: 65cc82d8e7fddf00012feb78
ghost_url: https://cyberjunky.nl/open-ms-url-shortcuts-on-ubuntu/
---

{% raw %}
We need to create a wrapper script and associate the file type with it.

```
$ sudo vi /usr/bin/open-url.sh

#!/bin/sh
# opens Windows .URL files in your default browser
# requires: xdg-open sed grep xargs
sed 's/^BASEURL=/URL=/' "$1" | grep -m 1 '^URL=' | sed 's/^URL=//' | sed 's/\r//' | xargs xdg-open
```

```
$ sudo chmod +x /usr/bin/open-url.sh
```

Now we can associate .URL files with the script. This might be the hard  
part.

```
$ cp /usr/share/applications/chromium-browser.desktop ~/.local/share/applications/open-url.desktop
```

Change first Exec command to point to our script

```
Exec=/usr/bin/open-url.sh %U
```

Associate mime-type:

Find name of mime-type by quering a example .url file

```
$ xdg-mime query filetype ~/Desktop/p/PHP-\ uniqid\ -\ Manual.url application/x-mswinurl
$ xdg-mime default open-url.desktop application/x-mswinurl
```
{% endraw %}
