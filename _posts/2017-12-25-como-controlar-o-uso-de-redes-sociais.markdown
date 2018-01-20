---
layout: post
title: Como controlar o uso de Redes Sociais
date: 2017-12-25 13:59:33
description: Bloquear o uso de Redes Sociais # Add post description (optional)
img: addict.jpg # Add image post (optional)
tags: [Universidade]
author: Lorenzo Cesconetto # Add name author (optional)
published: true # Shows or hides a post
---
&emsp; &emsp; Esse artigo é direcionado a todas as pessoas que gastam mais tempo do que gostariam com redes sociais.

&emsp; &emsp; Quando usamos redes sociais uma substância chamada dopamina é liberada no nosso cérebro, por isso nos sentimos bem ao usá-las. Essa mesma substância é liberada quando consumimos álcool, fumamos e etc, ou seja, a dopamina faz que essas atividades sejam altamente viciantes.

&emsp; &emsp; Além disso, diversas pesquisas apontam que o uso de redes sociais geram depressão (sugerindo um [artigo de harvard][HBR] sobre o assunto). Aproveito para sugerir a leitura do livro Hooked, um dos livros mais lidos no Vale do Silício sobre como criar produtos viciantes.

&emsp; &emsp; Alguns sintomas que o uso das redes sociais chegou à níveis preocupantes:
- Você abre a página (ou app) da sua rede social favorita sem se dar conta disso ("no automático").
- O número de likes nas suas fotos te preocupam bastante.
- Quando você se sente sozinho ou triste, você recorre à mídias sociais para se sentir melhor.

Eu quero que você retome o controle sobre a sua vida! Seu trabalho é quebrar um hábito bem enraizado. Vou te contar o que eu fiz para controlar esse mal hábito, talvez funcione com você:

- Eu deletei todos apps de rede social do meu celular. Quando eu realmente preciso acessar por algum motivo, eu baixo o app novamente, e depois que eu uso, deleto ele de novo.
- Bloqueei o Facebook, Instagram e Youtube no meu computador. Para acessar eu tenho o trabalho de desbloquear e depois bloquear novamente.

A idéia é criar uma barreira de forma que seja trabalhoso acessar os sites que tomam seu tempo. O método é radical, mas se você realmente quer mudar isso, é preciso abrir mão de algumas coisas. To colocando aqui um tutorial de como fazer o bloqueio desses sites no computador.

__Para bloquear sites no Mac ou Linux:__

1. Basta abrir o “Terminal”
1. Digitar

    ```
        sudo nano /etc/hosts
    ```

    Depois pressione "enter", entre com a sua senha e pressione "enter" novamente.

1. Agora, você está em um arquivo no seu computador que será editado com o editor de texto nano (ele vem embutido no Mac e sistemas operacionais UNIX-like). 

    Digite no final do documento a lista de sites a serem bloqueados no seguinte formato:
    ```
    127.0.0.1      www.facebook.com
    127.0.0.1      facebook.com
    ```
    Print de como ficaria a sua tela do terminal.
    ![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/Print-Terminal.png)
    Eu gosto de digitar o site com e sem o "www." pois assim a restrição funciona melhor.
    O que está acontecendo aqui é basicamente que você está ligando esses endereços a um servidor local, como você não serve estes sites, eles não vão funcionar mais.

1. Aperte "control + o" e aperte "enter" para salvar suas alterações. Depois basta pressionar "control + x" para fechar o editor nano.

1. Digite
    ```
    sudo dscacheutil -flushcache
    ```
Pressione "enter". Esse comando reseta os dados gravados de servidores no seu computador. Mas geralmente já funciona sem esse comando.

Se esse artigo te ajudou de alguma forma, ajude outras pessoas com problemas semelhantes.
Comenta aqui em baixo sugestões de posts! :)


[HBR]: https://hbr.org/2017/04/a-new-more-rigorous-study-confirms-the-more-you-use-facebook-the-worse-you-feel


