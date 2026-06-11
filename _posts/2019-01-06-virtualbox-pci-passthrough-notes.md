---
layout: post
title: Virtualbox PCI Passthrough Notes
slug: virtualbox-pci-passthrough-notes
status: published
date: 2019-01-06 11:23:45 +0000
tags:
- linux
- virtualbox
category: linux
author: Ron
excerpt: 'Some notes regarding exposing a PCI card inside a Virtualbox VM



  Determine PCI ID on host:



  vbox@vbox:~$ lspci|grep Ethernet

  01:00.0 Ethernet controller: Intel Corporation 82574L Gigabit Network Connection

  02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168B PCI Express
  Gigabit Ethernet controller (rev 03)




  Determine name VM:



  vbox@vbox:~$ VBoxManage list runningvms

  "node-server" {881f529e-5876-4f95-8784-ec7d8d8c8bf4}




  Inside VM, take note of used ID''s:



  user@node-s'
feature_image: /assets/images/2020/08/3a5772951965.jpg
ghost_id: 65cc82d8e7fddf00012feb82
ghost_url: https://cyberjunky.nl/virtualbox-pci-passthrough-notes/
---

Some notes regarding exposing a PCI card inside a Virtualbox VM

Determine PCI ID on host:

```
vbox@vbox:~$ lspci|grep Ethernet
01:00.0 Ethernet controller: Intel Corporation 82574L Gigabit Network Connection
02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168B PCI Express Gigabit Ethernet controller (rev 03)
```

Determine name VM:

```
vbox@vbox:~$ VBoxManage list runningvms
"node-server" {881f529e-5876-4f95-8784-ec7d8d8c8bf4}
```

Inside VM, take note of used ID's:

```
user@node-server:~$ lspci
00:00.0 Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma] (rev 02)
00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II]
00:01.1 IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01)
00:02.0 VGA compatible controller: InnoTek Systemberatung GmbH VirtualBox Graphics Adapter
00:03.0 Ethernet controller: Intel Corporation 82540EM Gigabit Ethernet Controller (rev 02)
00:04.0 System peripheral: InnoTek Systemberatung GmbH VirtualBox Guest Service
00:06.0 USB controller: Apple Inc. KeyLargo/Intrepid USB
00:07.0 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 08)
00:0b.0 USB controller: Intel Corporation 82801FB/FBM/FR/FW/FRW (ICH6 Family) USB2 EHCI Controller
00:0d.0 SATA controller: Intel Corporation 82801HM/HEM (ICH8M/ICH8M-E) SATA Controller [AHCI mode] (rev 02)
```

On Host machine:

```
$ VBoxManage modifyvm "node-server" --pciattach 01:00.0@01:01.0
VBoxManage: error: Host PCI attachment only supported with ICH9 chipset
```

So make sure the VM uses ICH9 chipset, change accordingly.

Attach PCI card to VM:

```
$ VBoxManage modifyvm "node-server" --pciattach 01:00.0@01:01.0
```