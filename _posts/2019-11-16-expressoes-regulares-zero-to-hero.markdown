---
layout: post
title: "Expressões Regulares: Zero to Hero"
date: 2019-11-16 17:14:44
img: regex_cover.jpg
tags: [Ciência de Dados]
author: Lorenzo Cesconetto
published: true
---

Esse _post_ foi feito por um grande amigo meu __<a target="_blank" href="https://www.linkedin.com/in/rodolfo-nobrega-de-resende-3a7a15165/" target="_">Rodolfo Nóbrega</a>__. Rodolfo é de longe a pessoa com maior fluência em expressões regulares (_regex_) que já conheci. Ele aplica _regex_ de formas muito criativas nos seus projetos de automatização (RPA). Por ter tanta autoridade no assunto, pedi a ele esse belo tutorial :)

O conteúdo é direcionado à pessoas que tenham noções básicas de programação.

# Tutorial de Expressões Regulares

Neste tutorial iremos aprender sobre expressões regulares.

Sem muita enrolação, expressões regulares servem para extrairmos dados de textos que sigam um determinado padrão.

É difícil fazer uma lista de tudo o que podemos fazer com as expressões regulares pois elas são úteis sempre que você precisar buscar ou validar um padrão de texto que pode ser variável, como:

* data
* horário
* número IP
* nome de pessoa
* endereço de e-mail
* endereço de Internet
* nome de usuário e senha
* declaração de uma função()
* dados na coluna N de um texto
* dados que estão entre \<tags\>\</tags\>
* campos específicos de um texto tabulado
* número de telefone, RG, CPF, cartão de crédito
* dados que estão apenas no começo ou no fim da linha

O foco aqui será aprender a sintaxe das expressões regulares e estas depois poderão ser aplicadas à sua linguagem de programação preferida.

Apesar de parecerem complicadas, as expressões regulares são na verdade bem simples, basta conhecer direitinho sua sintaxe.

Para este tutorial, iremos utilizar o site __<a target="_blank" href="https://www.regextester.com/" target="_">regextester</a>__. Neste site podemos ver em tempo real os dados selecionados nas expressões regulares que iremos criar. 

Este site é bem simples de ser utilizado, temos dois campos de texto, no campo de cima colocamos a expressão regular que estamos utilizando e no campo de baixo o texto que estamos "testando". O texto que está sendo selecionado ficará sombreado em tempo real.

Veja um exemplo na imagem abaixo de como o site funciona.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_1.png)

Na imagem acima podemos ver uma expressão regular que extrai datas de um texto (as datas estão marcadas em azul), não importa onde elas estão, seja perto de textos, espaços, números, algarismos especiais e etc. Logo à frente veremos que essa expressão possui falhas pois ela pode pegar coisas que se pareçam com datas mas não são, como 87/22/2001, afinal, não temos dia 87 e nem mês 22, no futuro veremos como fazer uma expressão regular mais refinada para pegar somente o que queremos mesmo. Mas lembrem-se sempre, quanto mais simples a _Regex_ (abreviação de _regular expression_), melhor.

Escrever uma expressão regular é parecido com escrever um texto, iremos definir qual caractere ou grupo de caracteres iremos selecionar e quantas vezes este pode se repetir, é bem simples, eu prometo :).

De inicio, irei apresentar todos os elementos básicos que podem compor uma expressão regular, em seguida, veremos alguns exemplos de extração de dados utilizando esta.

Os símbolos que tanto assustam e que iremos aprender a seguir são os seguintes: __. ? * + ^ $ \| [ ] { } ( ) \\__ . Complicado? Em breve você verá que nem tanto. 

Vou começar pelo mais simples, que são os __quantificadores__, ou seja, os elementos que definem __quantas vezes os caracteres podem se repetir__, existem 4 deles.

Os exemplos de uso dos quantificadores serão apresentados à frente quando formos apresentar outros elementos. Afinal, os quantificadores aparecem o tempo todo nas expressões regulares.

## A. Quantificadores:

### 1. O "?" (opcional)
O `?` define que um caractere ou conjunto de caracteres deve existir zero ou uma vez. Complicado? Imagine que você está extraindo um número que pode ser positivo ou negativo (-3.7, 5.4), o sinal de menos pode ou não existir, ou seja, ele existe zero ou uma vez, neste caso podemos usar o `?`. 

### 2. O "\*" (asterisco) 
O `*` define que um elemento se repetirá zero ou mais vezes (de zero a infinito), ou seja, o elemento pode ou não existir e caso exista, pode se repetir infinitas vezes. Imagine que você por algum motivo quer selecionar todos os números iniciados por 1 que depois existam ou não outros números (1, 12, 1248, 132547). Neste caso o `*` seria perfeito pra nós.

### 3. O "+" (mais)
O `+` é bem parecido com o `*`, no entanto, ele define um elemento que se repetirá uma ou mais vezes (de um a infinito), ou seja, o elemento tem obrigatoriamente que existir e pode se repetir infinitas vezes. Voltado ao exemplo anterior, é se quiser selecionar os números que começam com 1 e tenham 2 ou mais caracteres? (12, 1248, 132547), sendo assim, o `*` não nos atenderia mais e teríamos que usar o `+`. 

### 4. {m, n} (chaves) 
As `{}` são usadas quando o que estamos procurando possui um número específico de elementos. Quando vemos `{m, n}`, devemos entender "o elemento se repete de `m` a `n` vezes". Por exemplo `{2, 5}` significa que o elemento se repete de 2 a 5 vezes. E se omitirmos `n`? Caso o `n` seja omitido, podem existir 2 casos:

* `{5}` : Neste caso o elemento deve se repetir exatamente 5 vezes.
* `{5,}` : Notou uma vírgula ali? Não, não está errado, neste caso significa que o elemento se repetirá 5 ou mais vezes (de 5 a infinito). 
* `{,5}` : Entendeu a lógica? Neste caso é a mesma coisa que `{0,5}`, ou seja, o elemento se repetirá de 0 a 5 vezes.

Perceba que com as chaves `{}` é possível escrever todos os 3 primeiros quantificadores! Percebeu? Então vamos ver como ficaria cada um deles:

* `?` = `{0,1}`
* `*` = `{0,}`
* `+` = `{1,}`

Viu só, até aqui nada complicado né? Mas as coisas ainda estão um pouco abstratas eu sei. Nos próximos passos vamos começar a colocar a mão na massa e tudo vai ficar mais “palpável”.

## B. Metacaracteres de captura:

A ideia aqui não é entrar em detalhes sobre a nomenclatura, mas vamos chamar de metacaracteres todo o resto que compuser as nossas expressões regulares. Aliás, os quantificadores são também um tipo de metacaractere.

A partir de agora utilizaremos o site citado no começo deste guia para testarmos nossas expressões regulares, note porém que por padrão no campo “_Regular Expression_” já existe um `//g`. Ignore-o, o que nos interessa é tudo o que digitarmos, desconsiderando esse `//g`. Por exemplo, se digitarmos um `a`, a expressão regular no site será apresentada como `/a/g`, no entanto, para nós, a expressão regular será apenas o `a`.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_2.png)

Note que o `/` e o `/g` ficam com uma cor mais clara e apenas o nosso `a` nos importa.

Tendo isso em mente, podemos então finalmente conhecer nossos metacaracteres!

### 1. Texto normal:

Texto normal? O que você quer dizer com isso? Bom, vamos começar agora a “casar” as coisas que queremos utilizando as _Regex_, e a primeira coisa que temos que saber é que qualquer caractere pode ser usado para “casar” algo! Não entendeu? Vamos ver um exemplo.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_3.png)

Viu só? Nossa expressão regular é apenas um `e`, e o que ela fez? Oras, ela “pegou” todos os `e` que existiam no nosso texto, simples, não?
Mas será que `e` e `E` casam a mesma coisa?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_4.png)

