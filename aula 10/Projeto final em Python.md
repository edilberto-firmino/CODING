# Aula 10 — Projeto final em Python

**Duração:** 4 horas  
**Tema:** integração, finalização, testes, GitHub e apresentação  
**Produto da aula:** aplicação Python completa, versionada, documentada e apresentada

## Objetivos de aprendizagem

Ao final desta aula, o aluno deverá ser capaz de:

- transformar um problema em requisitos verificáveis;
- definir um escopo viável para o tempo disponível;
- organizar uma aplicação em módulos ou classes;
- integrar os conteúdos das aulas anteriores;
- validar entradas e tratar falhas esperadas;
- testar fluxos principais e casos de borda;
- utilizar Git para registrar a evolução;
- documentar instalação, execução e decisões;
- apresentar e demonstrar o projeto;
- refletir sobre limitações e próximos passos.

## Resultado esperado

O projeto final não precisa ser grande. Ele precisa ser:

- funcional;
- compreensível;
- coerente com os requisitos;
- testado;
- seguro para demonstrar;
- organizado;
- versionado;
- explicável pela equipe.

## Cronograma da aula

| Tempo | Etapa | Conteúdo e atividade |
| --- | --- | --- |
| 00:00–00:20 | Abertura | revisão do escopo e critérios de entrega |
| 00:20–00:40 | Planejamento final | quadro de tarefas e divisão de responsabilidades |
| 00:40–02:00 | Implementação | conclusão do fluxo principal e integrações |
| 02:00–02:10 | Intervalo | pausa de 10 minutos |
| 02:10–02:50 | Qualidade | testes, debugging, refatoração e revisão |
| 02:50–03:15 | Entrega | README, histórico Git e versão final |
| 03:15–03:50 | Apresentações | demonstrações das equipes |
| 03:50–04:00 | Encerramento | avaliação, retrospectiva e próximos passos |

> Idealmente, o projeto deve começar antes da Aula 10. Esta aula é dedicada à integração, acabamento, testes e apresentação, não à criação apressada de um sistema grande do zero.

---

## 1. Conteúdos integrados

| Aula | Evidência possível no projeto |
| --- | --- |
| 1 | variáveis, entradas, saídas e cálculos |
| 2 | decisões e regras de negócio |
| 3 | menus, repetições e validações |
| 4 | listas, tuplas e dicionários |
| 5 | funções, retornos e módulos |
| 6 | classes e composição, quando adequadas |
| 7 | Git, branches, commits, README e GitHub |
| 8 | tratamento de erros, debugging e testes |
| 9 | uso documentado e verificado de IA, se utilizado |

Não é obrigatório forçar todos os recursos. Uma solução simples e coerente vale mais que uma arquitetura complexa sem necessidade.

---

## 2. Opções de projeto

### Sistema acadêmico

- cadastro de alunos e disciplinas;
- notas e frequência;
- situação e resumo da turma;
- busca, edição e remoção.

### Controle de estoque

- produtos, preços e quantidades;
- entrada e saída;
- alertas de estoque baixo;
- valor total e relatório.

### Biblioteca

- livros e leitores;
- empréstimo e devolução;
- disponibilidade e atraso;
- buscas e relatórios.

### Finanças pessoais

- receitas e despesas fictícias;
- categorias;
- saldo e resumo mensal;
- filtros e limites.

### Agenda de tarefas

- cadastro, prioridade e prazo;
- conclusão e remoção;
- filtros por estado;
- indicadores de produtividade.

### Sistema de pedidos

- produtos e itens;
- quantidade e total;
- desconto controlado;
- situação do pedido.

Outros temas são permitidos desde que o professor aprove o escopo e os dados sejam seguros e fictícios.

---

## 3. Definição do problema

Antes de implementar, preencha:

```markdown
# Visão do projeto

## Problema

## Público-alvo

## Objetivo

## Funcionalidades obrigatórias

## Funcionalidades opcionais

## Fora do escopo

## Critérios de sucesso
```

### Exemplo de história de usuário

```text
Como responsável por uma turma,
quero cadastrar notas de alunos,
para consultar médias e situações acadêmicas.
```

