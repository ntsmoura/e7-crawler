<!-- Logo -->

<h1 align="center" style="font-family: Ubuntu; font-size: 45px; color: #333; margin-bottom: 0">
  E7 Crawler
</h1>

<!-- Description -->

The main purpose of this crawler is to retrieve data from https://page.onstove.com/epicseven/pt.

<!-- Summary -->

<h2>Summary</h2>

- [:book: Introduction](#book-introduction)
- [:rocket: Technologies](#rocket-technologies)
- [:boom: How to run](#how-to-run)

<a id="doc"></a>

<div align="justify">

<a id="introduction"></a>

## :book: Introduction

This application runs a predefined schedule periodically, each job in that schedule is responsible for retrieve some type of specific data from https://page.onstove.com/epicseven/pt, including check-in and buff events, news (in progress), patches (in progress). 
  
The events job can identify new active check-in and buff events and automatically post its schedule table on discord, using a webhook.
  
<p align="center">
<img src="https://i.imgur.com/kRiAZJe.png"/>
</p>

<a id="technologies"></a>

## :rocket: Technologies

This application needs the following thecnologies:

- [Python3](https://www.python.org/downloads/)
- [Selenium](https://pypi.org/project/selenium/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://pypi.org/project/requests/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [Web-driver-manager](https://pypi.org/project/webdriver-manager/)


## :boom: How to run
  
Install all the technologies, then follow the instructions:
  
```sh
# Clone the repository
$ git clone https://github.com/ntsmoura/e7-crawler
  
# Change to the directory
$ cd e7-crawler
  
# Copy the .env.example to a .env
$ cp .env.example .env
  
# Run
$ python3 main.py
```
Remember to fill the .env with correct data, to do that you need to create an [HTCI](https://hcti.io/) account and a Discord Webhook.
</div>


