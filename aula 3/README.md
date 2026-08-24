# Aula 3 — Estruturas de repetição com Python

**Duração:** 4 horas  
**Tema:** `while`, `for`, `range()`, contadores e acumuladores  
**Produto da aula:** sistema de registro e resumo de uma turma

## Objetivos de aprendizagem

Ao final desta aula, o aluno deverá ser capaz de:

- explicar por que estruturas de repetição são úteis;
- construir repetições controladas por condição com `while`;
- evitar e corrigir laços infinitos;
- validar entradas por meio de repetição;
- construir repetições com `for` e `range()`;
- diferenciar situações adequadas para `while` e `for`;
- utilizar contadores e acumuladores;
- calcular totais e médias de vários valores;
- controlar o fluxo com `break` e `continue`;
- combinar repetição e estruturas condicionais;
- testar corretamente programas que possuem laços.

## Conhecimentos necessários

Esta aula utiliza conteúdos das aulas anteriores:

- variáveis e tipos de dados;
- entrada, conversão e saída;
- operadores aritméticos e de comparação;
- `if`, `elif` e `else`;
- operadores lógicos `and`, `or` e `not`.

## Antes da aula

### Preparação do professor

- Confirmar que os alunos conseguem executar arquivos `.py`.
- Preparar exemplos de tarefas repetitivas do cotidiano.
- Revisar as regras de aprovação utilizadas na Aula 2.
- Testar todos os exemplos e casos de teste deste material.
- Explicar previamente como interromper um programa no terminal, caso ocorra um laço infinito.

Para interromper a execução no terminal, normalmente usamos:

```text
Ctrl + C
```

## Cronograma da aula

| Tempo | Etapa | Conteúdo e atividade |
| --- | --- | --- |
| 00:00–00:20 | Retomada | revisão de condicionais e atividade diagnóstica |
| 00:20–00:40 | Introdução | repetição, iteração e fluxo de execução |
| 00:40–01:15 | Laço `while` | condição, atualização e laço infinito |
| 01:15–01:45 | Aplicações do `while` | validação, contador, acumulador e sentinela |
| 01:45–01:55 | Intervalo | pausa de 10 minutos |
| 01:55–02:30 | Laço `for` | repetição por quantidade e `range()` |
| 02:30–02:55 | Controle do laço | `break`, `continue` e escolha do laço |
| 02:55–03:15 | Prática guiada | tabuada e média de uma turma |
| 03:15–03:50 | Desafio principal | sistema de registro de turma |
| 03:50–04:00 | Fechamento | revisão, avaliação e tarefa |

> Os tempos são uma referência. Se a turma demonstrar dificuldade, priorize a construção mental do laço: valor inicial, condição, instruções repetidas e atualização.

---

## 1. Retomada das condicionais

Na Aula 2, criamos programas capazes de escolher caminhos:

```python
nota = float(input("Digite a nota: "))

if 0 <= nota <= 10:
    print("Nota válida.")
else:
    print("Nota inválida.")
```

Se a nota for inválida, o programa apenas mostra uma mensagem e termina. Como poderíamos pedir a nota novamente até que o usuário informe um valor válido?

Copiar a mesma instrução várias vezes não resolve bem o problema:

```python
# Esta solução é limitada e repetitiva.
nota = float(input("Digite a nota: "))

if nota < 0 or nota > 10:
    nota = float(input("Digite a nota novamente: "))
```

E se o segundo valor também for inválido? Uma estrutura de repetição permite executar o mesmo bloco quantas vezes forem necessárias.

---

## 2. O que é uma estrutura de repetição?

Uma estrutura de repetição, também chamada de **laço** ou **loop**, executa um bloco de instruções mais de uma vez.

Exemplos do cotidiano:

- tentar uma senha novamente enquanto ela estiver incorreta;
- atender clientes enquanto houver pessoas na fila;
- corrigir cada atividade de uma turma;
- somar os valores de todos os produtos de uma compra;
- repetir um exercício dez vezes.

Cada execução do bloco é chamada de **iteração**.

