# Aula 4 — Listas, tuplas e dicionários com Python

**Duração:** 4 horas  
**Tema:** criação, acesso, alteração e percurso de coleções  
**Produto da aula:** sistema de cadastro e consulta de alunos em memória

## Objetivos de aprendizagem

Ao final desta aula, o aluno deverá ser capaz de:

- explicar por que usamos coleções;
- criar, acessar, alterar e percorrer listas;
- adicionar e remover elementos de uma lista;
- utilizar índices positivos e negativos;
- aplicar operações como `len()`, `in`, `sum()`, `min()` e `max()`;
- compreender a diferença entre listas e tuplas;
- criar e consultar dicionários;
- adicionar, alterar e remover pares de chave e valor;
- percorrer chaves, valores e itens de um dicionário;
- combinar listas e dicionários para representar registros;
- desenvolver buscas e resumos usando dados armazenados.

## Conhecimentos necessários

- variáveis, tipos, entrada e saída;
- condicionais;
- `while`, `for` e `range()`;
- contadores, acumuladores e validações.

## Cronograma da aula

| Tempo | Etapa | Conteúdo e atividade |
| --- | --- | --- |
| 00:00–00:20 | Retomada | revisão de laços e problema motivador |
| 00:20–01:00 | Listas | criação, índices, acesso e alteração |
| 01:00–01:35 | Métodos de lista | adicionar, remover, buscar e ordenar |
| 01:35–01:45 | Prática | lista de compras |
| 01:45–01:55 | Intervalo | pausa de 10 minutos |
| 01:55–02:15 | Tuplas | imutabilidade, acesso e aplicações |
| 02:15–02:55 | Dicionários | chaves, valores, alteração e percurso |
| 02:55–03:15 | Coleções combinadas | lista de dicionários e busca |
| 03:15–03:50 | Desafio principal | cadastro e consulta de alunos |
| 03:50–04:00 | Fechamento | revisão, avaliação e tarefa |

---

## 1. Por que usar coleções?

Na Aula 3, para guardar três notas separadamente, poderíamos criar:

```python
nota_1 = 8.0
nota_2 = 7.5
nota_3 = 9.0
```

Essa estratégia não funciona bem quando a quantidade cresce ou muda. Uma coleção permite armazenar vários valores em uma única variável:

```python
notas = [8.0, 7.5, 9.0]
```

Python oferece diferentes tipos de coleção. Nesta aula estudaremos:

| Coleção | Característica principal | Exemplo de uso |
| --- | --- | --- |
| lista | ordenada e alterável | notas, produtos, alunos |
| tupla | ordenada e imutável | coordenadas, meses, configurações fixas |
| dicionário | pares de chave e valor | cadastro de uma pessoa |

---

## 2. Listas

Uma lista armazena vários valores em determinada ordem. Ela é criada com colchetes:

```python
nomes = ["Ana", "Bruno", "Carla"]
notas = [8.5, 7.0, 9.2]
numeros = [10, 20, 30]
lista_vazia = []
```

Uma lista pode misturar tipos, embora normalmente seja mais claro manter valores relacionados:

```python
dados = ["Ana", 20, 8.5, True]
```

### Índices

Cada elemento possui uma posição chamada índice. O primeiro índice é zero.

```text
Valor:   Ana    Bruno   Carla
Índice:   0       1       2
```

```python
nomes = ["Ana", "Bruno", "Carla"]

print(nomes[0])
print(nomes[1])
print(nomes[2])
```

Índices negativos contam a partir do final:

```python
print(nomes[-1])  # Carla
print(nomes[-2])  # Bruno
```

Tentar acessar uma posição inexistente causa `IndexError`:

```python
# print(nomes[3])
```

### Alterando um elemento

Listas são mutáveis:

```python
nomes = ["Ana", "Bruno", "Carla"]
nomes[1] = "Beatriz"
print(nomes)
```

Resultado:

```text
['Ana', 'Beatriz', 'Carla']
```

### Quantidade de elementos

```python
print(len(nomes))
```

`len()` devolve a quantidade de itens da coleção.

### Verificando a existência de um valor

```python
if "Ana" in nomes:
    print("Ana está cadastrada.")

if "Daniel" not in nomes:
    print("Daniel não está cadastrado.")
```

---

## 3. Adicionando elementos

### append()

Adiciona um elemento ao final:

