# Aula 5 — Funções e modularização com Python

**Duração:** 4 horas  
**Tema:** funções, parâmetros, retorno, escopo e organização do código  
**Produto da aula:** sistema acadêmico organizado em funções e módulos

## Objetivos de aprendizagem

Ao final desta aula, o aluno deverá ser capaz de:

- explicar por que dividimos um programa em funções;
- declarar e chamar funções com `def`;
- definir parâmetros e fornecer argumentos;
- diferenciar exibição com `print()` e devolução com `return`;
- criar funções com múltiplos parâmetros e valores padrão;
- compreender escopo local e global;
- escrever funções com responsabilidade bem definida;
- documentar funções com *docstrings*;
- decompor um problema em partes menores;
- organizar funções em módulos Python;
- importar e reutilizar código;
- refatorar um programa sem alterar seu comportamento.

## Conhecimentos necessários

- variáveis, tipos, entrada e saída;
- condicionais e repetições;
- listas, tuplas e dicionários;
- criação de menus e validação de dados.

## Cronograma da aula

| Tempo | Etapa | Conteúdo e atividade |
| --- | --- | --- |
| 00:00–00:20 | Retomada | revisão do sistema da Aula 4 e identificação de repetições |
| 00:20–00:55 | Fundamentos | declaração, chamada e fluxo de uma função |
| 00:55–01:25 | Parâmetros | argumentos, valores padrão e argumentos nomeados |
| 01:25–01:45 | Retorno | `return`, composição e múltiplos retornos |
| 01:45–01:55 | Intervalo | pausa de 10 minutos |
| 01:55–02:20 | Qualidade | escopo, responsabilidade, nomes e docstrings |
| 02:20–02:50 | Modularização | arquivos, `import` e programa principal |
| 02:50–03:15 | Prática guiada | calculadora modular e validações reutilizáveis |
| 03:15–03:50 | Desafio principal | refatoração do sistema acadêmico |
| 03:50–04:00 | Fechamento | revisão, avaliação e tarefa |

---

## 1. Problema motivador

Na Aula 4, o sistema acadêmico possuía cadastro, busca, remoção, listagem e resumo dentro de um grande `while`. Embora funcional, um programa assim fica difícil de:

- ler e compreender;
- corrigir;
- testar;
- reutilizar;
- ampliar sem criar novos erros.

Considere uma validação repetida:

```python
nota_1 = float(input("Nota 1: "))
while nota_1 < 0 or nota_1 > 10:
    nota_1 = float(input("Nota inválida. Digite novamente: "))

nota_2 = float(input("Nota 2: "))
while nota_2 < 0 or nota_2 > 10:
    nota_2 = float(input("Nota inválida. Digite novamente: "))
```

Podemos escrever a regra uma vez e utilizá-la sempre que necessário:

```python
def ler_nota(mensagem):
    nota = float(input(mensagem))

    while nota < 0 or nota > 10:
        nota = float(input("Nota inválida. Digite novamente: "))

    return nota


nota_1 = ler_nota("Nota 1: ")
nota_2 = ler_nota("Nota 2: ")
```

Essa transformação é um exemplo de **refatoração**: melhorar a estrutura interna sem mudar o resultado esperado.

---

## 2. Criando e chamando funções

Uma função é um bloco de código com nome e propósito definidos.

```python
def exibir_boas_vindas():
    print("Bem-vindo ao sistema!")


exibir_boas_vindas()
```

### Anatomia

```python
def exibir_boas_vindas():
    print("Bem-vindo ao sistema!")
```

- `def` inicia a definição;
- `exibir_boas_vindas` é o nome;
- `()` recebe a lista de parâmetros;
- `:` inicia o bloco;
- o corpo fica indentado.

Definir não é executar. A função só roda quando é chamada:

```python
exibir_boas_vindas()
exibir_boas_vindas()
```

Nesse caso, a mensagem aparece duas vezes.

### Ordem de execução

O Python precisa conhecer a função antes da chamada:

```python
def mostrar_mensagem():
    print("Função executada.")


mostrar_mensagem()
```

