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

O conteúdo é direcionado à pessoas que tenham noções básicas de programação. Sendo um complemento para o post __<a target="_blank" href="{% post_url 2019-07-04-linha-de-comando-para-ciencia-de-dados %}" target="_">Linha de comando para Data Science</a>__.

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

Na imagem acima podemos ver uma expressão regular que extrai datas de um texto (as datas estão marcadas em azul), não importa onde elas estão, seja perto de textos, espaços, números, algarismos especiais e etc. Logo à frente veremos que essa expressão possui falhas pois ela pode pegar coisas que se pareçam com datas mas não são, como 87/22/2001, afinal, não temos dia 87 e nem mês 22, no futuro veremos como fazer uma expressão regular mais refinada para pegar somente o que queremos mesmo. Mas lembrem-se sempre, quanto mais simples a _regex_ (abreviação de _regular expression_), melhor.

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

Texto normal? O que você quer dizer com isso? Bom, vamos começar agora a “casar” as coisas que queremos utilizando as _regex_, e a primeira coisa que temos que saber é que qualquer caractere pode ser usado para “casar” algo! Não entendeu? Vamos ver um exemplo.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_3.png)

Viu só? Nossa expressão regular é apenas um `e`, e o que ela fez? Oras, ela “pegou” todos os `e` que existiam no nosso texto, simples, não?
Mas será que `e` e `E` casam a mesma coisa?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_4.png)

Veja só, `e` e `E` são coisas diferentes! Nossas expressões regulares são _case sensitive_, ou seja, existe diferença entre maiúsculas e minúsculas.

Esse “texto normal” a qual me referi como título deste tópico pode ser qualquer coisa, não só letras, mas também números, caracteres especiais (alguns caracteres precisam ser “escapados”, isso vamos ver um pouco mais à frente).

### 2. Lista []:

Lista? Não entendi. Bom, nas expressões regulares vamos definindo padrões, por exemplo: capture pra mim um texto que começa com uma letra qualquer, seguido de um ou mais espaços, seguido de três números cujo primeiro caractere seja um ou dois. Sacou? Vamos definindo as restrições para o _match_. 

Mas você leu o que coloquei ali? “um texto que começa com uma letra qualquer”. Até agora vimos como pegar uma só letra e em qualquer parte do texto, mas como faço para que sejam capturados um conjunto de letras ou números? É fácil. pra isso utilizamos a lista `[]`.

Veja, se eu escrever uma expressão regular `[abcd]`, significa que estou procurando o caractere `a`, ou `b` ou `c` ou `d`, ou seja, tudo o que está dentro desta lista. Podemos também misturar as coisas, colocar `[ab12]`, ou seja, estamos procurando `a` ou `b` ou `1` ou `2` como caractere.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_5.png)

Veja neste exemplo acima: Estou pegando todos os caracteres `a`, `b`, `c` e `d`. Mas e se eu tirar a lista?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_6.png)

Agora a _regex_ pegou apenas o `abcd` que coloquei de propósito no final do nosso texto. Entendeu? Sem a lista, o que falamos para a _regex_ é que ela tem que capturar a palavra `abcd`, ou seja, uma letra `a` que seja seguida de uma letra `b` que por sua vez seja seguida por `c` e que finalmente seja seguida por `d`, entendeu? Por isso ele capturou o `abcd` que colocamos no final!

Existem duas outras coisas que podem ser usadas em listas e que é muito importante pra nós. Vamos explorá-las logo a seguir.

### 3. O - (intervalo):

O intervalo `-`, que é definido através de um hífen, pode ser utilizado apenas dentro de uma lista. No exemplo anterior, vimos que se quisermos capturar as letras `a`, `b`, `c` ou `d`, podemos usar `[abcd]`, mas e se quisermos qualquer letra? E se for tanto maiúscula como minúscula? Devemos escrever um grupo com todas as letras? Bom, poderíamos fazer isso da mesma forma que fizemos anteiormente, mas nossa _regex_ ficaria um tanto quanto grande, não? Então, por isso existe o intervalo.

