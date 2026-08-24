# Aula 7 — Git, GitHub e qualidade de código

**Duração:** 4 horas  
**Tema:** controle de versão, commits, branches, colaboração e código limpo  
**Produto da aula:** projeto Python versionado, documentado e organizado

## Objetivos de aprendizagem

Ao final desta aula, o aluno deverá ser capaz de:

- explicar o propósito de um sistema de controle de versão;
- diferenciar Git e GitHub;
- criar e verificar um repositório Git;
- compreender os estados dos arquivos;
- preparar alterações e criar commits;
- escrever mensagens de commit claras;
- consultar o histórico e comparar alterações;
- criar, alternar e integrar branches;
- reconhecer conflitos e compreender sua resolução;
- publicar um projeto no GitHub, quando houver conta e internet;
- criar um `.gitignore` adequado para Python;
- organizar um README de projeto;
- identificar problemas básicos de legibilidade e manutenção;
- refatorar código com mudanças pequenas e verificáveis.

## Conhecimentos necessários

- arquivos e pastas;
- execução de programas Python no terminal;
- funções, módulos e classes;
- projeto acadêmico desenvolvido nas aulas anteriores.

## Recursos necessários

- Git instalado;
- Python 3;
- editor de código com terminal;
- projeto da Aula 6 ou um projeto Python equivalente;
- conta no GitHub e internet apenas para a etapa opcional de publicação.

## Antes da aula

### Preparação do professor

- Confirmar a instalação do Git:

```bash
git --version
```

- Preparar uma cópia de segurança do projeto usado na demonstração.
- Evitar demonstrar comandos destrutivos neste primeiro contato.
- Criar um repositório remoto vazio para a demonstração opcional.
- Não expor tokens, senhas, chaves ou endereços particulares no projetor.
- Preparar um pequeno conflito em arquivos de exemplo.

### Configuração inicial do Git

Em computadores pessoais, o aluno pode configurar nome e e-mail:

```bash
git config --global user.name "Nome do Aluno"
git config --global user.email "email@exemplo.com"
```

Em laboratório compartilhado, prefira a configuração apenas no repositório:

```bash
git config user.name "Nome do Aluno"
git config user.email "email@exemplo.com"
```

Verificação:

```bash
git config --list
```

> Não é necessário informar a senha do GitHub nesses comandos. O e-mail fica registrado como autoria dos commits.

## Cronograma da aula

| Tempo | Etapa | Conteúdo e atividade |
| --- | --- | --- |
| 00:00–00:20 | Introdução | problema, versões e diferença entre Git e GitHub |
| 00:20–01:00 | Fluxo básico | `init`, `status`, `add`, `commit`, `log` e `diff` |
| 01:00–01:25 | Boas práticas | commits pequenos, mensagens e `.gitignore` |
| 01:25–01:45 | Branches | criação, alternância e integração |
| 01:45–01:55 | Intervalo | pausa de 10 minutos |
| 01:55–02:20 | Remoto | GitHub, `remote`, `push`, `pull` e `clone` |
| 02:20–02:40 | Colaboração | conflito, revisão e pull request conceitual |
| 02:40–03:10 | Código limpo | nomes, funções, duplicação e organização |
| 03:10–03:50 | Desafio principal | versionar e refatorar o sistema acadêmico |
| 03:50–04:00 | Fechamento | revisão, avaliação e tarefa |

---

## 1. Por que controle de versão?

Sem controle de versão, projetos costumam terminar assim:

```text
projeto.py
projeto_final.py
projeto_final_agora_vai.py
projeto_final_corrigido_2.py
```

Esse método não informa claramente:

- o que mudou;
- quem alterou;
- quando e por que a mudança aconteceu;
- qual versão funciona;
- como combinar o trabalho de várias pessoas.

Um sistema de controle de versão registra a evolução do projeto. Cada registro importante é um **commit**.

### Git e GitHub não são a mesma coisa

| Git | GitHub |
| --- | --- |
| programa de controle de versão | serviço de hospedagem e colaboração |
| funciona localmente | normalmente exige internet |
| registra commits e branches | armazena repositórios remotos |
| não exige conta | exige conta para publicar em nome próprio |

