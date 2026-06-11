---
layout: post
title: Android 12 Developer Preview 1
slug: android-12-developer-preview-1
status: published
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
ghost_id: 65cc82d8e7fddf00012febb4
ghost_url: https://cyberjunky.nl/android-12-developer-preview-1/
---

{% raw %}
A developer preview of the new Android 12 is available, I installed it on my Pixel 3 XL, and it works fine, a lot of good news on social media too.

Nevertheless this can be worse with DP2 or later, so only do this on a spare phone, and if you know what you are doing.

[Android 12 Developer Preview | Android Developers

<!-- hide description -->

![](https://www.gstatic.com/devrel-devsite/prod/vbd904f2719533e871e3800dda1bebc56aa0bc95c3c9d01c4d7cebcf129bdf26c/android/images/touchicon-180.png)Android Developers

![](https://developer.android.com/images/social/android-developers.png)](https://developer.android.com/about/versions/12)[First preview of Android 12

Posted by Dave Burke, VP of Engineering Every day, Android apps help billions of people work, play, communicate, and create on a wi...

![](https://android-developers.googleblog.com/favicon.ico)Android Developers BlogGoogle

![](https://1.bp.blogspot.com/-eRnBIDn-ZZE/YC6eGA2hC5I/AAAAAAAAQGY/bea6RxVXWcs9q5FoLEZtjuTnLZvegzY2ACLcBGAsYHQ/w1200-h630-p-k-no-nu/Android%2B12_logo.png)](https://android-developers.googleblog.com/2021/02/android-12-dp1.html)

You can side-load it or unlock your boot loader and use the flash utility.

[Downloads for Google Pixel | Android 12 Developer Preview

Instructions for downloading and installing preview system images for Pixel devices

![](https://www.gstatic.com/devrel-devsite/prod/vbd904f2719533e871e3800dda1bebc56aa0bc95c3c9d01c4d7cebcf129bdf26c/android/images/touchicon-180.png)Android Developers

![](https://developer.android.com/images/social/android-developers.png)](https://developer.android.com/about/versions/12/download)

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
