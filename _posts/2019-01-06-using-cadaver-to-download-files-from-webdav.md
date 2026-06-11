---
layout: post
title: Using cadaver to download files from webDAV
slug: using-cadaver-to-download-files-from-webdav
status: published
date: 2019-01-06 11:22:25 +0000
tags:
- ubuntu
category: ubuntu
author: Ron
excerpt: "My Ubuntu installation refuses to mount a particular webdave share.\n\n\
  Using a share and GUI browser is for Windows users anyway.\n\n\nSo I used cadaver\
  \ instead!\n\n\n    $ sudo apt-get cadaver\n\n\n\nConnect to your webdav share\n\
  \n\n    $ cadaver http://webdav.server.com\n\n\n\nEnter your credentials.\n\n\n\
  Now you can use the following commands to interact with WebDav and your\n\nlocal\
  \ machine:\n\n\nls – Show a list of files available in the current directory.\n\n\
  cd – Go to the specified directory.\n\nget – Download the spe"
ghost_id: 65cc82d8e7fddf00012feb80
ghost_url: https://cyberjunky.nl/using-cadaver-to-download-files-from-webdav/
---

{% raw %}
My Ubuntu installation refuses to mount a particular webdave share.  
Using a share and GUI browser is for Windows users anyway.

So I used *cadaver* instead!

```
    $ sudo apt-get cadaver
```

Connect to your webdav share

```
    $ cadaver http://webdav.server.com
```

Enter your credentials.

Now you can use the following commands to interact with WebDav and your  
local machine:

ls – Show a list of files available in the current directory.  
cd – Go to the specified directory.  
get – Download the specified file to your local hard drive.  
mget – Download multiple files to your local hard drive.  
put – Upload a file from your local hard drive to the server.  
mput – Upload multiple files from your local hard drive to the server.

```
    dav:/webdav/DomotiGaServer/> ls
    Listing collection `/webdav/DomotiGaServer/': succeeded.
            AVControl.module                    6260  Dec  6 21:31
            Astro.module                        7050  Dec  6 21:31
            ...
    dav:/webdav/DomotiGaServer/> mget *
```

For local usage just put an l in front of the commands above, so lls,  
lcd etc...  
Happy downloading!
{% endraw %}