É possível utilizar Git sem GitHub. GitHub complementa o fluxo com compartilhamento, revisão e colaboração.

### Conceitos principais

| Conceito | Significado |
| --- | --- |
| repositório | pasta cujo histórico é controlado pelo Git |
| commit | registro identificado de um conjunto de alterações |
| branch | linha de desenvolvimento |
| repositório remoto | cópia hospedada em outro local |
| clone | cópia local de um repositório remoto |
| push | envio de commits locais ao remoto |
| pull | recebimento e integração de alterações remotas |

---

## 2. Criando um repositório

Abra o terminal dentro da pasta do projeto e confira o local atual antes de continuar.

Inicialize:

```bash
git init
```

Consulte o estado:

```bash
git status
```

O Git passa a acompanhar a pasta, mas ainda não registra automaticamente os arquivos.

### Os três estados do fluxo básico

```text
Pasta de trabalho  -- git add -->  Área de preparação  -- git commit -->  Histórico
```

- **pasta de trabalho:** arquivos que estamos editando;
- **área de preparação:** alterações escolhidas para o próximo commit;
- **histórico:** commits já registrados.

### Primeiro commit

```bash
git status
git add README.md
git status
git commit -m "docs: adiciona apresentação do projeto"
```

Para preparar todos os arquivos apropriados da pasta atual:

```bash
git add .
```

Antes desse comando, confira o `git status` e o `.gitignore`. Assim, arquivos temporários ou sensíveis não serão incluídos por engano.

---

## 3. Inspecionando alterações e histórico

### git status

Use frequentemente:

```bash
git status
```

Ele informa arquivos novos, alterados e preparados.

### git diff

Mostra alterações ainda não preparadas:

```bash
git diff
```

Mostra alterações que já estão na área de preparação:

```bash
git diff --staged
```

### git log

```bash
git log
```

Versão compacta:

```bash
git log --oneline
```

Histórico com representação de branches:

```bash
git log --oneline --graph --decorate --all
```

### Roteiro de trabalho seguro

Repita este ciclo:

```text
editar → testar → status → diff → add → diff --staged → commit
```

O commit deve registrar uma unidade de trabalho compreensível e funcional.

---

## 4. Bons commits

Um bom commit é:

- pequeno o suficiente para ser compreendido;
- focado em uma mudança relacionada;
- testado antes do registro;
- descrito por uma mensagem clara.

Mensagens pouco úteis:

```text
alterações
teste
coisas
agora vai
```

Mensagens melhores:

```text
feat: adiciona cadastro de alunos
fix: impede matrícula duplicada
docs: explica como executar o projeto
refactor: extrai validação de notas
test: adiciona cenários para cálculo de média
```

Os prefixos são uma convenção possível, não uma exigência do Git:

| Prefixo | Tipo de alteração |
| --- | --- |
| `feat` | funcionalidade |
| `fix` | correção |
| `docs` | documentação |
| `refactor` | reorganização sem mudança intencional de comportamento |
| `test` | testes |
| `style` | formatação sem alteração da lógica |

### Um assunto por commit

Evite misturar no mesmo commit:

- nova funcionalidade;
- correção não relacionada;
- renomeação de vários arquivos;
- reformatação geral.

Separar facilita revisão e investigação de problemas.

---

## 5. Ignorando arquivos

O arquivo `.gitignore` lista arquivos que não devem ser rastreados.

Exemplo para projetos Python:

```gitignore
__pycache__/
*.py[cod]
.venv/
venv/
.env
.vscode/
.idea/
```

Avalie os itens conforme o projeto. Configurações compartilhadas do editor podem ser úteis em alguns times.

### Nunca publique segredos

Não envie ao repositório:

- senhas;
- tokens de acesso;
- chaves de API;
- arquivos `.env` com credenciais;
- dados pessoais ou acadêmicos reais;
- chaves privadas.

Adicionar um segredo ao `.gitignore` depois do commit não o remove do histórico anterior. Se ocorrer exposição, a credencial deve ser revogada e substituída.