Se quisermos pegar uma lista de `a` a `z`, basta então escrever `[a-z]`, viram? simples não é? E se quisermos todas as letras de `a` a `z` e também as de `A` a `Z`? Basta usar `[a-zA-Z]`, note que podemos colocar números também `[a-zA-Z0-9]`, nessa última _regex_, estamos pegando qualquer letra de `a` a `z`, de `A` a `Z`, e todos os números de 0 a 9.

Guardem uma coisinha no coração de vocês, `[a-zA-Z]` pode ser substituído por `\w` (w de _word_) e `[0-9]` pode ser substituído por `\d` (d de _digit_). Vocês viram que o `\w` e o `\d` ficam sem o `[]` da lista né? Mas caso queiram combinar os dois, basta colocar ambos dentro de uma nova lista! Não entendeu? Lembra do nosso `[a-zA-Z0-9]`? Então, podemos escrever ele como `[\w\d]`. =)

Veja no exemplo abaixo onde utilizo a _regex_ `\w`, a _regex_ captura todas as letras, só não captura os números, espaços, caracteres especiais e etc, afinal, pedimos a ela que pegue apenas as letras, não é mesmo?

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

Viram ali? `[^a]+`, o que essa _regex_ faz? Pega tudo o que não for `a` e que se repita de uma a infinitas vezes. Simples, não?

Agora você deve estar se perguntando: "Ué, e se eu quiser colocar o `^` literalmente dentro de uma lista, como eu faço?"

