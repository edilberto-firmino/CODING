# Aula 1 — Fundamentos de lógica com Python

**Duração:** 4 horas  
**Tema:** variáveis, tipos de dados, entrada, saída e operadores  
**Produto da aula:** programa de cadastro e resumo de um aluno

## Objetivos de aprendizagem

Ao final desta aula, o aluno deverá ser capaz de:

- explicar, com suas próprias palavras, o que é um algoritmo;
- executar um programa Python simples;
- usar `print()` para exibir informações;
- criar variáveis com nomes claros;
- reconhecer os tipos `str`, `int`, `float` e `bool`;
- receber dados do usuário com `input()`;
- converter textos para números com `int()` e `float()`;
- realizar cálculos usando operadores aritméticos;
- montar mensagens com *f-strings*;
- desenvolver e testar um pequeno programa de forma independente.

## Antes da aula

### Preparação do professor

- Verificar se Python 3 está instalado nos computadores.
- Escolher o ambiente que será usado: VS Code, IDLE ou editor on-line.
- Testar no terminal:

```bash
python --version
```

Em alguns sistemas, o comando pode ser:

```bash
python3 --version
```

- Criar um arquivo chamado `primeiro_programa.py` e confirmar que ele executa.
- Deixar este README disponível para os alunos.

### Conhecimentos prévios

Nenhum conhecimento de programação é necessário. O aluno precisa apenas saber criar, salvar e localizar arquivos no computador.

## Recursos necessários

- computador com Python 3;
- editor de código;
- projetor ou compartilhamento de tela;
- terminal integrado ou prompt de comando;
- papel ou quadro para os exercícios de lógica.

## Cronograma da aula

| Tempo | Etapa | Conteúdo e atividade |
| --- | --- | --- |
| 00:00–00:20 | Abertura | apresentação da disciplina, exemplos de programas e diagnóstico da turma |
| 00:20–00:45 | Lógica e algoritmos | problema, sequência lógica, entrada, processamento e saída |
| 00:45–01:10 | Primeiro programa | execução de arquivo Python, `print()` e comentários |
| 01:10–01:35 | Variáveis e tipos | `str`, `int`, `float`, `bool` e `type()` |
| 01:35–01:45 | Exercício guiado | ficha pessoal exibida no terminal |
| 01:45–01:55 | Intervalo | pausa de 10 minutos |
| 01:55–02:20 | Entrada de dados | `input()`, conversão com `int()` e `float()` |
| 02:20–02:50 | Operadores | cálculos, precedência e operadores de comparação |
| 02:50–03:10 | Prática guiada | calculadora de média e orçamento simples |
| 03:10–03:45 | Desafio principal | cadastro e resumo de aluno |
| 03:45–04:00 | Fechamento | revisão, correção, perguntas e tarefa |

> Os tempos são uma referência. Se a turma estiver começando do zero, reserve mais tempo para salvar arquivos, localizar o terminal e interpretar mensagens de erro.

---

## 1. O que é lógica de programação?

Programar é escrever instruções que o computador consegue executar. Antes de escrever código, precisamos organizar uma solução em uma sequência lógica.

Um **problema** é algo que desejamos resolver. Um **algoritmo** é uma sequência finita e ordenada de passos para resolver esse problema.

### Exemplo do cotidiano: preparar café

1. Colocar água no recipiente.
2. Aquecer a água.
3. Colocar o filtro e o pó de café.
4. Despejar a água quente.
5. Servir o café.

Se os passos forem executados fora de ordem ou se uma informação estiver faltando, o resultado poderá ser incorreto. O mesmo acontece em um programa.

### Entrada, processamento e saída

Muitos programas podem ser entendidos por meio de três etapas:

| Etapa | Significado | Exemplo: calcular a média |
| --- | --- | --- |
| Entrada | dados recebidos pelo programa | nota 1 e nota 2 |
| Processamento | operação realizada com os dados | somar e dividir por 2 |
| Saída | resultado apresentado | média calculada |