### Arquivo já rastreado

O `.gitignore` atua principalmente sobre arquivos ainda não rastreados. Não execute comandos de remoção sem compreender o efeito. Nesta aula, peça auxílio ao professor caso um arquivo sensível já tenha sido incluído.

---

## 6. Branches

Uma branch permite desenvolver uma mudança sem misturá-la imediatamente à linha principal.

```text
main:       A---B-----------E
                 \         /
melhoria-menu:    C---D----
```

Consulte as branches:

```bash
git branch
```

Crie e alterne para uma nova branch:

```bash
git switch -c melhoria-menu
```

Faça a mudança, teste e registre:

```bash
git add .
git commit -m "refactor: organiza opções do menu"
```

Volte à principal:

```bash
git switch main
```

Integre a branch:

```bash
git merge melhoria-menu
```

### Antes de alternar

Consulte `git status`. Alterações não registradas podem acompanhar a troca ou impedir a operação. Para iniciantes, o fluxo mais claro é concluir ou registrar uma unidade coerente antes de mudar de branch.

### Nomes úteis

```text
feature/cadastro-aluno
fix/validacao-nota
refactor/classe-turma
docs/instrucoes-execucao
```

Adote a convenção acordada pela equipe.

---

## 7. Conflitos

Um conflito pode ocorrer quando o Git não consegue combinar automaticamente alterações feitas na mesma região.

O arquivo pode apresentar marcadores:

```text
<<<<<<< HEAD
versão da branch atual
=======
versão da outra branch
>>>>>>> nome-da-branch
```

Para resolver:

1. leia as duas versões;
2. decida o conteúdo final correto;
3. remova todos os marcadores;
4. salve e teste o programa;
5. use `git add` no arquivo resolvido;
6. conclua o commit de integração quando solicitado.

Não escolha uma versão automaticamente sem entender a regra do programa. Às vezes, a solução correta combina partes das duas.

Verifique se não restaram marcadores:

```bash
git status
```

Também procure por `<<<<<<<`, `=======` e `>>>>>>>` no projeto.

---

## 8. Repositório remoto e GitHub

Esta etapa é opcional quando não houver conta ou internet. Todo o aprendizado de Git local continua válido.

### Publicando um repositório existente

Crie no GitHub um repositório vazio e copie a URL apresentada. Depois:

```bash
git remote add origin URL_DO_REPOSITORIO
git remote -v
git push -u origin main
```

Não copie literalmente `URL_DO_REPOSITORIO`; substitua pela URL correta.

### Clonando

```bash
git clone URL_DO_REPOSITORIO
```

O comando cria uma pasta com os arquivos e o histórico.

### Enviando e recebendo

```bash
git push
git pull
```

Antes de iniciar trabalho colaborativo, atualize sua branch e verifique o estado local.

### Autenticação

O método depende da configuração do computador e do serviço. Não compartilhe tokens nem digite credenciais em código, README ou mensagens de commit. Em laboratório, encerre a sessão ao terminar.

---

## 9. Pull request e revisão

Uma *pull request* propõe integrar alterações de uma branch em outra. Fluxo conceitual:

```text
criar branch → implementar → testar → commits → push → abrir PR → revisar → integrar
```

Uma descrição útil informa:

- qual problema foi resolvido;
- o que mudou;
- como testar;
- limitações ou decisões importantes.

Checklist de revisão:

- o comportamento solicitado funciona?
- os nomes são compreensíveis?
- existe duplicação desnecessária?
- erros e entradas inválidas foram considerados?
- há segredos ou dados pessoais?
- documentação e testes foram atualizados?
- a mudança está focada?

Revisar código não é avaliar a pessoa. Comentários devem ser específicos, respeitosos e voltados ao resultado técnico.

---

## 10. README de projeto

Um README ajuda outra pessoa a compreender e executar o projeto.

Estrutura mínima:

````markdown
# Sistema Acadêmico

Breve descrição do projeto.

## Funcionalidades

- cadastrar alunos;
- adicionar notas;
- consultar situação;
- exibir resumo da turma.

## Requisitos

- Python 3

## Como executar

