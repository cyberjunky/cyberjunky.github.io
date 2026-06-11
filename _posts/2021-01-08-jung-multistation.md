---
layout: post
title: JUNG KNX multi station
slug: jung-multistation
status: published
date: 2021-01-08 16:00:33 +0000
tags:
- knx
- jung
- multistation
category: knx
author: Ron
excerpt: "Art. No. 23066REGHE\n\nI bought a few of these modules some time ago, they\
  \ were used for a short period in holiday homes and replaced by another non KNX\
  \ solution. Recently I had some time to look at them in detail, configure them with\
  \ ETS5 and test their functionality.\n\n'Multi' doesn't only tell something about\
  \ the functionality, the product documentation is 489 pages long and it has more\
  \ than 100 group objects to assign!\n\n\nProduct info\n\nPossible use cases:\n\n\
  \ * Switching of electrical loads with f"
feature_image: /assets/images/2021/01/JUNG_23066REGHE.png
ghost_id: 65cc82d8e7fddf00012febb1
ghost_url: https://cyberjunky.nl/jung-multistation/
---

### Art. No. 23066REGHE

I bought a few of these modules some time ago, they were used for a short period in holiday homes and replaced by another non KNX solution. Recently I had some time to look at them in detail, configure them with ETS5 and test their functionality.

'Multi' doesn't only tell something about the functionality, the product documentation is 489 pages long and it has more than 100 group objects to assign!

### Product info

**Possible use cases:**

- Switching of electrical loads with floating contacts
- Switching of electrically-driven blinds, shutters, awnings and similar hangings
- Switching of electro thermal drives
- Polling of conventional switching or push-button contacts, window contacts etc. in KNX systems, for reporting of states, meter levels, operation of loads, etc.
- Polling of external temperature sensors for heating control
- Logic functions to control building functions
- Mounting on DIN rail according to EN 60715 in distribution boxes

****Product characteristics****

- Actuator functions: switching, blinds, electro thermal drives
- Actuator function can be switched in pairs
- Integrated push-button interface with 6 inputs
- 2 integrated room temperature controllers
- 2 inputs for temperature sensors (ref.-no. [FF 7.8](https://www.jung.de/en/online-catalogue/63838534/))
- Outputs can be operated manually, construction site mode
- Feedback in manual mode and in bus mode
- Scene function
- Disabling of individual outputs manually or via bus

****Switching function****

- Max. 6 switching outputs
- Operation as NO or NC contacts
- Logic operation and forcing function
- Feedback function
- Central switching function with collective feedback
- Time functions: switch-on delay, switch-off delay, staircase lighting timer with pre-warning function

****Blinds function****

- Max. 3 blinds outputs
- Suitable for 230 V AC motors
- Blind/shutter position directly controllable
- Slat position directly controllable
- Feedback of movement status, blind/shutter position and slat position
- Forced position through higher-level controller
- Safety function: rain alarm, frost alarm, 3 independent wind alarms
- Sun protection function

****Function of valve drives****

- Max. 2 outputs for electro thermal drives
- Switching operation or PWM operation
- Actuators with characteristics "normally open" or "normally closed" can be controlled
- Emergency operation in case of bus voltage failure for summer and winter
- Protection against jamming valves
- Forced position
- Cyclical monitoring of the input signals can be parameterised

****Heating controller****

- 2 internal controllers to control two independent rooms
- Control for heating or cooling, optionally with additional level
- On-off, PWM or PI control
- Predefined heating types (hot water heating, fan coil unit ...) or individual parameters possible

****Inputs****

- 6 inputs for push-buttons
- Input functions: switching, dimming, blinds control, light scene extension unit, brightness or temperature value transmitter
- 2 inputs for external temperature sensors

****Logic functions****

- Up to 10 logic operations with up to 8 inputs each, e.g. for AND, OR and XOR operations
- Conversion of data point types, e.g. from 1-bit to 8-bit
- Comparative operations, e.g. <, >, ≤, ≥
- Arithmetic functions, e.g. +, –, \*, :

### My use case

I have rooms with a central heating radiator and shutters. So I want to control both the heating and the window covers per room, and I want to measure the room temperature.

If window is open, close heating valve, if room temperature is low open valve, if temperature is reached close valve. Control shutters via manual switch and automatically, if strong wind gusts outside open shutter, if window is open don't close shutter, etc.  
Later install and connect cheaper non KNX motions sensors, like described here: <https://www.jung.de/en/10521/products/new-items-2020/new-products-2020-part-3/motion-detector-mini-basic/>

### Some ETS5 screenshots

![](/assets/images/2021/01/group-objects.png)

![](/assets/images/2021/01/parameters.jpg)

![](/assets/images/2021/01/programs.png)

![](/assets/images/2021/01/properties.png)

### Schematic

![](/assets/images/2021/01/1_jung_multistation-1.png)

### Some resources

Online catalog: [[JUNG - Multi station Actuators for rail mounting Devices for rail mounting KNX OVERVIEW](https://www.jung.de/en/online-catalogue/350288497/)](https://www.jung.de/en/online-catalogue/350288497/)

Product Information: <https://downloads.jung.de/public/en/pdf/productdocumentation/en_23066REGHE_td_21022018.pdf>