### Critérios de aceite

```text
- matrícula não pode ser repetida;
- notas devem estar entre 0 e 10;
- média deve mostrar duas casas;
- busca deve informar quando o aluno não existe;
- sistema não deve encerrar com texto em um campo numérico.
```

Critérios verificáveis ajudam implementação, testes e apresentação.

---

## 4. Produto mínimo viável

Defina três níveis:

### Obrigatório

Fluxo mínimo que resolve o problema.

### Desejável

Melhorias importantes, feitas somente depois do obrigatório funcionar.

### Futuro

Ideias que não serão implementadas nesta entrega.

Exemplo:

| Prioridade | Funcionalidade |
| --- | --- |
| obrigatória | cadastrar, listar e buscar alunos |
| obrigatória | registrar notas e calcular situação |
| desejável | editar dados |
| desejável | ranking por média |
| futura | interface gráfica e banco de dados |

Evite ampliar o escopo durante a aula. Primeiro conclua e teste o produto mínimo.

---

## 5. Organização sugerida

```text
projeto_final/
├── .gitignore
├── README.md
├── main.py
├── modelos/
│   ├── __init__.py
│   ├── aluno.py
│   └── turma.py
├── servicos/
│   ├── __init__.py
│   └── relatorios.py
├── utilitarios/
│   ├── __init__.py
│   └── validacoes.py
└── testes/
    └── test_regras.py
```

Essa estrutura é apenas referência. Projetos pequenos podem usar menos arquivos. Cada módulo deve possuir uma responsabilidade compreensível.

### Separação recomendada

- interface: entrada, menu e mensagens;
- domínio: entidades e regras centrais;
- serviços: operações que combinam entidades;
- validações: conversão e regras de entrada;
- testes: cenários verificáveis.

---

## 6. Fluxo Git da equipe

Branch principal deve manter a versão integrada. Mudanças relevantes podem usar branches:

```text
feature/cadastro
feature/relatorio
fix/validacao
docs/readme
```

Ciclo:

```text
escolher tarefa → criar branch → implementar → testar → revisar diff → commit → integrar
```

Antes de integrar:

- confirme o escopo;
- execute os testes;
- remova mensagens de debugging;
- confira dados e segredos;
- revise os arquivos alterados;
- atualize documentação relevante.

### Divisão de responsabilidades

Em equipe, todos devem compreender o projeto completo. Dividir tarefas não significa isolar conhecimento. Faça revisões cruzadas e pequenas integrações frequentes.

---

## 7. Requisitos técnicos mínimos

O projeto deve conter:

- menu ou fluxo de interação compreensível;
- pelo menos três funcionalidades relacionadas ao problema;
- condicionais e repetição;
- uma ou mais coleções;
- funções com parâmetros e retornos;
- módulos organizados;
- classes quando agregarem clareza;
- validação de entradas;
- tratamento de exceções esperadas;
- dados fictícios;
- testes de regras centrais;
- README;
- histórico Git com commits coerentes.

Não serão aceitos como completos:

- código que não executa;
- projeto copiado que a equipe não explica;
- credenciais ou dados pessoais no repositório;
- uma única função contendo todo o sistema;
- histórico com apenas um commit final sem justificativa;
- saída previamente escrita que simula funcionalidades inexistentes.

---

## 8. Plano de testes

Crie uma tabela antes da demonstração:

| ID | Funcionalidade | Entrada | Resultado esperado | Resultado obtido | Estado |
| --- | --- | --- | --- | --- | --- |
| T01 | cadastro | dados válidos | item cadastrado |  |  |
| T02 | cadastro | identificador repetido | operação recusada |  |  |
| T03 | valor numérico | texto inválido | nova solicitação |  |  |
| T04 | busca | item existente | dados exibidos |  |  |
| T05 | busca | item ausente | mensagem específica |  |  |
| T06 | resumo | coleção vazia | sem divisão por zero |  |  |

Inclua:

- caminho principal;
- limites;
- entrada vazia;
- texto no lugar de número;
- identificador duplicado;
- item ausente;
- coleção vazia;
- estado após alteração e remoção.

### Testes automatizados simples