```bash
python main.py
```

## Estrutura

Descrição dos módulos principais.

## Autores

Nomes dos integrantes.
````

Use dados fictícios nos exemplos e mantenha as instruções compatíveis com o projeto atual.

---

## 11. O que é código limpo?

Código limpo comunica sua intenção, reduz esforço de manutenção e torna erros mais visíveis. Não significa escrever o menor número de linhas.

### Nomes claros

Evite:

```python
x = 0
for a in alunos:
    x += a.calcular_media()
```

Prefira:

```python
soma_das_medias = 0

for aluno in alunos:
    soma_das_medias += aluno.calcular_media()
```

### Funções pequenas e focadas

Evite uma função que lê dados, calcula, modifica coleções e imprime relatório ao mesmo tempo. Separe responsabilidades quando isso tornar o fluxo mais claro.

### Evite repetição de regras

Se aprovação é definida em vários lugares, uma alteração poderá deixar o sistema inconsistente. Mantenha a regra em um único método ou função.

### Constantes para valores importantes

```python
MEDIA_APROVACAO = 7
MEDIA_RECUPERACAO = 4


def definir_situacao(media):
    if media >= MEDIA_APROVACAO:
        return "Aprovado"
    if media >= MEDIA_RECUPERACAO:
        return "Recuperação"
    return "Reprovado"
```

### Comentários explicam o porquê

Evite comentário que apenas repete o código:

```python
# Soma um ao contador.
contador += 1
```

Um comentário é útil quando registra uma decisão não óbvia:

```python
# Alunos sem avaliação não entram na média geral da turma.
if media is not None:
    medias.append(media)
```

### Formatação consistente

- use quatro espaços para indentação;
- mantenha linhas e blocos legíveis;
- separe funções e classes;
- remova código comentado que não tem utilidade;
- mantenha imports organizados;
- siga o padrão já adotado pelo projeto.

---

## 12. Refatoração segura

Refatorar é melhorar a estrutura interna sem alterar intencionalmente o comportamento externo.

Fluxo recomendado:

1. execute e compreenda o comportamento atual;
2. escolha um problema pequeno;
3. registre ou preserve testes de exemplo;
4. faça uma alteração focada;
5. execute os testes novamente;
6. revise o `diff`;
7. crie um commit descritivo.

Exemplo:

```python
# Antes
if media >= 7:
    return "Aprovado"
elif media >= 4:
    return "Recuperação"
else:
    return "Reprovado"
```

```python
# Depois
if media >= MEDIA_APROVACAO:
    return "Aprovado"
if media >= MEDIA_RECUPERACAO:
    return "Recuperação"
return "Reprovado"
```

A segunda versão elimina `else` depois de retornos e nomeia os limites. Confirme com testes nos valores `3.9`, `4`, `6.9` e `7`.

---

## 13. Prática guiada — histórico de uma melhoria

Use uma cópia do projeto acadêmico da Aula 6.

### Etapa 1 — iniciar

```bash
git init
git status
```

Crie `.gitignore` e `README.md`. Faça o primeiro commit:

```bash
git add .
git diff --staged
git commit -m "chore: inicia sistema acadêmico"
```

### Etapa 2 — documentar

Complete o README com funcionalidades e execução:

```bash
git add README.md
git commit -m "docs: adiciona instruções de execução"
```

### Etapa 3 — criar branch

```bash
git switch -c refactor/regras-academicas
```

Extraia os valores 7 e 4 para constantes, teste e registre:

```bash
git diff
git add .
git commit -m "refactor: nomeia limites acadêmicos"
```

### Etapa 4 — integrar

```bash
git switch main
git merge refactor/regras-academicas
git log --oneline --graph --decorate --all
```

Ao final, peça que o aluno explique o propósito de cada commit olhando apenas o histórico.

---

## 14. Desafio principal — versionar e melhorar o projeto

Trabalhe sobre uma cópia do sistema acadêmico da Aula 6.

### Entregas obrigatórias

O projeto deve possuir:

```text
sistema_academico/
├── .gitignore
├── README.md
├── main.py
├── aluno.py
├── turma.py
└── validacoes.py
```

