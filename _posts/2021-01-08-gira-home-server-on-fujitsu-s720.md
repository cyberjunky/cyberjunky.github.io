---
layout: post
title: Gira Home Server 4 on Fujitsu S720
slug: gira-home-server-on-fujitsu-s720
status: published
date: 2021-01-08 10:11:15 +0000
tags:
- knx
- home server
- hs4
- gira
category: knx
author: Ron
excerpt: 'IMPORTANT NOTE: This setup is pure for testing/HSL development/knowledge
  gathering only, don''t use this in production environment or for replacement of
  the Home Server hardware. I''m not responsable for any possible damages!


  For plugin development and to check out version 4.11 I bought a refurbished Fujitsu
  Futro S720 thin client.



  S720 mini-pc


  It contains a D3313-B13 GS 1 motherboard with a 2GB memory module and a 2GB mSATA
  3SE from innodisk for disk storage, no fan, so as quiet as possible. '
feature_image: /assets/images/2021/01/imageedit_1_2780732523.gif
ghost_id: 65cc82d8e7fddf00012febb0
ghost_url: https://cyberjunky.nl/gira-home-server-on-fujitsu-s720/
---

{% raw %}
IMPORTANT NOTE: This setup is pure for testing/HSL development/knowledge gathering only, don't use this in production environment or for replacement of the Home Server hardware. I'm not responsable for any possible damages!

For plugin development and to check out version 4.11 I bought a refurbished Fujitsu Futro S720 thin client.

### S720 mini-pc

It contains a D3313-B13 GS 1 motherboard with a 2GB memory module and a 2GB mSATA 3SE from innodisk for disk storage, no fan, so as quiet as possible. The newer HS4 hardware use a 4GB disk module, but 2GB is still supported.

I replaced the memory with a 4GB module (because I had one laying around) Samsung 4GB 1Rx8 PC3L-12800S.

It comes very close to the original HS4 hardware.

More technical details can be found here: <https://www.parkytowers.me.uk/thin/Futro/s720/>

### Prepare and update motherboard

I created an USB stick (2GB) to update the BIOS and prepare the settings.

1. Download Rufus portable version from <https://rufus.ie/> and create a 'FreeDOS' type image on the stick.
2. Download DMIEdit tools from <https://www.file-upload.net/download-13728821/DMIEDIT_utility.rar.html> copy it's contents to root of stick.
3. Download BIOS Admin package from <https://support.ts.fujitsu.com/IndexDownload.asp?SoftwareGuid=08E73A9C-C14F-4A71-8AD0-475F1126E66A> copy the contents of the 'DOS' directory to the root of stick.
4. Boot with F12 to select USB.
5. Run DosFlash.bat to update the BIOS. (from 1.15.0 to 1.18.0 in my case)
6. Set Consumer Serial Number to your HS4 Serial Number by running AMIDEDOS /ss  <YOUR SERIAL>
7. Set BIOS clock to correct date/time, and 'Prefer USB boot' to enabled. Save and reboot, check Serial Number on the BIOS information screen.

### Install Home Server software

Create an USB stick to install firmware and transfer your first project

1. Use Rufus again to prepare USB stick (minimal 2GB in size) select ISO file 'hs.iso' from Gira HS/FS subfolder 'firmware\usb'.
2. Use Upload firmware from HomeServer menu to write to this USB stick.
3. Boot it and await the 6 beeps, you can reboot now and check the console for errors.
4. Transfer your Project (for setting network and password settings) using the same stick and reboot. (you can combine these steps)
5. The HS should be reachable via network now.
{% endraw %}