Representação do algoritmo:

```text
INÍCIO
    receber a primeira nota
    receber a segunda nota
    calcular (primeira nota + segunda nota) / 2
    mostrar a média
FIM
```

### Atividade rápida — pense antes de codificar

Em duplas, escrevam no papel os passos necessários para calcular a área de um retângulo. Identifiquem:

- quais dados entram no algoritmo;
- qual cálculo será realizado;
- qual informação será exibida.

Resposta esperada:

```text
Entrada: largura e altura
Processamento: largura × altura
Saída: área do retângulo
```

---

## 2. Primeiro programa em Python

Crie um arquivo chamado `primeiro_programa.py`.

```python
print("Olá, mundo!")
print("Estou aprendendo Python.")
```

A função `print()` exibe um valor na tela. Os textos ficam entre aspas porque são dados do tipo texto.

Execute o arquivo no terminal:

```bash
python primeiro_programa.py
```

### Comentários

Comentários ajudam a explicar o código e não são executados pelo Python.

```python
# Este é um comentário de uma linha.
print("Esta linha será executada.")
```

### Erros fazem parte do aprendizado

Teste este código e observe a mensagem apresentada:

```python
print("Olá, mundo!"
```

O parêntese não foi fechado. O Python informa o local aproximado do problema. Ao encontrar um erro:

1. leia a última linha da mensagem;
2. confira a linha indicada;
3. procure aspas, parênteses ou nomes incorretos;
4. corrija apenas uma coisa por vez;
5. execute novamente.

### Prática de 5 minutos

Crie um programa que mostre, cada item em uma linha:

- seu nome;
- seu curso;
- uma tecnologia que deseja aprender.

Exemplo:

```python
print("Nome: Ana")
print("Curso: Sistemas de Informação")
print("Quero aprender: desenvolvimento de aplicações")
```

---

## 3. Variáveis

Uma variável é um nome que usamos para guardar um valor durante a execução do programa.

```python
nome = "Ana"
idade = 20
altura = 1.65
estuda_python = True

print(nome)
print(idade)
print(altura)
print(estuda_python)
```

O sinal `=` realiza uma **atribuição**: o valor que está à direita é armazenado na variável indicada à esquerda.

### Regras e boas práticas para nomes

```python
nome_completo = "Ana Lima"  # claro e válido
nota_1 = 8.5                 # válido
idade = 20                   # válido
```

- use nomes que expliquem o conteúdo;
- comece com uma letra ou `_`, nunca com um número;
- não use espaços;
- diferencie maiúsculas e minúsculas: `nome` e `Nome` são variáveis diferentes;
- prefira palavras em minúsculas separadas por `_`;
- evite acentos em identificadores para facilitar a portabilidade do código.

Exemplos que produzem erro:

```python
# 1nome = "Ana"       # começa com número
# nome completo = "Ana"  # contém espaço
```

### Atualizando uma variável

O valor armazenado pode mudar:

```python
pontos = 10
print(pontos)

pontos = pontos + 5
print(pontos)
```

O resultado final será `15`. Primeiro, o Python calcula `pontos + 5`; depois, guarda o novo resultado em `pontos`.

---

## 4. Tipos de dados básicos

| Tipo | Uso | Exemplos |
| --- | --- | --- |
| `str` | texto | `"Python"`, `"Maria"`, `"10"` |
| `int` | número inteiro | `10`, `-3`, `0` |
| `float` | número decimal | `7.5`, `-2.3`, `10.0` |
| `bool` | valor lógico | `True`, `False` |

Podemos descobrir o tipo de um valor com `type()`:

```python
nome = "Carlos"
idade = 22
nota = 8.5
matriculado = True

print(type(nome))
print(type(idade))
print(type(nota))
print(type(matriculado))
```

### Atenção ao separador decimal

No código Python, números decimais usam ponto:

```python
preco = 19.90
```

### Texto não é número

```python
print("10" + "5")  # resultado: 105
print(10 + 5)       # resultado: 15
```

No primeiro caso, o operador `+` junta dois textos. No segundo, soma dois números.

### Verificação de aprendizagem

Identifique o tipo de cada valor antes de executar o código:

```python
produto = "Caderno"
quantidade = 3
preco = 12.50
disponivel = True
```

Resposta: `produto` é `str`, `quantidade` é `int`, `preco` é `float` e `disponivel` é `bool`.

---

## 5. Exibindo valores e usando f-strings

Podemos passar vários valores para `print()`:

```python
nome = "João"
idade = 19

print("Nome:", nome)
print("Idade:", idade)
```

Uma *f-string* permite colocar variáveis dentro de um texto. Basta adicionar `f` antes das aspas e escrever o nome da variável entre chaves:

```python
nome = "João"
idade = 19

print(f"Meu nome é {nome} e tenho {idade} anos.")
```

Também podemos formatar números decimais. O trecho `.2f` mostra duas casas após o ponto:

```python
preco = 7.5
print(f"Preço: R$ {preco:.2f}")
```

Saída:

```text
Preço: R$ 7.50
```

---

## 6. Entrada de dados com input()

A função `input()` mostra uma pergunta, espera o usuário digitar algo e devolve a resposta como texto.

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

### Conversão de tipos

Mesmo quando o usuário digita números, o resultado de `input()` é uma `str`. Para calcular, precisamos converter o valor.

```python
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Idade informada: {idade}")
print(f"Altura informada: {altura:.2f} m")
```

- `int()` converte um valor compatível para inteiro;
- `float()` converte um valor compatível para decimal;
- `str()` converte um valor para texto.

Este código não calcula corretamente:

```python
numero_1 = input("Primeiro número: ")
numero_2 = input("Segundo número: ")
print(numero_1 + numero_2)
```

Se o usuário digitar `10` e `5`, o resultado será `105`, pois os valores ainda são textos.

Versão corrigida:

```python
numero_1 = float(input("Primeiro número: "))
numero_2 = float(input("Segundo número: "))
print(numero_1 + numero_2)
```

> Nesta aula, considere que o usuário digitará dados válidos. O tratamento de entradas inválidas será estudado na Aula 8.

---

## 7. Operadores

### Operadores aritméticos

| Operador | Operação | Exemplo | Resultado |
| --- | --- | --- | --- |
| `+` | adição | `10 + 3` | `13` |
| `-` | subtração | `10 - 3` | `7` |
| `*` | multiplicação | `10 * 3` | `30` |
| `/` | divisão | `10 / 4` | `2.5` |
| `//` | divisão inteira | `10 // 4` | `2` |
| `%` | resto da divisão | `10 % 4` | `2` |
| `**` | potência | `2 ** 3` | `8` |

Exemplo:

```python
largura = 5
altura = 3
area = largura * altura

print(f"A área é {area}.")
```

### Ordem das operações

O Python respeita a precedência matemática. Use parênteses para deixar a intenção clara.

```python
media = (8 + 6) / 2
print(media)
```

Sem os parênteses, a divisão seria feita antes da adição.

### Operadores de comparação

Uma comparação produz `True` ou `False`.

| Operador | Significado | Exemplo |
| --- | --- | --- |
| `==` | igual a | `5 == 5` |
| `!=` | diferente de | `5 != 3` |
| `>` | maior que | `8 > 4` |
| `<` | menor que | `2 < 7` |
| `>=` | maior ou igual a | `6 >= 6` |
| `<=` | menor ou igual a | `3 <= 5` |

```python
idade = 20
print(idade >= 18)
print(idade == 20)
print(idade != 20)
```

Não confunda:

- `=` atribui um valor a uma variável;
- `==` compara dois valores.

As decisões baseadas nessas comparações serão aprofundadas na Aula 2.

---