O histórico deve demonstrar pelo menos:

1. início do projeto;
2. documentação;
3. uma refatoração de qualidade;
4. uma funcionalidade ou correção;
5. integração de uma branch.

### Melhorias de código

Escolha pelo menos quatro:

- substituir nomes vagos;
- extrair números importantes para constantes;
- remover duplicação;
- dividir uma função grande;
- separar entrada e regra de negócio;
- adicionar docstrings úteis;
- organizar imports;
- remover código morto ou comentários obsoletos;
- tratar lista vazia;
- melhorar mensagens ao usuário.

### Funcionalidade na branch

Crie uma branch para implementar uma destas opções:

- editar nome de aluno;
- remover uma nota;
- listar alunos por situação;
- mostrar aluno com maior média;
- calcular percentual de aprovação.

Teste antes de integrar.

### Plano de commits sugerido

```text
chore: inicia sistema acadêmico
docs: documenta instalação e uso
refactor: centraliza limites acadêmicos
refactor: separa apresentação do resumo
feat: adiciona filtro por situação
```

Não copie as mensagens se não corresponderem ao que realmente foi alterado.

### Casos de teste

- projeto inicia sem erros;
- cadastro aceita dados válidos;
- nota inválida é recusada;
- matrícula duplicada é recusada;
- busca existente e ausente funciona;
- média e situação permanecem corretas;
- nova funcionalidade funciona nos limites;
- comportamento anterior continua funcionando depois do merge.

### Checklist Git

- [ ] O repositório foi iniciado na pasta correta.
- [ ] `git status` não mostra segredos nem arquivos temporários preparados.
- [ ] O `.gitignore` cobre arquivos locais apropriados.
- [ ] Cada commit possui uma mudança coerente.
- [ ] As mensagens descrevem o conteúdo real.
- [ ] Uma branch foi criada e utilizada.
- [ ] A branch foi integrada à principal.
- [ ] O histórico pode ser compreendido com `git log --oneline`.
- [ ] O estado final está limpo.

### Checklist de qualidade

- [ ] Nomes comunicam intenção.
- [ ] Funções e métodos possuem responsabilidade clara.
- [ ] Regras importantes não estão duplicadas.
- [ ] Constantes substituem números mágicos relevantes.
- [ ] Comentários explicam decisões, não sintaxe óbvia.
- [ ] README explica como executar.
- [ ] Não existem credenciais ou dados pessoais.
- [ ] O sistema foi testado depois da refatoração.

### Publicação opcional

Se houver GitHub disponível:

- crie um repositório remoto;
- conecte com `git remote add origin`;
- envie a branch principal;
- publique também a branch da funcionalidade antes de integrá-la;
- abra uma pull request;
- peça revisão de um colega;
- integre somente após verificar o código.

### Extensões

- Crie uma *issue* descrevendo uma melhoria futura.
- Use um template simples na descrição da pull request.
- Marque uma versão inicial com tag depois da entrega.
- Adicione uma licença apenas depois de discutir sua finalidade.

---

## 15. Exercícios de fixação

### Exercício 1 — sequência de commits

Crie um projeto pequeno e faça três alterações independentes, cada uma em seu próprio commit. Explique por que essa divisão é melhor que um commit único.

### Exercício 2 — leitura de histórico

Troque o computador com um colega e tente explicar a evolução do projeto usando apenas `git log --oneline` e `git diff`.

### Exercício 3 — branch de documentação

Crie `docs/melhora-readme`, amplie a documentação e integre à branch principal.

### Exercício 4 — conflito controlado

Com orientação do professor, altere a mesma linha em duas branches, tente integrá-las e resolva o conflito preservando a intenção correta.

### Exercício 5 — revisão de código

Revise um módulo e identifique nomes vagos, duplicações, funções grandes, números mágicos e comentários desnecessários. Registre cada melhoria proposta.

### Exercício 6 — refatoração incremental

Faça três pequenas refatorações, executando o programa e criando um commit após cada uma.

---

## 16. Erros comuns

### Iniciar o repositório na pasta errada

