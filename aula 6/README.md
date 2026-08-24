# Aula 6 — Programação Orientada a Objetos com Python

**Duração:** 4 horas  
**Tema:** classes, objetos, atributos, métodos e composição  
**Produto da aula:** sistema acadêmico orientado a objetos

## Objetivos de aprendizagem

Ao final desta aula, o aluno deverá ser capaz de:

- explicar os conceitos de classe e objeto;
- diferenciar atributos e métodos;
- criar classes com `class`;
- inicializar objetos com `__init__`;
- compreender o papel do parâmetro `self`;
- criar e utilizar métodos de instância;
- representar o estado de um objeto com atributos;
- proteger regras por meio de métodos e propriedades;
- criar representações textuais com `__str__`;
- relacionar objetos por composição;
- transformar dicionários do sistema acadêmico em objetos;
- reconhecer quando POO ajuda ou adiciona complexidade desnecessária.

## Conhecimentos necessários

- variáveis, condicionais e repetições;
- listas e dicionários;
- funções, parâmetros e retornos;
- módulos e importações.

## Cronograma da aula

| Tempo | Etapa | Conteúdo e atividade |
| --- | --- | --- |
| 00:00–00:20 | Retomada | revisão de funções e modelagem com dicionários |
| 00:20–00:50 | Fundamentos de POO | classe, objeto, atributo e método |
| 00:50–01:25 | Construção de classes | `class`, `__init__` e `self` |
| 01:25–01:45 | Métodos | comportamento, retorno e alteração de estado |
| 01:45–01:55 | Intervalo | pausa de 10 minutos |
| 01:55–02:25 | Modelagem | propriedades, validações e `__str__` |
| 02:25–02:55 | Relações | composição e listas de objetos |
| 02:55–03:15 | Prática guiada | classes `Produto` e `Carrinho` |
| 03:15–03:50 | Desafio principal | classes `Aluno` e `Turma` |
| 03:50–04:00 | Fechamento | revisão, avaliação e tarefa |

---

## 1. Do dicionário ao objeto

Na Aula 5, um aluno poderia ser representado por um dicionário:

```python
aluno = {
    "matricula": "001",
    "nome": "Ana",
    "notas": [8.0, 7.5],
    "media": 7.75,
    "situacao": "Aprovado",
}
```

E as regras ficavam em funções separadas:

```python
def calcular_media(notas):
    return sum(notas) / len(notas)
```

Na Programação Orientada a Objetos, podemos reunir os dados e os comportamentos relacionados:

```python
class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.notas = []

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
```

O objeto passa a cuidar das operações relacionadas ao seu próprio estado.

---

## 2. Conceitos fundamentais

### Classe

Uma classe é um modelo que define características e comportamentos de determinado tipo de objeto.

Exemplos:

- `Aluno`;
- `Produto`;
- `ContaBancaria`;
- `Livro`;
- `Pedido`.

### Objeto

Um objeto é uma instância concreta de uma classe.

```python
aluno_1 = Aluno("001", "Ana")
aluno_2 = Aluno("002", "Bruno")
```

`aluno_1` e `aluno_2` são objetos diferentes da mesma classe.

### Atributo

Um atributo guarda um dado ou estado do objeto:

```python
print(aluno_1.nome)
print(aluno_1.matricula)
```

### Método

Um método é uma função definida dentro da classe e representa um comportamento:

```python
media = aluno_1.calcular_media()
```

### Comparação com um projeto arquitetônico

```text
Classe: projeto de uma casa
Objeto: uma casa construída a partir do projeto
Atributos: cor, endereço, quantidade de quartos
Métodos: abrir porta, acender luz, calcular área
```

A analogia ajuda, mas objetos de software representam regras e comportamentos, não apenas coisas físicas.

---

## 3. Criando a primeira classe

```python
class Pessoa:
    pass
```

`pass` indica que o bloco está vazio. Já podemos criar objetos:

```python
pessoa_1 = Pessoa()
pessoa_2 = Pessoa()

print(type(pessoa_1))
print(pessoa_1 == pessoa_2)
```

Mesmo pertencendo à mesma classe, são objetos distintos.

### Convenção de nomes

- classes: `PascalCase`, como `ContaBancaria`;
- variáveis e métodos: `snake_case`, como `saldo_atual` e `calcular_total`.

---

## 4. Inicialização com __init__