Lembra que comentei que alguns caracteres precisavam ser “escapados”? Então, este é um deles. Caso queira colocar o `^` (circunflexo) dentro de uma lista para capturá-lo você tem 2 opções: A primeira é não colocar ele na primeira posição da lista e a segunda é “escapar” o `^` utilizando uma contra-barra `\`, ficando assim `[\^]`. De forma bem resumida, a contra-barra “anula” a função de um metacaractere de uma _regex_ e torna o caractere literal. Toda vez que “escapamos” um caractere, a _regex_ ignora a contra-barra e lê o caractere especial como caractere literal, por exemplo, `\^` para a _regex_ é como se fosse um `^` no texto que estamos trabalhando. Mais à frente veremos isso em mais detalhes, só deixando este adendo agora para que não cause confusão depois.

### 5. O . (ponto) - O Coringa:

Esse é o mais simples de entender. O ponto `.` significa literalmente qualquer coisa exceto uma quebra de linha. Pode ser um espaço, uma letra, um número, um arroba, vocês entenderam né? Sendo assim, o que aconteceria se eu usasse a _regex_ `.+`? Exatamente, vamos pegar todo o texto, tirando apenas a quebra de linha! Afinal, pode ser qualquer coisa repetidas de uma a infinitas vezes.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_11.png)

Vocês vão ver que o ponto será um dos metacaracteres mais usados em suas _regex_. Podemos pensar em algo assim: qualquer coisa, seguido de um espaço, seguido de dois números, por exemplo.
O ponto é mais um dos caracteres que podem ser escapados, afinal, e se quisermos capturar literalmente um ponto, como faremos? Simples, basta usar `\.`.

## C. Metacaracteres de posição:

Viram que até agora tudo o que pegamos estava “em qualquer lugar”? E se quisermos pegar o início ou fim de uma palavra, ou então o início de um parágrafo, como fazemos? Com o que vimos até agora até que dá pra fazer alguma coisa. O início de uma palavra, por exemplo, pode ser identificado como uma lista negada de tudo o que não é uma letra seguido de uma letra. O final de uma palavra, por sua vez, tudo o que for letra seguido do que não é letra. Mas as _regex_ estão preparadas para lidar com isso de uma maneira mais simples, veremos 3 destes metacaracteres de posição.

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

A contra-barra é utilizada para "escapar" os caracteres especiais, é bem simples de entender ela! Você viu que temos alguns metacaracteres especiais né? Como por exemplo o ponto, o asterisco, o mais... E se quisermos usar eles literalmente, como fazemos? Basta usar a contra-barra, e.g. `\.`. A contra-barra é como uma _kryptonita_, ela anula a função especial dos metacaracteres. Então, por exemplo, `\.` vai "casar" um ponto, `\+` vai "casar" um mais e assim por diante! Se algum caractere é especial e quiser utilizar ele literalmente, basta colocar uma contra-barra nele, inclusive na própria contra-barra `\\` que seria uma contra-barra escapando ela mesma!

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_19.png)

### 2. ()  - O grupo:

Percebeu que falei, falei, falei... e você entendeu como casar esses dados, mas pra onde eles vão? Bom, na maioria das linguagens, se utilizarmos um grupo, que nada mais é que colocar parênteses no local onde queremos capturar uma parte de uma expressão regular, estes valores vão para um _Array_. O grupo não altera em nada nossa _regex_, ele não casa coisa a mais ou a menos, ele apenas diz para nossa linguagem de programação quais dos valores devem ser retornados pela nossa função de _regex_.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_20.png)

Viu a nossa _regex_? Ela seleciona letras seguido de números seguido de letras! Mas apenas os números estão com parênteses, viu? `(\d+)`, sendo assim, estes números irão ser retornados em um _Array_ utilizando a função _regex_ da linguagem que estiver trabalhando. Não entendeu? Bom, nossa _regex_ vai __casando__ todos os caracteres que nós definimos e nos mostra por onde ela está "andando", mas, de modo geral, quando utilizamos uma _regex_ nós queremos capturar um dado, então, apenas o que está dentro do parênteses '`()` é que será retornado pela minha função. Vamos supor, temos um texto enorme e no fim dele temos a seguinte string:

São Paulo, 20 de julho de 2019.

Se nós quisermos pegar o ano deste documento, temos que usar uma _regex_ que case a linha que eu quero para garantir que estou pegando o número certo, mas apenas o número é importante para mim, por isso, eu poderia usar a seguinte _regex_ para fazer o trabalho:

`São Paulo.+(\d+)\.`

Viram que eu casei toda a minha string mas apenas o 2019 foi capturado? se eu usasse um `(\d+)` eu iria capturar todos os números do meu texto, o que não é o que eu quero... Por isso entenda, caracteres que foram casados, não necessariamente são capturados.


E ah, os parênteses também podem ser escapados, viu? Por isso se quisermo parênteses literais, temos que usar `\(` e `\)`.

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

### 5. O grupo negador (?!)

Esse é bem parecido com a lista negada, mas, é um grupo e não uma lista... 
Em algum momento você deve ter pensado... e se eu quiser EXCLUIR algum caractere, conjunto de caracteres ou coisas do tipo, como eu faço? A lista negada funciona, mas ela só funciona para um caractere ou lista de caracteres, mas não para uma palavra inteira, por exemplo. Bom, agora vou te ensinar como usar o grupo negador, mas note que este funciona de um modo __um pouquinho diferente__, mas nada que não possamos entender, okay?

Vamos supor que temos as palavras:

Haha
Hehe
Hihi
Hoho
Huhu

E se nós quisermos casar palavras que começam com __H__ e em seguida tenham letras __DIFERENTES__ de __a__, como fazemos?
Para resolvermos este problema, apresentou pra vocês o grupo negador `(?!)`, e como ele funciona? Para entendermos, vamos resolver o problema proposto acima?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_24.png)

Bom, vamos analisar até aqui:
Eu quero coisas que tenham `H` seguido de um `(?!a)`, conseguem entender essa ultima parte? O grupo `(?!)` é um negador, tudo o que estiver depois de `!` será negado, neste caso, a letra `a`.
Só que veja bem, preste atenção no detalhe, a nossa _regex_ só selecionou o `H`, ela não selecionou o próximo caractere (que é diferente de `a`), e ai temos uma coisa importante: a lista negadora __não casa nada__, ela só define o que não queremos, __para casar os próximos caracteres temos que continuar nossa expressão regular__. Vamos supor que queremos o próximo caractere após o `H`, podemos casá-lo utilizando o `.`, correto? Pois bem, vamos fazer isso:

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_25.png)

Ótimo, missão cumprida!
Mas... vocês sabem me dizer... E se eu quisesse tudo o que é `H` e logo após não pode ter nem `a` e nem `e`, como fazemos? É simples, dentro do grupo negador eu posso usar as expressões regulares normalmente, lembra do nosso querido `|` (ou) ? Podemos utilizar ele.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_26.png)

Agora ficou claro, certo? Mas, só por garantia, e se não quiséssemos após o `H`, nem `a`, nem `e` e nem `i`, podemos usar vários `|`, certo? Sim, dará certo, mas por que não podemos usar nossa querida lista `[]` ?


![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_27.png)

Viram? Apesar de diferente, basta prestar atenção na estrutura da nossa _regex_ que tudo dará certo!
Eu sei que vocês entenderam até aqui, mas vamos pra um exemplo um pouquinho mais difícil?
Vamos supor que agora temos os seguintes dados:

EFI Internal Shell
EFI Hard Drive
EFI Drive

E vamos supor que queremos casar todas as linhas que __não__ contenham a palavra __Drive__ nela, ok? Como podemos fazer isso?
Bom, a melhor maneira de fazermos isso é começar selecionando o que não queremos e então negar isso, assim, poderemos casar apenas o que queremos... Vamos tentar?
Então primeiramente vamos casar o que não queremos, e pra isso, vou fazer o seguinte: Eu quero qualquer coisa até encontrar a palavra __Drive__ e depois pode ter qualquer coisa (inclusive nada) faz sentido?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_28.png)

Com o que sabemos até aqui podemos ver que essa _regex_ faz exatamente o que descrevi acima! Agora basta colocar isso em nosso grupo negador `(?!)`.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_29.png)

Veja, os riscos rosas da imagem acima representam os caracteres que estão disponíveis para capturarmos, mas temos um problema... Depois do __D__ da palavra __Drive__, vem __ive__ (o restante da palavra Drive sem o D), correto? E a partir dali realmente não tem mais a palavra Drive, então na teoria aquilo está disponível pra nós, mas e agora? Calma, pra resolvermos isso basta adicionar um `^` ao início da nossa _regex_.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_30.png)

E com isso estamos restringindo que nossa string começa com nossa restrição, logo, após encontrar Drive a minha _regex_ irá parar. Eu sei, eu sei, é confuso, mas __é só seguir essa receitinha que tudo vai dar certo__, eu prometo!Lembra que falei que nossa restrição não casa caractere algum? Pois é, até agora não temos capturados sequer um caractere, vamos então pegar a linha toda utilizando o famoso `.+` ? Basta adicionar isso ao final da nossa restrição:

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_31.png)

Note que coloquei o `.+` dentro de parênteses e que como vimos anteriormente este valor será capturado.
Bom, com estes dois exemplos acredito que poderão brincar tranquilamente com o grupo negador por aí.


## E. Exemplos práticos

E aí, chegou até aqui? viu que ER não é um monstro? É só ir aos poucos e aprender a ler e escrever uma ER e tudo fica bem!

Vamos ver um exemplo prático de extração de dados?

### 1. Pokémon Go

Vamos supor que você joga _Pokémon Go_ e quer adicionar novos amigos no jogo. Você descobre que tem o _site_ __<a target="_blank" href="https://pogotrainer.club/" target="_">pogotrainer.club</a>__ que tem o _id_ de vários jogadores, e decide acessar essa página.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_32.png)

Poxa, legal, tá aí alguns _trainer codes_, que é justamente o que você procurava! Você quer montar um _excel_ disso pra facilitar o processo de adicioná-los no jogo! Mas e aí? copiar um por um? E se selecionarmos todo o texto, será que não conseguimos extrair esses dados com alguma expressão regular?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_33.png)

Olha que simples, sabemos que são vários números seguido de um hífen, seguido de vários números, hífen de novo, seguido de vários números. Em poucos segundos conseguimos extrair os dados que queremos!

### 2. Datas
Lembra lá no começo que eu falei que a _regex_ de data que eu fiz estava muito simples e que era cabivel de erro? Agora vou mostrar uma um pouquinho melhor, que evita alguns erros mas que ainda não é perfeita!

Mas por que não é perfeita? Simples, porque essa _regex_ nos permitirá capturar dias 31/02/2019, por exemplo, um dia que não existe, mas será impossivel capturar um mês além do mês 12 ou um dia além do dia 31.

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_34.png)

Sem mais delongas, ai está nossa _regex_: `([0-2][0-9]|3[0-1])\/(0[0-9]|1[0-2])\/(\d{4})`

Ela parece um bicho de 7 cabeças, eu sei, mas vamos ver elas aos poucos e vamos conseguir entender!

Vou desmembrar nossa _regex_:

`([0-2][0-9]|3[0-1])`

Aqui podemos observar pelos parênteses de fora que este dado será capturado, correto? Logo, o dia da minha data será retornado na minha função de _regex_!

Reparem dentro, temos um __ou__ `|`. Mas __ou__ o que?

`[0-2][0-9]` ou `3[0-1]`

Um número de 0 a 2 `[0-2]` seguido de um número de 0 a 9 `0-9` ou um número 3 `3` seguido de um número de 0 a 1 `[0-1]`.

Ou seja, todos os dias do dia 0 ao 29, ou então um dia do dia 30 ao 31, certo?

Esse número é seguido de um `\/` ou seja, uma barra escapada, ou seja, uma barra `/`.

`(0[0-9]|1[0-2])`

Aqui de novo temos parênteses demonstrando a captura do nosso dado, ou seja, nosso mês também será capturado e retornado para nosso array, além disso, novamente temos a presença do __ou__ `|`.

`0[0-9]` ou `1[0-2]`

Um número 0 `0` seguido de um número de 0 a 9 `[0-9]` ou um número 1 `1` seguido de um número de 0 a 2 `[0-2]`.

Logo, qualquer mês de 00 a 09 ou o mês de 10 a 12.

Novamente esse número é seguido de um `\/` ou seja, uma barra escapada, ou seja, uma barra `/`.

Por fim mas não mesmo importante, temos: `(\d{4})`, ou seja, uma sequência de 4 números que será o nosso ano.

Com isso, caso utilizemos essa _regex_ na string 21/02/2016, por exemplo, teremos como saída no nosso array o seguinte:

Array[0] = 21
Array[1] = 02
Array[2] = 2016


### 3. Número de telefone

E se você quer extrair o telefone de alguém, como fazer?

![Print da tela do terminal configurada]({{site.baseurl}}/assets/img/rodolfo_re_35.png)

Parece maluca essa ER? vamos ler juntos?

Bom, essa ER captura o DDD e o telefone da pessoa e se não tiver DDD, ela captura apenas o telefone! Vamos montar ela aos poucos...

* `\(\d+\)` -> um “abre parênteses” seguido de vários números, seguido de um “fecha parênteses”.

* `\((\d+)\)` -> Aqui coloquei o `\d+` dentro de parênteses pois quero capturar esse DDD, apenas o número, sem os caracteres dos paranteres (não confundir o caractere de parênteses com o metacaractere de parênteses). Mas quero que o número possa ou não ter um DD, como faço isso? Basta colocar minha _regex_ que captura o DDD dentro de um grupo sem captura e tornar esse grupo sem captura opcional (veja aqui que posso colocar um grupo de captura dentro de um grupo sem captura. Caso o DDD exista, este será retornado pela minha função de _regex_, caso contrário, minha _regex_ continuará mesmo seo o DDD).

* `(?:\((\d+)\))?` -> Aqui colocamos ele dentro de um grupo sem captura com um `?` na frente, ou seja, esse grupo pode ou não existir.

* `(\d+\-?\d+)` -> Aqui nada de complexo né? Apenas legal enfatizar o `\-?` que eu coloquei que assim o número de telefone pode ou não ter hífen.

Viu? construindo nossa ER aos poucos elas se tornam menos assustadoras e de fácil compreensão!

Espero que tenha ajudado vocês e lembrem-se dos ensinamentos do E.T Bilu: Busquem conhecimento!

Aquele beijo a todos!

{% include rodolfo-box.html %}