Confira a pasta atual e os arquivos exibidos antes de `git init`.

### Usar git add sem revisar

Consulte `git status`, mantenha `.gitignore` e confira `git diff --staged`.

### Commitar segredo

Nunca use o repositório para guardar credenciais. Se ocorrer, avise imediatamente e revogue a credencial.

### Mensagem que não explica a mudança

Descreva a intenção, não apenas “arquivos alterados”.

### Misturar várias mudanças

Commits menores facilitam revisão, mas não devem dividir uma única mudança em pedaços que não funcionam.

### Trabalhar muito tempo sem commit

Registre unidades completas e testadas ao longo do desenvolvimento.

### Integrar sem testar

Execute o comportamento relevante antes e depois do merge.

### Resolver conflito apagando marcadores sem compreender

Primeiro defina o conteúdo correto. Depois remova os marcadores e teste.

### Refatorar e adicionar funcionalidade ao mesmo tempo

Quando possível, separe as mudanças para deixar o histórico e a revisão mais claros.

---

## 17. Referência rápida de comandos

| Comando | Finalidade |
| --- | --- |
| `git init` | inicia um repositório |
| `git status` | mostra o estado dos arquivos |
| `git add arquivo` | prepara um arquivo |
| `git add .` | prepara alterações apropriadas da pasta atual |
| `git diff` | mostra alterações não preparadas |
| `git diff --staged` | mostra o que entrará no commit |
| `git commit -m "mensagem"` | cria um commit |
| `git log --oneline` | exibe histórico resumido |
| `git branch` | lista branches |
| `git switch -c nome` | cria e acessa uma branch |
| `git switch nome` | muda de branch |
| `git merge nome` | integra uma branch à atual |
| `git remote -v` | lista remotos configurados |
| `git clone URL` | clona um repositório |
| `git push` | envia commits ao remoto |
| `git pull` | recebe e integra alterações remotas |

Não memorize tudo de uma vez. Aprenda o ciclo principal e consulte a referência conforme necessário.

---

## 18. Fechamento da aula

### Revisão oral

1. Qual é a diferença entre Git e GitHub?
2. O que um commit representa?
3. Qual é a função da área de preparação?
4. Para que servem `status` e `diff`?
5. O que caracteriza uma boa mensagem de commit?
6. Para que serve `.gitignore`?
7. Por que segredos não devem ser versionados?
8. O que é uma branch?
9. Quando ocorre um conflito?
10. O que é uma pull request?
11. O que é refatoração?
12. Como Git contribui para uma refatoração segura?

### Bilhete de saída

Cada aluno deve registrar:

- um benefício do controle de versão;
- uma mensagem de commit adequada;
- um arquivo que deve ser ignorado;
- uma melhoria de qualidade aplicada ao projeto.

### Critérios de avaliação formativa

| Critério | Evidência esperada |
| --- | --- |
| Fluxo Git | usa `status`, `add`, `diff` e `commit` conscientemente |
| Histórico | produz commits focados e compreensíveis |
| Branches | desenvolve e integra uma mudança isolada |
| Segurança | exclui segredos e arquivos locais inadequados |
| Documentação | entrega README suficiente para executar o projeto |
| Código limpo | melhora nomes, responsabilidades e duplicações |
| Refatoração | preserva o comportamento e testa incrementalmente |
| Colaboração | comunica mudanças e revisa com respeito |

Sugestão de pontuação para o desafio: 3 pontos para fluxo e histórico Git, 1 para branch e integração, 1 para segurança, 1 para README, 3 para qualidade da refatoração e 1 para testes.

## Tarefa para casa

Finalize o desafio, revise o histórico e entregue o repositório conforme orientação do professor. Se a publicação no GitHub não for possível, compacte a pasta preservando o diretório oculto `.git` ou apresente o histórico local em sala.

## Ponte para a Aula 8

Nesta aula, organizamos e versionamos o código. Na Aula 8, usaremos esse histórico como proteção para depurar, tratar exceções e refatorar com mais segurança. Estudaremos `try`, `except`, `else`, `finally`, mensagens de erro e estratégias sistemáticas para localizar defeitos.