O método `__init__` é executado durante a criação do objeto:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa = Pessoa("Ana", 20)
print(pessoa.nome)
print(pessoa.idade)
```

### O papel de self

`self` representa o objeto que está utilizando o método.

```python
pessoa_1 = Pessoa("Ana", 20)
pessoa_2 = Pessoa("Bruno", 25)
```

Quando escrevemos:

```python
print(pessoa_1.nome)
```

Python consulta o atributo `nome` do objeto `pessoa_1`. Cada objeto mantém seu próprio estado.

No método:

```python
def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
```

- `nome` e `idade` são parâmetros temporários;
- `self.nome` e `self.idade` são atributos que permanecem no objeto.

Não passamos `self` explicitamente:

```python
pessoa = Pessoa("Ana", 20)
```

Python fornece a própria instância automaticamente.

### Prática rápida — classe Livro

Crie uma classe `Livro` com título, autor e quantidade de páginas. Instancie dois livros e mostre seus atributos.

<details>
<summary>Ver uma solução possível</summary>

```python
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


livro_1 = Livro("Dom Casmurro", "Machado de Assis", 256)
livro_2 = Livro("O Alienista", "Machado de Assis", 96)

print(livro_1.titulo)
print(livro_2.titulo)
```

</details>

---

## 5. Métodos de instância

Métodos recebem `self` como primeiro parâmetro e podem consultar ou alterar o objeto.

```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            return False

        self.saldo -= valor
        return True

    def consultar_saldo(self):
        return self.saldo
```

Utilização:

```python
conta = ContaBancaria("Ana", 100)

if conta.depositar(50):
    print("Depósito realizado.")

if conta.sacar(30):
    print("Saque realizado.")

print(f"Saldo: R$ {conta.consultar_saldo():.2f}")
```

As regras de depósito e saque ficam próximas dos dados que protegem.

### Método que não altera o estado

```python
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
```

Esses métodos apenas calculam e retornam valores.

---

## 6. Modelando a classe Aluno

```python
class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            return True
        return False

    def calcular_media(self):
        if len(self.notas) == 0:
            return None
        return sum(self.notas) / len(self.notas)

    def obter_situacao(self):
        media = self.calcular_media()

        if media is None:
            return "Sem notas"
        if media >= 7:
            return "Aprovado"
        if media >= 4:
            return "Recuperação"
        return "Reprovado"
```

Uso:

```python
aluno = Aluno("001", "Ana")
aluno.adicionar_nota(8)
aluno.adicionar_nota(7.5)

print(aluno.nome)
print(aluno.notas)
print(aluno.calcular_media())
print(aluno.obter_situacao())
```

Perguntas para a turma:

1. Por que `notas` começa como lista vazia?
2. Por que `adicionar_nota()` retorna um booleano?
3. Por que a média pode retornar `None`?
4. Por que `obter_situacao()` chama `calcular_media()`?

---

## 7. Encapsulamento básico

Encapsular significa controlar como o estado do objeto é consultado ou alterado. Em Python, um sublinhado inicial indica que um atributo é de uso interno por convenção:

```python
class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0

    def depositar(self, valor):
        if valor <= 0:
            return False
        self._saldo += valor
        return True

    def consultar_saldo(self):
        return self._saldo
```

`_saldo` ainda pode ser acessado tecnicamente, mas o sublinhado comunica: “não altere diretamente; utilize os métodos”.

```python
# Evite:
# conta._saldo = -1000

# Prefira:
conta.depositar(100)
```

### Propriedades

Uma propriedade permite consultar um método como se fosse um atributo:

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco <= 0:
            return
        self._preco = novo_preco
```

```python
produto = Produto("Teclado", 100)
print(produto.preco)
produto.preco = 120
```

Para esta introdução, propriedades são uma extensão. O foco principal são classes, atributos e métodos claros.

---

## 8. Representação textual com __str__

Ao imprimir um objeto sem personalização, a saída costuma ser pouco amigável. O método especial `__str__` define sua representação para usuários:

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


produto = Produto("Mouse", 79.9)
print(produto)
```

Saída:

```text
Mouse - R$ 79.90
```

Para `Aluno`:

```python
def __str__(self):
    media = self.calcular_media()
    texto_media = "Sem notas" if media is None else f"{media:.2f}"
    return f"{self.matricula} - {self.nome} - Média: {texto_media}"
```

O método deve retornar uma string, não apenas usar `print()`.

---

## 9. Composição

Composição ocorre quando um objeto contém ou utiliza outros objetos.

Uma turma possui alunos:

```python
class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def quantidade_alunos(self):
        return len(self.alunos)
```

```python
turma = Turma("Python 2026")
aluno = Aluno("001", "Ana")
turma.adicionar_aluno(aluno)

print(turma.quantidade_alunos())
```

Relação:

```text
Turma
└── alunos
    ├── objeto Aluno
    ├── objeto Aluno
    └── objeto Aluno
