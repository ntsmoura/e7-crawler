<!-- Logo -->

<h1 align="center" style="font-family: Ubuntu; font-size: 45px; color: #333; margin-bottom: 0">
  E7 Crawler
</h1>

<!-- Description -->

The main purpose of this crawler is to retrieve data from https://page.onstove.com/epicseven/pt.

<!-- Summary -->

<h2>Guia</h2>

- [:book: Introduction](#book-introduction)
- [:rocket: Tecnologias](#rocket-tecnologias)
- [:boom: Como rodar](#boom-como-rodar)
    - [Prerequisitos](#prerequisitos)
    - [Rodando com xampp](#rodando-com-xampp)

<a id="doc"></a>

<div align="justify">

<a id="introduction"></a>

## :book: Introduction

This application runs a predefined schedule periodically, each job in that schedule is responsible for retrieve some type of specific data from https://page.onstove.com/epicseven/pt, including check-in and buff events, news (in progress), patchs (in progress). 
  
The events job can identify active check-in and buff events and automatically post its schedule table on discord, using a webhook.
  
![events_webhook](https://i.imgur.com/kRiAZJe.png)


<a id="tecnologias"></a>

## :rocket: Tecnologias

Essa aplicação utiliza as seguintes tecnologias:

- [ThreeJs](https://threejs.org/)

<a id="como-executar"></a>

## :boom: Como rodar

#### Prerequisitos

Para rodar essa aplicação é necessário somente um servidor HTTP, como Apache, VS Code Live Server, Nginx, entre outros. Mostrarei um exemplo utilizando o apache através do [Xampp](https://www.apachefriends.org/pt_br/index.html)

#### Rodando com xampp

Após instalar o xampp e configurar o terminal para o diretório principal de onde instalei-o, executo a seguinte sequência de comandos:

```sh
# Muda para o diretório htdocs e clona o repositório
$ cd htdocs
$ git clone https://github.com/MATA65-2022-1/atividade-01---visita-guiada-virtual-ntsmoura/

```

Ao clonar o repositório estou fazendo download de todas as dependências da aplicação, já que estas estão incluídas na pasta [Assets](https://github.com/MATA65-2022-1/atividade-01---visita-guiada-virtual-ntsmoura/tree/main/Assets). No caso do Xampp, eu inicio o servidor Apache e em qualquer browser acesso o link http://localhost/atividade-01---visita-guiada-virtual-ntsmoura/Passeio.html. Algo similar a isto deve aparecer:

![tela_inicial](https://i.imgur.com/bEbBqpR.jpeg)

</div>