Em Python, estudaremos duas estruturas principais:

| Estrutura | Uso mais comum |
| --- | --- |
| `while` | repetir enquanto uma condição for verdadeira |
| `for` | percorrer uma sequência ou repetir uma quantidade definida de vezes |

---

## 3. Repetição com while

A palavra `while` significa “enquanto”. O bloco é repetido enquanto sua condição for verdadeira.

```python
contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1

print("Fim da contagem.")
```

Saída:

```text
1
2
3
4
5
Fim da contagem.
```

### Anatomia do while

O exemplo possui quatro partes importantes:

1. **Inicialização:** `contador = 1`.
2. **Condição:** `contador <= 5`.
3. **Bloco repetido:** `print(contador)`.
4. **Atualização:** `contador = contador + 1`.

Fluxo da execução:

```text
definir contador como 1
         |
   contador <= 5? ---- não ----> fim
         |
        sim
         |
 mostrar contador
 somar 1 ao contador
         |
         +-------- voltar à condição
```

### Atribuição abreviada

Estas duas instruções produzem o mesmo resultado:

```python
contador = contador + 1
contador += 1
```

Também existem `-=`, `*=`, `/=` e outros operadores de atribuição.

### Simulação manual

| Iteração | Valor antes do teste | Condição `<= 5` | Ação | Novo valor |
| ---: | ---: | --- | --- | ---: |
| 1 | 1 | `True` | mostra 1 | 2 |
| 2 | 2 | `True` | mostra 2 | 3 |
| 3 | 3 | `True` | mostra 3 | 4 |
| 4 | 4 | `True` | mostra 4 | 5 |
| 5 | 5 | `True` | mostra 5 | 6 |
| — | 6 | `False` | encerra | 6 |

Fazer essa tabela no papel é uma ótima maneira de entender ou depurar um laço.

### Prática rápida — contagem regressiva

```python
numero = 5

while numero >= 1:
    print(numero)
    numero -= 1

print("Começar!")
```

Altere o programa para começar em um número informado pelo usuário.

---

## 4. Laços infinitos

Um laço infinito ocorre quando a condição nunca se torna falsa.

```python
contador = 1

while contador <= 5:
    print(contador)
```

O valor de `contador` nunca muda. Logo, `contador <= 5` permanece verdadeiro para sempre.

Se isso acontecer, interrompa o programa com `Ctrl + C` e verifique:

- a variável da condição está sendo atualizada?
- a atualização aproxima o valor do encerramento?
- a condição de parada pode realmente ser alcançada?
- a atualização está dentro do bloco correto?

Outro erro comum é atualizar na direção errada:

```python
contador = 1

# O contador diminui e nunca ficará maior que 5.
while contador <= 5:
    print(contador)
    contador -= 1
```

---

## 5. Validação de entrada com while

Podemos solicitar novamente um dado enquanto ele for inválido.

```python
nota = float(input("Digite uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida.")
    nota = float(input("Digite uma nota de 0 a 10: "))

print(f"Nota registrada: {nota:.2f}")
```

Leia a condição como uma frase: “enquanto a nota for menor que zero **ou** maior que dez, peça novamente”.

### Validando uma opção

```python
opcao = input("Deseja continuar? Digite sim ou não: ")

while opcao != "sim" and opcao != "não":
    print("Opção inválida.")
    opcao = input("Digite sim ou não: ")

print(f"Opção escolhida: {opcao}")
```

O laço continua quando a resposta é diferente de `sim` **e** também diferente de `não`.

> O `while` valida o valor depois da conversão. Se o usuário digitar texto onde se espera um número, ainda poderá ocorrer `ValueError`. Esse problema será tratado com `try` e `except` na Aula 8.

### Prática — idade válida

Crie um programa que solicite uma idade entre 0 e 120. Enquanto o valor estiver fora desse intervalo, mostre uma mensagem e solicite novamente.

<details>
<summary>Ver uma solução possível</summary>

```python
idade = int(input("Digite a idade: "))

while idade < 0 or idade > 120:
    print("Idade inválida.")
    idade = int(input("Digite a idade novamente: "))

print(f"Idade registrada: {idade} anos.")
```

