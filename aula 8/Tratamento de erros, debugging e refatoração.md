# Aula 8 — Tratamento de erros, debugging e refatoração

**Duração:** 4 horas  
**Tema:** exceções, investigação de defeitos e melhoria segura do código  
**Produto da aula:** sistema acadêmico resiliente a entradas inválidas e acompanhado por testes

## Objetivos de aprendizagem

Ao final desta aula, o aluno deverá ser capaz de:

- diferenciar erro de sintaxe, exceção e erro de lógica;
- interpretar um *traceback*;
- tratar exceções específicas com `try` e `except`;
- utilizar `else` e `finally` quando forem adequados;
- criar exceções intencionais com `raise`;
- evitar capturas genéricas que escondem defeitos;
- reproduzir, isolar e corrigir um erro sistematicamente;
- usar mensagens temporárias, depurador e testes simples;
- refatorar preservando o comportamento;
- registrar correções e refatorações em commits separados.

## Cronograma da aula

| Tempo | Etapa | Conteúdo e atividade |
| --- | --- | --- |
| 00:00–00:20 | Retomada | revisão do projeto e levantamento de falhas possíveis |
| 00:20–00:50 | Tipos de erro | sintaxe, execução, lógica e leitura do traceback |
| 00:50–01:25 | Exceções | `try`, `except`, `else` e `finally` |
| 01:25–01:45 | Validações | exceções específicas, `raise` e mensagens úteis |
| 01:45–01:55 | Intervalo | pausa de 10 minutos |
| 01:55–02:30 | Debugging | reprodução, hipótese, isolamento e depurador |
| 02:30–03:00 | Testes e refatoração | `assert`, regressão e commits pequenos |
| 03:00–03:45 | Desafio principal | tornar o sistema acadêmico resiliente |
| 03:45–04:00 | Fechamento | revisão, avaliação e tarefa |

---

## 1. Tipos de problema

### Erro de sintaxe

O código não respeita a gramática da linguagem:

```python
# if nota >= 7
#     print("Aprovado")
```

O Python normalmente indica a região onde não conseguiu continuar.

### Exceção em tempo de execução

O código é sintaticamente válido, mas uma operação falha:

```python
idade = int(input("Idade: "))
```

Se o usuário digitar `vinte`, ocorrerá `ValueError`.

### Erro de lógica

O programa executa, mas produz resultado incorreto:

```python
nota_1 = 8
nota_2 = 6
media = nota_1 + nota_2 / 2  # deveria usar parênteses
```

Erros de lógica exigem comparação entre resultado obtido e resultado esperado.

---

## 2. Como ler um traceback

Exemplo:

```python
def calcular_media(notas):
    return sum(notas) / len(notas)


print(calcular_media([]))
```

O traceback informa:

- arquivos e funções percorridos;
- linhas envolvidas;
- tipo da exceção, como `ZeroDivisionError`;
- mensagem associada.

Estratégia de leitura:

1. comece pela última linha;
2. identifique o tipo e a mensagem;
3. localize a última linha do seu próprio código;
4. observe os valores usados;
5. descubra por que aquela operação era inválida.

Não corrija apenas a linha indicada sem investigar a origem do dado incorreto.

---

## 3. try e except

```python
try:
    idade = int(input("Idade: "))
    print(f"Idade registrada: {idade}")
except ValueError:
    print("Digite a idade usando um número inteiro.")
```

O bloco `try` contém a operação que pode falhar. O `except` trata uma falha esperada.

### Repetindo até receber um valor válido

```python
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
```

Para decimal:

```python
def ler_decimal(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Use um número, como 8.5.")
```

### Exceções específicas

```python
try:
    indice = int(input("Índice: "))
    print(nomes[indice])
except ValueError:
    print("O índice precisa ser inteiro.")
except IndexError:
    print("Essa posição não existe.")
```

Evite:

```python
# except:
#     print("Algo deu errado")
```

Uma captura ampla pode esconder erros de programação e dificultar o diagnóstico.

---

## 4. else e finally

`else` executa quando nenhuma exceção acontece:

```python
try:
    numero = int(input("Número: "))
except ValueError:
    print("Entrada inválida.")
else:
    print(f"Dobro: {numero * 2}")
```

`finally` executa havendo erro ou não:

```python
arquivo = None

try:
    arquivo = open("dados.txt", encoding="utf-8")
    print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    if arquivo is not None:
        arquivo.close()
```

Para arquivos, normalmente prefira o gerenciador de contexto:

```python
with open("dados.txt", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
```

Use `finally` para liberar recursos ou executar uma finalização necessária, não para toda mensagem de encerramento.

---

## 5. Validação e raise

Conversão e validação resolvem problemas diferentes:

- conversão: o texto pode virar número?
- validação: o número atende à regra do sistema?

```python
def validar_nota(nota):
    if not 0 <= nota <= 10:
        raise ValueError("A nota deve estar entre 0 e 10.")
    return nota
```

```python
try:
    nota = validar_nota(float(input("Nota: ")))
except ValueError as erro:
    print(f"Não foi possível registrar: {erro}")
```

`raise` comunica que a função não consegue cumprir seu contrato com aquele valor.

### Exceção não substitui decisão normal

Não use exceções para um resultado esperado, como aluno não encontrado em uma busca comum, quando `None` ou `False` comunica bem o resultado.

---

## 6. Estratégia de debugging

Use um processo repetível:

```text
reproduzir → observar → formular hipótese → isolar → testar → corrigir → testar novamente
```

### 1. Reproduzir

Registre entrada, resultado esperado e resultado obtido.

### 2. Reduzir

Descubra a menor entrada que ainda produz a falha.

### 3. Inspecionar valores

```python
print(f"DEBUG media={media!r}, quantidade={quantidade!r}")
```

`!r` ajuda a visualizar o valor de maneira técnica, incluindo aspas em textos.

### 4. Usar o depurador

Coloque um ponto de interrupção antes da linha suspeita e observe:

- valores das variáveis;
- condição atual;
- pilha de chamadas;
- execução linha a linha.

Também é possível inserir temporariamente:

```python
breakpoint()
```

### 5. Corrigir a causa

Uma conversão falha pode ser consequência de uma entrada não validada. Um `KeyError` pode revelar modelagem inconsistente. Procure a origem, não apenas o sintoma.

### 6. Remover instrumentação

Retire mensagens `DEBUG` e pontos de interrupção antes da entrega.

---

## 7. Testes simples com assert

```python
def calcular_media(notas):
    if len(notas) == 0:
        return None
    return sum(notas) / len(notas)


assert calcular_media([8, 6]) == 7
assert calcular_media([10]) == 10
assert calcular_media([]) is None
```

Teste limites das regras:

```python
assert definir_situacao(7) == "Aprovado"
assert definir_situacao(6.9) == "Recuperação"
assert definir_situacao(4) == "Recuperação"
assert definir_situacao(3.9) == "Reprovado"
```

Um teste de regressão registra o comportamento correto após corrigirmos um defeito, evitando que ele retorne silenciosamente.

> `assert` é útil didaticamente, mas projetos reais costumam usar ferramentas próprias de teste. Não use `assert` para validar entrada do usuário ou regras de segurança.

---

## 8. Refatoração protegida por testes

Sequência recomendada:

1. deixe os testes atuais passando;
2. faça uma alteração estrutural pequena;
3. execute os testes;
4. revise o `git diff`;
5. crie um commit específico;
6. repita.

Refatorações comuns:

- renomear variável ou método;
- extrair função;
- remover duplicação;
- simplificar condição;
- separar interface e regra de negócio;
- dividir uma classe com responsabilidades excessivas.

Não misture uma grande refatoração com uma funcionalidade nova no mesmo commit.

---

## 9. Práticas guiadas

### Prática 1 — divisão segura

```python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("O divisor não pode ser zero.")
    return a / b


try:
    primeiro = float(input("Primeiro número: "))
    segundo = float(input("Segundo número: "))
    resultado = dividir(primeiro, segundo)
except ValueError:
    print("Digite apenas números.")
except ZeroDivisionError as erro:
    print(erro)
else:
    print(f"Resultado: {resultado:.2f}")
```

### Prática 2 — localizar o defeito

```python
def calcular_desconto(valor, percentual):
    return valor - percentual / 100
```

Escreva casos esperados, reproduza o erro e corrija a fórmula. Depois crie um teste de regressão.

### Prática 3 — dicionário seguro

Receba uma matrícula, busque o aluno e diferencie:

- entrada vazia;
- aluno ausente;
- dicionário sem uma chave opcional;
- cadastro encontrado normalmente.

Use decisões comuns para resultados esperados e exceções somente para operações que realmente podem falhar.

---

## 10. Desafio principal — sistema acadêmico resiliente

Use uma branch criada a partir do projeto da Aula 7:

```bash
git switch -c fix/tratamento-erros
```

### Requisitos

