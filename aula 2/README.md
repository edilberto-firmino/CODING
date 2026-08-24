# Aula 2 — Estruturas condicionais com Python

**Duração:** 4 horas  
**Tema:** `if`, `elif`, `else`, comparações e operadores lógicos  
**Produto da aula:** sistema de análise da situação acadêmica de um aluno

## Objetivos de aprendizagem

Ao final desta aula, o aluno deverá ser capaz de:

- explicar como uma condição altera o fluxo de um programa;
- criar decisões simples com `if`;
- definir caminhos alternativos com `if` e `else`;
- testar várias possibilidades com `if`, `elif` e `else`;
- utilizar corretamente os operadores de comparação;
- combinar condições com `and`, `or` e `not`;
- compreender a importância da indentação em Python;
- identificar condições sobrepostas ou incompletas;
- testar diferentes caminhos de execução de um programa;
- desenvolver um sistema de decisão com base em regras definidas.

## Conhecimentos necessários

Esta aula utiliza os conceitos estudados na Aula 1:

- variáveis;
- tipos `str`, `int`, `float` e `bool`;
- entrada com `input()`;
- conversão com `int()` e `float()`;
- saída com `print()` e f-strings;
- operadores aritméticos e de comparação.

## Antes da aula

### Preparação do professor

- Confirmar que os alunos conseguem criar e executar arquivos `.py`.
- Separar exemplos de decisões presentes no cotidiano.
- Testar todos os códigos deste material.
- Preparar valores de entrada que exercitem caminhos diferentes dos programas.
- Revisar o desafio da Aula 1, pois ele será ampliado nesta aula.

## Cronograma da aula

| Tempo | Etapa | Conteúdo e atividade |
| --- | --- | --- |
| 00:00–00:20 | Retomada | revisão da Aula 1 e correção de dúvidas |
| 00:20–00:45 | Decisões e condições | fluxo de execução, expressões booleanas e `if` |
| 00:45–01:15 | Dois caminhos | `if`, `else`, indentação e prática guiada |
| 01:15–01:45 | Vários caminhos | `elif`, ordem das condições e classificação |
| 01:45–01:55 | Intervalo | pausa de 10 minutos |
| 01:55–02:30 | Operadores lógicos | `and`, `or`, `not` e tabelas-verdade |
| 02:30–02:55 | Condições compostas | intervalos, validações simples e condições aninhadas |
| 02:55–03:15 | Prática guiada | análise de média e frequência |
| 03:15–03:50 | Desafio principal | sistema de situação acadêmica |
| 03:50–04:00 | Fechamento | revisão, bilhete de saída e tarefa |

> Os tempos são flexíveis. Dê atenção especial à indentação e à ordem das condições, pois são fontes frequentes de erro para iniciantes.

---

## 1. Retomada da Aula 1

Analise este programa:

```python
nome = input("Nome do aluno: ")
nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))
media = (nota_1 + nota_2) / 2

print(f"A média de {nome} é {media:.2f}.")
```

Ele recebe dados, realiza um cálculo e mostra o resultado. Porém, ainda não informa se o aluno foi aprovado. Para isso, o programa precisa tomar uma decisão.

Perguntas para a turma:

1. Quais são as entradas?
2. Qual é o processamento?
3. Qual é a saída?
4. Que regra poderia determinar a aprovação?
5. O programa deve produzir a mesma mensagem para todas as médias?

---

## 2. O que é uma estrutura condicional?

Uma estrutura condicional permite que determinadas instruções sejam executadas somente quando uma condição for verdadeira.

Exemplo do cotidiano:

```text
SE estiver chovendo
    levar guarda-chuva
SENÃO
    sair sem guarda-chuva
```

Nesse algoritmo, apenas um dos caminhos será escolhido.

Em Python:

```python
esta_chovendo = True

if esta_chovendo:
    print("Leve o guarda-chuva.")
else:
    print("Você pode sair sem guarda-chuva.")
```

Uma condição sempre será interpretada como verdadeira (`True`) ou falsa (`False`).

### Fluxo de uma decisão

```text
            condição
           /        \
    verdadeira      falsa
        |              |
    bloco do if    bloco do else
           \        /
        continuação do programa
```

---

## 3. Decisão simples com if

A palavra `if` significa “se”. O bloco abaixo dela será executado somente quando a condição for verdadeira.

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")