</details>

---

## 6. Contadores e acumuladores

### Contador

Um contador registra quantas vezes algo aconteceu. Normalmente começa em zero e aumenta de um em um.

```python
contador = 0

while contador < 3:
    nome = input("Digite um nome: ")
    print(f"Nome registrado: {nome}")
    contador += 1
```

### Acumulador

Um acumulador guarda uma soma que cresce a cada iteração.

```python
contador = 1
total = 0

while contador <= 3:
    valor = float(input(f"Digite o {contador}º valor: R$ "))
    total += valor
    contador += 1

print(f"Total: R$ {total:.2f}")
```

### Calculando uma média

Para calcular a média de vários números, precisamos do total e da quantidade:

```python
quantidade = int(input("Quantas notas serão digitadas? "))
contador = 1
soma = 0

while contador <= quantidade:
    nota = float(input(f"Digite a {contador}ª nota: "))
    soma += nota
    contador += 1

media = soma / quantidade
print(f"Média: {media:.2f}")
```

Antes de fazer a divisão, o programa deveria garantir que `quantidade` seja maior que zero.

### Comparação

| Papel | Exemplo | Atualização comum |
| --- | --- | --- |
| contador | quantidade de alunos | `quantidade += 1` |
| acumulador | soma das notas | `soma += nota` |

---

## 7. Repetição com sentinela

Uma **sentinela** é um valor especial que indica o fim da entrada de dados. Ela é útil quando não sabemos antecipadamente quantos valores serão informados.

```python
numero = int(input("Digite um número ou 0 para encerrar: "))
soma = 0

while numero != 0:
    soma += numero
    numero = int(input("Digite outro número ou 0 para encerrar: "))

print(f"Soma: {soma}")
```

O zero não entra na soma; ele apenas encerra o laço.

### Evitando divisão por zero

Ao calcular uma média com sentinela, talvez o usuário encerre antes de informar qualquer valor:

```python
nota = float(input("Digite uma nota ou -1 para encerrar: "))
soma = 0
quantidade = 0

while nota != -1:
    soma += nota
    quantidade += 1
    nota = float(input("Digite uma nota ou -1 para encerrar: "))

if quantidade > 0:
    media = soma / quantidade
    print(f"Média: {media:.2f}")
else:
    print("Nenhuma nota foi informada.")
```

---

## 8. Repetição com for

O `for` é indicado quando percorremos uma sequência ou sabemos quantas repetições serão realizadas.

```python
for numero in range(1, 6):
    print(numero)
```

Saída:

```text
1
2
3
4
5
```

A cada iteração, `numero` recebe o próximo valor produzido por `range()`.

### range() com um argumento

```python
for numero in range(5):
    print(numero)
```

Produz `0`, `1`, `2`, `3` e `4`. O limite final `5` não é incluído.

### range() com início e fim

```python
for numero in range(1, 6):
    print(numero)
```

Começa em `1` e para antes de `6`.

### range() com início, fim e passo

```python
for numero in range(0, 11, 2):
    print(numero)
```

Produz os números pares de `0` a `10`. O terceiro argumento é o passo.

### Contagem regressiva

```python
for numero in range(5, 0, -1):
    print(numero)

print("Começar!")
```

Quando o início é maior que o fim, o passo deve ser negativo.

### Resumo do range()

| Código | Valores produzidos |
| --- | --- |
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 5)` | 1, 2, 3, 4 |
| `range(2, 11, 2)` | 2, 4, 6, 8, 10 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

Regra importante: o valor final não é incluído.

---

## 9. Práticas com for e range()

### Prática 1 — tabuada

```python
numero = int(input("Digite um número: "))

print(f"\n--- Tabuada do {numero} ---")

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} × {multiplicador} = {resultado}")
```

### Prática 2 — soma de 1 até N

```python
limite = int(input("Somar de 1 até: "))
soma = 0

for numero in range(1, limite + 1):
    soma += numero