As duas linhas em branco entre a função e o código principal seguem uma convenção de estilo e ajudam na leitura.

### Nomes de funções

Prefira verbos que expressem uma ação:

```python
calcular_media()
buscar_aluno()
exibir_menu()
validar_nota()
```

Evite nomes vagos como `fazer()`, `processar_coisa()` ou `funcao1()`.

### Prática rápida

Crie funções sem parâmetros para:

- mostrar o nome da disciplina;
- exibir uma linha separadora;
- apresentar três opções de um menu.

---

## 3. Parâmetros e argumentos

Um parâmetro é uma variável declarada na função. Um argumento é o valor enviado na chamada.

```python
def saudar(nome):
    print(f"Olá, {nome}!")


saudar("Ana")
saudar("Bruno")
```

Em `def saudar(nome)`, `nome` é o parâmetro. Nas chamadas, `"Ana"` e `"Bruno"` são argumentos.

### Múltiplos parâmetros

```python
def exibir_aluno(nome, curso, media):
    print(f"Nome: {nome}")
    print(f"Curso: {curso}")
    print(f"Média: {media:.2f}")


exibir_aluno("Ana", "ADS", 8.5)
```

Por padrão, a posição dos argumentos precisa corresponder à dos parâmetros.

### Argumentos nomeados

```python
exibir_aluno(media=8.5, nome="Ana", curso="ADS")
```

Argumentos nomeados tornam a chamada mais explícita e permitem mudar a ordem.

### Valores padrão

```python
def saudar(nome, mensagem="Bem-vindo"):
    print(f"{mensagem}, {nome}!")


saudar("Ana")
saudar("Bruno", "Bom dia")
```

Parâmetros sem valor padrão devem vir antes dos que possuem padrão:

```python
def exibir_preco(produto, preco, moeda="R$"):
    print(f"{produto}: {moeda} {preco:.2f}")
```

---

## 4. Retorno com return

`return` devolve um resultado ao ponto em que a função foi chamada.

```python
def calcular_media(nota_1, nota_2):
    media = (nota_1 + nota_2) / 2
    return media


resultado = calcular_media(8, 6)
print(f"Média: {resultado:.2f}")
```

### print() não substitui return

Versão que apenas exibe:

```python
def mostrar_media(nota_1, nota_2):
    print((nota_1 + nota_2) / 2)
```

Versão que devolve e permite reutilizar:

```python
def calcular_media(nota_1, nota_2):
    return (nota_1 + nota_2) / 2


media = calcular_media(8, 6)

if media >= 7:
    print("Aprovado.")
```

Uma boa regra inicial:

- use `print()` para apresentar algo ao usuário;
- use `return` para entregar um resultado a outra parte do programa.

### return encerra a função

```python
def dividir(numero_1, numero_2):
    if numero_2 == 0:
        return None

    return numero_1 / numero_2
```

Quando o primeiro `return` é executado, o restante da função não roda.

### Múltiplos valores

```python
def calcular_resultados(nota_1, nota_2):
    media = (nota_1 + nota_2) / 2
    maior = max(nota_1, nota_2)
    return media, maior


media, maior_nota = calcular_resultados(8, 6)
```

Os valores são devolvidos em uma tupla e podem ser desempacotados.

### Composição de funções

```python
def calcular_media(notas):
    return sum(notas) / len(notas)


def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    if media >= 4:
        return "Recuperação"
    return "Reprovado"


notas = [8, 7]
media = calcular_media(notas)
situacao = definir_situacao(media)
```

Cada função resolve uma parte do problema, e os resultados são combinados.

---

## 5. Escopo de variáveis

Uma variável criada dentro de uma função possui escopo local:

```python
def calcular_dobro(numero):
    resultado = numero * 2
    return resultado


dobro = calcular_dobro(5)
print(dobro)

# print(resultado) causaria NameError.
```

`resultado` existe somente durante a execução da função.

Uma variável criada fora das funções possui escopo global:

```python
nome_sistema = "Sistema Acadêmico"


def exibir_titulo():
    print(nome_sistema)
```

