---
layout: post
title: Create a Self-Signed Certificate on MikroTik
slug: create-self-sign-cert-for-mikrotik
status: published
date: 2019-03-27 11:05:09 +0000
tags:
- mikrotik
- routeros
category: mikrotik
author: Ron
excerpt: '/certificate add name=SSL common-name=SSL key-size=2048

  /certificate create-certificate-request template=SSL key-passphrase=mypassword123


  Copy these files (via files download) from your MikroTik to a Linux system:


  certificate-request.pem

  certificate-request_key.pem


  On the Linux server navigate to the folder where the files are located via terminal


  openssl rsa -in certificate-request_key.pem -text > certificate-request2.pem

  openssl x509 -req -days 9999 -in certificate-request.pem -signkey cer'
feature_image: /assets/images/2019/03/SSL-Certificate-Image-1024x458.jpeg
ghost_id: 65cc82d8e7fddf00012feb8b
ghost_url: https://cyberjunky.nl/create-self-sign-cert-for-mikrotik/
---

{% raw %}
```
/certificate add name=SSL common-name=SSL key-size=2048
/certificate create-certificate-request template=SSL key-passphrase=mypassword123
```

Copy these files (via files download) from your MikroTik to a Linux system:

**certificate-request.pem**  
**certificate-request\_key.pem**

On the Linux server navigate to the folder where the files are located via terminal

```
openssl rsa -in certificate-request_key.pem -text > certificate-request2.pem
openssl x509 -req -days 9999 -in certificate-request.pem -signkey certificate-request2.pem -out mikrotik_ssl.crt
```

Copy these files (via files upload) from your Linux system to MikroTik device:

**mikrotik\_ssl.crt**  
**certificate-request2.pem**

Back on the MikroTik device

```
/certificate import file-name=mikrotik_ssl.crt
/certificate import file-name=certificate-request2.pem
passphrase: *****
     certificates-imported: 0
     private-keys-imported: 1
            files-imported: 1
       decryption-failures: 0
  keys-with-no-certificate: 0

/certificate print
```

Finally, set the www-ssl service to use the certificate if not already linked

```
/ip service set www-ssl certificate=mikrotik_ssl.crt_0
```

Enjoy!
{% endraw %}