## 8. Práticas guiadas

### Prática 1 — ficha pessoal

Crie `ficha_pessoal.py`. O programa deve solicitar nome, idade, cidade e curso, e apresentar uma frase com os dados.

```python
nome = input("Nome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")
curso = input("Curso: ")

print("\n--- Ficha pessoal ---")
print(f"{nome} tem {idade} anos, mora em {cidade} e cursa {curso}.")
```

Perguntas para a turma:

1. Por que apenas a idade foi convertida?
2. O que acontece se retirarmos o `f` da última linha?
3. Qual é a finalidade de `\n`?

### Prática 2 — calculadora de média

Crie `media.py`:

```python
nome = input("Nome do aluno: ")
nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))
media = (nota_1 + nota_2) / 2

print(f"A média de {nome} é {media:.2f}.")
```

Teste com pelo menos três conjuntos de valores e confira o cálculo manualmente.

### Prática 3 — orçamento de compra

Crie `orcamento.py`. Peça o nome do produto, o preço unitário e a quantidade. Calcule e exiba o custo total.

Tente desenvolver antes de consultar a solução.

<details>
<summary>Ver uma solução possível</summary>

```python
produto = input("Produto: ")
preco_unitario = float(input("Preço unitário: R$ "))
quantidade = int(input("Quantidade: "))
total = preco_unitario * quantidade

print("\n--- Orçamento ---")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Total: R$ {total:.2f}")
```

</details>

---

## 9. Desafio principal — cadastro e resumo de aluno

Crie um arquivo chamado `cadastro_aluno.py`.

### Requisitos obrigatórios

O programa deve:

1. solicitar nome, curso e período do aluno;
2. solicitar duas notas;
3. calcular a média das notas;
4. solicitar a quantidade de faltas e o total de aulas;
5. calcular a porcentagem de presença;
6. exibir um resumo organizado;
7. mostrar números decimais com duas casas.

Use esta fórmula:

```text
presença = ((total de aulas - faltas) / total de aulas) × 100
```

### Exemplo de execução

```text
Nome: Marina Souza
Curso: Análise e Desenvolvimento de Sistemas
Período: 1
Nota 1: 8.5
Nota 2: 7
Quantidade de faltas: 2
Total de aulas: 20

--- RESUMO DO ALUNO ---
Nome: Marina Souza
Curso: Análise e Desenvolvimento de Sistemas
Período: 1
Média: 7.75
Presença: 90.00%
```

### Planejamento antes do código

Preencha antes de programar:

```text
Entradas:

Processamentos:

Saídas:
```

### Checklist de entrega

- [ ] O arquivo possui a extensão `.py`.
- [ ] As variáveis têm nomes claros.
- [ ] As entradas numéricas foram convertidas.
- [ ] A média está correta.
- [ ] A presença está correta.
- [ ] A saída está organizada.
- [ ] Os valores decimais mostram duas casas.
- [ ] O programa foi testado pelo menos duas vezes.

<details>
<summary>Ver uma solução de referência</summary>

```python
nome = input("Nome: ")
curso = input("Curso: ")
periodo = int(input("Período: "))

nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
media = (nota_1 + nota_2) / 2

faltas = int(input("Quantidade de faltas: "))
total_aulas = int(input("Total de aulas: "))
presenca = ((total_aulas - faltas) / total_aulas) * 100

print("\n--- RESUMO DO ALUNO ---")
print(f"Nome: {nome}")
print(f"Curso: {curso}")
print(f"Período: {periodo}")
print(f"Média: {media:.2f}")
print(f"Presença: {presenca:.2f}%")
```

</details>

### Extensões para quem terminar antes

- Peça a carga horária total e calcule quantas horas já foram cursadas.
- Peça o valor da mensalidade e calcule o custo de seis meses.
- Compare a média com `7` e apenas exiba o resultado booleano.
- Personalize o cabeçalho e a organização do resumo.

---