print(f"Soma: {soma}")
```

Usamos `limite + 1` porque o fim de `range()` não é incluído.

### Prática 3 — média de uma turma

```python
quantidade_alunos = int(input("Quantidade de alunos: "))
soma_medias = 0

for numero_aluno in range(1, quantidade_alunos + 1):
    media = float(input(f"Média do aluno {numero_aluno}: "))
    soma_medias += media

media_turma = soma_medias / quantidade_alunos
print(f"Média da turma: {media_turma:.2f}")
```

Melhoria necessária: validar se a quantidade é maior que zero e se cada média está entre 0 e 10.

---

## 10. while ou for?

| Situação | Estrutura recomendada |
| --- | --- |
| repetir até a senha estar correta | `while` |
| pedir uma nota enquanto for inválida | `while` |
| repetir até o usuário escolher sair | `while` |
| exibir números de 1 a 10 | `for` |
| cadastrar uma quantidade conhecida de alunos | `for` |
| gerar uma tabuada | `for` |

Pergunta principal:

- a repetição depende de uma condição ou de uma quantidade ainda desconhecida? Geralmente use `while`;
- a quantidade de repetições é conhecida? Geralmente use `for`.

Alguns problemas podem ser resolvidos com ambos. Escolha a estrutura que torna a intenção mais clara.

---

## 11. break e continue

### break

`break` encerra imediatamente o laço mais próximo.

```python
while True:
    opcao = input("Digite sair para encerrar: ")

    if opcao == "sair":
        break

    print(f"Você digitou: {opcao}")

print("Programa encerrado.")
```

`while True` cria intencionalmente um laço cuja condição sempre é verdadeira. Nesse padrão, é indispensável existir um caminho alcançável até o `break`.

### continue

`continue` interrompe apenas a iteração atual e volta ao início do laço.

```python
for numero in range(1, 11):
    if numero % 2 == 0:
        continue

    print(numero)
```

O programa mostra apenas números ímpares, pois ignora o restante da iteração quando encontra um número par.

### Use com cuidado

`break` e `continue` são úteis, mas muitos saltos podem dificultar a leitura. Antes de utilizá-los, verifique se uma condição clara resolveria o problema.

---

## 12. Combinando condições e repetições

Este programa lê cinco números e conta quantos são positivos, negativos ou iguais a zero:

```python
positivos = 0
negativos = 0
zeros = 0

