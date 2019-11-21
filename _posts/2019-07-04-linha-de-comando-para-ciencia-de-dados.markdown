---
layout: post
title: Linha de comando para Ciência de Dados
date: 2019-07-04 21:31:57
img: terminal-code.jpg
tags: [Ciência de Dados]
author: Lorenzo Cesconetto
published: true
---

<!--

OBSERVAÇOES:

1) CRIAR SECAO DE FLAGS / DEFAULT PARA CADA COMANDO.

2) COMEÇAR EXPLICANDO O COMANDO E DEPOIS SUA APLICAÇÃO EM CIENCIA DE DADOS.

3) COLOCAR OS OUTPUTS.

-->


&emsp; &emsp; O conteúdo desse post é direcionado à pessoas **técnicas** na área de computação, não é preciso ter experiência prévia com de Ciência de Dados. Mas é recomendável conhecimento básico do terminal unix.

Você deve estar se perguntando, porque diabos eu deveria utilizar a linha de comando para Ciência de Dados? Primeiramente, os comandos em **Shell Script** para a manipulação de arquivos são muito mais rápidos do que os comandos em Python ou R, e são muito eficientes em termos de memória. Além disso, pode ser conveniente começar a limpeza dos dados pela linha de comando, e terminar em uma outra linguagem utilizando funções mais complexas.

> __Observação importante:__ Estou utilizando um MacBook OSX Mojave. Alguns comandos possuem uma implementação um pouco diferente da plataforma Unix original.

Como é muito difícil memorizar todos os comandos "de primeira", recomendo ler o conteúdo desse _post_ enquanto executa os comandos ensinados na sua própria máquina, depois disso salve o link desse guia para realizar consultas quando não lembrar de alguma sintaxe (espero que isso te economize tempo de pesquisa no Google).

Para criar um arquivo *teste.txt*, navegue até o diretório onde se deseje criar o arquivo, e digite no terminal:

```
touch teste.txt
```

Depois disso, abra o arquivo no editor de texto _nano_ (ou o editor de sua preferência) com o comando:

```
nano teste.txt
```

Copie e cole o seguinte conteúdo (assim nós dois teremos o mesmo arquivo para comparar os resultados):

```
codigo_produto;descricao;preço;estoque;mês
2;Maça;01,50;2;January
5;Uva;1,00;1;February
3;Banana;2,00;4;March
4;Pera;3:00;10;December
5;Uva;1,00;1;February
6;Melão;0,50;0;November
3;Banana;2,00;4;March
5;Uva;1,00;1;February
6;Melão;0,50;0;November
```
<br>
# Unix Commands
<br>
Como _reminder_ inicial, o comando `man` (abreviação de _manual_) nos mostra a documentação de um comando. Por exemplo, para saber o que o comando `iconv` faz, basta digitar `man iconv`.

<br>
### 1. iconv

Erros de _enconding_ podem ser muito irritantes. Quase todo mundo que trabalha na área de Ciência de Dados já teve problemas desse tipo. O comando `iconv` converte fácilmente o _enconding_ de arquivos e funciona muito bem!
	
Antes de aplicar o `iconv`, é interessante utilizar o comando `file -I` (na plataforma Linux `file -i`) para descobrir qual o encoding atual do arquivo.

```
file -I teste.txt
```

A saída deve ser algo do tipo:

<div class="alert alert-secondary" role="alert">
	teste.txt: text/plain; charset=utf-8
</div>

Agora podemos fazer a conversão especificando as flags:

* _-f_: que indica __de qual__ _encoding_ vamos trasformar.
* _-t_: que indica __para qual__ _encoding_ estamos convertendo (do inglês _to_).

```
iconv -f UTF-8 -t ISO-8859-1 teste.txt
```

Recomendo _<a target="_blank" href="https://www.youtube.com/watch?v=MijmeoH9LT4" target="_">esse vídeo</a>_ para uma breve discussão sobre o UTF-8.

<br>

### 2. wc

O comando **wc** (abreviação de _word count_), apesar do nome, retorna a contagem de linhas, palavras e _bytes_ de um arquivo (nessa ordem). É muito útil para saber o número de observações que temos nos nossos dados sem precisar "abrir" o arquivo ("abrir" pode ser infactível se o arquivo for muito grande).

```
wc teste.txt
```

O output do comando será:

<div class="alert alert-secondary" role="alert">
  9      10     252 teste.txt
</div>

<br>

