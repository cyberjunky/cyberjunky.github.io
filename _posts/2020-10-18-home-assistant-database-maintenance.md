---
layout: post
title: Home Assistant Database Maintenance
slug: home-assistant-database-maintenance
status: published
date: 2020-10-18 17:40:48 +0000
tags:
- home-assistant
category: home-assistant
author: Ron
excerpt: 'Some commands to investigate and cleanup my Home Assistant database.


  I''m using MariaDB in docker, open a docker cli on homeassistant docker image (using
  Portainer for example)


  bash-5.0# mysql homeassistant

  Reading table information for completion of table and column names

  You can turn off this feature to get a quicker startup with -A


  Welcome to the MariaDB monitor.  Commands end with ; or \g.

  Your MariaDB connection id is 38

  Server version: 10.4.13-MariaDB MariaDB Server


  Copyright (c) 2000, '
feature_image: /assets/images/2020/10/dbsize-1.png
ghost_id: 65cc82d8e7fddf00012febaa
ghost_url: https://cyberjunky.nl/home-assistant-database-maintenance/
---

{% raw %}
Some commands to investigate and cleanup my Home Assistant database.

I'm using MariaDB in docker, open a docker cli on homeassistant docker image (using Portainer for example)

```
bash-5.0# mysql homeassistant
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 38
Server version: 10.4.13-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [homeassistant]>
```

First show all databases, and delete unused, if you install and add-on and remove it, the database is kept so it seems.

```
MariaDB [homeassistant]> show databases;
+--------------------+
| Database           |
+--------------------+
| homeassistant      |
| information_schema |
| mysql              |
| nginxproxymanager  |
| performance_schema |
| phpmyadmin         |
| test               |
+--------------------+
7 rows in set (0.001 sec)

MariaDB [homeassistant]> 

MariaDB [homeassistant]> drop database nginxproxymanager;
Query OK, 14 rows affected (0.499 sec)

MariaDB [homeassistant]> drop database phpmyadmin;
Query OK, 19 rows affected (0.646 sec)

MariaDB [homeassistant]> drop database test;
Query OK, 19 rows affected (0.646 sec)
```

Show tables inside homeassistant database.

```
MariaDB [homeassistant]> show tables;
+-------------------------+
| Tables_in_homeassistant |
+-------------------------+
| events                  |
| recorder_runs           |
| schema_changes          |
| states                  |
+-------------------------+
4 rows in set (0.000 sec)
```

Show structure of the 2 most important tables.

```
MariaDB [homeassistant]> show columns from events;
+-------------------+-------------+------+-----+---------+----------------+
| Field             | Type        | Null | Key | Default | Extra          |
+-------------------+-------------+------+-----+---------+----------------+
| event_id          | int(11)     | NO   | PRI | NULL    | auto_increment |
| event_type        | varchar(32) | YES  | MUL | NULL    |                |
| event_data        | text        | YES  |     | NULL    |                |
| origin            | varchar(32) | YES  |     | NULL    |                |
| time_fired        | datetime    | YES  | MUL | NULL    |                |
| created           | datetime    | YES  |     | NULL    |                |
| context_id        | varchar(36) | YES  | MUL | NULL    |                |
| context_user_id   | varchar(36) | YES  | MUL | NULL    |                |
| context_parent_id | char(36)    | YES  | MUL | NULL    |                |
+-------------------+-------------+------+-----+---------+----------------+
9 rows in set (0.002 sec)

MariaDB [homeassistant]> show columns from states;
+-----------------+--------------+------+-----+---------+----------------+
| Field           | Type         | Null | Key | Default | Extra          |
+-----------------+--------------+------+-----+---------+----------------+
| state_id        | int(11)      | NO   | PRI | NULL    | auto_increment |
| domain          | varchar(64)  | YES  |     | NULL    |                |
| entity_id       | varchar(255) | YES  | MUL | NULL    |                |
| state           | varchar(255) | YES  |     | NULL    |                |
| attributes      | text         | YES  |     | NULL    |                |
| event_id        | int(11)      | YES  | MUL | NULL    |                |
| last_changed    | datetime     | YES  |     | NULL    |                |
| last_updated    | datetime     | YES  | MUL | NULL    |                |
| created         | datetime     | YES  |     | NULL    |                |
| context_id      | varchar(36)  | YES  |     | NULL    |                |
| context_user_id | varchar(36)  | YES  |     | NULL    |                |
| old_state_id    | int(11)      | YES  |     | NULL    |                |
+-----------------+--------------+------+-----+---------+----------------+
12 rows in set (0.001 sec)
```