print("Fim do programa.")
```

Se a idade for menor que 18, a primeira mensagem não aparecerá. A mensagem `Fim do programa.` será exibida em qualquer caso porque está fora do bloco do `if`.

### Anatomia do if

```python
if idade >= 18:
    print("Você é maior de idade.")
```

- `if` inicia a decisão;
- `idade >= 18` é a condição;
- `:` marca o início do bloco;
- os quatro espaços antes de `print()` formam a indentação;
- a linha indentada pertence ao `if`.

### Indentação

Python usa indentação para identificar quais instruções pertencem a cada bloco.

```python
saldo = 100

if saldo > 0:
    print("Existe saldo disponível.")
    print(f"Saldo: R$ {saldo:.2f}")

print("Consulta encerrada.")
```

As duas primeiras mensagens pertencem ao `if`. A última está fora dele.

Este código está incorreto:

```python
# if saldo > 0:
# print("Existe saldo disponível.")
```

O Python produzirá um erro porque esperava um bloco indentado.

### Prática rápida — número positivo

Crie um programa que receba um número e mostre uma mensagem somente se ele for positivo.

```python
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
```

Teste com um número positivo, um negativo e zero. Observe em quais testes a mensagem aparece.

---

## 4. Dois caminhos com if e else

A palavra `else` significa “senão”. Seu bloco é executado quando a condição do `if` é falsa.

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
```

Somente uma das mensagens será exibida.

### Exemplo — número par ou ímpar

O resto da divisão de um número par por 2 é zero.

```python
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

Observe que:

- `%` calcula o resto da divisão;
- `==` compara dois valores;
- `=` seria uma atribuição e não deve ser usado nessa comparação.

### Exemplo — senha simples

```python
senha = input("Digite a senha: ")

if senha == "python123":
    print("Acesso permitido.")
else:
    print("Acesso negado.")
```

> Este exemplo serve apenas para estudar condições. Sistemas reais nunca devem deixar senhas expostas diretamente no código.

### Prática — meta de vendas

Receba o valor vendido por uma pessoa e a meta do mês. Informe se a meta foi atingida.

<details>
<summary>Ver uma solução possível</summary>

```python
vendas = float(input("Total de vendas: R$ "))
meta = float(input("Meta do mês: R$ "))

if vendas >= meta:
    print("Meta atingida!")
else:
    valor_faltante = meta - vendas
    print(f"Ainda faltam R$ {valor_faltante:.2f} para atingir a meta.")
```

</details>

---

## 5. Vários caminhos com if, elif e else

Quando há mais de duas possibilidades, podemos usar `elif`, uma abreviação de “senão, se”.

```python
media = float(input("Digite a média: "))

if media >= 7:
    print("Aprovado.")
elif media >= 4:
    print("Recuperação.")
else:
    print("Reprovado.")
```

O Python testa as condições de cima para baixo e para na primeira que for verdadeira.

### A ordem das condições importa

Considere esta versão incorreta:

```python
media = 8

if media >= 4:
    print("Recuperação.")
elif media >= 7:
    print("Aprovado.")
else:
    print("Reprovado.")
```

A média `8` também é maior que `4`. Portanto, o primeiro bloco é executado e o Python nem chega à segunda condição.

Para esse tipo de classificação, organize as condições da mais restritiva para a mais abrangente:

```python
if media >= 7:
    print("Aprovado.")
elif media >= 4:
    print("Recuperação.")
else:
    print("Reprovado.")