```python
frutas = ["maçã", "banana"]
frutas.append("laranja")
print(frutas)
```

### insert()

Adiciona em uma posição específica:

```python
frutas.insert(1, "uva")
print(frutas)
```

### extend()

Adiciona todos os elementos de outra coleção:

```python
frutas.extend(["manga", "melancia"])
print(frutas)
```

Compare:

```python
lista = [1, 2]
lista.append([3, 4])  # adiciona uma lista como um único elemento

outra_lista = [1, 2]
outra_lista.extend([3, 4])  # adiciona os elementos separadamente
```

---

## 4. Removendo elementos

### remove()

Remove a primeira ocorrência de um valor:

```python
frutas = ["maçã", "banana", "uva"]
frutas.remove("banana")
```

Se o valor não existir, ocorrerá `ValueError`. Verifique antes:

```python
fruta = input("Fruta a remover: ")

if fruta in frutas:
    frutas.remove(fruta)
    print("Fruta removida.")
else:
    print("Fruta não encontrada.")
```

### pop()

Remove e devolve o elemento de uma posição. Sem argumento, usa o último:

```python
ultima_fruta = frutas.pop()
print(f"Removida: {ultima_fruta}")
```

```python
primeira_fruta = frutas.pop(0)
```

### clear()

Remove todos os elementos:

```python
frutas.clear()
```

Use essa operação com atenção, pois os dados da lista serão descartados.

---

## 5. Percorrendo listas

### Percorrendo os valores

```python
nomes = ["Ana", "Bruno", "Carla"]

for nome in nomes:
    print(nome)
```

Essa é a forma mais simples quando precisamos apenas dos valores.

### Percorrendo índices

```python
for indice in range(len(nomes)):
    print(f"{indice}: {nomes[indice]}")
```

### Posição e valor com enumerate()

```python
for posicao, nome in enumerate(nomes, start=1):
    print(f"{posicao}. {nome}")
```

`enumerate()` evita o controle manual do índice e permite escolher o número inicial exibido.

### Somando e calculando a média

```python
notas = [8.0, 7.5, 9.0]
media = sum(notas) / len(notas)

print(f"Maior nota: {max(notas):.2f}")
print(f"Menor nota: {min(notas):.2f}")
print(f"Média: {media:.2f}")
```

Antes de dividir por `len(notas)`, certifique-se de que a lista não está vazia.

---

## 6. Ordenação e outros métodos

```python
numeros = [8, 3, 10, 1]
numeros.sort()
print(numeros)
```

Ordem decrescente:

```python
numeros.sort(reverse=True)
```

`sort()` modifica a própria lista. `sorted()` produz uma nova lista:

```python
originais = [8, 3, 10, 1]
ordenados = sorted(originais)
```

Outras operações úteis:

```python
valores = [10, 20, 10, 30]

print(valores.count(10))  # quantidade de ocorrências
print(valores.index(20))  # índice da primeira ocorrência
valores.reverse()         # inverte a ordem atual
```

### Fatiamento

O fatiamento seleciona parte de uma lista:

```python
numeros = [10, 20, 30, 40, 50]

print(numeros[1:4])  # [20, 30, 40]
print(numeros[:3])   # [10, 20, 30]
print(numeros[2:])   # [30, 40, 50]
print(numeros[::2])  # [10, 30, 50]
```

Como em `range()`, o limite final não é incluído.

---

## 7. Prática guiada — lista de compras

Crie `lista_compras.py`:

```python
produtos = []

while True:
    print("\n1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Remover produto")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        produto = input("Produto: ")
        produtos.append(produto)
        print("Produto adicionado.")

    elif opcao == "2":
        if len(produtos) == 0:
            print("A lista está vazia.")
        else:
            for posicao, produto in enumerate(produtos, start=1):
                print(f"{posicao}. {produto}")

    elif opcao == "3":
        produto = input("Produto a remover: ")
        if produto in produtos:
            produtos.remove(produto)
            print("Produto removido.")
        else:
            print("Produto não encontrado.")

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")

print("Programa encerrado.")
```

Melhorias sugeridas:

- impedir a inclusão de texto vazio;
- impedir produtos duplicados;
- ordenar a lista antes de exibi-la;
- remover um produto pela posição.

---

## 8. Tuplas

Uma tupla é uma coleção ordenada que não pode ser alterada depois de criada. Utiliza parênteses:

```python
dias_semana = (
    "segunda",
    "terça",
    "quarta",
    "quinta",
    "sexta",
    "sábado",
    "domingo",
)
```

O acesso e o percurso são semelhantes aos de uma lista:

```python
print(dias_semana[0])
print(dias_semana[-1])

for dia in dias_semana:
    print(dia)
```

Porém, não podemos alterar um item:

```python
# dias_semana[0] = "domingo"  # TypeError
```

### Tupla com um elemento

A vírgula é necessária:

```python
uma_tupla = (10,)
nao_e_tupla = (10)
```

### Desempacotamento

```python
coordenada = (10, 25)
x, y = coordenada

print(x)
print(y)
```

### Quando usar tupla?

Use quando os valores formam um conjunto fixo que não deveria ser alterado, como coordenadas, meses, opções predefinidas ou configurações constantes.

| Lista | Tupla |
| --- | --- |
| `[]` | `()` |
| mutável | imutável |
| possui `append()` e `remove()` | não possui esses métodos |
| adequada para dados que mudam | adequada para dados fixos |

---

## 9. Dicionários

Um dicionário armazena pares de **chave** e **valor**. Em vez de consultar uma posição, usamos uma chave descritiva.

```python
aluno = {
    "nome": "Ana Lima",
    "idade": 20,
    "curso": "Sistemas de Informação",
    "media": 8.5,
}
```

### Acessando valores

```python
print(aluno["nome"])
print(aluno["media"])
```

Uma chave inexistente causa `KeyError`. O método `get()` permite fornecer um valor padrão:

```python
print(aluno.get("telefone", "Não informado"))
```

### Adicionando e alterando

```python
aluno["email"] = "ana@email.com"
aluno["media"] = 9.0
```

Se a chave não existe, ela é adicionada. Se já existe, seu valor é substituído.

### Removendo

```python
email_removido = aluno.pop("email")
print(email_removido)
```

Também existe `del aluno["email"]`, mas `pop()` é conveniente quando queremos utilizar o valor removido.

### Verificando uma chave

```python
if "curso" in aluno:
    print("O curso foi informado.")
```

O operador `in` verifica as chaves do dicionário.

---

## 10. Percorrendo dicionários

### Chaves

```python
for chave in aluno:
    print(chave)
```

Também podemos escrever `aluno.keys()`.

### Valores

```python
for valor in aluno.values():
    print(valor)
```

### Chaves e valores

```python
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
```

Resumo:

| Método | Resultado percorrido |
| --- | --- |
| `keys()` | chaves |
| `values()` | valores |
| `items()` | pares de chave e valor |

### Prática — cadastro de produto

```python
produto = {
    "nome": input("Nome do produto: "),
    "preco": float(input("Preço: R$ ")),
    "quantidade": int(input("Quantidade: ")),
}

produto["total"] = produto["preco"] * produto["quantidade"]

print("\n--- PRODUTO ---")
print(f"Nome: {produto['nome']}")
print(f"Preço: R$ {produto['preco']:.2f}")
print(f"Quantidade: {produto['quantidade']}")
print(f"Total: R$ {produto['total']:.2f}")
```

As aspas simples dentro das chaves evitam conflito com as aspas da f-string.

---

## 11. Coleções combinadas

Um dicionário representa bem um aluno. Uma lista de dicionários representa uma turma:

```python
alunos = [
    {"nome": "Ana", "media": 8.0},
    {"nome": "Bruno", "media": 6.5},
    {"nome": "Carla", "media": 9.0},
]
```

Percorrendo os registros:

```python
for aluno in alunos:
    print(f"{aluno['nome']}: {aluno['media']:.2f}")
```

Adicionando um cadastro:

```python
novo_aluno = {
    "nome": input("Nome: "),
    "media": float(input("Média: ")),
}

alunos.append(novo_aluno)
```

### Busca linear

```python
nome_buscado = input("Nome a buscar: ")
encontrado = False

for aluno in alunos:
    if aluno["nome"] == nome_buscado:
        print(f"Média: {aluno['media']:.2f}")
        encontrado = True
        break

if not encontrado:
    print("Aluno não encontrado.")
```

Essa busca verifica um registro de cada vez até encontrar o nome ou terminar a lista.

### Cuidado ao reutilizar dicionários

Crie um novo dicionário dentro de cada repetição:

```python
alunos = []

for numero in range(2):
    aluno = {}
    aluno["nome"] = input("Nome: ")
    alunos.append(aluno)
```

Reutilizar e alterar o mesmo dicionário pode fazer várias posições da lista apontarem para o mesmo objeto.

---

## 12. Desafio principal — cadastro e consulta de alunos

Crie `cadastro_alunos.py`.

### Estrutura esperada

Use uma lista chamada `alunos`. Cada elemento será um dicionário com:

```python
{
    "matricula": "2026001",
    "nome": "Ana Lima",
    "notas": [8.0, 7.5],
    "media": 7.75,
    "situacao": "Aprovado",
}
```

### Menu

```text
=== SISTEMA ACADÊMICO ===
1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar por matrícula
4 - Remover aluno
5 - Exibir resumo da turma
0 - Sair
```

### Regras

#### Cadastrar

- matrícula não pode estar vazia nem repetida;
- nome não pode estar vazio;
- receba duas notas entre 0 e 10;
- calcule a média;
- média a partir de 7: aprovado;
- média de 4 até abaixo de 7: recuperação;
- média abaixo de 4: reprovado;
- adicione um novo dicionário à lista.

#### Listar

- informe quando não houver alunos;
- mostre matrícula, nome, média e situação;
- numere os registros com `enumerate()`.

#### Buscar

- solicite a matrícula;
- percorra a lista até encontrá-la;
- mostre todos os dados ou “Aluno não encontrado”.

#### Remover

- localize o aluno pela matrícula;
- remova o dicionário encontrado;
- informe se a matrícula não existir.

#### Resumo

- total de alunos;
- média geral;
- maior e menor média;
- quantidade em cada situação.

### Organização sugerida

```text
criar lista vazia

enquanto o usuário não escolher sair
    mostrar menu
    receber opção

    se opção for cadastrar
        verificar matrícula
        receber e validar dados
        criar novo dicionário
        adicionar à lista

    senão, se opção for listar
        percorrer e exibir a lista

    senão, se opção for buscar
        fazer busca linear

    senão, se opção for remover
        localizar e remover

    senão, se opção for resumo
        percorrer e calcular indicadores
```

### Casos de teste

Cadastre:

| Matrícula | Nome | Notas | Situação esperada |
| --- | --- | --- | --- |
| 001 | Ana | 8 e 8 | aprovado |
| 002 | Bruno | 6 e 5 | recuperação |
| 003 | Carla | 3 e 3 | reprovado |

Depois teste:

- cadastro com matrícula repetida;
- notas `-1` e `11` antes de notas válidas;
- listagem com três alunos;
- busca pela matrícula `002`;
- busca por matrícula inexistente;
- remoção da matrícula `001`;
- remoção repetida da mesma matrícula;
- resumo antes e depois da remoção;
- todas as opções com a lista vazia.

### Checklist de entrega

- [ ] Os alunos são armazenados em uma lista de dicionários.
- [ ] As notas são armazenadas em uma lista.
- [ ] Matrículas vazias e repetidas são recusadas.
- [ ] As notas são validadas.
- [ ] Todas as opções do menu funcionam.
- [ ] A busca informa sucesso ou ausência.
- [ ] A remoção altera a lista corretamente.
- [ ] O resumo trata a lista vazia.
- [ ] Média geral, maior e menor média estão corretas.
- [ ] O programa só termina quando a opção zero é escolhida.

<details>
<summary>Ver uma solução de referência</summary>

