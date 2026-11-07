---
layout: post
title: Android 12 Developer Preview 1
date: 2021-02-23 18:37:57 +0000
tags:
- android
- pixel
- google
category: android
author: Ron
excerpt: 'A developer preview of the new Android 12 is available, I installed it on
  my Pixel 3 XL, and it works fine, a lot of good news on social media too.

  Nevertheless this can be worse with DP2 or later, so only do this on a spare phone,
  and if you know what you are doing.

  Android 12 Developer Preview | Android Developers<!-- hide description -->Android
  DevelopersFirst preview of Android 12Posted by Dave Burke, VP of Engineering Every
  day, Android apps help billions of people work, play, communicate'
feature_image: /assets/images/2021/02/Android-12.png
---

{% raw %}
A developer preview of the new Android 12 is available, I installed it on my Pixel 3 XL, and it works fine, a lot of good news on social media too.

Nevertheless this can be worse with DP2 or later, so only do this on a spare phone, and if you know what you are doing.

> **[Android 12 Developer Preview | Android Developers](https://developer.android.com/about/versions/12)**

> **[First preview of Android 12](https://android-developers.googleblog.com/2021/02/android-12-dp1.html)**  
> Posted by Dave Burke, VP of Engineering Every day, Android apps help billions of people work, play, communicate, and create on a wi...

You can side-load it or unlock your boot loader and use the flash utility.

> **[Downloads for Google Pixel | Android 12 Developer Preview](https://developer.android.com/about/versions/12/download)**  
> Instructions for downloading and installing preview system images for Pixel devices

Make sure you have installed the USB driver and start the Android Flash Tool from Chrome. <https://flash.android.com/welcome>

To lock your phone's boot-loader afterwards, do this:

Install the platform tools from here:

<https://developer.android.com/studio/releases/platform-tools>

And do this:

```
adb.exe reboot bootloader
fastboot.exe flashing lock
```
{% endraw %}