### 3. head e tail

Em projetos de Ciência de Dados é muito comum se deparar com arquivos *csv* (ou similares) que sejam muito grandes, o que impossibilita sua visualização por meio de editores de texto. Um comando rápido para visualizar as primeiras linhas (e descobrir que tipo de dados temos ali) do arquivo é o `head` (ou para visualizar as últimas `tail`):

Flags:
* _-n:_ Especifica o número de linhas.

```
head -n 2 teste.txt # Retorna as primeiras 2 linhas
tail -n 1 teste.txt # Retorna a última linha
```

O output do primeiro comando será:


<div class="alert alert-secondary" role="alert">
codigo_produto;descricao;preço;estoque;mês <br/>
2;Maça;01,50;2;January
</div>

	
Para pular as _n_ primeiras linhas do arquivo, utiliza-se o comando `tail` com o sinal "+" junto ao número de linhas. Por exemplo:

```
tail -n +2 teste.txt # Retorna todas as linhas exceto a primeira
```
Nesse caso, o comando irá retornar as linhas até o final do arquivo a partir da segunda linha.

<br>

### 4. cut
Pode ser muito útil selecionar apenas as colunas relevantes de um arquivo antes de lê-lo em nosso programa (economia de memória, e menor tempo para carregar os dados). Quando temos um arquivo com dados separados por caracter reservado (ex: _csv_) podemos realizar essa seleção através do comando **cut**. No nosso caso, esse caracter é o ";". 

Flags:
* *-d:* indica o caracter delimitador.
* *-f:* indica quais colunas vamos selecionar.

No código abaixo precisaremos escapar o caracter especial ; com uma contra barra, e iremos selecionar as colunas de 1 à 3 e a coluna 5.

```
cut -d \; -f 1-3,5 teste.txt # Retorna as colunas 1, 2, 3 e 5
```
Note que a coluna 4 (estoque) é retirada
<br>
<br>
### 5. sed
Uma operação bem comum na limpeza de dados é trocar as vírgulas que separam os número por pontos, por exemplo, de 1,50 para 1.50, assim fica mais fácil para realizar o _parse_ para _float_. No código abaixo, a _string_ `'s/,/./'` está explicitando uma substituição (daí o primeiro `s`) de `,` por `.`. É possível explicitar múltiplas substituições simultaneamente, basta finalizar cada uma com um `;`:

```
sed 's/,/./' teste.txt # Substitui "," com "."
sed 's/,/./; s/:/./' teste.txt # Substitui "," e ":" por "."
```
<br>
### 6. | (símbolo pipe)
Para combinar múltiplos comandos, utiliza-se o caracter _pipe_, `|`. Ele permite que se crie uma "linha de produção", onde cada comando passa o seu _output_ como _input_ para o próximo. No código abaixo, estamos tomando todas as descrições de produto excluindo o cabeçalho:
```
cut -d \; -f 2 teste.txt | tail -n +2 # Retorna o nome das frutas
```
<div class="alert alert-secondary" role="alert">
Maça <br>
Uva <br>
Banana <br>
Pera <br>
Uva <br>
Melão <br>
Banana <br>
Uva <br>
Melão
</div>

<br>
### 7. sort
O comando `sort` ordena as linhas do arquivo de dados de acordo com os valores da coluna que quisermos, e é muitas vezes pré-requisito para que outros comando funcionem corretamente (por exemplo o `join` que veremos mais adiante). 

Flags:
* *-t:* Especifica o caracter delimitador do arquivo.
* *-n*: deve ser especificada para realizar a ordenação de forma numérica (e não alfabética que é o _default_). 
* *-r:* implica na ordenação inversa, ou seja, do maior para o menor (do ingês _reverse_)
* *-k:* especifica o índice da coluna a ser utilizada para a ordenação.
* *-M:* Realiza a ordenação com os nomes dos meses do ano.

```
sort -t \; teste.txt # Ordena a 1 coluna
sort -k 2 -t \; teste.txt # Ordena a 2 coluna
sed 's/,:/./' teste.txt | sort -k 3 -nr -t \; # Ordena a 3 coluna de forma numérica
sort -k 5 -t \; -M teste.txt # A opcao M faz o sorting com nome dos meses
```
<br>
### 8. uniq
O comando `uniq` realiza operações envolvendo a propriedade de repetição de linhas. Pode ser muito útil para "enxugar" um arquivo muito grande que apresente muitas repetições, ou até para tornar possível carregar o arquivo inteiro na memória. Um detalhe importante desse comando, é que ele exige que o arquivo esteja já ordenado, pois ele realiza as suas operações comparando linhas consecutivas.