Embora funções possam ler variáveis globais, depender delas em excesso dificulta testes e manutenção. Prefira parâmetros e retornos:

```python
def exibir_titulo(titulo):
    print(titulo)


nome_sistema = "Sistema Acadêmico"
exibir_titulo(nome_sistema)
```

Evite modificar variáveis globais com `global` nesta etapa do curso. Retorne o novo valor ou altere explicitamente uma coleção recebida.

### Coleções mutáveis como argumento

```python
def adicionar_nome(nomes, nome):
    nomes.append(nome)


alunos = []
adicionar_nome(alunos, "Ana")
print(alunos)
```

A lista original é alterada. Isso pode ser útil, mas deve estar claro no nome e no propósito da função.

---

## 6. Uma responsabilidade por função

Uma função deve ter um objetivo principal.

Função com responsabilidades misturadas:

```python
def processar_tudo():
    # recebe dados, valida, calcula, cadastra,
    # busca, imprime relatório e controla o menu
    pass
```

Divisão mais clara:

```python
def exibir_menu():
    pass


def ler_nota(mensagem):
    pass


def calcular_media(notas):
    pass


def buscar_aluno(alunos, matricula):
    pass


def cadastrar_aluno(alunos):
    pass


def listar_alunos(alunos):
    pass
```

Sinais de que uma função pode estar grande demais:

- o nome precisa usar “e” para explicar o que ela faz;
- possui muitos níveis de indentação;
- recebe muitos parâmetros sem relação clara;
- é difícil testá-la isoladamente;
- parte dela seria útil em outro ponto do programa.

---

## 7. Docstrings e anotações de tipo

Uma *docstring* descreve o propósito da função e fica logo após sua declaração:

```python
def calcular_media(notas):
    """Calcula e devolve a média aritmética de uma lista de notas."""
    return sum(notas) / len(notas)
```

Para funções mais complexas:

```python
def buscar_aluno(alunos, matricula):
    """Busca um aluno pela matrícula.

    Retorna o dicionário do aluno ou None quando não encontra.
    """
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno

    return None
```

Anotações de tipo documentam os tipos esperados:

```python
def calcular_media(notas: list[float]) -> float:
    """Calcula a média de uma lista não vazia de notas."""
    return sum(notas) / len(notas)
```

Elas ajudam pessoas e ferramentas, mas Python não impede automaticamente uma chamada com outro tipo.

Nesta aula, use anotações simples sem deixar que elas desviem o foco da lógica.

---

## 8. Refatoração passo a passo

Código inicial:

```python
nota_1 = float(input("Nota 1: "))
while nota_1 < 0 or nota_1 > 10:
    nota_1 = float(input("Nota inválida: "))

nota_2 = float(input("Nota 2: "))
while nota_2 < 0 or nota_2 > 10:
    nota_2 = float(input("Nota inválida: "))

media = (nota_1 + nota_2) / 2

if media >= 7:
    situacao = "Aprovado"
elif media >= 4:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"
```

Primeiro, extraímos a leitura:

```python
def ler_nota(mensagem):
    nota = float(input(mensagem))
    while not 0 <= nota <= 10:
        nota = float(input("Nota inválida. Digite de 0 a 10: "))
    return nota
```

Depois, o cálculo:

```python
def calcular_media(notas):
    return sum(notas) / len(notas)
```

Depois, a regra acadêmica:

```python
def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    if media >= 4:
        return "Recuperação"
    return "Reprovado"
```

Código principal:

```python
notas = [ler_nota("Nota 1: "), ler_nota("Nota 2: ")]
media = calcular_media(notas)
situacao = definir_situacao(media)

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
```

Faça uma alteração de cada vez e execute novamente. Assim, se algo quebrar, será mais fácil localizar a causa.

---

## 9. Modularização em arquivos

Um **módulo** é um arquivo Python que pode fornecer funções para outros arquivos.

Estrutura sugerida:

```text
sistema_academico/
├── main.py
├── calculos.py
└── validacoes.py
```

### calculos.py