```

`Turma` não precisa copiar todos os dados do aluno; ela guarda referências aos objetos.

### Composição não é herança

- composição: uma turma **possui** alunos;
- herança: um professor **é uma** pessoa.

Herança será apenas mencionada nesta aula. É melhor dominar objetos e composição antes de criar hierarquias.

---

## 10. Listas de objetos

Percorrer objetos é semelhante a percorrer dicionários:

```python
alunos = [
    Aluno("001", "Ana"),
    Aluno("002", "Bruno"),
]

for aluno in alunos:
    print(aluno.nome)
```

Busca:

```python
def buscar_aluno(alunos, matricula):
    for aluno in alunos:
        if aluno.matricula == matricula:
            return aluno
    return None
```

Uma alternativa é transformar a busca em método de `Turma`:

```python
class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def buscar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None
```

A segunda opção expressa que a busca ocorre dentro de uma turma específica.

---

## 11. Prática guiada — Produto e Carrinho

Crie `produto.py`:

```python
class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.codigo} - {self.nome} - R$ {self.preco:.2f}"
```

Crie `carrinho.py`:

```python
class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def remover(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                return True
        return False

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

    def listar(self):
        for produto in self.produtos:
            print(produto)
```

Crie `main.py`:

```python
from carrinho import Carrinho
from produto import Produto


carrinho = Carrinho()
carrinho.adicionar(Produto("P01", "Mouse", 79.90))
carrinho.adicionar(Produto("P02", "Teclado", 129.90))

carrinho.listar()
print(f"Total: R$ {carrinho.calcular_total():.2f}")
```

Discuta:

- qual classe representa cada entidade;
- quais atributos pertencem a cada objeto;
- quem deve calcular o total;
- por que `Carrinho` recebe um objeto `Produto`;
- o que acontece se o mesmo produto for adicionado duas vezes.

---

## 12. Desafio principal — sistema acadêmico orientado a objetos

Crie a estrutura:

```text
sistema_academico/
├── main.py
├── aluno.py
├── turma.py
└── validacoes.py
```

### Classe Aluno

Deve possuir:

- atributos `matricula`, `nome` e `notas`;
- método `adicionar_nota(nota)`;
- método `calcular_media()`;
- método `obter_situacao()`;
- método `__str__()`.

Regras:

- notas válidas estão entre 0 e 10;
- sem notas, a média deve ser `None`;
- média a partir de 7: aprovado;
- média de 4 até abaixo de 7: recuperação;
- média abaixo de 4: reprovado;
- sem notas: situação “Sem notas”.

### Classe Turma

Deve possuir:

- atributos `codigo`, `disciplina` e `alunos`;
- método `adicionar_aluno(aluno)`;
- método `buscar_aluno(matricula)`;
- método `remover_aluno(matricula)`;
- método `calcular_media_geral()`;
- método `obter_resumo()`;
- método `listar_alunos()` ou uma forma de devolver os alunos.

Regras:

- não aceitar matrícula repetida;
- busca ausente retorna `None`;
- remoção devolve `True` ou `False`;
- alunos sem nota não participam da média geral;
- resumo deve contabilizar cada situação.

### Interface principal

O `main.py` deve permitir:

```text
1 - Cadastrar aluno
2 - Adicionar nota
3 - Listar alunos
4 - Buscar aluno
5 - Remover aluno
6 - Exibir resumo
0 - Sair
```

Entrada e mensagens ficam no `main.py` ou em funções auxiliares. Regras acadêmicas ficam nas classes.

### Esqueleto de Aluno

```python
class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        if not 0 <= nota <= 10:
            return False
        self.notas.append(nota)
        return True

    def calcular_media(self):
        if len(self.notas) == 0:
            return None
        return sum(self.notas) / len(self.notas)

    def obter_situacao(self):
        media = self.calcular_media()

        if media is None:
            return "Sem notas"
        if media >= 7:
            return "Aprovado"
        if media >= 4:
            return "Recuperação"
        return "Reprovado"

    def __str__(self):
        media = self.calcular_media()
        texto_media = "Sem notas" if media is None else f"{media:.2f}"
        return (
            f"{self.matricula} - {self.nome} - "
            f"Média: {texto_media} - {self.obter_situacao()}"
        )
```

### Esqueleto de Turma

```python
class Turma:
    def __init__(self, codigo, disciplina):
        self.codigo = codigo
        self.disciplina = disciplina
        self.alunos = []

    def buscar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def adicionar_aluno(self, aluno):
        if self.buscar_aluno(aluno.matricula) is not None:
            return False
        self.alunos.append(aluno)
        return True

    def remover_aluno(self, matricula):
        aluno = self.buscar_aluno(matricula)
        if aluno is None:
            return False
        self.alunos.remove(aluno)
        return True

    def calcular_media_geral(self):
        medias = []

        for aluno in self.alunos:
            media = aluno.calcular_media()
            if media is not None:
                medias.append(media)

        if len(medias) == 0:
            return None
        return sum(medias) / len(medias)

    def obter_resumo(self):
        resumo = {
            "total": len(self.alunos),
            "Aprovado": 0,
            "Recuperação": 0,
            "Reprovado": 0,
            "Sem notas": 0,
        }

        for aluno in self.alunos:
            situacao = aluno.obter_situacao()
            resumo[situacao] += 1

        resumo["media_geral"] = self.calcular_media_geral()
        return resumo
```

### Casos de teste obrigatórios

Teste as classes antes do menu:

```python
from aluno import Aluno
from turma import Turma


turma = Turma("PY01", "Introdução ao Python")

ana = Aluno("001", "Ana")
ana.adicionar_nota(8)
ana.adicionar_nota(6)

bruno = Aluno("002", "Bruno")
bruno.adicionar_nota(5)
bruno.adicionar_nota(5)

carla = Aluno("003", "Carla")

print(turma.adicionar_aluno(ana))
print(turma.adicionar_aluno(bruno))
print(turma.adicionar_aluno(carla))
print(turma.adicionar_aluno(ana))  # deve ser False

for aluno in turma.alunos:
    print(aluno)

print(turma.calcular_media_geral())  # 6.0
print(turma.obter_resumo())
```

Tabela de testes:

| Operação | Entrada | Resultado esperado |
| --- | --- | --- |
| adicionar nota | `8` | `True` |
| adicionar nota | `-1` ou `11` | `False` |
| média sem notas | lista vazia | `None` |
| adicionar aluno | matrícula nova | `True` |
| adicionar aluno | matrícula repetida | `False` |
| buscar aluno | matrícula existente | objeto `Aluno` |
| buscar aluno | matrícula ausente | `None` |
| remover aluno | matrícula existente | `True` |
| remover aluno | matrícula ausente | `False` |
| média geral | somente alunos sem notas | `None` |

### Checklist de entrega

- [ ] `Aluno` e `Turma` estão em módulos separados.
- [ ] Objetos são inicializados com `__init__`.
- [ ] Métodos utilizam `self` corretamente.
- [ ] Notas inválidas não são adicionadas.
- [ ] Matrículas repetidas não são aceitas.
- [ ] `Aluno` calcula sua própria média e situação.
- [ ] `Turma` gerencia sua lista de alunos.
- [ ] Alunos sem notas não entram na média geral.
- [ ] `__str__()` produz uma saída compreensível.
- [ ] As classes foram testadas antes da interface.
- [ ] O menu completo funciona.

### Extensões para quem terminar antes

- Crie uma classe `Disciplina` e associe turmas a ela.
- Adicione frequência ao objeto `Aluno`.
- Crie método para editar nome sem alterar matrícula.
- Impeça que `notas` seja alterada diretamente usando uma cópia ou propriedade.
- Modele `Professor` e associe um professor à turma.
- Adicione data ou descrição para cada avaliação.

---

## 13. Quando usar POO?

POO é especialmente útil quando:

- o domínio possui entidades com dados e comportamentos relacionados;
- existem vários objetos com a mesma estrutura;
- regras precisam proteger ou alterar o estado;
- objetos colaboram entre si;
- o sistema tende a crescer.

Uma classe pode ser desnecessária quando:

- o problema é um cálculo pequeno e direto;
- não existe estado relevante;
- funções simples deixam a solução mais clara;
- a classe serviria apenas como recipiente sem comportamento.

Não transforme tudo em classe. O objetivo é tornar a modelagem mais compreensível.

---

## 14. Exercícios de fixação

### Exercício 1 — Retângulo

Crie uma classe com largura e altura e métodos para calcular área e perímetro. Recuse medidas não positivas.

### Exercício 2 — Conta bancária

Crie titular, saldo e métodos depositar, sacar e consultar saldo. Não permita depósito negativo nem saque maior que o saldo.

### Exercício 3 — Produto

Crie nome, preço e estoque. Implemente entrada, saída, valor total do estoque e aplicação de desconto.

### Exercício 4 — Livro e Biblioteca

`Livro` deve possuir título, autor e disponibilidade. `Biblioteca` deve cadastrar, buscar, emprestar e devolver livros.

### Exercício 5 — Tarefa e ListaDeTarefas

`Tarefa` possui descrição e estado de conclusão. `ListaDeTarefas` adiciona, conclui, remove e lista tarefas.

### Exercício 6 — Funcionário

Crie nome e salário, com métodos para aplicar reajuste e calcular salário anual. Depois crie uma classe `Empresa` com uma lista de funcionários.

### Exercício 7 — Pedido

Modele `Produto`, `ItemPedido` com quantidade e `Pedido` com uma lista de itens. Calcule subtotal por item e total do pedido.

---

## 15. Erros comuns

### Esquecer self

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def saudar(self):
        return f"Olá, sou {self.nome}."
```

### Confundir parâmetro e atributo

Sem `self.nome = nome`, o valor recebido não permanece no objeto.

### Chamar método sem parênteses

```python
print(aluno.calcular_media())  # executa
print(aluno.calcular_media)    # mostra referência ao método
```

### Criar atributo somente em alguns caminhos

Inicialize os atributos essenciais no `__init__` para que todos os objetos possuam uma estrutura previsível.

### Usar print() onde deveria retornar

Métodos de cálculo devem normalmente devolver o resultado. A interface decide como mostrá-lo.

### Alterar diretamente um estado protegido

Prefira métodos como `depositar()` ou `adicionar_nota()` quando existem regras de validade.

### Criar classes com responsabilidades demais

`Aluno` não deve controlar o menu completo, e `Turma` não deve ler todas as entradas do terminal.

### Usar herança apenas para reaproveitar código

Primeiro verifique se composição ou uma função resolve a relação de forma mais clara.

---

## 16. Estratégia de testes

Teste cada classe sem depender do menu:

1. crie um objeto com valores comuns;
2. consulte seus atributos iniciais;
3. execute cada método com valor válido;
4. execute com valores nos limites;
5. tente operações inválidas;
6. confirme o estado depois de cada operação;
7. teste objetos diferentes para garantir estados independentes;
8. somente depois teste a interação entre classes.

Exemplo:

```python
conta = ContaBancaria("Ana", 100)

print(conta.depositar(50) == True)
print(conta.consultar_saldo() == 150)
print(conta.sacar(200) == False)
print(conta.consultar_saldo() == 150)
```

Em código real, prefira simplesmente `assert conta.depositar(50)` em vez de comparar booleanos com `True`. Testes automatizados serão aprofundados junto à qualidade de código.

---

## 17. Fechamento da aula

### Revisão oral

1. Qual é a diferença entre classe e objeto?
2. O que é um atributo?
3. O que é um método?
4. Para que serve `__init__`?
5. O que `self` representa?
6. Por que cada objeto mantém seu próprio estado?
7. Qual é a diferença entre parâmetro e atributo?
8. Para que serve `__str__`?
9. O que significa encapsular?
10. O que é composição?
11. Por que uma turma deve possuir objetos `Aluno`?
12. Quando uma função simples pode ser melhor que uma classe?

### Bilhete de saída

Cada aluno deve registrar:

- uma classe possível em um sistema conhecido;
- três atributos dessa classe;
- dois métodos;
- uma relação de composição com outra classe.

### Critérios de avaliação formativa

| Critério | Evidência esperada |
| --- | --- |
| Modelagem | identifica classes adequadas ao domínio |
| Inicialização | cria atributos consistentes em `__init__` |
| Métodos | associa comportamentos à classe correta |
| Estado | consulta e altera dados por operações claras |
| Encapsulamento | mantém regras próximas aos atributos protegidos |
| Composição | relaciona objetos sem duplicar dados |
| Organização | separa classes e interface em módulos |
| Testes | verifica estado e retorno após cada operação |

Sugestão de pontuação para o desafio: 2 pontos para `Aluno`, 2 para `Turma`, 2 para regras e encapsulamento, 1 para composição, 1 para interface, 1 para organização e 1 para testes.

## Tarefa para casa

Implemente dois exercícios de fixação. Um deve envolver apenas uma classe e outro deve utilizar composição entre duas ou mais classes. Registre os cenários de teste, incluindo pelo menos uma operação inválida.

## Resumo da sintaxe

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        if not 0 <= percentual <= 100:
            return False

        self.preco -= self.preco * percentual / 100
        return True

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


produto = Produto("Teclado", 150)
produto.aplicar_desconto(10)
print(produto)
```

Composição:

```python
class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)
```

## Ponte para a Aula 7

Nesta aula, modelamos o sistema com classes e módulos. Na Aula 7, aprenderemos a registrar a evolução desse projeto com Git e GitHub, trabalhar com commits e branches e aplicar práticas de organização e código limpo para facilitar colaboração e manutenção.
