---
layout: post
title: OCZ Vertex 2 serial port diagnostics
slug: ocz-vertex-2-serial-port-diagnostics
status: published
date: 2019-01-06 11:16:14 +0000
tags:
- ssd
category: ssd
author: Ron
excerpt: "Found my dead OCZ SSD drive again and connected it to the serial port of\n\
  \nmy Ubuntu desktop.\n\n\nThis is what I get upon startup when i connect to it at\
  \ 115200 Baud\n\n\n    CLI> PINRST\n    *** ROM 106 Mar 12 2009 20:29:35 ***\n \
  \   FW_SRC 0 SHA PASS!\n    *** EEPROM 207 Jan  3 2011 18:36:43 BuildServer:FW_Common_Critical_Fixes:P1_EEPROM_2_0_7_drop-290232\
  \ ***\n    Hynix Timing EPch\n    *** Patch 1.4.1 Apr  8 2011 00:55:09 BuildServer:P1_3_6_1_MP4_Patch1_20110408:P1_3_6_1_MP4_Patch1_20110408-305073\
  \ ***\n  "
ghost_id: 65cc82d8e7fddf00012feb76
ghost_url: https://cyberjunky.nl/ocz-vertex-2-serial-port-diagnostics/
---

Found my dead OCZ SSD drive again and connected it to the serial port of  
my Ubuntu desktop.

This is what I get upon startup when i connect to it at 115200 Baud

```
    CLI> PINRST
    *** ROM 106 Mar 12 2009 20:29:35 ***
    FW_SRC 0 SHA PASS!
    *** EEPROM 207 Jan  3 2011 18:36:43 BuildServer:FW_Common_Critical_Fixes:P1_EEPROM_2_0_7_drop-290232 ***
    Hynix Timing EPch
    *** Patch 1.4.1 Apr  8 2011 00:55:09 BuildServer:P1_3_6_1_MP4_Patch1_20110408:P1_3_6_1_MP4_Patch1_20110408-305073 ***
    Hynix Timing EPch
    RCPch SAK0+Fmgr
    *** ERROR REPORT ***

    IMPWIRE: 00300000

    [PART]
    SCHE:    80104404: 00000000
    SATA:    81001804: 00000000
    BUFR:    82201404: 00000000
    FLSH;    83004004: 00000000
    SIDX:    84400004: 00000000


    PANIC: file=src/root/DirectRdWr.c  line=197
    PANIC: error=0x80120003  Flash Command received an interrupt
    [BOOT MAIN] Root Not Found!
    FW_SRC 0 SHA PASS!
    *** EEPROM 207 Jan  3 2011 18:36:43 BuildServer:FW_Common_Critical_Fixes:P1_EEPROM_2_0_7_drop-290232 ***
    EPch SHI
    sysclk 150 MHz
    JTAG En 0
    Link ...
    up
```

Going to see if google has any pointers...