```python
def calcular_media(notas):
    return sum(notas) / len(notas)


def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    if media >= 4:
        return "Recuperação"
    return "Reprovado"
```

### validacoes.py

```python
def ler_nota(mensagem):
    nota = float(input(mensagem))

    while not 0 <= nota <= 10:
        nota = float(input("Nota inválida. Digite de 0 a 10: "))

    return nota
```

### main.py

```python
from calculos import calcular_media, definir_situacao
from validacoes import ler_nota


nota_1 = ler_nota("Nota 1: ")
nota_2 = ler_nota("Nota 2: ")
media = calcular_media([nota_1, nota_2])
situacao = definir_situacao(media)

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
```

Execute `main.py` a partir da pasta do projeto:

```bash
python main.py
```

### Formas de importação

```python
import calculos

media = calculos.calcular_media([8, 6])
```

```python
from calculos import calcular_media

media = calcular_media([8, 6])
```

A primeira forma deixa explícito de qual módulo veio a função. Evite `from calculos import *`, pois dificulta identificar a origem dos nomes.

### Programa principal

Um padrão comum é:

```python
def main():
    print("Iniciando o sistema.")


if __name__ == "__main__":
    main()
```

O bloco chama `main()` quando o arquivo é executado diretamente e não quando é apenas importado.

---

## 10. Práticas guiadas

### Prática 1 — calculadora modular

Crie funções:

```python
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None
    return a / b
```

Depois, crie um menu que chama a função correspondente. O menu não deve realizar os cálculos diretamente.

### Prática 2 — funções de lista

Implemente e teste:

```python
def calcular_media(valores):
    if len(valores) == 0:
        return None
    return sum(valores) / len(valores)


def contar_pares(numeros):
    quantidade = 0
    for numero in numeros:
        if numero % 2 == 0:
            quantidade += 1
    return quantidade


def buscar_maior(numeros):
    if len(numeros) == 0:
        return None
    return max(numeros)
```

Teste cada função separadamente, inclusive com lista vazia.

### Prática 3 — busca reutilizável

```python
def buscar_aluno(alunos, matricula):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None
```

Use a mesma função nas opções buscar, remover e impedir matrícula duplicada.

---

## 11. Desafio principal — sistema acadêmico modular

Refatore o projeto da Aula 4. Crie uma pasta com:

```text
sistema_academico/
├── main.py
├── alunos.py
├── calculos.py
└── validacoes.py
```

### Responsabilidade dos módulos

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | menu e coordenação do programa |
| `alunos.py` | cadastro, busca, remoção e listagem |
| `calculos.py` | média, situação e resumo |
| `validacoes.py` | leitura de nota e textos obrigatórios |

### Funções mínimas

```python
# validacoes.py
ler_texto_obrigatorio(mensagem)
ler_nota(mensagem)

# calculos.py
calcular_media(notas)
definir_situacao(media)
calcular_resumo(alunos)

# alunos.py
buscar_aluno(alunos, matricula)
cadastrar_aluno(alunos)
listar_alunos(alunos)
remover_aluno(alunos, matricula)

# main.py
exibir_menu()
main()
```

### Contratos sugeridos

| Função | Recebe | Retorna ou altera |
| --- | --- | --- |
| `ler_nota` | mensagem | `float` entre 0 e 10 |
| `calcular_media` | lista não vazia | `float` |
| `definir_situacao` | média | `str` |
| `buscar_aluno` | lista e matrícula | dicionário ou `None` |
| `remover_aluno` | lista e matrícula | `True` ou `False` |
| `calcular_resumo` | lista | dicionário de indicadores ou `None` |

### Requisitos

- o comportamento do sistema da Aula 4 deve ser preservado;
- não duplique a lógica de busca;
- cálculos não devem chamar `input()`;
- funções de validação devem devolver valores válidos;
- `main.py` deve possuir pouco código fora das funções;
- cada função deve ter nome claro e uma responsabilidade principal;
- funções de cálculo e busca devem possuir docstrings;
- imports não devem formar dependências circulares.

### Exemplo de cálculo do resumo

