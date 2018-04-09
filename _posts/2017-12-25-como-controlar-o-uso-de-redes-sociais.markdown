---
layout: post
title: Como controlar o uso de Redes Sociais
date: 2017-12-25 13:59:33
description: Bloquear o uso de Redes Sociais # Add post description (optional)
img: addict.jpg # Add image post (optional)
tags: [Universidade]
author: Lorenzo Cesconetto # Add name author (optional)
published: true
---
&emsp; &emsp; Esse artigo é direcionado a todas as pessoas que gastam mais tempo do que gostariam com redes sociais.

&emsp; &emsp; Primeiramente, por que o facebook ou instagram são tão viciantes? Quando utilizamos alguma rede social uma substância chamada dopamina é liberada no nosso cérebro, essa substância é responsável por aquela sensação boa quando um amigo que gostamos nos deixa um comentário em um post. Essa mesma substância é liberada quando consumimos álcool, fumamos e etc, ou seja, a dopamina faz que essas atividades sejam altamente viciantes.

&emsp; &emsp; Por isso as pessoas estão sempre buscando mais interações nessas plataformas, um exemplo claro disso é quando estamos nos sentindo sozinhos e resolvemos mandar um "eii, tudo bem?" para 10 amigos em seqüência. Existem técnicas para criar plataformas viciantes, e elas são descritas no livro __"Hooked: How to Build Habit-Forming Products"__, escrito por Nir Eyal. O livro sugere que para obter "produtos que formam hábitos" é preciso fazer com que o usuário sinta uma mistura de sensações boas e ruins, por exemplo, sensação de ansiedade através das notificações ou a sensação de recompensa através de likes (quando um cachorro busca um frisbee você dá um biscoito como recompensa, quando uma pessoa posta uma foto ela ganha likes. O resultado disso é que o cachorro sempre vai buscar frisbees e a pessoa sempre vai postar fotos). É natural se perguntar se essa mistura de sensações causa algum tipo de distúrbio mental. Diversas pesquisas apontam que o uso de redes sociais geram depressão (sugerindo um <a target="_blank" href="https://hbr.org/2017/04/a-new-more-rigorous-study-confirms-the-more-you-use-facebook-the-worse-you-feel">artigo de harvard</a> sobre o assunto).

&emsp; &emsp; Alguns sintomas que o uso das redes sociais pode estar atrapalhando a sua vida:
- Você abre a página (ou app) da sua rede social favorita sem se dar conta disso, ou seja, no automático.
- O número de likes nas suas fotos te preocupam bastante.
- Quando você se sente sozinho ou triste, você recorre à mídias sociais para se sentir melhor.

Se você quer gastar menos horas com redes sociais, seu trabalho é quebrar um hábito bem enraizado. Vou te contar o que eu fiz para controlar isso, deve funcionar com você:

- Deletei todos apps de rede social do meu celular. Quando eu realmente preciso acessar por algum motivo, eu baixo o app novamente, e depois que eu uso, deleto ele de novo.
- Bloqueei o Facebook, Instagram e Youtube no meu computador. Para acessar eu tenho o trabalho de desbloquear e depois bloquear novamente.
- Sempre carrego um livro na minha mochila, assim sempre que fico entediado em um ônibus ou uma fila, tenho algo para me entreter. Esse ponto provavelmente é o mais importante e o mais difícil de se manter fiel.

A idéia é criar uma barreira de forma que seja trabalhoso acessar os sites que tomam seu tempo. To colocando aqui um tutorial de como fazer o bloqueio desses sites no computador.

__Para bloquear sites no Mac ou Linux:__

1. Basta abrir o “Terminal”
1. Digitar

    ```
        sudo nano /etc/hosts
    ```

    Depois pressione "enter", entre com a sua senha e pressione "enter" novamente.

1. Agora, você está em um arquivo no seu computador que será editado com o editor de texto nano (ele vem embutido no Mac/Linux e sistemas operacionais UNIX-like). 

    Digite no final do documento a lista de sites a serem bloqueados no seguinte formato:
    ```
    127.0.0.1      www.facebook.com
    127.0.0.1      facebook.com
    ```
    Print de como ficaria a sua tela do terminal.
    ![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/Print-Terminal.png)
    Eu normalmente digito o site com e sem o "www." pois assim a restrição funciona melhor.
    O que está acontecendo aqui é basicamente que você está ligando esses endereços a um servidor local, como você não serve estes sites, eles não vão funcionar mais.

1. Aperte "control + o" e aperte "enter" para salvar suas alterações. Depois basta pressionar "control + x" para fechar o editor nano.

1. Digite
    ```
    sudo dscacheutil -flushcache
    ```
Pressione "enter". Esse comando reseta os dados gravados de servidores no seu computador. As vezes já funciona sem esse comando.

__Para bloquear sites no Windows:__

Acessa esse __<a target="_blank" href="https://www.pcworld.com/article/249077/web-apps/how-to-block-websites.html">tutorial</a>__.

Se esse artigo te ajudou, ajude outras pessoas a quebrar esse mal hábito. Entre em contato comigo pelo <a href="https://www.linkedin.com/in/lorenzo-cesconetto/">LinkedIn</a>.
