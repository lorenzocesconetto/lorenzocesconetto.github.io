---
layout: post
title: Linha de comando para Ciência de Dados
date: 2019-07-04 21:31:57
img: terminal-code.jpg
tags: [Ciência de Dados]
author: Lorenzo Cesconetto
published: true
---

&emsp; &emsp; O conteúdo desse post é direcionado à pessoas **técnicas** na área de computação, não é preciso ter experiência prévia com de Ciência de Dados. Mas é recomendável conhecimento básico do terminal unix.

Você deve estar se perguntando, porque diabos eu deveria utilizar a linha de comando? Primeiramente, os comandos em **Shell Script** para a manipulação de arquivos são muito mais rápidos do que os comandos em Python ou R. Além disso, pode ser conveniente começar a limpeza dos dados pela linha de comando, e terminar em uma outra linguagem utilizando funções mais complexas.

> __Observação importante:__ Estou utilizando um MacBook OSX Mojave. Alguns comandos possuem uma implementação um pouco diferente da plataforma Unix original.

Como é muito difícil memorizar todos os comandos "de primeira", recomendo ler o conteúdo desse _post_ enquanto executa os comandos ensinados na sua própria máquina, depois disso salve o link desse guia para realizar consultas quando não lembrar dos comandos (espero que isso te economize muito tempo de pesquisa no Google).

Para criar um arquivo *teste.txt*, navegue até o diretório onde se deseje criar o arquivo, e digite no terminal:

```
touch teste.txt
```

Depois disso, abra o arquivo no editor de texto nano (ou o editor de sua preferência) com o comando:

```
nano teste.txt
```

E copie e cole o seguinte conteúdo (assim nós dois teremos o mesmo arquivo para comparar os resultados):

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
Como _reminder_ inicial, o comando `man` permite que possamos acessar página de ajuda para qualquer comando. Então, para saber o que o comando **iconv** faz, basta digitar `man iconv`.

<br>
### 1. iconv

Erros de _enconding_ podem ser muito irritantes. Quase todo mundo que trabalha na área de Ciência de Dados já teve problemas desse tipo. O comando `iconv` converte fácilmente o _enconding_ de arquivos e funciona muito bem!
	
Antes de aplicar o `iconv`, é interessante utilizar o comando `file -I` (na plataforma Linux `file -i`) para descobrir qual o encoding atual do arquivo.

```
file -I teste.txt
```


A saída deve ser algo do tipo:


| teste.txt: text/plain; charset=utf-8 |

Agora podemos fazer a conversão especificando as opções _-f_ (_from_) e _-t_ (_to_) que indicam __de qual__ e __para qual__ _encoding_ estamos convertendo respctivamente: 

```
iconv -f UTF-8 -t ISO-8859-1 teste.txt
```

Recomendo _<a target="_blank" href="https://www.youtube.com/watch?v=MijmeoH9LT4" target="_">esse vídeo</a>_ para uma breve discussão sobre o UTF-8.

<br>

### 2. wc

O comando **wc** (abreviação de _word count_), apesar do nome, retorna a contagem de linhas, palavras e bytes de um arquivo (nessa ordem). É muito útil para saber o número de observações que temos nos nossos dados sem precisar abrir o arquivo (abrir pode ser infactível se o arquivo for muito grande).

```
wc teste.txt
```

O output do comando será:

<div class="alert alert-secondary" role="alert">
  9      10     252 teste.txt
</div>

<pre>
	<strong>
		9      10     252 teste.txt
	</strong>
</pre>

<br>

### 3. head e tail

Em projetos de Ciência de Dados é muito comum se deparar com arquivos *csv* (ou similares) que sejam muito grandes, o que impossibilita sua visualização por meio de editores de texto como o Sublime Text. Um comando rápido para visualizar as primeiras linhas (e descobrir que tipo de dados temos ali) do arquivo é o **head** (ou para visualizar as últimas **tail**):

```
head -n 2 teste.txt # Retorna as primeiras 2 linhas
tail -n 1 teste.txt # Retorna a última linha
```

O output do primeiro comando será:

|codigo_produto;descricao;preço;estoque;mês|
|2;Maça;01,50;2;January|

	
Para obter pular as _n_ primeiras linhas do arquivo, utiliza-se o comando _tail_ com o sinal "+" junto ao número de linhas. Por exemplo:

```
tail -n +2 teste.txt # Retorna todas as linhas exceto a primeira
```
Nesse caso, o comando irá retornar as linhas até o final do arquivo a partir da segunda linha.

<br>

### 4. cut
Podemos selecionar as colunas de um arquivo com dados separados por caracter reservado, e.g., csv. No nosso caso, esse caracter é o ";". Esse comando é o **cut**, que tem como um das opções o *-d* que indica o delimitador (precisaremos escapar o caracter especial ; com uma contra barra), e a opção *-f* que indica quais colunas vamos selecionar (no código abaixo estamos selecionando as colunas de 1 à 3 e a coluna 5):

```
cut -d \; -f 1-3,5 teste.txt # Retorna as colunas 1, 2, 3 e 5
```
Note que a coluna 4 (estoque) é retirada
<br>
<br>
### 5. sed
Uma operação bem comum na limpeza de dados é trocar as vírgulas que separam os número por pontos, por exemplo, de 1,50 para 1.50. No código abaixo, a _string_ `'s/,/./'` está explicitando uma substituição (daí o primeiro `s`) de `,` por `.`. É possível explicitar múltiplas substituições simultaneamente, basta finalizar cada uma com um `;`:

```
sed 's/,/./' teste.txt # Substitui , com .
sed 's/,/./; s/:/./' teste.txt # Substitui , com . e : com .
```
<br>
### 6. | (símbolo pipe)
Para combinar múltiplos comandos, utiliza-se o caracter _pipe_, \|. Ele permite que se crie uma "linha de produção", onde cada comando passa o seu _output_ como _input_ para o próximo. No código abaixo, estamos tomando todas as descrições de produto excluindo o cabeçalho:
```
cut -d \; -f 2 teste.txt | tail -n +2 # Retorna o nome das frutas
```
<br>
### 7. sort
O comando **sort** é bem útil para realizar fazer uma exploração inicial rápida. A flag *-n* deve ser especificada para realizar a ordenação de forma numérica (e não alfabética que é o _default_) e a opção *-r* implica na ordenação inversa (do maior para o menor, em ingês _reverse_):

```
sort -t \; teste.txt # Ordena a 1 coluna
sort -k 2 -t \; teste.txt # Ordena a 2 coluna
sed 's/,:/./' teste.txt | sort -k 3 -nr -t \; # Ordena a 3 coluna de forma numérica
sort -k 5 -t \; -M teste.txt # A opcao M faz o sorting com nome dos meses
```
<br>
### 8. uniq
O comando `uniq` realiza operações envolvendo a propriedade de repetição de linhas. Um detalhe importante desse comando, é que ele exige que o arquivo esteja já ordenado, pois ele realiza as suas operações comparando linhas consecutivas.
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
Faça o teste sem utilizar __>>__. Você verá que a primeira linha, "Frutas únicas", não estará mais lá.
<br>

### 10. echo
O echo é um comando simples que pega os inputs passados (argumentos) e os retorna como _standard outputs_, assim é possível utilizar essa saída como entrada de outras funções. Alguns exemplos de uso:

```
echo some text > some_file.txt  # escreve "some text" em um novo arquivo
echo *.jpeg  # imprimir todos os arquivos com extensão jpeg
echo $PATH # imprime a variavel global PATH
```
<br>

### 11. paste
O comando __paste__ é utilizado para juntar dois arquivos em um __lateralmente__. Abaixo um exemplo:

O código de exemplo abaixo foi retirado desse <a target="_blank" href="https://medium.com/@kadek/command-line-tricks-for-data-scientists-c98e0abe5da" target="_">artigo do Medium</a> escrito por Kade Killary.

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
|Linear Algebra,2|
|Deep Learning,1|
|Discrete Optimization,3|
<br>

### 12. join
Esse comando é um pouco parecido com um _join_ de uma _query_ em SQL. O comando faz o _match_ linha a linha das tabelas onde os valores de uma determinada coluna são iguais em ambos os arquivos. Uma observação muito importante, é que os campos chave para o matching devem estar ordenados, caso contrário, o __join__ pode não retornar todos os matches. Então, na prática deve-se rodar o comando __sort__ em ambos os arquivos antes de realizar o _join_.

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
<br>

### 13. regex
Expressões regulares (also known as _regex_) são uma forma de expressar uma seleção inteligente. Ela é capaz de encontrar padrões especificados de forma automatizada em um texto.

Caracteres especiais, comumente chamados de _Wildcards_:
	* `^`: Começo de palavra.
	* `$`: Final de linha.
	* `[aA]`: Qualquer um dos elementos dentro dos colchetes (nesse caso 'a' ou 'A').
	* `.`: Representa um único caracter, qualquer que ele seja.
	* `{n}`: Repete a expressão anterior _n_ vezes.
	* `+`: Repete a expressão anterior uma ou mais vezes.
	* `*`: Repete a expressão anterior zero ou mais vezes.

```
[1-2]-?{aula}.*
```
<br>

### 14. grep
O comando grep (Global search for a regular expression and print) é utilizado para encontrar padrões específicos em textos, strings ou outputs. Ele retorna as partes do texto que contém o pedaço de texto que você deseja:

```
ls | grep data  # retorna todos os arquivos cujo o nome contém 'data'
grep -i uva teste.txt # ocorrencias de uva (-i torna a busca case insensitive) no teste
grep -E '\d+\s?paginas' myfile
```
<br>

### 15. awk
<br>

## Comandos Extras
Por último, e talvez um pouco menos importantes (para um Cientista de Dados), trago aqui alguns comandos que podem ajudar no dia-a-dia:

<br>

1. __tr__

	O comando __tr__ (abreviação de _translate_) pode fazer diversos tipos de modificações no arquivo.
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
	!-1 # equivalente ao anterior
	!-2 # executa o penúltimo comando
	!hea # executa o último comando começado em “hea”)
	```

__Fim!!!__ Espero que esse _post_ sirva como um apoio rápido para muitos Cientistas de Dados (e aspirantes). Qualquer dúvida ou sugestão de melhoria, basta enviar um comentário.

## Fontes:
- https://www.rootusers.com/17-bash-history-command-examples-in-linux/
- https://medium.com/@kadek/command-line-tricks-for-data-scientists-c98e0abe5da







