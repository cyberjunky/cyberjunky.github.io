---
layout: post
title: How to install Wallabag on Debian
slug: how-to-install-wallabag-on-debian
status: published
date: 2023-12-23 17:23:07 +0000
author: Ron
excerpt: 'Was looking for a tool to store my bookmarks and items to read. Did this
  by sending myself e-mails which was not very clean...


  I opted to move to Wallabag, so installed it on a VPS like so.


  Install Debian 12, with minimal installation and SSH terminal selected.


  Wallabag needs PHP and Nginx


  su -

  apt install sudo

  adduser user sudo

  sudo apt update && sudo apt upgrade


  sudo apt install git make composer

  sudo apt install php-fpm php-mysql php-bcmath php-xml php-zip php-curl php-mbstring
  php-gd ph'
feature_image: /assets/images/2024/02/unnamed.png
ghost_id: 65cc82d8e7fddf00012febba
ghost_url: https://cyberjunky.nl/how-to-install-wallabag-on-debian/
---

Was looking for a tool to store my bookmarks and items to read. Did this by sending myself e-mails which was not very clean...

I opted to move to Wallabag, so installed it on a VPS like so.

Install Debian 12, with minimal installation and SSH terminal selected.

Wallabag needs **PHP** and **Nginx**

```
su -
apt install sudo
adduser user sudo
sudo apt update && sudo apt upgrade

sudo apt install git make composer
sudo apt install php-fpm php-mysql php-bcmath php-xml php-zip php-curl php-mbstring php-gd php-tidy php-tokenizer nginx composer  sqlite3 php-sqlite3 certbot python3-certbot-nginx

sudo mkdir -p /var/www/wallabag.cyberjunky.nl/{public_html,logs}
sudo vi /etc/nginx/sites-available/wallabag.cyberjunky.nl

server {
server_name wallabag.cyberjunky.nl; # Change this to fit your needs
root /var/www/wallabag.cyberjunky.nl/public_html/web;
access_log /var/www/wallabag.cyberjunky.nl/logs/access.log;
error_log /var/www/wallabag.cyberjunky.nl/logs/error.log;
location / {
    try_files $uri /app.php$is_args$args;
}
location ~ ^/app\.php(/|$) {
    fastcgi_pass unix:/run/php/php8.2-fpm.sock; # Change this to fit your needs
    fastcgi_split_path_info ^(.+\.php)(/.*)$;
    include fastcgi_params;
    fastcgi_param  SCRIPT_FILENAME  $realpath_root$fastcgi_script_name;
    fastcgi_param DOCUMENT_ROOT $realpath_root;
    internal;
}
}

sudo ln -s /etc/nginx/sites-available/wallabag.cyberjunky.nl /etc/nginx/sites-enabled/wallabag.cyberjunky.nl

sudo git clone https://github.com/wallabag/wallabag.git /var/www/wallabag.cyberjunky.nl/public_html/

sudo chown -R www-data:www-data /var/www/wallabag.cyberjunky.nl
sudo -u www-data /bin/bash

cd /var/www/wallabag.cyberjunky.nl/public_html/ && make install
```

Give these answers:

```
database_driver (pdo_mysql): pdo_sqlite 
database_driver_class (null): 
database_host (127.0.0.1): 
database_port (null): 
database_name (wallabag): 
database_user (root): 
database_password (null): 
database_path (null): /var/www/wallabag.cyberjunky.nl/data
database_table_prefix (wallabag_): 
database_socket (null): 
database_charset (utf8mb4): 
domain_name ('https://your-wallabag-url-instance.com'): https://wallabag.cyberjunky.nl
mailer_transport (smtp): 
mailer_host (127.0.0.1): smtp.gmail.com
mailer_user (null): user@gmail.com
mailer_password (null): user-password
locale (en): 
secret (ovmpmAWXRCabNlMgzlzSGwdstrghGv): 
twofactor_auth (true): false
twofactor_sender (no-reply@wallabag.org): user@gmail.com
fosuser_registration (true): 
fosuser_confirmation (true):      
from_email (no-reply@wallabag.org): user@gmail.com
rss_limit (50): 
rabbitmq_host (localhost): 
rabbitmq_port (5672): 
rabbitmq_user (guest): 
rabbitmq_password (guest): 
rabbitmq_prefetch_count (10): 
redis_scheme (tcp): 
redis_host (localhost): 
redis_port (6379): 
redis_path (null): 
redis_password (null):
```

Reply yes, when asked to reset the database, and create the admin user.

```
ctrl-c
sudo certbot --nginx -d wallabag.cyberjunky.nl
sudo systemctl restart nginx
```