- `ler_inteiro()` deve repetir após `ValueError`;
- `ler_decimal()` deve repetir após `ValueError`;
- `ler_nota()` deve aceitar somente valores de 0 a 10;
- entradas vazias obrigatórias devem ser recusadas;
- operações com aluno ausente devem exibir mensagem específica;
- lista vazia não deve causar divisão por zero;
- arquivo ausente, se houver persistência, deve ser tratado;
- regras acadêmicas devem ter testes de limite;
- mensagens devem orientar o usuário sem exibir detalhes internos desnecessários;
- exceções inesperadas não devem ser silenciosamente ignoradas.

### Defeito obrigatório

Introduza em uma branch de exercício uma fórmula incorreta para média, reproduza o erro com um teste, corrija e registre:

```text
test: reproduz erro no cálculo de média
fix: corrige precedência no cálculo de média
```

### Testes mínimos

| Cenário | Resultado esperado |
| --- | --- |
| idade digitada como texto | nova solicitação |
| nota `-1` ou `11` | nova solicitação |
| média de `[8, 6]` | `7.0` |
| lista de notas vazia | `None` ou regra documentada |
| matrícula ausente | mensagem específica |
| divisor zero | erro controlado |
| arquivo opcional ausente | sistema continua com estado inicial |

### Checklist

- [ ] Exceções específicas são usadas.
- [ ] Não existe `except` vazio.
- [ ] Conversão e regra de domínio estão separadas.
- [ ] Mensagens ajudam a corrigir a entrada.
- [ ] Há testes para limites e falhas corrigidas.
- [ ] A refatoração preservou funcionalidades anteriores.
- [ ] Instrumentação temporária foi removida.
- [ ] Commits de correção e refatoração estão separados.
- [ ] A branch foi testada antes da integração.

### Extensões

- Crie exceções próprias, como `NotaInvalidaError`.
- Registre erros técnicos em arquivo sem expô-los na interface.
- Separe testes em um módulo próprio.
- Adicione persistência em arquivo JSON com tratamento de falhas.

---

## 11. Exercícios de fixação

1. Crie uma calculadora que trate texto inválido e divisão por zero.
2. Leia uma posição de uma lista e trate `ValueError` e `IndexError` separadamente.
3. Leia um arquivo e diferencie arquivo ausente e conteúdo inválido.
4. Encontre e corrija três erros lógicos em um programa fornecido pelo professor.
5. Escreva testes com `assert` para uma classe `ContaBancaria`.
6. Refatore uma função longa em três funções, executando testes após cada etapa.

---

## 12. Erros comuns

- envolver o programa inteiro em um único `try`;
- usar `except Exception` sem necessidade e esconder defeitos;
- mostrar “erro” sem orientar o usuário;
- repetir lógica de validação em vários lugares;
- corrigir sem primeiro reproduzir;
- alterar muitas coisas antes de testar;
- manter `print()` de debugging na entrega;
- modificar o teste apenas para fazer uma implementação errada passar;
- confundir ausência esperada com exceção inesperada.

---

## 13. Fechamento

### Revisão oral

1. Qual é a diferença entre exceção e erro de lógica?
2. Por onde começamos a ler um traceback?
3. Quando usar `else` em um `try`?
4. Quando `finally` é útil?
5. Por que capturar exceções específicas?
6. Para que serve `raise`?
7. Qual é a sequência de debugging?
8. O que é teste de regressão?
9. Como Git protege uma refatoração?

### Avaliação formativa

| Critério | Evidência esperada |
| --- | --- |
| Diagnóstico | reproduz e isola o defeito |
| Traceback | identifica tipo, mensagem e origem provável |
| Tratamento | captura exceções específicas |
| Validação | separa formato e regra de domínio |
| Testes | cobre fluxo normal, limites e regressões |
| Refatoração | melhora estrutura sem quebrar comportamento |
| Git | registra mudanças pequenas e descritivas |

Sugestão de pontuação: 2 pontos para tratamento, 2 para diagnóstico, 2 para testes, 2 para refatoração, 1 para mensagens e 1 para histórico Git.

## Tarefa para casa

Finalize o desafio e documente no README três falhas que o sistema trata. Para cada uma, informe entrada, resultado esperado e método ou função responsável.

## Ponte para a Aula 9

Na próxima aula, usaremos IA como apoio para explicar código, criar casos de teste, sugerir hipóteses de defeitos e revisar mudanças. Toda sugestão será verificada com leitura, execução, testes e `git diff` antes de ser aceita.