```

### Exemplo — classificação por idade

```python
idade = int(input("Idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Criança.")
elif idade <= 17:
    print("Adolescente.")
elif idade <= 59:
    print("Adulto.")
else:
    print("Pessoa idosa.")
```

Depois que sabemos que a idade não é menor ou igual a 12, basta testar `idade <= 17`. Não é necessário repetir o limite inferior.

### Prática — conceito por nota

Crie um programa que receba uma nota de 0 a 10 e mostre:

| Nota | Conceito |
| --- | --- |
| 9 a 10 | A |
| 7 a 8,99 | B |
| 5 a 6,99 | C |
| 0 a 4,99 | D |
| fora de 0 a 10 | nota inválida |

Teste os valores `10`, `9`, `8.5`, `7`, `6.9`, `5`, `4.9`, `0`, `-1` e `11`.

<details>
<summary>Ver uma solução possível</summary>

```python
nota = float(input("Digite a nota: "))

if nota < 0 or nota > 10:
    print("Nota inválida.")
elif nota >= 9:
    print("Conceito A.")
elif nota >= 7:
    print("Conceito B.")
elif nota >= 5:
    print("Conceito C.")
else:
    print("Conceito D.")
```

</details>

---

## 6. Operadores de comparação

As comparações produzem valores booleanos: `True` ou `False`.

| Operador | Significado | Exemplo | Resultado |
| --- | --- | --- | --- |
| `==` | igual a | `5 == 5` | `True` |
| `!=` | diferente de | `5 != 5` | `False` |
| `>` | maior que | `8 > 3` | `True` |
| `<` | menor que | `8 < 3` | `False` |
| `>=` | maior ou igual a | `7 >= 7` | `True` |
| `<=` | menor ou igual a | `4 <= 6` | `True` |

Podemos armazenar o resultado de uma comparação:

```python
idade = 20
maior_de_idade = idade >= 18

print(maior_de_idade)
print(type(maior_de_idade))
```

Também podemos usar a variável booleana como condição:

```python
if maior_de_idade:
    print("A pessoa é maior de idade.")
```

### Comparando textos

```python
resposta = input("Deseja continuar? Digite sim ou não: ")

if resposta == "sim":
    print("Continuando...")
else:
    print("Programa encerrado.")
```

Por enquanto, o usuário precisa escrever exatamente `sim` em letras minúsculas. Métodos para normalizar textos serão estudados com mais profundidade na Aula 4.

---

## 7. Operadores lógicos

Operadores lógicos permitem combinar ou inverter condições.

### and — todas as condições devem ser verdadeiras

```python
media = 8
frequencia = 80

if media >= 7 and frequencia >= 75:
    print("Aprovado.")
else:
    print("Os critérios de aprovação não foram atendidos.")
```

O aluno será aprovado somente se atingir a média **e** a frequência mínima.

Tabela-verdade do `and`:

| Condição A | Condição B | A `and` B |
| --- | --- | --- |
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

### or — pelo menos uma condição deve ser verdadeira

```python
dia = input("Digite o dia da semana: ")

if dia == "sábado" or dia == "domingo":
    print("É fim de semana.")
else:
    print("É dia útil.")
```

Tabela-verdade do `or`:

| Condição A | Condição B | A `or` B |
| --- | --- | --- |
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

### not — inverte o valor lógico

```python
esta_chovendo = False

if not esta_chovendo:
    print("Não é necessário levar guarda-chuva.")
```

| Condição | `not` condição |
| --- | --- |
| `True` | `False` |
| `False` | `True` |

### Escolhendo o operador

Pergunte:

- todos os critérios precisam ser atendidos? Use `and`;
- basta um dos critérios ser atendido? Use `or`;
- preciso inverter uma condição? Use `not`.

### Atividade sem computador

Para cada caso, escolha `and` ou `or`:

1. Para receber certificado, o aluno precisa ter média mínima **e** frequência mínima.
2. Há desconto se o cliente for estudante **ou** tiver mais de 60 anos.
3. O acesso é liberado se o usuário informar o e-mail correto **e** a senha correta.
4. A entrega é gratuita se a compra superar R$ 200 **ou** o cliente possuir um cupom.

Respostas: `and`, `or`, `and`, `or`.

---

## 8. Intervalos e validações simples

### Verificando se um número está em um intervalo

```python
nota = float(input("Digite uma nota: "))

if nota >= 0 and nota <= 10:
    print("Nota válida.")
else:
    print("Nota inválida.")
```

Python também permite a comparação encadeada:

```python
if 0 <= nota <= 10:
    print("Nota válida.")
else:
    print("Nota inválida.")
```

As duas versões representam a mesma regra.

### Detectando um valor fora do intervalo

```python
if nota < 0 or nota > 10:
    print("Nota inválida.")
else:
    print("Nota válida.")
```

### Validar não é o mesmo que tratar erros

Nesta aula, podemos verificar se uma nota está entre 0 e 10. Porém, se o usuário digitar `oito` onde o programa espera `float`, ocorrerá um erro antes da condição.

O tratamento desse tipo de entrada com `try` e `except` será estudado na Aula 8.

---

## 9. Condições aninhadas

Uma condição pode estar dentro de outra:

```python
idade = int(input("Idade: "))
possui_documento = input("Possui documento? Digite sim ou não: ")

if idade >= 18:
    if possui_documento == "sim":
        print("Entrada autorizada.")
    else:
        print("Apresente um documento para entrar.")
else:
    print("Entrada não autorizada para menores de idade.")
```

O segundo `if` só é testado quando a pessoa tem pelo menos 18 anos.

Muitas condições aninhadas deixam o código difícil de ler. Quando as regras permitirem, uma condição composta pode ser mais simples:

```python
if idade >= 18 and possui_documento == "sim":
    print("Entrada autorizada.")
else:
    print("Entrada não autorizada.")
```

As versões não exibem exatamente os mesmos detalhes, mas ilustram duas formas de organizar decisões.

---

## 10. Práticas guiadas

### Prática 1 — maior entre dois números

Crie `maior_numero.py`. Receba dois números e informe qual é o maior ou se eles são iguais.

```python
numero_1 = float(input("Primeiro número: "))
numero_2 = float(input("Segundo número: "))

if numero_1 > numero_2:
    print(f"{numero_1} é o maior número.")
elif numero_2 > numero_1:
    print(f"{numero_2} é o maior número.")
else:
    print("Os números são iguais.")
```

Testes recomendados:

- primeiro número maior;
- segundo número maior;
- números iguais;
- números negativos;
- números decimais.

### Prática 2 — desconto em uma compra

Regras:

- compras de R$ 500 ou mais recebem 10% de desconto;
- compras a partir de R$ 200 recebem 5%;
- compras abaixo de R$ 200 não recebem desconto.

```python
valor_compra = float(input("Valor da compra: R$ "))

if valor_compra >= 500:
    percentual_desconto = 10
elif valor_compra >= 200:
    percentual_desconto = 5
else:
    percentual_desconto = 0

desconto = valor_compra * percentual_desconto / 100
valor_final = valor_compra - desconto

print(f"Desconto: {percentual_desconto}%")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
```

Pergunta para a turma: por que o cálculo do desconto foi colocado depois da estrutura condicional?

### Prática 3 — média e frequência

Um aluno é aprovado quando possui média igual ou superior a 7 e frequência igual ou superior a 75%.

```python
media = float(input("Média: "))
frequencia = float(input("Frequência: "))

if media >= 7 and frequencia >= 75:
    print("Aluno aprovado.")
else:
    print("Aluno não aprovado.")
```

Teste, no mínimo, estes cenários:

| Média | Frequência | Resultado esperado |
| ---: | ---: | --- |
| 8 | 90 | aprovado |
| 6 | 90 | não aprovado |
| 8 | 70 | não aprovado |
| 6 | 70 | não aprovado |
| 7 | 75 | aprovado |

Esse conjunto demonstra por que testar apenas um caso não é suficiente.

---

## 11. Desafio principal — situação acadêmica

Crie um arquivo chamado `situacao_academica.py`.

### Regras do sistema

Primeiro, valide os dados:

- cada nota deve estar entre 0 e 10;
- a quantidade de faltas não pode ser negativa;
- o total de aulas deve ser maior que zero;
- as faltas não podem superar o total de aulas.

Se os dados forem válidos, calcule:

```text
média = (nota 1 + nota 2) / 2
frequência = ((total de aulas - faltas) / total de aulas) × 100
```

Classifique o aluno nesta ordem:

1. **Reprovado por falta:** frequência menor que 75%, independentemente da média.
2. **Aprovado:** frequência mínima de 75% e média igual ou superior a 7.
3. **Recuperação:** frequência mínima de 75% e média de 4 até abaixo de 7.
4. **Reprovado por nota:** frequência mínima de 75% e média abaixo de 4.

### Exemplo de execução

```text
Nome do aluno: Marina Souza
Nota 1: 8.5
Nota 2: 7.0
Quantidade de faltas: 2
Total de aulas: 20

--- RESULTADO ACADÊMICO ---
Aluno: Marina Souza
Média: 7.75
Frequência: 90.00%
Situação: Aprovado
```

### Planejamento

Antes de codificar, responda:

```text
Entradas:

Cálculos:

Condições de validade:

Ordem das condições acadêmicas:

Saídas:
```

### Casos de teste obrigatórios

| Nota 1 | Nota 2 | Faltas | Aulas | Resultado esperado |
| ---: | ---: | ---: | ---: | --- |
| 8 | 6 | 2 | 20 | aprovado |
| 7 | 7 | 5 | 20 | aprovado |
| 6 | 4 | 1 | 20 | recuperação |
| 3 | 4 | 1 | 20 | reprovado por nota |
| 9 | 9 | 6 | 20 | reprovado por falta |
| 11 | 8 | 2 | 20 | dados inválidos |
| 8 | 8 | 21 | 20 | dados inválidos |
| 8 | 8 | 0 | 0 | dados inválidos |

### Checklist de entrega

- [ ] O programa recebe todos os dados solicitados.
- [ ] As entradas numéricas são convertidas corretamente.
- [ ] Dados fora dos intervalos são identificados.
- [ ] A média é calculada corretamente.
- [ ] A frequência é calculada corretamente.
- [ ] A frequência é analisada antes da média.
- [ ] Todos os resultados acadêmicos são possíveis.
- [ ] A saída usa f-strings e duas casas decimais.
- [ ] O código possui indentação consistente.
- [ ] Todos os casos de teste foram executados.

<details>
<summary>Ver uma solução de referência</summary>

```python
nome = input("Nome do aluno: ")
nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
faltas = int(input("Quantidade de faltas: "))
total_aulas = int(input("Total de aulas: "))

notas_validas = 0 <= nota_1 <= 10 and 0 <= nota_2 <= 10
frequencia_valida = total_aulas > 0 and 0 <= faltas <= total_aulas

if not notas_validas or not frequencia_valida:
    print("Dados inválidos. Verifique as notas, faltas e total de aulas.")
else:
    media = (nota_1 + nota_2) / 2
    frequencia = ((total_aulas - faltas) / total_aulas) * 100

    if frequencia < 75:
        situacao = "Reprovado por falta"
    elif media >= 7:
        situacao = "Aprovado"
    elif media >= 4:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado por nota"

    print("\n--- RESULTADO ACADÊMICO ---")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Frequência: {frequencia:.2f}%")
    print(f"Situação: {situacao}")
```

</details>

### Extensões para quem terminar antes

- Informe exatamente qual dado é inválido.
- Adicione uma situação especial para média igual a 10 e frequência igual a 100%.
- Informe quantos pontos faltaram para o aluno atingir média 7.
- Calcule a quantidade máxima de faltas permitida para a carga horária informada.
- Adicione uma disciplina e um período ao relatório.

---

## 12. Exercícios de fixação

### Exercício 1 — positivo, negativo ou zero

Receba um número e informe se ele é positivo, negativo ou igual a zero.

### Exercício 2 — maior entre três números

Receba três números e informe qual é o maior. Considere também a possibilidade de empate.

### Exercício 3 — calculadora simples

Receba dois números e uma operação (`+`, `-`, `*` ou `/`). Realize somente a operação escolhida. Na divisão, verifique se o segundo número é diferente de zero.

### Exercício 4 — ano bissexto simplificado

Na primeira versão, considere bissexto todo ano divisível por 4. Depois, pesquise e implemente a regra completa:

- divisível por 4;
- exceto quando divisível por 100;
- a menos que também seja divisível por 400.

### Exercício 5 — entrega gratuita

Uma loja oferece entrega gratuita quando o valor da compra é igual ou superior a R$ 150 ou quando o cliente possui um cupom. Receba os dados e informe se haverá cobrança de frete.

### Exercício 6 — reajuste salarial

Calcule o novo salário conforme as regras:

| Salário atual | Reajuste |
| --- | ---: |
| até R$ 1.500 | 12% |
| até R$ 3.000 | 8% |
| acima de R$ 3.000 | 5% |

Mostre salário atual, percentual, valor do aumento e novo salário.

### Exercício 7 — triângulo

Receba três medidas positivas. Primeiro verifique se elas podem formar um triângulo: cada lado deve ser menor que a soma dos outros dois. Se formarem, classifique-o:

- equilátero: três lados iguais;
- isósceles: dois lados iguais;
- escaleno: três lados diferentes.

---

## 13. Erros comuns nesta aula

### Usar = no lugar de ==

```python
# Incorreto em uma condição
# if idade = 18:

# Correto
if idade == 18:
    print("A idade é 18.")
```

### Esquecer os dois-pontos

```python
# Incorreto
# if nota >= 7

# Correto
if nota >= 7:
    print("Aprovado.")
```

### Indentar de forma inconsistente

Use quatro espaços por nível e mantenha as linhas do mesmo bloco alinhadas.

```python
if nota >= 7:
    print("Aprovado.")
    print("Parabéns!")
```

### Ordenar condições incorretamente

Se `nota >= 5` for testado antes de `nota >= 9`, uma nota 10 ficará presa na primeira condição verdadeira.

### Criar intervalos incompletos

Sempre teste os valores nos limites: exatamente `0`, `4`, `7`, `10`, `75` e outros pontos onde o resultado muda.

### Usar and quando a regra pede or

Traduza a regra para uma frase antes de programar:

- “precisa atender aos dois critérios” indica `and`;
- “basta atender a um dos critérios” indica `or`.

### Dividir por zero

Antes de calcular uma frequência ou divisão, garanta que o divisor seja maior que zero.

---

## 14. Estratégia de testes

Não teste apenas valores “comuns”. Para cada condição, utilize:

- um valor que torne a condição verdadeira;
- um valor que a torne falsa;
- um valor exatamente no limite;
- um valor logo abaixo do limite;
- um valor logo acima do limite;
- uma entrada inválida, quando houver validação.

Exemplo para a regra `media >= 7`:

| Valor | Motivo do teste |
| ---: | --- |
| 8 | acima do limite |
| 7 | exatamente no limite |
| 6.9 | logo abaixo do limite |
| -1 | entrada inválida |
| 11 | entrada inválida |

Teste é parte do desenvolvimento, não uma atividade realizada apenas quando o código está pronto.

---

## 15. Fechamento da aula

### Revisão oral

1. Para que serve uma estrutura condicional?
2. Qual é a diferença entre `if`, `elif` e `else`?
3. Por que a indentação é necessária?
4. O que acontece depois que uma condição de uma cadeia é verdadeira?
5. Quando devemos usar `and`?
6. Quando devemos usar `or`?
7. O que o operador `not` faz?
8. Por que a ordem das condições importa?
9. Qual é a diferença entre `=` e `==`?
10. Por que devemos testar valores nos limites?

### Bilhete de saída

Cada aluno deve escrever:

- uma regra cotidiana que poderia ser representada com `if` e `else`;
- um exemplo de condição com `and`;
- um exemplo de condição com `or`;
- uma dúvida que ainda possui.

### Critérios de avaliação formativa

| Critério | Evidência esperada |
| --- | --- |
| Condições | transforma regras em expressões booleanas corretas |
| Fluxo | usa `if`, `elif` e `else` de forma coerente |
| Operadores lógicos | diferencia `and`, `or` e `not` |
| Intervalos | cobre limites sem deixar lacunas |
| Indentação | organiza corretamente os blocos |
| Testes | verifica todos os caminhos relevantes |
| Clareza | usa variáveis e mensagens compreensíveis |

Sugestão de pontuação para o desafio: 2 pontos para entradas e validação, 2 para cálculos, 3 para regras condicionais, 1 para apresentação e 2 para casos de teste.

## Tarefa para casa

Implemente três exercícios de fixação em arquivos separados. Um deles deve utilizar `and`, outro deve utilizar `or` e pelo menos um deve possuir `if`, `elif` e `else`. Para cada programa, registre três casos de teste e os resultados obtidos.

## Resumo da sintaxe

```python
# Decisão simples
if condicao:
    print("Executado se a condição for verdadeira.")

# Dois caminhos
if condicao:
    print("Caminho verdadeiro.")
else:
    print("Caminho falso.")

# Vários caminhos
if primeira_condicao:
    print("Primeiro caminho.")
elif segunda_condicao:
    print("Segundo caminho.")
else:
    print("Caminho restante.")

# Condições compostas
if condicao_1 and condicao_2:
    print("As duas são verdadeiras.")

if condicao_1 or condicao_2:
    print("Pelo menos uma é verdadeira.")

if not condicao:
    print("A condição original é falsa.")
```

## Ponte para a Aula 3

Nesta aula, os programas passaram a escolher caminhos. Na Aula 3, aprenderemos a repetir instruções com `while`, `for` e `range()`. Isso permitirá solicitar dados novamente, processar vários alunos e executar uma mesma tarefa sem copiar o código diversas vezes.
