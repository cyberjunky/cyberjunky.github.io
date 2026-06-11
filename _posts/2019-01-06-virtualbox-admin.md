---
layout: post
title: Virtualbox Admin
slug: virtualbox-admin
status: published
date: 2019-01-06 11:23:06 +0000
tags:
- virtualbox
- linux
category: virtualbox
author: Ron
excerpt: "I run several machines on top of Virtual Box on Debian (headless).\n\nHere\
  \ some notes I made...\n\n\nInstall latest version from virtualbox site\n\n\nThe\
  \ one in Ubuntu's repo is old\n\n\n    $ sudo vi /etc/apt/sources.list  \n\n\n\n\
  add this line:\n\n\n    deb http://download.virtualbox.org/virtualbox/debian trusty\
  \ contrib\n\n    $ wget -q http://download.virtualbox.org/virtualbox/debian/oracle\\\
  _vbox.asc -O- | sudo apt-key add -  \n    $ sudo apt-get update  \n    $ sudo apt-get\
  \ install virtualbox-4.3\n\n\n\nUpdates\n\n\nBef"
ghost_id: 65cc82d8e7fddf00012feb81
ghost_url: https://cyberjunky.nl/virtualbox-admin/
---

{% raw %}
I run several machines on top of Virtual Box on Debian (headless).  
Here some notes I made...

**Install latest version from virtualbox site**

The one in Ubuntu's repo is old

```
    $ sudo vi /etc/apt/sources.list
```

add this line:

```
    deb http://download.virtualbox.org/virtualbox/debian trusty contrib

    $ wget -q http://download.virtualbox.org/virtualbox/debian/oracle\_vbox.asc -O- | sudo apt-key add -  
    $ sudo apt-get update  
    $ sudo apt-get install virtualbox-4.3
```

**Updates**

Before upgrading the virtualbox package make sure the VM's are shutdown  
otherwise this prevents the upgrade to run smoothly.

Shut them down via sudo shutdow -h now, or via Virtualbox admin page.  
On the host machine

```
    sudo apt-get update
    sudo apt-get upgrade
```

**Update Extension Pack**

After this update (including virtualbox)  
Make sure you update the VirtualBox Extension Pack to the same version  
(now 4.3.12)

Check currently installed version with

```
    # VBoxManage list extpacks
    Pack no. 0:   Oracle VM VirtualBox Extension Pack
    Version:      4.3.8
    Revision:     92456
    Edition:      
    Description:  USB 2.0 Host Controller, Host Webcam, VirtualBox RDP, PXE ROM with E1000 support.
    VRDE Module:  VBoxVRDP
    Usable:       true 
    Why unusable:
```

Visit <https://www.virtualbox.org/wiki/Downloads> and copy link behind  
'All supported platforms'  
Currently  
[http://download.virtualbox.org/virtualbox/4.3.12/Oracle\\_VM\\_VirtualBox\\_Extension\\_Pack-4.3.12-93733.vbox-extpack](http://download.virtualbox.org/virtualbox/4.3.12/Oracle%5C_VM%5C_VirtualBox%5C_Extension%5C_Pack-4.3.12-93733.vbox-extpack)

So as root on host machine:

```
    # wget http://download.virtualbox.org/virtualbox/4.3.12/Oracle_VM_VirtualBox_Extension_Pack-4.3.12-93733.vbox-extpack
    # VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-4.3.12-93733.vbox-extpack --replace
    0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
    Successfully installed "Oracle VM VirtualBox Extension Pack".

    # VBoxManage list extpacks
    Extension Packs: 1
    Pack no. 0:   Oracle VM VirtualBox Extension Pack
    Version:      4.3.12
    Revision:     93733
    Edition:      
    Description:  USB 2.0 Host Controller, Host Webcam, VirtualBox RDP, PXE ROM with E1000 support.
    VRDE Module:  VBoxVRDP
    Usable:       true 
    Why unusable:
```

Cleanup old installs

```
    # VBoxManage extpack cleanup
    Successfully performed extension pack cleanup
```

**Fix 'not finding module vboxdrv' after upgrade**

```
    sudo dpkg-reconfigure virtualbox-4.2 
    sudo service vboxdrv restart
    sudo service vboxweb-service restart
```

**List passthrough USB devices**

```
    # VBoxManage list usbhost
    VirtualBox Command Line Management Interface Version 3.1.2
    (C) 2005-2009 Sun Microsystems, Inc.
    All rights reserved.

    Host USB Devices:

    UUID: b6efd3fd-051f-48ea-9a33-e484363f19d5
    VendorId: 0x04b3 (04B3)
    ProductId: 0x310b (310B)
    Revision: 1.96 (0196)
    Address: {745A17A0-74D3-11D0-B6FE-00A0C90F57DA}001
    Current State: Busy

    UUID: 5caaa4a1-7164-4630-9593-fce070b515dd
    VendorId: 0x090c (090C)
    ProductId: 0×1000 (1000)
    Revision: 16.41 (1641)
    Manufacturer: USB
```

**VM Autostart**

```
    $ sudo mkdir /etc/vbox
    $ sudo vi /etc/vbox/autostart.cfg

    default_policy = deny
    vbox = {
        allow = true
    }

    $ sudo chown -R vbox:vbox /etc/vbox

    Enable autostart on the VM's you want to autostart, the machine must be stopped when doing this.

    $ VBoxManage modifyvm  --autostart-enabled on
```

**Install PHPVirtualBox**

```
    $ cd ~/install
    $ wget `wget -q -O - http://phpvirtualbox.googlecode.com/files/LATEST.txt` -O phpvirtualbox-latest.zip
    $ unzip phpvirtualbox-latest.zip

    $ sudo mv phpvirtualbox-4.2-4 /var/www/phpvirtualbox

    $ cd /var/www/phpvirtualbox
    $ sudo cp config.php-example config.php
    $ sudo vi config.php
```

**Install LinuxAdditions on VM's**

Attach ISO file to DVD drive

```
    $ mount /dev/sr0
    $ cd /media/cdrom
    $ sh ./VBoxLinuxAdditions.sh
```
{% endraw %}
