---
layout: post
title: Migrate a Redmine site to another server
slug: migrate-a-redmine-site-to-another-server
status: published
date: 2019-01-06 11:14:47 +0000
tags:
- redmine
category: redmine
author: Ron
excerpt: "On current server:\n\n\n    # service apache2 stop\n    # cd /opt/redmine/files\n\
  \    # scp -r * root@:/opt/redmine/files\n\n\n\nMake MySQL backup\n\n\n    # mysqldump\
  \ -u root -p redmine >/root/dump.sql\n    # scp /root/dump.sql root@1:/root\n\n\n\
  \nOn new server:\n\n\n    # cd /opt/redmine/files\n    # chown -R www-data:www-data\
  \ *\n\n\n\nDelete test database (is needed) and reload new database\n\n\n    # mysqladmin\
  \ -u root -p drop redmine\n    # mysqladmin -u root -p create redmine\n    # mysql\
  \ -u root -p redmine \n\n\n\nReload/m"
ghost_id: 65cc82d8e7fddf00012feb74
ghost_url: https://cyberjunky.nl/migrate-a-redmine-site-to-another-server/
---

{% raw %}
On current server:

```
    # service apache2 stop
    # cd /opt/redmine/files
    # scp -r * root@:/opt/redmine/files
```

Make MySQL backup

```
    # mysqldump -u root -p redmine >/root/dump.sql
    # scp /root/dump.sql root@1:/root
```

On new server:

```
    # cd /opt/redmine/files
    # chown -R www-data:www-data *
```

Delete test database (is needed) and reload new database

```
    # mysqladmin -u root -p drop redmine
    # mysqladmin -u root -p create redmine
    # mysql -u root -p redmine
```

```
Reload/migrate redmine data and plugins
```

```
    # rake db:migrate RAILS_ENV=production
    # rake redmine:plugins:migrate RAILS_ENV=production

    # rake tmp:cache:clear
    # rake tmp:sessions:clear

    # service apache2 restart
```
{% endraw %}