```python
alunos = []

while True:
    print("\n=== SISTEMA ACADÊMICO ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar por matrícula")
    print("4 - Remover aluno")
    print("5 - Exibir resumo da turma")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        matricula = input("Matrícula: ")

        matricula_repetida = False
        for aluno in alunos:
            if aluno["matricula"] == matricula:
                matricula_repetida = True
                break

        if matricula == "":
            print("A matrícula não pode ficar vazia.")
            continue

        if matricula_repetida:
            print("Essa matrícula já está cadastrada.")
            continue

        nome = input("Nome: ")
        while nome == "":
            nome = input("O nome não pode ficar vazio. Digite novamente: ")

        notas = []
        for numero_nota in range(1, 3):
            nota = float(input(f"Nota {numero_nota}: "))
            while nota < 0 or nota > 10:
                nota = float(input("Nota inválida. Digite de 0 a 10: "))
            notas.append(nota)

        media = sum(notas) / len(notas)

        if media >= 7:
            situacao = "Aprovado"
        elif media >= 4:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        novo_aluno = {
            "matricula": matricula,
            "nome": nome,
            "notas": notas,
            "media": media,
            "situacao": situacao,
        }
        alunos.append(novo_aluno)
        print("Aluno cadastrado.")

    elif opcao == "2":
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            print("\n--- ALUNOS ---")
            for posicao, aluno in enumerate(alunos, start=1):
                print(
                    f"{posicao}. {aluno['matricula']} - {aluno['nome']} - "
                    f"Média: {aluno['media']:.2f} - {aluno['situacao']}"
                )

    elif opcao == "3":
        matricula = input("Matrícula a buscar: ")
        aluno_encontrado = None

        for aluno in alunos:
            if aluno["matricula"] == matricula:
                aluno_encontrado = aluno
                break

        if aluno_encontrado is None:
            print("Aluno não encontrado.")
        else:
            print(f"Nome: {aluno_encontrado['nome']}")
            print(f"Notas: {aluno_encontrado['notas']}")
            print(f"Média: {aluno_encontrado['media']:.2f}")
            print(f"Situação: {aluno_encontrado['situacao']}")

    elif opcao == "4":
        matricula = input("Matrícula a remover: ")
        aluno_encontrado = None

        for aluno in alunos:
            if aluno["matricula"] == matricula:
                aluno_encontrado = aluno
                break

        if aluno_encontrado is None:
            print("Aluno não encontrado.")
        else:
            alunos.remove(aluno_encontrado)
            print("Aluno removido.")

    elif opcao == "5":
        if len(alunos) == 0:
            print("Não há dados para o resumo.")
        else:
            medias = []
            aprovados = 0
            recuperacoes = 0
            reprovados = 0

            for aluno in alunos:
                medias.append(aluno["media"])

                if aluno["situacao"] == "Aprovado":
                    aprovados += 1
                elif aluno["situacao"] == "Recuperação":
                    recuperacoes += 1
                else:
                    reprovados += 1

            print("\n--- RESUMO ---")
            print(f"Total de alunos: {len(alunos)}")
            print(f"Média geral: {sum(medias) / len(medias):.2f}")
            print(f"Maior média: {max(medias):.2f}")
            print(f"Menor média: {min(medias):.2f}")
            print(f"Aprovados: {aprovados}")
            print(f"Em recuperação: {recuperacoes}")
            print(f"Reprovados: {reprovados}")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
```

</details>

### Extensões para quem terminar antes

- Permita editar as notas de um aluno.
- Ordene a listagem por nome ou por média.
- Cadastre três ou mais notas por aluno.
- Mostre todos os alunos de uma situação escolhida.
- Guarde endereço em um dicionário dentro do dicionário do aluno.
- Crie uma classificação da maior para a menor média.

> Os dados existem apenas enquanto o programa está em execução. Persistência em arquivos pode ser adicionada posteriormente ao curso.

---

## 13. Exercícios de fixação

### Exercício 1 — análise de números

Receba cinco números, armazene-os em uma lista e mostre soma, média, maior, menor e a lista em ordem crescente.

### Exercício 2 — nomes únicos

Crie um menu para adicionar nomes a uma lista. Não permita nomes vazios ou repetidos. Mostre a lista em ordem alfabética.

### Exercício 3 — meses do ano

Armazene os doze meses em uma tupla. Receba um número de 1 a 12 e mostre o mês correspondente, validando o intervalo.

### Exercício 4 — agenda

Use um dicionário no qual o nome seja a chave e o telefone seja o valor. Permita cadastrar, buscar, alterar e remover contatos.

### Exercício 5 — estoque

Use uma lista de dicionários para produtos com nome, preço e quantidade. Mostre o valor total de cada produto e do estoque inteiro.

### Exercício 6 — votação

Armazene candidatos em um dicionário e contabilize votos. Mostre o resultado ordenado do mais votado para o menos votado.

### Exercício 7 — boletim

Crie um dicionário com nome e uma lista de notas. Calcule média, maior nota, menor nota e situação.

---

## 14. Erros comuns

### Confundir índice e valor

```python
nomes = ["Ana", "Bruno"]
print(nomes[0])  # índice
```

