---
layout: post
title: OCZ Vertex 2 SSD R.I.P.
slug: ocz-vertex-2-ssd-r-i-p
status: published
date: 2019-01-06 11:16:43 +0000
tags:
- ssd
category: ssd
author: Ron
excerpt: "I'm the proud owner of a dead OCZ Vertex 2 SSD.\n\nIt was working for more\
  \ than 1,5 years in a Ubuntu server without any\n\nproblem.\n\nAn after a reboot/power\
  \ cycle last week it died.\n\n\nThe green LED goes on and stays on, no red LED blinking\
  \ once, like an\n\nother working Vertex drive does.\n\n\nWhen trying to boot from\
  \ it the BIOS tries to detect it for a more than\n\na minute.\n\nAnd fails with\
  \ the message:\n\n\n    Auto-Detecting AHCI Port 1..\n    ...\n    Auto-Detecting\
  \ AHCI Port 4..\n\n\n\ndmesg in Ubuntu is tel"
ghost_id: 65cc82d8e7fddf00012feb77
ghost_url: https://cyberjunky.nl/ocz-vertex-2-ssd-r-i-p/
---

I'm the proud owner of a dead OCZ Vertex 2 SSD.  
It was working for more than 1,5 years in a Ubuntu server without any  
problem.  
An after a reboot/power cycle last week it died.

The green LED goes on and stays on, no red LED blinking once, like an  
other working Vertex drive does.

When trying to boot from it the BIOS tries to detect it for a more than  
a minute.  
And fails with the message:

```
    Auto-Detecting AHCI Port 1..
    ...
    Auto-Detecting AHCI Port 4..
```

dmesg in Ubuntu is telling this when it's hotplugged in a eSata cradle:

```
    [14420.804605] ata7: irq_stat 0x00000040, connection status changed
    [14420.804608] ata7: SError: { PHYRdyChg CommWake DevExch }
    [14420.804616] ata7: hard resetting link
    [14421.526959] ata7: SATA link down (SStatus 0 SControl 300)
    [14421.542903] ata7: EH complete
```

According to  
[https://ata.wiki.kernel.org/index.php/Libata\\_error\\_messages](https://ata.wiki.kernel.org/index.php/Libata%5C_error%5C_messages)

The device presence is detected (DevExch) and Physical ready state  
changed (PHYRdyChg).

While Googling for it, I find a lot of similar stories with the Vertex  
2's.  
Many go in a panic mode, but drives in that mode have the Red and Green  
LEDs on.  
Mine only has the Green one lid.

Drives in panic mode can only be repaired by OCZ.  
I don't mind the drive, but I lost some data, I have backups, but lost  
a few weeks.

Because I changed the passwords of my Synology accounts, the backup  
script failed to acces the storage.  
And I did't notice that until it was too late.  
The simplebackup tool I use, mails me every day, but I didn't read all  
those e-mails.

So some lessons learned.  
Luckily I haven't done major coding during these last weeks since I was  
very busy at work.

Implement backups right now and check them reguarly!

If anyone has any idea what to do let me know, but the drive cannot be  
accessed at all.  
There are some of serial/JTAG ports on the board btw.

Click "here":<http://domotiga.nl/attachments/560/oczvertex2.jpg> for board  
similar to mine.  
I'm the proud owner of a dead OCZ Vertex 2 SSD.  
It was working for more than 1,5 years in a Ubuntu server without any  
problem.  
An after a reboot/power cycle last week it died.

The green LED goes on and stays on, no red LED blinking once, like an  
other working Vertex drive does.

When trying to boot from it the BIOS tries to detect it for a more than  
a minute.  
And fails with the message:

```
    Auto-Detecting AHCI Port 1..
    ...
    Auto-Detecting AHCI Port 4..
```

dmesg in Ubuntu is telling this when it's hotplugged in a eSata cradle:

```
    [14420.804605] ata7: irq_stat 0x00000040, connection status changed
    [14420.804608] ata7: SError: { PHYRdyChg CommWake DevExch }
    [14420.804616] ata7: hard resetting link
    [14421.526959] ata7: SATA link down (SStatus 0 SControl 300)
    [14421.542903] ata7: EH complete
```

According to  
[https://ata.wiki.kernel.org/index.php/Libata\\_error\\_messages](https://ata.wiki.kernel.org/index.php/Libata%5C_error%5C_messages)

The device presence is detected (DevExch) and Physical ready state  
changed (PHYRdyChg).

While Googling for it, I find a lot of similar stories with the Vertex  
2's.  
Many go in a panic mode, but drives in that mode have the Red and Green  
LEDs on.  
Mine only has the Green one lid.

Drives in panic mode can only be repaired by OCZ.  
I don't mind the drive, but I lost some data, I have backups, but lost  
a few weeks.

Because I changed the passwords of my Synology accounts, the backup  
script failed to acces the storage.  
And I did't notice that until it was too late.  
The simplebackup tool I use, mails me every day, but I didn't read all  
those e-mails.

So some lessons learned.  
Luckily I haven't done major coding during these last weeks since I was  
very busy at work.

Implement backups right now and check them reguarly!

If anyone has any idea what to do let me know, but the drive cannot be  
accessed at all.  
There are some of serial/JTAG ports on the board btw.

Resource: <http://www.techpowerup.com/forums/showthread.php?t=154610>