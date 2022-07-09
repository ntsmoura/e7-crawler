<!-- Logo -->

<h1 align="center" style="font-family: Ubuntu; font-size: 45px; color: #333; margin-bottom: 0">
  E7 Crawler
</h1>

<!-- Description -->

The main purpose of this crawler is to retrieve data from https://page.onstove.com/epicseven/pt.

<!-- Summary -->

<h2>Guia</h2>

- [:book: Introduction](#book-introduction)
- [:rocket: Technologies](#rocket-technologies)
- [:boom: How to run](#how-to-run)

<a id="doc"></a>

<div align="justify">

<a id="introduction"></a>

## :book: Introduction

This application runs a predefined schedule periodically, each job in that schedule is responsible for retrieve some type of specific data from https://page.onstove.com/epicseven/pt, including check-in and buff events, news (in progress), patchs (in progress). 
  
The events job can identify active check-in and buff events and automatically post its schedule table on discord, using a webhook.
  
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


<a id="how-to-run"></a>

```sh
# Muda para o diretório htdocs e clona o repositório
$ cd htdocs
$ git clone https://github.com/MATA65-2022-1/atividade-01---visita-guiada-virtual-ntsmoura/

```

Ao clonar o repositório estou fazendo download de todas as dependências da aplicação, já que estas estão incluídas na pasta [Assets](https://github.com/MATA65-2022-1/atividade-01---visita-guiada-virtual-ntsmoura/tree/main/Assets). No caso do Xampp, eu inicio o servidor Apache e em qualquer browser acesso o link http://localhost/atividade-01---visita-guiada-virtual-ntsmoura/Passeio.html. Algo similar a isto deve aparecer:

![tela_inicial](https://i.imgur.com/bEbBqpR.jpeg)

</div>


