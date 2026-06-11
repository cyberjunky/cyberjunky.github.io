---
layout: post
title: Crypto trading with freqtrade
slug: crypto-trading-with-freqtrade
status: published
date: 2024-02-14 09:15:48 +0000
author: Ron
excerpt: 'Some snippets/notes on how to use freqtrade.


  https://www.freqtrade.io/en/latest/

  https://github.com/freqtrade/freqtrade


  $ sudo apt install -y python3-pip python3-venv python3-pandas python3-pip git


  $ git clone https://github.com/freqtrade/freqtrade.git


  $ cd freqtrade

  $ git checkout stable


  $ ./setup.sh -i

  ubuntu-pc:~/freqtrade$ ./setup.sh -i


  /usr/bin/python3.8

  using Python 3.8

  -------------------------

  Installing mandatory dependencies

  -------------------------

  Debian/Ubuntu detected. Setup'
feature_image: /assets/images/2024/02/d6659780-a0e1-11eb-8a38-933cd666cdeb.png
ghost_id: 65cc82d8e7fddf00012febb6
ghost_url: https://cyberjunky.nl/crypto-trading-with-freqtrade/
---

Some snippets/notes on how to use *freqtrade*.

<https://www.freqtrade.io/en/latest/>  
<https://github.com/freqtrade/freqtrade>

```
$ sudo apt install -y python3-pip python3-venv python3-pandas python3-pip git

$ git clone https://github.com/freqtrade/freqtrade.git

$ cd freqtrade
$ git checkout stable

$ ./setup.sh -i
ubuntu-pc:~/freqtrade$ ./setup.sh -i

/usr/bin/python3.8
using Python 3.8
-------------------------
Installing mandatory dependencies
-------------------------
Debian/Ubuntu detected. Setup for this system in-progress
[sudo] password for ron: 
...
----------------------------
Reseting branch and virtual env
----------------------------
Reset git branch? (This will remove all changes you made!) [y/N]? 
...
EAD is now at 38b96f07 Merge pull request #4434 from freqtrade/new_release
- Deleting your previous virtual env
...
-------------------------
Updating your virtual env
-------------------------
pip install in-progress. Please wait...
Collecting pip
  Using cached pip-21.0.1-py3-none-any.whl (1.5 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.0.2
    Uninstalling pip-20.0.2:
      Successfully uninstalled pip-20.0.2
Successfully installed pip-21.0.1
Do you want to install dependencies for dev [y/N]? y
Do you want to install plotting dependencies (plotly) [y/N]? y
Do you want to install hyperopt dependencies [y/N]? y
...
-------------------------
Please use 'freqtrade new-config -c config.json' to generate a new configuration file.
-------------------------
-------------------------
Run the bot !
-------------------------
You can now use the bot by executing 'source .env/bin/activate; freqtrade <subcommand>'.
You can see the list of available bot sub-commands by executing 'source .env/bin/activate; freqtrade --help'.
You verify that freqtrade is installed successfully by running 'source .env/bin/activate; freqtrade --version'.

$ source .env/bin/activate
$ freqtrade new-config -c config.json

(.env) ubuntu-pc:~/freqtrade$ freqtrade new-config -c config.json
? Do you want to enable Dry-run (simulated trades)? Yes
? Please insert your stake currency: EUR
? Please insert your stake amount: 33
? Please insert max_open_trades (Integer or 'unlimited'): 3
? Please insert your desired timeframe (e.g. 5m): 5m
? Please insert your display Currency (for reporting): EUR
? Select exchange other
? Type your exchange name (Must be supported by ccxt) xxxxxxxx
? Do you want to enable Telegram? Yes
? Insert Telegram token *********************************************
? Insert Telegram chat id xxxxxxxxx
2021-03-19 14:52:58,091 - freqtrade.commands.build_config_commands - INFO - Writing config to `config.json`.

Edit config.json and add API key and secret.

Get available trading pairs from your exchange

$ freqtrade list-pairs -1

Add them to config.json pairlist

Get data

$ freqtrade  download-data -c config.json --timerange 20200101- -t 1h

$ freqtrade backtesting --ticker-interval 1h -s BbandRsi -c config.json b --export trades --export-filename user_data/backtest_results/backtest-result.json


Plot Graphs
$ python3 ./scripts/plot_dataframe.py -s BbandRsi  -p ZEC/BTC --indicators1 bb_lowerband,bb_middleband,bb_upperband --indicators2 rsi
```