```python
def test_calcular_media():
    assert calcular_media([8, 6]) == 7


def test_situacao_limites():
    assert definir_situacao(7) == "Aprovado"
    assert definir_situacao(6.9) == "Recuperação"
    assert definir_situacao(4) == "Recuperação"
    assert definir_situacao(3.9) == "Reprovado"
```

Adapte ao projeto. Testes devem validar resultados, não apenas executar linhas.

---

## 9. Revisão de qualidade

### Funcionalidade

- todos os requisitos obrigatórios funcionam?
- mensagens correspondem ao resultado real?
- estado permanece consistente depois das operações?

### Código

- nomes comunicam intenção?
- funções e métodos têm foco?
- regras não estão duplicadas?
- módulos possuem responsabilidades claras?
- existem números mágicos importantes?

### Resiliência

- entradas inválidas são tratadas?
- coleções vazias funcionam?
- busca ausente é prevista?
- exceções específicas são usadas?

### Segurança e privacidade

- há senha, token ou chave?
- há dados pessoais reais?
- `.env`, ambientes virtuais e arquivos temporários estão ignorados?
- comandos e dependências são necessários e conhecidos?

### Entrega

- README corresponde ao projeto atual?
- instruções foram testadas em um terminal novo?
- histórico é compreensível?
- versão final está na branch correta?

---

## 10. README obrigatório

```markdown
# Nome do projeto

Descrição breve do problema e da solução.

## Funcionalidades

## Tecnologias e requisitos

## Como executar

## Como testar

## Estrutura do projeto

## Exemplos de uso

## Decisões e limitações

## Uso de IA

## Autores
```

Em “Uso de IA”, informe se houve uso, sua finalidade e como o conteúdo foi verificado. Se não houve, declare isso brevemente.

---

## 11. Uso responsável de IA no projeto

Se a equipe utilizar IA:

- não envie dados sensíveis;
- limite o escopo de cada solicitação;
- compreenda todas as mudanças;
- execute testes próprios;
- revise `git diff`;
- registre decisões aceitas e rejeitadas;
- não atribua à IA autoria ou responsabilidade pela entrega.

A apresentação pode incluir:

- um exemplo em que a IA ajudou;
- um erro ou sugestão inadequada detectada;
- como a equipe verificou o resultado.

---

## 12. Roteiro das últimas horas

### Bloco 1 — estabilizar

- congelar novas ideias;
- concluir fluxo obrigatório;
- eliminar erros que impedem execução;
- integrar branches essenciais.

### Bloco 2 — verificar

- executar tabela de testes;
- corrigir defeitos por prioridade;
- realizar testes de regressão;
- revisar código e segurança.

### Bloco 3 — entregar

- atualizar README;
- conferir `.gitignore`;
- revisar histórico;
- criar commit ou versão de entrega;
- preparar dados fictícios da demonstração.

### Bloco 4 — apresentar

- ensaiar o roteiro;
- definir quem apresenta cada parte;
- preparar alternativa caso uma entrada falhe;
- controlar o tempo.

---

## 13. Apresentação final

Tempo sugerido: cinco a oito minutos por equipe, ajustado ao tamanho da turma.

### Roteiro

1. problema e público;
2. funcionalidades entregues;
3. demonstração do fluxo principal;
4. estrutura técnica;
5. tratamento de um caso inválido;
6. testes realizados;
7. uso de Git e IA;
8. limitação e próximo passo.

### Boas práticas

- use dados já preparados e fictícios;
- demonstre o sistema real;
- não leia todo o código;
- explique uma decisão técnica relevante;
- mostre uma validação ou teste;
- reconheça limitações sem inventar funcionalidade;
- respeite o tempo.

### Plano alternativo

Tenha capturas ou uma saída de exemplo apenas como apoio caso haja problema no ambiente, sem apresentá-las como execução ao vivo.

---

## 14. Desafio final

### Fase 1 — planejamento

- [ ] problema definido;
- [ ] público identificado;
- [ ] funcionalidades obrigatórias escolhidas;
- [ ] itens fora do escopo registrados;
- [ ] critérios de aceite escritos;
- [ ] tarefas distribuídas.

