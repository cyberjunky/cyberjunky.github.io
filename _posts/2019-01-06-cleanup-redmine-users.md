---
layout: post
title: Cleanup Redmine users
slug: cleanup-redmine-users
status: published
date: 2019-01-06 11:07:14 +0000
tags:
- redmine
- mysql
category: redmine
author: Ron
excerpt: "Startup MySQL tool\n\n\n    # mysql -u root -p redmine\n\n\n\nMaybe first\
  \ use below queries with SELECT to see what matches there are,\n\nbefore running\
  \ with DELETE.\n\nThese will show records with state register from 7 days or older.\n\
  \n\n    DELETE FROM tokens WHERE action='register' and created_on < now() - INTERVAL\
  \ 7 DAY;\n\n    DELETE FROM users WHERE status=2 and created_on < now() - INTERVAL\
  \ 7 DAY;\n\n    DELETE FROM tokens WHERE action='register';\n    DELETE FROM users\
  \ WHERE status=2;\n"
ghost_id: 65cc82d8e7fddf00012feb69
ghost_url: https://cyberjunky.nl/cleanup-redmine-users/
---

{% raw %}
Startup MySQL tool

```
    # mysql -u root -p redmine
```

Maybe first use below queries with SELECT to see what matches there are,  
before running with DELETE.  
These will show records with state register from 7 days or older.

```
    DELETE FROM tokens WHERE action='register' and created_on < now() - INTERVAL 7 DAY;

    DELETE FROM users WHERE status=2 and created_on < now() - INTERVAL 7 DAY;

    DELETE FROM tokens WHERE action='register';
    DELETE FROM users WHERE status=2;
```
{% endraw %}