### Acessar uma posição inexistente

Os índices válidos vão de zero até `len(lista) - 1`.

### Remover um valor ausente

Use `if valor in lista` antes de `remove()`.

### Dividir pelo tamanho de uma lista vazia

```python
if len(notas) > 0:
    media = sum(notas) / len(notas)
```

### Confundir método com função

```python
nomes.append("Carla")  # método da lista
quantidade = len(nomes)  # função
```

### Esperar que sort() crie uma nova lista

`sort()` altera a lista e devolve `None`. Use `sorted(lista)` quando precisar preservar a ordem original.

### Consultar uma chave inexistente

Use `dicionario.get("chave", valor_padrao)` quando a chave for opcional.

### Alterar uma tupla

Tuplas são imutáveis. Se os dados precisam mudar, considere uma lista.

### Alterar a coleção durante o percurso

Remover vários itens enquanto percorre a mesma lista pode pular elementos. Para operações mais complexas, construa uma nova lista ou percorra uma cópia.

---

## 15. Estratégia de testes

Teste as operações com:

- coleção vazia;
- coleção com um elemento;
- vários elementos;
- primeiro e último índice;
- valor existente e inexistente;
- chave existente e inexistente;
- itens repetidos;
- remoção seguida de nova consulta;
- valores exatamente nos limites;
- resumo antes e depois de alterações.

Para o sistema acadêmico, confirme também que a soma das quantidades por situação é igual ao total de alunos.

---

## 16. Fechamento da aula

### Revisão oral

1. Por que uma lista é melhor que várias variáveis numeradas?
2. Qual é o primeiro índice de uma lista?
3. Qual é a diferença entre `append()` e `extend()`?
4. Qual é a diferença entre `remove()` e `pop()`?
5. Quando usamos `enumerate()`?
6. Qual é a diferença entre lista e tupla?
7. O que é uma chave de dicionário?
8. Para que servem `keys()`, `values()` e `items()`?
9. Como representamos vários alunos com coleções?
10. Como evitar divisão por zero ao calcular a média de uma lista?

### Bilhete de saída

Cada aluno deve registrar:

- um exemplo adequado para lista;
- um exemplo adequado para tupla;
- um exemplo adequado para dicionário;
- uma dúvida sobre coleções combinadas.

### Critérios de avaliação formativa

| Critério | Evidência esperada |
| --- | --- |
| Escolha da coleção | utiliza lista, tupla ou dicionário de forma coerente |
| Manipulação | adiciona, altera e remove elementos corretamente |
| Percurso | usa laços sem acessar índices inválidos |
| Modelagem | representa um registro com chaves claras |
| Combinação | organiza vários registros em uma lista de dicionários |
| Busca | diferencia item encontrado e ausente |
| Resumo | calcula indicadores sem falhar com coleção vazia |
| Testes | cobre inclusão, consulta, alteração e remoção |

Sugestão de pontuação para o desafio: 2 pontos para modelagem dos dados, 2 para cadastro e validação, 2 para consultas e remoção, 2 para resumo, 1 para clareza e 1 para testes.

## Tarefa para casa

Implemente três exercícios de fixação:

- um utilizando lista;
- um utilizando tupla;
- um utilizando dicionário ou lista de dicionários.

Para cada programa, teste uma coleção vazia, um valor existente e um valor inexistente quando essas situações forem aplicáveis.

## Resumo da sintaxe

```python
# Lista
nomes = []
nomes.append("Ana")
nomes.remove("Ana")

for nome in nomes:
    print(nome)

# Tupla
dias = ("segunda", "terça", "quarta")
print(dias[0])

# Dicionário
aluno = {"nome": "Ana", "media": 8.5}
aluno["curso"] = "ADS"

print(aluno["nome"])
print(aluno.get("telefone", "Não informado"))

for chave, valor in aluno.items():
    print(chave, valor)

# Lista de dicionários
alunos = []
alunos.append({"nome": "Ana", "media": 8.5})

for aluno in alunos:
    print(aluno["nome"], aluno["media"])
```

## Ponte para a Aula 5

Nesta aula, construímos um sistema completo, mas grande parte do código ficou concentrada no mesmo arquivo e dentro do menu. Na Aula 5, aprenderemos funções, parâmetros e retornos para dividir o programa em partes menores, reutilizáveis, testáveis e mais fáceis de compreender.