Flags:
* _Default:_ Retorna apenas as linhas únicas do arquivo.
* _-c:_ Retorna cada linha com a contagem de quantas vezes apareceu.
* _-d:_ Retorna apenas linhas com duas ou mais ocorrências.
* _-u:_ Retorna apenas as linhas que são únicas.

```
sort -k 1 -t \; teste.txt | uniq # Retorna as linhas do arquivo removendo repetições
sort -t \; -k 1 teste.txt | uniq -c # Conta as ocorrências de cada linha
sort -k 1 -t \; teste.txt | uniq -d # Retorna somente linhas duplicadas
sort -k 1 -t \; teste.txt | uniq -u # Retorna somente linhas não duplicadas
```
<br>

### 9. > (símbolo maior)
Você já deve estar se perguntando, e se eu quisesse salvar o _output_ do meu comando ao invés de simplesmente vê-lo no _terminal_? Você pode guardar o resultado das suas operações em um arquivo utilizando o símbolo de maior, `>`. Caso o arquivo especificado ainda não exista, essa operação irá criar um novo arquivo. Caso um arquivo com esse nome já exista, o comando irá __sobre-escrever__ o conteúdo existente. Por isso, este comando deve ser utilizado com cautela. Caso se queira apenas adicionar o conteúdo ao final de um arquivo já existente (fazer um _append_), deve-se utilizado o `>>`.

```
cat "Frutas únicas" > new_file.txt # Cria o arquivo e escreve na primeira linha
cut -d \; -f 2 teste.txt | tail -n +2 | uniq >> new_file.txt # Append de frutas únicas
```
Faça o teste sem utilizar `>>`. Você verá que a primeira linha, "Frutas únicas", não estará mais lá.
<br>

### 10. echo
O `echo` é um comando simples que pega os _inputs_ passados (argumentos) e os retorna como _standard outputs_, assim é possível utilizar essa saída como entrada de outras funções. Alguns exemplos de uso:

```
echo some text > some_file.txt  # escreve "some text" em um novo arquivo
echo *.jpeg  # imprimir todos os arquivos com extensão jpeg
echo $PATH # imprime a variavel global PATH
```
<br>

### 11. paste
O comando `paste` é utilizado para juntar dois arquivos em um __lateralmente__. Abaixo um exemplo:

Flags:
* _-d:_ Indica qual o delimitador a ser utilizado, por _default_ o _tab_ é utilizado.

```
# Arquivo courses.txt
Linear Algebra
Deep Learning
Discrete Optimization

# Arquivo codes.txt
MAT202
DL101
OPT303

# Arquivo dificulty.txt
2
1
3

paste -d ',' courses.txt codes.txt dificulty.txt
```
<div class="alert alert-secondary" role="alert">
Linear Algebra,MAT202,2<br>
Deep Learning,DL101,1<br>
Discrete Optimization,OPT303,3<br>
</div>

<br>

### 12. join
Esse comando é um pouco parecido com um _join_ de uma _query_ em SQL. O comando faz o _match_ linha a linha das tabelas onde os valores de uma determinada coluna são iguais em ambos os arquivos. Uma observação muito importante: os campos chave para o _matching_ __devem estar ordenados__, caso contrário, o `join` pode não retornar todos os matches. Então, na prática deve-se rodar o comando `sort` em ambos os arquivos antes de realizar o `join`.

Flags:
* _-t:_ Especifica o caracter delimitador do _input_ e do _output_.
* _-a:_ Retorna as linhas sem _match_ do arquivo cujo índice foi especificado.
* _-1 -2 ... :_ Utilizar _-index_ para especificar qual a coluna de _join_ do arquivo de índice correspondente (deve ficar mais claro com o exemplo abaixo).

```
# arquivo_1.txt
cliente,saldo
1,100
2,300
3,500
4,700

# arquivo_2.txt
salário,cliente
15000,1
10000,2
30000,3

join -t , -2 2 arquivo_1.txt arquivo_2.txt
join -a 1 -t , -1 1 -2 2 arquivo_1.txt arquivo_2.txt
```

Os _outputs_ dos dois comandos são respectivamente:

<div class="alert alert-secondary" role="alert">
cliente,saldo,salário <br>
1,100,15000 <br>
2,300,10000 <br>
3,500,30000 <br>
</div>

<div class="alert alert-secondary" role="alert">
cliente,saldo,salário <br>
1,100,15000 <br>
2,300,10000 <br>
3,500,30000 <br>
4,700 <br>
</div>

<br>

### 13. regex
Expressão regular (ou _regex_) é simplesmente uma sequencia de caracteres que definem um padrão de busca. Em outras palavras, uma forma de especificar para o computador como ele deve realizar uma busca em um texto. Aqui daremos somente breve introdução. 

Para entender mais, recomendo o __<a target="_blank" href="{% post_url 2019-11-16-expressoes-regulares-zero-to-hero %}" target="_"> tutorial de Regex: Zero to Hero</a>__, escrito por um amigo __ninja__ no assunto.

Aqui, listamos alguns dos caracteres especiais mais importantes do _regex_ (comumente chamados de _Wildcards_):
* `^`: Indica começo de linha.
* `$`: Indica final de linha.
* `[aA]`: Considera um _match_ se encontrar qualquer um dos elementos dentro dos colchetes (nesse caso "a" ou "A").
* `.`: Considera um caracter qualquer, exceto quebra de linha, para construir um _match_.
* `{n}`: Repete a expressão anterior _n_ vezes.
* `+`: Repete a expressão anterior uma ou mais vezes.
* `*`: Repete a expressão anterior zero ou mais vezes.
* `?`: Repete a expressão anterior zero ou uma vez.
* `\d`: Faz o _match_ para qualquer digito (um algarismo 0-9).

O comando `grep` é o que busca as expressões regulares em textos no **Shell Script**. O interessante de aprender expressões regulares é que a maioria das linguagens oferecem suporte para esse tipo de busca.

Vamos ver alguns exemplos na próxima seção.
<br>

### 14. grep
O comando grep (_Global search for a Regular Expression and Print_) é utilizado para encontrar padrões específicos em textos, _strings_ ou _outputs_. Ele retorna as partes do texto que contém o texto que você buscou. Para esse comando em específico, estou utilizando a implementação do _GNU_ dada que a implementação do _OSX Mojave_ não inclui algumas _flags_ importantes.

Flags:
* _-i:_ Busca _case insensitive_.
* _-E:_ Expressões regulares extendidas.
* _-o:_ Faz o _output_ somente do _match_, e não da linha completa.

```
ls | grep data  # retorna todos os arquivos cujo o nome contém 'data'
grep -i uva teste.txt # retorna ocorrencias de uva no teste
grep -Eo '\d+' myfile.txt  # retorna todos os números
grep -Eo '\d+\s+anos' myfile.txt  # retorna "10 anos"
```
<br>

## Comandos Extras
Por último, trago aqui alguns comandos que podem ajudar no dia-a-dia:

<br>

1. __tr__

	O comando `tr` (abreviação de _translate_) pode fazer diversos tipos de modificações no arquivo.
	```
	tr ';' '*' < teste.txt  # Substitui ; por *
	tr '[A-Z]' '[a-z]' < teste.txt  # converte letras para minusculas
	tr "[:lower:]" "[:upper:]" < teste.txt  # converte letras para maiusculas
	tr -cs "[:alpha:]" "\n" < teste.txt # Lista as palavras contidas no arquivo
	```
	<br>
	<br>

1. __less__

	O comando `less`  (antigamente `more`), permite que utilize um modo de visualização mais agradável de um arquivo, e evita _prints_ que poluem a linha de comando:
	```
	less new_file.txt
	```
	<br>
	<br>

1. __history__

	O bash mantém um histório de todos os comandos executados. Você pode acessar esse histórico através do `history`.

	```
	history 4 # mostra os últimos 4 comandos executados
	!! # executa último comando novamente
	!-1 # executa último comando novamente
	!-2 # executa o penúltimo comando
	!hea # executa o último comando começado em “hea”)
	```

__Fim!!!__ Espero que esse _post_ sirva como um apoio rápido para muitos Cientistas de Dados (e aspirantes). Qualquer dúvida ou sugestão de melhoria, basta enviar um comentário.

## Fontes:
- Documentação de cada comando, acessado pelo comando `man`
- <a target="_blank" href="https://www.rootusers.com/17-bash-history-command-examples-in-linux/" target="_"> https://www.rootusers.com/17-bash-history-command-examples-in-linux/</a>