Veja só, `e` e `E` são coisas diferentes! Nossas expressões regulares são _case sensitive_, ou seja, existe diferença entre maiúsculas e minúsculas.

Esse “texto normal” a qual me referi como título deste tópico pode ser qualquer coisa, não só letras, mas também números, caracteres especiais (alguns caracteres precisam ser “escapados”, isso vamos ver um pouco mais à frente).

### 2. Lista []:

Lista? Não entendi. Bom, nas expressões regulares vamos definindo padrões, por exemplo: capture pra mim um texto que começa com uma letra qualquer, seguido de um ou mais espaços, seguido de três números cujo primeiro caractere seja um ou dois. Sacou? Vamos definindo as restrições para o _match_. 

Mas você leu o que coloquei ali? “um texto que começa com uma letra qualquer”. Até agora vimos como pegar uma só letra e em qualquer parte do texto, mas como faço para que sejam capturados um conjunto de letras ou números? É fácil. pra isso utilizamos a lista `[]`.

Veja, se eu escrever uma expressão regular `[abcd]`, significa que estou procurando o caractere `a`, ou `b` ou `c` ou `d`, ou seja, tudo o que está dentro desta lista. Podemos também misturar as coisas, colocar `[ab12]`, ou seja, estamos procurando a ou b ou 1 ou 2 como caractere.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_5.png)

Veja neste exemplo, estou pegando todos os caracteres a, b, c e d. Mas e se eu tirar a lista?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_6.png)

Agora a _Regex_ pegou apenas o `abcd` que coloquei de propósito no final do nosso texto. Entendeu? Sem a lista, o que falamos para a _Regex_ é que ela tem que capturar a palavra `abcd`, ou seja, uma letra `a` que seja seguida de uma letra `b` que por sua vez seja seguida por `c` e que finalmente seja seguida por `d`, entendeu? Por isso ele capturou o `abcd` que colocamos no final!

Existem duas outras coisas que podem ser usadas em listas e que é muito importante pra nós. Vamos explorá-las logo a seguir.

### 3. O - (intervalo):

O intervalo, que é definido através de um hífen, pode ser utilizado apenas dentro de uma lista. No exemplo anterior, vimos que se quisermos capturar as letras `a`, `b`, `c` ou `d`, podemos usar `[abcd]`, mas e se quisermos qualquer letra? E se for tanto maiúscula como minúscula? Devemos escrever um grupo com todas as letras? Bom, poderíamos fazer isso da mesma forma que fizemos anteiormente, mas nossa _Regex_ ficaria um tanto quanto grande, não? Então, por isso existe o intervalo.

Se quisermos pegar uma lista de `a` a `z`, basta então escrever `[a-z]`, viram? simples não é? E se quisermos todas as letras de `a` a `z` e também as de `A` a `Z`? Basta usar `[a-zA-Z]`, note que podemos colocar números também `[a-zA-Z0-9]`, nessa última Regex, estamos pegando qualquer letra de `a` a `z`, de `A` a `Z`, e todos os números de 0 a 9.

Guardem uma coisinha no coração de vocês, `[a-zA-Z]` pode ser substituído por `\w` (w de _word_) e `[0-9]` pode ser substituído por `\d` (d de _digit_). Vocês viram que o `\w` e o `\d` ficam sem o `[]` da lista né? Mas caso queiram combinar os dois, basta colocar ambos dentro de uma nova lista! Não entendeu? Lembra do nosso `[a-zA-Z0-9]`? Então, podemos escrever ele como `[\w\d]`. =)

Veja no exemplo abaixo onde utilizo a _Regex_ `\w`, a _Regex_ captura todas as letras, só não captura os números, espaços, caracteres especiais e etc, afinal, pedimos a ela que pegue apenas as letras, não é mesmo?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_7.png)

Você viu que os caracteres estão todos capturados separadamente? E se quisermos capturar as palavras inteiras, como fazemos?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_8.png)