```python
def calcular_resumo(alunos):
    """Retorna indicadores acadêmicos ou None para uma lista vazia."""
    if len(alunos) == 0:
        return None

    medias = [aluno["media"] for aluno in alunos]

    resumo = {
        "total": len(alunos),
        "media_geral": sum(medias) / len(medias),
        "maior_media": max(medias),
        "menor_media": min(medias),
        "aprovados": 0,
        "recuperacoes": 0,
        "reprovados": 0,
    }

    for aluno in alunos:
        if aluno["situacao"] == "Aprovado":
            resumo["aprovados"] += 1
        elif aluno["situacao"] == "Recuperação":
            resumo["recuperacoes"] += 1
        else:
            resumo["reprovados"] += 1

    return resumo
```

> A expressão que cria `medias` é uma compreensão de lista. Se preferir, construa a lista com `for` e `append()`. Compreensões podem ser apresentadas como extensão, sem cobrar seu domínio nesta aula.

### Casos de teste

Teste funções antes de testar o sistema completo:

| Função | Entrada | Resultado esperado |
| --- | --- | --- |
| `calcular_media` | `[8, 6]` | `7.0` |
| `definir_situacao` | `7` | `Aprovado` |
| `definir_situacao` | `6.9` | `Recuperação` |
| `definir_situacao` | `3.9` | `Reprovado` |
| `buscar_aluno` | matrícula existente | dicionário correspondente |
| `buscar_aluno` | matrícula ausente | `None` |
| `remover_aluno` | matrícula existente | `True` e lista alterada |
| `remover_aluno` | matrícula ausente | `False` |
| `calcular_resumo` | lista vazia | `None` |

Depois, execute o fluxo completo:

- cadastrar três alunos;
- impedir matrícula duplicada;
- listar e buscar;
- remover um aluno;
- conferir o resumo;
- sair e iniciar novamente.

### Checklist de entrega

- [ ] O projeto possui os quatro arquivos solicitados.
- [ ] Cada módulo possui uma responsabilidade clara.
- [ ] Parâmetros e retornos são utilizados adequadamente.
- [ ] Não há lógica de cálculo repetida.
- [ ] `buscar_aluno()` é reutilizada.
- [ ] A lista de alunos é criada em `main()` e passada às funções.
- [ ] Funções de cálculo não dependem de variáveis globais.
- [ ] As funções principais possuem docstrings.
- [ ] Os casos de teste isolados foram realizados.
- [ ] O comportamento completo foi preservado.

### Extensões para quem terminar antes

- Adicione função para editar notas.
- Crie `formatar_aluno()` que devolve uma linha formatada.
- Faça `listar_alunos()` receber uma situação opcional como filtro.
- Adicione um arquivo `config.py` para limites de aprovação.
- Crie um módulo separado para a interface do terminal.

---

## 12. Exercícios de fixação

### Exercício 1 — conversores

Crie funções puras para converter Celsius em Fahrenheit, quilômetros em milhas e horas em minutos. Elas devem receber valores e retornar resultados, sem usar `input()` internamente.

### Exercício 2 — análise de texto

Crie funções para contar caracteres, verificar se um texto está vazio e montar uma saudação. Organize-as em `textos.py`.

### Exercício 3 — estatísticas

Crie funções que recebam uma lista e retornem soma, média, maior, menor e quantidade de valores acima da média. Trate a lista vazia.

### Exercício 4 — área de figuras

Crie funções para calcular área de retângulo, triângulo e círculo. Um menu deve coletar os dados e chamar a função correta.

### Exercício 5 — estoque modular

Refatore o exercício de estoque da Aula 4 em módulos para produtos, cálculos e programa principal.

### Exercício 6 — autenticação

Crie uma função que receba usuário e senha e retorne `True` ou `False`. O controle de três tentativas deve ficar fora dela.

### Exercício 7 — relatório de vendas

Crie funções para cadastrar vendas, calcular faturamento, localizar a maior venda e contar vendas acima de um valor informado.

---

## 13. Erros comuns

### Definir e não chamar

```python
def mostrar_mensagem():
    print("Olá")


mostrar_mensagem()
```