for posicao in range(1, 6):
    numero = float(input(f"Digite o {posicao}º número: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

print("\n--- RESUMO ---")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")
```

Observe a organização:

- os contadores são inicializados antes do laço;
- o `for` controla quantos valores serão lidos;
- o `if` classifica cada valor;
- apenas um contador é atualizado em cada iteração;
- o resumo é mostrado depois do laço.

---

## 13. Encontrando o maior e o menor valor

Não devemos começar o maior valor em zero, pois todos os dados podem ser negativos. Uma estratégia segura é usar o primeiro valor informado:

```python
quantidade = int(input("Quantidade de valores: "))

primeiro_valor = float(input("Digite o 1º valor: "))
maior = primeiro_valor
menor = primeiro_valor

for posicao in range(2, quantidade + 1):
    valor = float(input(f"Digite o {posicao}º valor: "))

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
```

Antes desse trecho, a quantidade deve ser validada para garantir que seja maior que zero.

---

## 14. Desafio principal — registro de uma turma

Crie um arquivo chamado `registro_turma.py`.

### Requisitos

O programa deve:

1. solicitar a quantidade de alunos e exigir um valor maior que zero;
2. repetir o cadastro para cada aluno;
3. receber o nome, duas notas, faltas e total de aulas;
4. exigir notas entre 0 e 10;
5. exigir total de aulas maior que zero;
6. exigir faltas entre zero e o total de aulas;
7. calcular média e frequência de cada aluno;
8. classificar cada aluno segundo as regras da Aula 2;
9. mostrar o resultado individual logo após o cadastro;
10. ao final, mostrar um resumo da turma.

### Regras acadêmicas

- frequência menor que 75%: reprovado por falta;
- frequência mínima de 75% e média igual ou superior a 7: aprovado;
- frequência mínima de 75% e média de 4 até abaixo de 7: recuperação;
- frequência mínima de 75% e média abaixo de 4: reprovado por nota.

### Resumo da turma

O resumo deve informar:

- quantidade total de alunos;
- quantidade de aprovados;
- quantidade em recuperação;
- quantidade de reprovados por nota;
- quantidade de reprovados por falta;
- média geral da turma;
- maior média registrada;
- menor média registrada.

### Planejamento das variáveis

| Variável | Papel | Valor inicial sugerido |
| --- | --- | --- |
| `quantidade_alunos` | controla o `for` | entrada do usuário |
| `soma_medias` | acumulador | `0` |
| `aprovados` | contador | `0` |
| `recuperacoes` | contador | `0` |
| `reprovados_nota` | contador | `0` |
| `reprovados_falta` | contador | `0` |
| `maior_media` | comparação | `None` |
| `menor_media` | comparação | `None` |

### Pseudocódigo

```text
receber quantidade de alunos
enquanto quantidade não for positiva
    solicitar novamente

inicializar acumuladores e contadores

para cada aluno
    receber nome
    receber e validar as duas notas
    receber e validar aulas e faltas
    calcular média e frequência
    classificar situação
    atualizar o contador correspondente
    atualizar soma, maior média e menor média
    mostrar resultado individual

calcular média geral
mostrar resumo da turma
```

### Casos de teste mínimos

Use uma turma com quatro alunos:

| Aluno | Nota 1 | Nota 2 | Faltas | Aulas | Situação esperada |
| --- | ---: | ---: | ---: | ---: | --- |
| Ana | 8 | 8 | 2 | 20 | aprovado |
| Bruno | 6 | 5 | 3 | 20 | recuperação |
| Carla | 3 | 3 | 2 | 20 | reprovado por nota |
| Diego | 9 | 9 | 6 | 20 | reprovado por falta |

Resultado esperado para as médias:

```text
Média geral: 6.38
Maior média: 9.00
Menor média: 3.00
```

Também teste entradas inválidas antes dos valores válidos:

- quantidade de alunos igual a zero;
- nota `-1` ou `11`;
- total de aulas igual a zero;
- faltas negativas;
- faltas maiores que o total de aulas.

### Checklist de entrega

- [ ] A quantidade de alunos é validada com `while`.
- [ ] O cadastro é repetido com `for`.
- [ ] As notas, aulas e faltas são validadas.
- [ ] Média e frequência são calculadas corretamente.
- [ ] Cada aluno recebe somente uma situação.
- [ ] Os quatro contadores acadêmicos são atualizados.
- [ ] A soma das médias é acumulada.
- [ ] A maior e a menor média são identificadas.
- [ ] O resumo aparece somente depois de todos os cadastros.
- [ ] Os casos de teste foram executados.

<details>
<summary>Ver uma solução de referência</summary>

```python
quantidade_alunos = int(input("Quantidade de alunos: "))

while quantidade_alunos <= 0:
    print("A quantidade deve ser maior que zero.")
    quantidade_alunos = int(input("Quantidade de alunos: "))

soma_medias = 0
aprovados = 0
recuperacoes = 0
reprovados_nota = 0
reprovados_falta = 0
maior_media = None
menor_media = None

for numero_aluno in range(1, quantidade_alunos + 1):
    print(f"\n--- ALUNO {numero_aluno} ---")
    nome = input("Nome: ")

    nota_1 = float(input("Nota 1: "))
    while nota_1 < 0 or nota_1 > 10:
        print("A nota deve estar entre 0 e 10.")
        nota_1 = float(input("Nota 1: "))

    nota_2 = float(input("Nota 2: "))
    while nota_2 < 0 or nota_2 > 10:
        print("A nota deve estar entre 0 e 10.")
        nota_2 = float(input("Nota 2: "))

    total_aulas = int(input("Total de aulas: "))
    while total_aulas <= 0:
        print("O total de aulas deve ser maior que zero.")
        total_aulas = int(input("Total de aulas: "))

    faltas = int(input("Quantidade de faltas: "))
    while faltas < 0 or faltas > total_aulas:
        print("A quantidade de faltas é inválida.")
        faltas = int(input("Quantidade de faltas: "))

    media = (nota_1 + nota_2) / 2
    frequencia = ((total_aulas - faltas) / total_aulas) * 100
    soma_medias += media

    if maior_media is None or media > maior_media:
        maior_media = media

    if menor_media is None or media < menor_media:
        menor_media = media

    if frequencia < 75:
        situacao = "Reprovado por falta"
        reprovados_falta += 1
    elif media >= 7:
        situacao = "Aprovado"
        aprovados += 1
    elif media >= 4:
        situacao = "Recuperação"
        recuperacoes += 1
    else:
        situacao = "Reprovado por nota"
        reprovados_nota += 1

    print(f"Média: {media:.2f}")
    print(f"Frequência: {frequencia:.2f}%")
    print(f"Situação: {situacao}")

media_geral = soma_medias / quantidade_alunos

print("\n=== RESUMO DA TURMA ===")
print(f"Total de alunos: {quantidade_alunos}")
print(f"Aprovados: {aprovados}")
print(f"Em recuperação: {recuperacoes}")
print(f"Reprovados por nota: {reprovados_nota}")
print(f"Reprovados por falta: {reprovados_falta}")
print(f"Média geral: {media_geral:.2f}")
print(f"Maior média: {maior_media:.2f}")
print(f"Menor média: {menor_media:.2f}")
```

</details>

### Extensões para quem terminar antes

- Conte quantos alunos possuem média acima da média geral.
- Mostre o nome do aluno com a maior média.
- Permita encerrar o cadastro antecipadamente com uma palavra especial.
- Calcule a porcentagem de alunos em cada situação.
- Crie um menu que permita iniciar outra turma ou encerrar o programa.

> Algumas extensões ficam mais simples com listas, que serão estudadas na Aula 4.

---

## 15. Exercícios de fixação

### Exercício 1 — sequência numérica

Mostre os números de 1 a 100. Depois, mostre apenas os pares e apenas os múltiplos de 5.

### Exercício 2 — tabuada completa

Receba um número e mostre sua tabuada de 1 a 10. Depois, permita que o usuário escolha o início e o fim da tabuada.

### Exercício 3 — fatorial

Receba um inteiro não negativo e calcule seu fatorial. Exemplo: `5! = 5 × 4 × 3 × 2 × 1 = 120`. Considere que `0! = 1`.

### Exercício 4 — tentativas de senha

Solicite uma senha e permita no máximo três tentativas. Informe quando o acesso for permitido ou quando as tentativas terminarem.

### Exercício 5 — caixa eletrônico

Mostre um menu com as opções consultar saldo, depositar, sacar e sair. Repita o menu até que o usuário escolha sair. Não permita saque superior ao saldo nem valores negativos.

### Exercício 6 — pesquisa de opinião

Leia a idade e uma nota de satisfação de cinco participantes. Ao final, mostre a média das idades, a média da satisfação e quantas avaliações foram iguais ou superiores a 8.

### Exercício 7 — números primos

Receba um número inteiro maior que 1 e verifique se ele é primo. Um número primo é divisível somente por 1 e por ele mesmo.

### Exercício 8 — maior e menor

Leia dez números e mostre o maior e o menor, sem usar as funções prontas `max()` e `min()`.

---

## 16. Erros comuns nesta aula

### Esquecer a atualização do while

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Sem a última linha, o laço não termina.

### Atualizar fora do bloco

A atualização precisa estar indentada quando deve ocorrer em cada iteração.

### Errar o limite do range()

```python
# Mostra de 1 até 10.
for numero in range(1, 11):
    print(numero)
```

O segundo limite não é incluído.

### Reiniciar o acumulador dentro do laço

```python
soma = 0

for numero in range(1, 4):
    # Não escreva soma = 0 aqui.
    soma += numero
```

Se `soma` voltar a zero em cada iteração, os valores anteriores serão perdidos.

### Dividir antes do fim da coleta

Acumule todos os valores dentro do laço e calcule a média depois dele.

### Dividir por zero

Valide a quantidade antes de calcular `soma / quantidade`.

### Usar a variável errada na condição

Confira se a condição e a atualização utilizam a mesma variável de controle.

### Mostrar o resumo dentro do laço

Resultados individuais pertencem ao laço. O resumo geral deve aparecer depois que a repetição terminar.

---

## 17. Estratégia de testes para laços

Teste sempre:

- a menor quantidade válida de repetições;
- uma quantidade comum;
- zero repetições, quando aplicável;
- entradas nos limites das condições;
- entradas inválidas seguidas por uma válida;
- o encerramento por sentinela;
- o caminho que executa `break` ou `continue`;
- a soma, os contadores e a quantidade final.

### Tabela de rastreamento

Para depurar, registre o estado das variáveis a cada iteração:

| Iteração | Entrada | Contador | Soma | Condição |
| ---: | ---: | ---: | ---: | --- |
| 1 | 5 | 1 | 5 | continua |
| 2 | 8 | 2 | 13 | continua |
| 3 | 2 | 3 | 15 | encerra |

Você também pode inserir temporariamente um `print()` dentro do laço:

```python
print(f"DEBUG: contador={contador}, soma={soma}")
```

Remova a mensagem de depuração depois de corrigir o programa.

---

## 18. Fechamento da aula

### Revisão oral

1. O que é uma iteração?
2. Quando o `while` é mais indicado?
3. Quando o `for` é mais indicado?
4. Quais são as partes essenciais de um `while`?
5. Por que um laço pode se tornar infinito?
6. O valor final de `range()` é incluído?
7. Qual é a diferença entre contador e acumulador?
8. Para que serve uma sentinela?
9. O que `break` faz?
10. O que `continue` faz?
11. Por que acumuladores são inicializados antes do laço?
12. Como testar uma estrutura de repetição?

### Bilhete de saída

Cada aluno deve registrar:

- uma situação adequada para `while`;
- uma situação adequada para `for`;
- a diferença entre contador e acumulador;
- uma dificuldade encontrada durante o desafio.

### Critérios de avaliação formativa

| Critério | Evidência esperada |
| --- | --- |
| Escolha do laço | usa `while` ou `for` de forma coerente |
| Controle | define início, condição e atualização corretamente |
| Validação | repete a entrada até receber um valor aceitável |
| Contadores | contabiliza eventos sem perder valores anteriores |
| Acumuladores | calcula somas e médias corretamente |
| Condicionais | classifica cada item dentro da repetição |
| Encerramento | evita laços infinitos e divisões por zero |
| Testes | verifica limites e múltiplas iterações |

Sugestão de pontuação para o desafio: 2 pontos para validações, 2 para controle dos laços, 2 para cálculos, 2 para classificação e contadores, 1 para apresentação e 1 para testes.

## Tarefa para casa

Implemente três exercícios de fixação em arquivos separados:

- um obrigatoriamente com `while`;
- um obrigatoriamente com `for` e `range()`;
- um combinando repetição e condicionais.

Para cada exercício, registre os valores usados nos testes e o resultado esperado.

## Resumo da sintaxe

```python
# while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# validação
nota = float(input("Nota: "))
while nota < 0 or nota > 10:
    nota = float(input("Nota inválida. Digite novamente: "))

# for e range
for numero in range(1, 6):
    print(numero)

# acumulador
soma = 0
for numero in range(1, 6):
    soma += numero

# interromper o laço
while True:
    opcao = input("Opção: ")
    if opcao == "sair":
        break

# pular uma iteração
for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)
```

## Ponte para a Aula 4

Nesta aula, processamos vários valores, mas precisamos tratá-los um de cada vez. Na Aula 4, estudaremos listas, tuplas e dicionários. Essas coleções permitirão guardar vários alunos, notas ou produtos, percorrer os dados novamente e organizar informações relacionadas.
