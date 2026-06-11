---
layout: post
title: Hosting a Ghost blog on Google Cloud
slug: hosting-a-ghost-blog-on-google-cloud
status: published
date: 2022-11-11 15:25:50 +0000
author: Ron
excerpt: 'I switched from the paid (although cheap) AWS Lightsail to Google Compute
  Engine for hosting this blog.


  NOTE: I bought the support for one month to get support on disabling DNSSEC

  I hope to run the Google Cloud VM Instance for free (using the monthly credits)


  The difference between this instance and the old one which ran at AWS is also a
  newer Debian distribution 11, and Ghost 5 instead of Ghost 3.


  Compute Engine: Virtual Machines (VMs) | Google CloudCompute Engine delivers configurable
  virtu'
feature_image: /assets/images/2022/11/gcp.png
ghost_id: 65cc82d8e7fddf00012febb8
ghost_url: https://cyberjunky.nl/hosting-a-ghost-blog-on-google-cloud/
---

I switched from the paid (although cheap) AWS Lightsail to Google Compute Engine for hosting this blog.

![](/assets/images/2022/11/Screenshot-from-2022-11-10-15-31-46.png)

NOTE: I bought the support for one month to get support on disabling DNSSEC  
I hope to run the Google Cloud VM Instance for free (using the monthly credits)

The difference between this instance and the old one which ran at AWS is also a newer Debian distribution 11, and Ghost 5 instead of Ghost 3.

[Compute Engine: Virtual Machines (VMs) | Google Cloud

Compute Engine delivers configurable virtual machines running in Google’s data centers with access to high-performance

![](https://www.gstatic.com/devrel-devsite/prod/v8b5224dd5a12318d5f6ab78c52530208ebc55112b691b517d54e8b153c58ecd1/cloud/images/favicons/onecloud/super_cloud.png)Google Cloud

![](https://cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png)](https://cloud.google.com/compute)

Google has free micro instances:

*“All customers get a general purpose machine (e2-micro instance) per month for free, not charged against your credits.”*

This is what i selected:

Zone: europe-west4-a  
Machine type: e2-micro x86/64  
Image: debian-11-bullseye-v20220920  
Disk: Standard persistent disk

Old entry based in US, just for reference:

![](/assets/images/2022/11/Screenshot-from-2022-11-10-14-35-02.png)![](/assets/images/2022/11/Screenshot-from-2022-11-10-15-15-29.png)

Don't forget to remove RDP and SSH from default firewall rules.

After creation, connect with web SSH terminal  
If you want to connect with local SSH client and/or WinSCP import the key.

### Update OS

```
vi update.sh

#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoclean
sudo apt-get clean
sudo apt-get autoremove
>~/.bash_history
history -c

chmod +x update.sh
./update.sh
```

### Install Docker

<https://docs.docker.com/engine/install/debian/>

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

[this can takes some time]

```
sudo usermod -aG docker ${USER}
```

### Install docker compose

```
sudo curl -SL https://github.com/docker/compose/releases/download/v2.12.2/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Now disconnect and reconnect to activate new group membership

### Caddy and Ghost installation

I choose `/home/${USER}/docker` as docker's base directory.

```
mkdir -p ~/docker/caddy/data
mkdir -p ~/docker/caddy/config
cd ~/docker

vi caddy/Caddyfile

{
    # Global options block. Entirely optional, https is on by default
    # Optional email key for lets encrypt
    email your@email.address
    # Optional staging lets encrypt for testing. Comment out for production.
    # acme_ca https://acme-staging-v02.api.letsencrypt.org/directory
}
yoursite.com {
    reverse_proxy ghost:2368
}
www.yoursite.nl {
    redir https://yoursite.com{uri}
}


vi docker-compose.yaml

services:
        caddy:
                image: caddy:2-alpine
                restart: always
                container_name: caddy
                ports:
                        - 443:443
                volumes:
                        - ./caddy/Caddyfile:/etc/caddy/Caddyfile
                        - ./caddy/data:/data
                        - ./caddy/config:/config
                labels:
                        - com.centurylinklabs.watchtower.enable=true

        ghost:
                image: ghost:5-alpine
                restart: always
                container_name: ghost
                ports:
                        - 2368:2368
                volumes:
                        - ./ghost/data:/var/lib/ghost/content
                environment:
                        - NODE_ENV=production
                        - url=https://yoursite.com
                        - database__client=sqlite3
                        - database__connection__filename="content/data/ghost.db"
                        - database__useNUllAsDefault=true
                        - database__debug=False
                labels:
                        - com.centurylinklabs.watchtower.enable=true

        watchtower:
        		image: v2tec/watchtower
                restart: always
                container_name: watchtower
                volumes:
                        - /var/run/docker.sock:/var/run/docker.sock
                labels:
                        - com.centurylinklabs.watchtower.enable=true
                command: --schedule "0 0 4 * * *" --cleanup --label-enable
```

As you can see I also install and run Watchtower to keep the images up to date.

Now you can start them with:

```
docker-compose start -d
```

### Backups

```
#!/bin/bash
backup_path="/home/ron/backup"
tar_opts="--exclude='/var/run/*' --exclude='/home/ron/backup/*' --exclude='/home/ron/backup-server.tar.gz' --exclude='/home/ron/docker/ghost/data/logs/*'"
cd "${BASH_SOURCE%/*}" || exit
rm -rf $backup_path
mkdir -p $backup_path
cp backup.sh update.sh $backup_path

for i in `docker inspect --format='{{.Name}}' $(docker ps -qa) | cut -f2 -d\/`
  do container_name=$i
  mkdir -p $backup_path/$container_name
  echo -n "$container_name - "
  docker run --rm \
    --volumes-from $container_name \
    -v $backup_path:/backup \
    -e TAR_OPTS="$tar_opts" \
    piscue/docker-backup \
    backup "$container_name/$container_name-volume.tar.xz"
  echo "OK"
done

tar -czvf ./backup-server.tar.gz --exclude=".[^/]*" ./backup
rm -rf $backup_path
```