Viu o nosso quantificador em ação? O `+` definiu que buscamos um `\w` (qualquer letra) que se repita `+` (uma ou mais) vezes. Mas veja bem, o `\w` é quem vai se repetir, não significa que a letra precisa ser repetida. Sendo assim, a expressão regular `\w+` vai pegar todas as palavras inteiras =)

O `abcd` pegava um `a` seguido de um `b` e assim sucessivamente. O `\w+` pega um `\w` seguido de um `\w` seguido de um `\w`, quantas vezes for possível.

Mas e se quisermos pegar as palavras junto com os espaços? Podemos também usar uma lista! Dentro de uma lista posso colocar qualquer caractere, e o espaço é um deles, veja:

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_9.png)

Seguindo a mesma lógica anterior, ele vai capturar se for um `\w` ou um espaço até encontrar algo que não seja isso, seja um ponto, uma quebra de linha ou qualquer outro caractere.

### 4. A Lista Negada [^]:

Ahn? Lista Negada? É, então, repararam que até agora definimos tudo o que queremos? E se nós quisermos definir o que não queremos?
Vamos supor, e se quisermos pegar tudo o que não seja letra, como faremos? Temos que criar uma lista com tudo o que existe menos as letras? Você até pode fazer isso, mas dará um pouco de trabalho! E se ao invés disso tivesse um jeito de definirmos o que não queremos?! Pois bem, isso existe e é a lista negada. A sua sintaxe é bem parecida com a lista de verdade, no entanto existe um `^` logo no começo da lista.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_10.png)

Viram ali? `[^a]`, o que essa _Regex_ faz? Pega tudo o que não for `a` e que se repita de uma a infinitas vezes. Simples, não?

Agora você deve estar se perguntando: "Ué, e se eu quiser colocar o `^` literalmente dentro de uma lista, como eu faço?"