### Fase 2 — implementação

- [ ] fluxo principal completo;
- [ ] regras centrais implementadas;
- [ ] validações funcionando;
- [ ] módulos ou classes organizados;
- [ ] branches integradas;
- [ ] nenhum segredo incluído.

### Fase 3 — verificação

- [ ] testes do caminho principal;
- [ ] testes de limites;
- [ ] entradas inválidas;
- [ ] busca ausente;
- [ ] coleção vazia;
- [ ] regressão após correções;
- [ ] revisão do diff final.

### Fase 4 — entrega

- [ ] README completo;
- [ ] instruções testadas;
- [ ] `.gitignore` correto;
- [ ] histórico compreensível;
- [ ] branch principal funcional;
- [ ] repositório publicado ou entregue conforme orientação;
- [ ] apresentação ensaiada.

---

## 15. Rubrica de avaliação

| Critério | Pontos | Evidência |
| --- | ---: | --- |
| Funcionalidade | 2,0 | requisitos obrigatórios funcionam |
| Lógica e dados | 1,5 | regras e coleções estão corretas |
| Organização | 1,0 | funções, módulos e classes são coerentes |
| Resiliência | 1,0 | entradas e falhas esperadas são tratadas |
| Testes | 1,0 | casos principais, limites e regressões |
| Git e histórico | 1,0 | commits e branches demonstram evolução |
| Documentação | 1,0 | README permite compreender e executar |
| Apresentação e domínio | 1,0 | equipe demonstra e explica decisões |
| Uso responsável de IA | 0,5 | transparência e verificação, se aplicável |
| **Total** | **10,0** |  |

O uso de IA não é pontuado pela quantidade de conteúdo gerado. Avalia-se responsabilidade, compreensão e verificação. Se não houver uso, o critério pode ser incorporado ao domínio técnico conforme orientação do professor.

---

## 16. Perguntas para a banca ou turma

- Qual problema o projeto resolve?
- Por que essa estrutura de dados foi escolhida?
- Onde estão as regras centrais?
- Como o sistema reage a entrada inválida?
- Qual foi o defeito mais difícil?
- Que teste protege essa correção?
- Como o trabalho foi dividido?
- O que o histórico Git revela?
- Qual limitação seria resolvida primeiro?
- Que trecho cada integrante consegue explicar?

---

## 17. Retrospectiva

Depois das apresentações, cada equipe responde:

### Continuar

O que funcionou bem e deve ser mantido?

### Parar

O que gerou retrabalho ou risco?

### Começar

Que prática será adotada no próximo projeto?

Reflexão individual:

- qual conceito domino melhor agora?
- qual conceito preciso praticar?
- qual contribuição concreta fiz?
- qual decisão técnica mudaria?
- qual será meu próximo projeto pequeno?

---

## 18. Erros comuns na entrega

- começar uma funcionalidade grande no fim;
- deixar testes para depois da implementação inteira;
- demonstrar com dados pessoais;
- ter README diferente do comportamento atual;
- ignorar falhas porque “na apresentação não acontecerão”;
- misturar todas as alterações em um commit;
- publicar segredos ou arquivos locais;
- incluir bibliotecas que ninguém da equipe compreende;
- apresentar código gerado que ninguém explica;
- esconder limitações em vez de documentá-las.

---

## 19. Encerramento do curso

Ao concluir as dez aulas, o aluno percorreu um ciclo completo:

```text
problema
  → lógica
  → decisões
  → repetições
  → coleções
  → funções
  → objetos
  → versionamento
  → tratamento de erros
  → apoio responsável de IA
  → produto testado e apresentado
```

O próximo passo não é memorizar mais comandos, mas construir projetos pequenos, ler código, testar hipóteses e melhorar continuamente. Um bom portfólio nasce de aplicações que funcionam, têm documentação clara e mostram evolução real.

## Entrega final

Entregue conforme orientação do professor:

- link do repositório ou arquivo preservando o histórico Git;
- README atualizado;
- código-fonte;
- testes ou tabela de testes preenchida;
- registro de uso de IA, quando aplicável;
- identificação dos integrantes;
- breve lista de limitações e próximos passos.
