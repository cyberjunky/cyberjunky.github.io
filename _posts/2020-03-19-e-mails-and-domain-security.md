---
layout: post
title: email and domain security
slug: e-mails-and-domain-security
status: published
date: 2020-03-19 20:56:53 +0000
tags:
- security
- dnssec
- dkim
- spf
category: security
author: Ron
excerpt: 'About SPF, DMARC and DNSSEC


  DMARC:


  Create a 14 Day trial account at https://dmarcian.

  Setup and get unique email addresses, create a DMARC TXT record:


  _dmarc.cyberjunky.nl

  v=DMARC1; p=reject; rua=mailto:ci2xsqr1@ag.dmarcian.com; ruf=mailto:ci2xsqr1@fr.dmarcian.com;


  https://dmarcian.com/dmarc-inspector/?domain=cyberjunky.nl



  SPF:


  To check send an email from the domain you want to test to check-auth@verifier.port25.com


  Create a SPF TXT record (hosted by Google''s gmail):


  v=spf1 include:_spf'
feature_image: /assets/images/2020/03/SPF-DKIM-DMARC.png
ghost_id: 65cc82d8e7fddf00012feb9a
ghost_url: https://cyberjunky.nl/e-mails-and-domain-security/
---

About SPF, DMARC and DNSSEC

DMARC:

Create a 14 Day trial account at https://dmarcian.  
Setup and get unique email addresses, create a DMARC TXT record:

```
_dmarc.cyberjunky.nl
v=DMARC1; p=reject; rua=mailto:ci2xsqr1@ag.dmarcian.com; ruf=mailto:ci2xsqr1@fr.dmarcian.com;
```

<https://dmarcian.com/dmarc-inspector/?domain=cyberjunky.nl>

SPF:

To check send an email from the domain you want to test to [check-auth@verifier.port25.com](mailto:check-auth@verifier.port25.com)

Create a SPF TXT record (hosted by Google's gmail):

```
v=spf1 include:_spf.google.com -all
```

[Network Tools: DNS,IP,Email

DNS and Network troubleshooting and diagnostic tools integrated into one sweet interface.

![](https://mxtoolbox.com/public/images/favicons/android-chrome-192x192.png)MxToolbox

![](https://mxtoolbox.com/Public/Images/logo_square_1900.png)](https://mxtoolbox.com/SuperTool.aspx?action=spf%3acyberjunky.nl&run=toolpage)

DNSSEC:

Already taken care of by Versio:

<https://dnssec-debugger.verisignlabs.com/cyberjunky.nl>

Resources:

<https://kitterman.com/dmarc/assistant.html>