Lembra que comentei que alguns caracteres precisavam ser “escapados”? Então, este é um deles. Caso queira colocar o `^` (circunflexo) dentro de uma lista para capturá-lo você tem 2 opções: A primeira é não colocar ele na primeira posição da lista e a segunda é “escapar” o `^` utilizando uma contra-barra `\`, ficando assim `[\^]`. De forma bem resumida, a contra-barra “anula” a função de um metacaractere de uma _Regex_ e torna o caractere literal. Toda vez que “escapamos” um caractere, a _Regex_ ignora a contra-barra e lê o caractere especial como caractere literal, por exemplo, `\^` para a _Regex_ é como se fosse um `^` no texto que estamos trabalhando. Mais à frente veremos isso em mais detalhes, só deixando este adendo agora para que não cause confusão depois.

### 5. O . (ponto) - O Coringa:
Esse é o mais simples de entender. O ponto `.` significa literalmente qualquer coisa exceto uma quebra de linha. Pode ser um espaço, uma letra, um número, um arroba, vocês entenderam né? Sendo assim, o que aconteceria se eu usasse a regex `.+`? Exatamente, vamos pegar todo o texto, tirando apenas a quebra de linha! Afinal, pode ser qualquer coisa repetidas de uma a infinitas vezes.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_11.png)

Vocês vão ver que o ponto será um dos metacaracteres mais usados em suas _Regex_. Podemos pensar em algo assim: qualquer coisa, seguido de um espaço, seguido de dois números, por exemplo.
O ponto é mais um dos caracteres que precisam ser escapados, afinal, e se quisermos capturar literalmente um ponto, como faremos? Simples, basta usar `\.`.

## C. Metacaracteres de posição:

Viram que até agora tudo o que pegamos estava “em qualquer lugar”? E se quisermos pegar o início ou fim de uma palavra, ou então o início de um parágrafo, como fazemos? Com o que vimos até agora até que dá pra fazer alguma coisa. O início de uma palavra, por exemplo, pode ser identificado como uma lista negada de tudo o que não é uma letra seguido de uma letra. O final de uma palavra, por sua vez, tudo o que for letra seguido do que não é letra. Mas as Regex estão preparadas para lidar com isso de uma maneira mais simples, veremos 3 destes metacaracteres de posição.

### 1. ^ (circunflexo) - O Início de uma linha:
Quando começamos uma expressão regular com `^`, significa que o que estamos procurando deve começar do início da linha e não em qualquer lugar. Vamos ver um exemplo pra ficar mais claro?
Neste exemplo iremos usar uma nova expressão regular que ainda não usamos, que é a `\s` que irá casar espaços ou _tabs_.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_12.png)

Vamos ler juntos essa expressão regular? Estou dizendo para "casar" o texto se ele começar com um ou mais espaços, podendo ter qualquer coisa logo após! Ué, mas não casou nada, por que? Simples, porque o nosso texto não começa com espaço!
Agora o que acontece se tirarmos esse `^` dali?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_13.png)

Viu só? A expressão regular vai encontrar o primeiro espaço, independente de onde ele estiver e em seguida pegar tudo o que tem após!
E se utilizarmos a primeira expressão regular e adicionarmos um espaço no início do texto, vamos ver o que acontece?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_14.png)

Viu só? agora ele capturou o nosso texto!

### 2. $ (cifrão) - O fim de uma linha:

Acho que já entenderam né? Se eu usar o `$` no final de uma expressão regular, eu estou definindo que tudo o que tiver antes só é válido se eu chegar no final da linha! Não entendeu? Vamos supor que eu quero selecionar tudo só se no final da linha tiver a letra `a`.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_15.png)

Viu só? Ele capturou apenas a palavra Amora pois é a única que a linha termina com `a`. E se quiséssemos selecionar todas as linhas que terminam com vogal, como faríamos?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_16.png)

Legal né? Utilizamos um grupo e conseguimos selecionar facilmente todas as palavras que terminam em vogal.

### 3. \b  - A borda:
O `\b` serve para definirmos borda de palavra, ou seja, o início ou fim dela. Vamos supor que queremos selecionar todas as palavras que comecem com vogal em um texto, como fazemos? É simples!

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_17.png)

Curtiu? e se quiséssemos as palavras que terminam em vogal?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_18.png)

Simples, não? Viu como poupamos muito trabalho utilizando as expressões regulares?

## D. Metacaracteres de especiais:

### 1. \  - A kryptonita:

A contra-barra é utilizada para "escapar" os caracteres especiais, é bem simples de entender ela! Você viu que temos alguns metacaracteres especiais né? Como por exemplo o ponto, o asterisco, o mais... E se quisermos usar eles literalmente, como fazemos? Basta usar a contra-barra, e.g. `\.`. A contra-barra é como uma _kryptonita_, ela anula a função especial dos metacaracteres. Então, por exemplo, `\.` vai "casar" um ponto, `\+` vai "casar" um mais e assim por diante! Se algum caracter é especial e quiser utilizar ele literalmente, basta colocar uma contra-barra nele, inclusive na própria contra-barra `\\` que seria uma contra-barra escapando ela mesma!

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_19.png)

### 2. ()  - O grupo:

Percebeu que falei, falei, falei... e você entendeu como capturar esses dados, mas pra onde eles vão? Bom, na maioria das linguagens, se utilizarmos um grupo, que nada mais é que colocar parênteses no local onde queremos uma parte de uma expressão regular, estes valores vão para um _Array_.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_20.png)

Viu a nossa _regex_? Ela seleciona letras seguido de números seguido de letras! Mas apenas os números estão com parênteses, viu? `(\d+)`, sendo assim, estes números irão ser retornados em um _Array_ utilizando a função _regex_ da linguagem que estiver trabalhando. Lembre que se quiséssemos parênteses literais teríamos que escapá-los `\(` e `\)`.

Os grupos possuem uma condição especial que se não quisermos capturarmos o que tem dentro dele, basta começa-lo com `?:`, por exemplo `(?:\d+)`, este grupo irá agir exatamente como o anterior, só que os dados não serão capturados para o _Array_. 

Por que iríamos querer um grupo sem captura? Este tipo de grupo serve para utilizarmos o “ou”, que será descrito abaixo.

### 3. \|  - O “ou”:
O nome é intuitivo, não? Quando utilizamos uma barra vertical queremos dizer “ou”, mas veja bem, este metacaractere pode ser usado apenas dentro de grupos.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_21.png)

Veja essa expressão regular, perceberam que eu recriei o `\b`? Não? Veja o que está escrito ali!

`(?:^|\s)` : Um grupo sem captura, onde o caractere que estou procurando deve ser o início de uma linha `^` ou um espaço `\s`. 

Captaram a ideia?

### 4. Quantificadores gulosos e não gulosos:

Estranho esse nome? Mas o conceito é simples, vamos vê-lo a partir de um exemplo:

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_22.png)

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_23.png)

Qual é a diferença entre essas duas expressões regulares? Se você observou bem, existe um `?` a mais na segunda expressão regular (ER).

Na primeira ER `<.+>` falamos para ela "casar" um sinal de menor, seguido de qualquer coisa até encontrar um sinal de maior, certo? E foi o que ela fez! A segunda ER fez a mesma coisa, então qual a diferença?

É simples, se utilizarmos um `?` logo após os metacaracteres quantificadores `+` ou `*`, a ER irá parar na primeiro _match_ que conseguir. Sendo assim, na segunda ER estamos dizendo: pegue um sinal de menor seguido de qualquer coisa até você encontrar o primeiro sinal de maior.

Já na primeira ER, não temos esse `?`, logo, dizemos que essa é uma ER __gulosa__, ela vai tentar pegar o máximo de coisas até o último caractere! Vamos ler juntos? "Case" um sinal de menor seguido de qualquer coisa até o último sinal de maior que você encontrar.

## E. Exemplos práticos

E aí, chegou até aqui? viu que ER não é um monstro? É só ir aos poucos e aprender a ler e escrever uma ER e tudo fica bem!

Vamos ver um exemplo prático de extração de dados?

### 1. Pokémon Go

Vamos supor que você joga _Pokémon Go_ e quer adicionar novos amigos no jogo. Você descobre que tem o _site_ __<a target="_blank" href="https://pogotrainer.club/" target="_">pogotrainer.club</a>__ que tem o _id_ de vários jogadores, e decide acessar essa página.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_24.png)

Poxa, legal, tá aí alguns _trainer codes_, que é justamente o que você procurava! Você quer montar um _excel_ disso pra facilitar o processo de adicioná-los no jogo! Mas e aí? copiar um por um? E se selecionarmos todo o texto, será que não conseguimos extrair esses dados com alguma expressão regular?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_25.png)

Olha que simples, sabemos que são vários números seguido de um hífen, seguido de vários números, hífen de novo, seguido de vários números. Em poucos segundos conseguimos extrair os dados que queremos!

### 2. Número de telefone

E se você quer extrair o telefone de alguém, como fazer?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_26.png)

Parece maluca essa ER? vamos ler juntos?

Bom, essa ER captura o DDD e o telefone da pessoa e se não tiver DDD, ela captura apenas o telefone! Vamos montar ela aos poucos...

* `\(\d+\)` -> um “abre parênteses” seguido de vários números, seguido de um “fecha parênteses”.

* `\((\d+)\)` -> Aqui coloquei o `\d+` dentro de parênteses pois quero capturar esse DDD. Mas quero que isso possa ou não existir, como faço? Só colocar ele dentro de um grupo sem captura e torná-lo opcional.

* `(?:\((\d+)\))?` -> Aqui colocamos ele dentro de um grupo sem captura com um `?` na frente, ou seja, esse grupo pode ou não existir.

* `(\d+\-?\d+)` -> Aqui nada de complexo né? Apenas legal enfatizar o `\-?` que eu coloquei que assim o número de telefone pode ou não ter hífen.

Viu? construindo nossa ER aos poucos elas se tornam menos assustadoras e de fácil compreensão!

{% include rodolfo-box.html %}