Show all domains logged.

```
MariaDB [homeassistant]> SELECT DISTINCT domain FROM states; 
+----------------+
| domain         |
+----------------+
| switch         |
| sensor         |
| person         |
| binary_sensor  |
| light          |
| climate        |
| zone           |
| scene          |
| input_boolean  |
| input_select   |
| device_tracker |
+----------------+
11 rows in set (3.158 sec)
```

Show all entities logged.

```
MariaDB [homeassistant]> SELECT DISTINCT entity_id FROM states;

| sun.sun                                                                |
| switch.alles_uit                                                       |
| switch.alles_uit_aan                                                   |
| switch.alles_uit_off                                                   |
| switch.bureau                                                          |
| switch.hobbykamer_plug                                                 |
| switch.incident_response                                               |
| switch.pc_ron                                                          |
| switch.schuur_siren                                                    |
| switch.server                                                          |
| switch.sim_racing_plug                                                 |
| timer.bwr_nesthub                                                      |
| timer.fsr_nesthub                                                      |
| weather.br_unknown_station                                             |
| zone.home                                                              |
| zone.sportcity                                                         |
| zone.work                                                              |
+------------------------------------------------------------------------+
627 rows in set (0.019 sec)
```

Show all device\_tracker entries.

```
MariaDB [homeassistant]> SELECT entity_id FROM states WHERE domain = "device_tracker"; 


| device_tracker.84_0d_8e_5d_53_70    |
| device_tracker.6001941eedfa         |
| device_tracker.a4cf12c60075         |
| device_tracker.philipstvslpk        |
| device_tracker.xn826l               |
| device_tracker.ringchimeboven       |
+-------------------------------------+
27766 rows in set (2.047 sec)
```

Some delete examples, use with care!

```
MariaDB [homeassistant]> DELETE from states where entity_id = 'device_tracker.f4_06_16_86_7e_1d';
Query OK, 684 rows affected (0.079 sec)


MariaDB [homeassistant]> DELETE from states where domain = 'device_tracker';
Query OK, 26671 rows affected (10.161 sec)
```

Optimize tables.

```
MariaDB [homeassistant]> OPTIMIZE TABLE states;
+----------------------+----------+----------+-------------------------------------------------------------------+
| Table                | Op       | Msg_type | Msg_text                                                          |
+----------------------+----------+----------+-------------------------------------------------------------------+
| homeassistant.states | optimize | note     | Table does not support optimize, doing recreate + analyze instead |
| homeassistant.states | optimize | status   | OK                                                                |
+----------------------+----------+----------+-------------------------------------------------------------------+
2 rows in set (55.374 sec)
```

Check you purge day setting from home assistant config.

```
MariaDB [homeassistant]> select min(created),max(created) from events;
+---------------------+---------------------+
| min(created)        | max(created)        |
+---------------------+---------------------+
| 2020-09-08 02:12:34 | 2020-10-09 13:14:09 |
+---------------------+---------------------+
1 row in set (1.765 sec)
```

Show all domains and entities active in your home assistant using Lovelace cards.

```
cards:
  - content: >-
      **domains:** {%- set unique_domains = states | map(attribute='domain')
      |list | unique | list -%} {%- for domain in unique_domains -%} {{"\n"}}-
      {{domain}} {%- endfor -%} {{"\n"}}
    type: markdown
  - content: >-
      **entities:** {%- for state in states -%} {{"\n"}} - {{state.entity_id}}
      {%- endfor -%}
    type: markdown
type: horizontal-stack
```
{% endraw %}