### Esquecer os parênteses na chamada

`mostrar_mensagem` representa a função; `mostrar_mensagem()` executa a função.

### Confundir print() e return

Uma função que apenas imprime normalmente devolve `None`:

```python
def somar(a, b):
    print(a + b)


resultado = somar(2, 3)
print(resultado)  # None
```

### Esquecer de retornar em um caminho

Verifique se todos os caminhos relevantes chegam a um `return` coerente.

### Usar variável local fora da função

Receba o resultado pelo `return` e armazene-o em outra variável.

### Criar funções grandes demais

Divida entrada, cálculo, busca e apresentação quando forem responsabilidades independentes.

### Criar importação circular

Se `alunos.py` importa `calculos.py`, evite que `calculos.py` importe `alunos.py`. Mova responsabilidades compartilhadas ou reorganize as dependências.

### Executar código ao importar

Coloque a chamada principal sob:

```python
if __name__ == "__main__":
    main()
```

---

## 14. Estratégia de testes

Funções pequenas facilitam testes isolados. Para cada uma:

1. identifique entradas válidas comuns;
2. teste valores nos limites;
3. teste coleção vazia ou valor ausente;
4. compare o retorno com o esperado;
5. somente depois teste a integração entre módulos.

Teste manual simples:

```python
resultado = calcular_media([8, 6])
print(resultado == 7.0)
```

Uma falha isolada aponta diretamente para a função responsável. Testes automatizados serão introduzidos junto às práticas de qualidade nas aulas seguintes.

---

## 15. Fechamento da aula

### Revisão oral

1. Qual é a diferença entre definir e chamar uma função?
2. Qual é a diferença entre parâmetro e argumento?
3. Qual é a diferença entre `print()` e `return`?
4. O que acontece depois de um `return`?
5. O que é escopo local?
6. Por que evitar dependência excessiva de variáveis globais?
7. O que significa uma função ter responsabilidade única?
8. Para que serve uma docstring?
9. O que é um módulo?
10. Para que serve o bloco `if __name__ == "__main__"`?
11. O que é refatoração?
12. Por que testar funções separadamente?

### Bilhete de saída

Cada aluno deve registrar:

- uma repetição de código que pode virar função;
- um exemplo de parâmetro;
- um exemplo de retorno;
- uma divisão possível de um programa em módulos.

### Critérios de avaliação formativa

| Critério | Evidência esperada |
| --- | --- |
| Decomposição | divide o problema em funções coerentes |
| Parâmetros | envia dependências explicitamente |
| Retornos | devolve resultados reutilizáveis |
| Escopo | evita dependência desnecessária de globais |
| Responsabilidade | mantém entrada, cálculo e apresentação organizados |
| Modularização | distribui funções em arquivos coerentes |
| Reutilização | evita duplicação de regras e buscas |
| Testes | verifica funções isoladas e integração |

Sugestão de pontuação para o desafio: 2 pontos para decomposição, 2 para parâmetros e retornos, 2 para módulos e imports, 2 para preservação do comportamento, 1 para documentação e 1 para testes.

## Tarefa para casa

Implemente três exercícios de fixação. Pelo menos um deve possuir dois módulos além do arquivo principal. Documente as funções centrais e registre ao menos três testes para cada função de cálculo.

## Resumo da sintaxe

```python
def calcular_dobro(numero):
    """Retorna o dobro de um número."""
    return numero * 2


def saudar(nome, mensagem="Olá"):
    return f"{mensagem}, {nome}!"


resultado = calcular_dobro(5)
texto = saudar(nome="Ana")

print(resultado)
print(texto)
```

Importação:

```python
from calculos import calcular_media
```

Programa principal:

```python
def main():
    print("Programa iniciado.")


if __name__ == "__main__":
    main()
```

## Ponte para a Aula 6

Nesta aula, agrupamos comportamentos em funções e código relacionado em módulos. Na Aula 6, estudaremos Programação Orientada a Objetos para reunir dados e comportamentos relacionados em classes, criando objetos como `Aluno`, `Produto` ou `Conta` com atributos e métodos próprios.