## 10. Exercícios de fixação

### Exercício 1 — antecessor e sucessor

Receba um número inteiro e mostre seu antecessor e seu sucessor.

Exemplo para a entrada `10`:

```text
Antecessor: 9
Número: 10
Sucessor: 11
```

### Exercício 2 — conversor de temperatura

Receba uma temperatura em graus Celsius e converta para Fahrenheit:

```text
fahrenheit = (celsius × 9 / 5) + 32
```

### Exercício 3 — idade em meses

Receba nome e idade em anos. Mostre a idade aproximada em meses.

### Exercício 4 — divisão de conta

Receba o valor total de uma conta e a quantidade de pessoas. Mostre quanto cada pessoa deverá pagar.

### Exercício 5 — salário com reajuste

Receba um salário e uma porcentagem de reajuste. Calcule o aumento e o novo salário.

Fórmulas:

```text
aumento = salário × porcentagem / 100
novo salário = salário + aumento
```

---

## 11. Erros comuns nesta aula

### Esquecer as aspas em um texto

```python
# Incorreto
# cidade = Recife

# Correto
cidade = "Recife"
```

### Tentar somar texto e número

```python
idade = 20

# Incorreto: "Idade: " + idade
print("Idade:", idade)
print(f"Idade: {idade}")
```

### Não converter o resultado de input()

```python
# Incorreto para realizar cálculos
idade = input("Idade: ")

# Correto
idade = int(input("Idade: "))
```

### Usar vírgula em número decimal

```python
# Incorreto como número decimal
# nota = 8,5

# Correto
nota = 8.5
```

### Confundir atribuição e comparação

```python
idade = 18        # atribuição
print(idade == 18)  # comparação
```

---

## 12. Fechamento da aula

### Revisão oral

Peça aos alunos que respondam sem consultar o material:

1. O que é um algoritmo?
2. Qual função exibe informações no terminal?
3. Qual função recebe dados do usuário?
4. Qual tipo representa um texto?
5. Qual é a diferença entre `int` e `float`?
6. Por que precisamos converter algumas entradas?
7. Qual é a diferença entre `=` e `==`?
8. Para que serve uma f-string?

### Bilhete de saída

Antes de sair, cada aluno deve registrar:

- uma coisa que aprendeu;
- uma dúvida que ainda possui;
- uma pequena alteração feita no desafio principal.

### Critérios de avaliação formativa

| Critério | Evidência esperada |
| --- | --- |
| Compreensão da lógica | identifica entrada, processamento e saída |
| Uso de variáveis | escolhe nomes válidos e compreensíveis |
| Tipos e conversões | usa `int()` e `float()` quando necessário |
| Cálculos | aplica operadores e parênteses corretamente |
| Apresentação | usa `print()` e f-strings para uma saída legível |
| Teste | executa o programa com diferentes valores |

Sugestão de pontuação para o desafio: 2 pontos para entradas e conversões, 3 para cálculos, 2 para saída, 2 para organização do código e 1 para testes.

## Tarefa para casa

Escolha dois exercícios de fixação, implemente-os em arquivos separados e teste cada um com pelo menos três entradas diferentes. Leve para a próxima aula uma dúvida ou uma melhoria que gostaria de fazer.

## Resumo de comandos da aula

```python
# Saída
print("Olá")

# Entrada
nome = input("Nome: ")

# Conversões
idade = int(input("Idade: "))
nota = float(input("Nota: "))

# Variáveis e cálculo
media = (8.0 + 7.0) / 2

# Mensagem formatada
print(f"Média: {media:.2f}")

# Verificação de tipo
print(type(media))
```

## Ponte para a Aula 2

Nesta aula, o programa calculou e mostrou valores. Na próxima, aprenderemos a tomar decisões com `if`, `elif` e `else`. Assim, em vez de apenas exibir uma média, o programa poderá informar se o aluno foi aprovado, ficou em recuperação ou foi reprovado.
