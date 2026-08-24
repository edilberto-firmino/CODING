# Aula 9 — Inteligência artificial aplicada à programação

**Duração:** 4 horas  
**Tema:** geração, explicação, debugging, testes e auditoria de código com IA  
**Produto da aula:** melhoria auditada do sistema acadêmico com registro das interações com IA

## Objetivos de aprendizagem

Ao final desta aula, o aluno deverá ser capaz de:

- explicar benefícios e limites da IA na programação;
- fornecer contexto e critérios claros em um prompt;
- solicitar explicações adequadas ao próprio nível;
- decompor tarefas grandes antes de pedir código;
- verificar código gerado por leitura, execução e testes;
- usar IA para propor hipóteses de debugging;
- solicitar casos de teste e revisar sua cobertura;
- auditar segurança, privacidade e qualidade;
- reconhecer respostas plausíveis, porém incorretas;
- registrar autoria, decisões e uso de IA com transparência.

## Princípio central

```text
IA propõe; o programador compreende, verifica e decide.
```

Não entregue código que você não consegue explicar. Nunca envie credenciais, dados pessoais, código confidencial ou informações acadêmicas reais a uma ferramenta de IA.

## Cronograma da aula

| Tempo | Etapa | Conteúdo e atividade |
| --- | --- | --- |
| 00:00–00:25 | Fundamentos | capacidades, limites e responsabilidade |
| 00:25–01:00 | Prompts | contexto, objetivo, restrições e formato |
| 01:00–01:30 | Explicação e geração | decomposição e exemplos pequenos |
| 01:30–01:45 | Verificação | leitura, execução, testes e diff |
| 01:45–01:55 | Intervalo | pausa de 10 minutos |
| 01:55–02:25 | Debugging com IA | evidências, hipóteses e reprodução |
| 02:25–02:55 | Auditoria | qualidade, segurança, privacidade e vieses |
| 02:55–03:15 | Prática comparativa | melhorar prompts e avaliar respostas |
| 03:15–03:50 | Desafio principal | melhoria assistida e auditada |
| 03:50–04:00 | Fechamento | reflexão e avaliação |

---

## 1. O que a IA pode fazer

Usos produtivos:

- explicar um trecho de código;
- sugerir uma decomposição;
- gerar um primeiro rascunho;
- propor nomes e documentação;
- levantar hipóteses para um erro;
- criar casos de teste;
- revisar legibilidade e riscos;
- comparar alternativas;
- ajudar a interpretar mensagens de erro.

Limitações:

- pode inventar funções, bibliotecas ou fatos;
- pode gerar código inseguro;
- pode não conhecer todo o contexto;
- pode corrigir o sintoma e preservar a causa;
- pode alterar comportamento durante refatoração;
- pode produzir testes que confirmam o próprio erro;
- não assume a responsabilidade da entrega.

Fluência textual não é evidência de correção.

---

## 2. Anatomia de um bom pedido

Um pedido útil costuma conter:

```text
Contexto + objetivo + código ou evidência + restrições + critérios + formato esperado
```

Pedido vago:

```text
Melhore meu código.
```

Pedido verificável:

```text
Este é um sistema acadêmico em Python para alunos iniciantes.
Refatore apenas o método obter_resumo da classe Turma.
Não altere o formato do dicionário retornado nem use bibliotecas externas.
Explique cada mudança e proponha testes para turma vazia, um aluno sem notas
e três alunos em situações diferentes. Não edite outros arquivos.
```

### Checklist antes de enviar

- Qual problema desejo resolver?
- Qual parte do código está no escopo?
- O que não pode mudar?
- Como saberei se a resposta funciona?
- Qual nível de explicação preciso?
- Existe informação sensível no conteúdo?

---

## 3. Pedindo explicações

Exemplo:

```text
Explique esta função para alguém que conhece listas e laços, mas está
aprendendo classes. Descreva parâmetros, retorno, fluxo e casos de borda.
Depois faça três perguntas de verificação. Não reescreva o código.
```

Boas variações:

- “simule a execução com estes valores”;
- “explique por que retorna `None`”;
- “compare as duas versões”;
- “aponte onde o estado do objeto muda”;
- “desenhe uma tabela de rastreamento”.

Depois da resposta, explique o código com suas próprias palavras e confirme no programa.

---

## 4. Geração de código em etapas

Evite pedir um sistema inteiro de uma vez. Trabalhe por unidades:

1. defina requisitos;
2. modele dados e responsabilidades;
3. escolha uma função ou classe;
4. peça implementação pequena;
5. leia e execute;
6. crie testes;
7. integre;
8. revise o `diff`;
9. faça commit.

Exemplo de sequência:

```text
1. Sugira contratos para os métodos, sem implementar.
2. Implemente apenas buscar_aluno conforme o contrato escolhido.
3. Gere casos de teste, incluindo matrícula ausente e duplicada.
4. Revise a implementação com base nos resultados apresentados.
```

Código menor é mais fácil de compreender e verificar.

---

## 5. Verificação obrigatória

Para qualquer código sugerido:

- leia linha por linha;
- confira imports e dependências;
- execute em ambiente controlado;
- teste fluxo normal e limites;
- compare com os requisitos;
- verifique entradas e saídas;
- analise segurança e privacidade;
- revise todas as mudanças com `git diff`;
- rejeite alterações fora do escopo.

### Perguntas de auditoria

1. A solução faz exatamente o que foi solicitado?
2. Há divisão por zero, índice ou chave inexistente?
3. Entradas inválidas são tratadas?
4. Existe `except` genérico escondendo falhas?
5. Algum segredo foi inserido no código?
6. A IA adicionou dependência desnecessária?
7. Os testes realmente poderiam falhar?
8. A refatoração mudou regras?
9. Consigo explicar cada linha alterada?

---

## 6. Debugging com IA

Forneça evidências, não apenas “não funciona”:

```text
Objetivo: calcular a média de duas notas.
Entrada: 8 e 6.
Esperado: 7.0.
Obtido: 11.0.
Código: media = nota_1 + nota_2 / 2
Explique a causa, proponha a menor correção e crie três testes de regressão.
Não refatore outras partes.
```

Fluxo:

```text
reproduzir → coletar evidências → pedir hipóteses → testar uma hipótese → corrigir → regressão
```

Não aceite uma lista de hipóteses como diagnóstico confirmado. Teste cada hipótese relevante.

### Mensagens de erro

Inclua:

- traceback completo necessário;
- trecho mínimo relacionado;
- entrada usada;
- versões relevantes;
- alterações recentes.

Remova caminhos, usuários, tokens e dados privados antes de compartilhar.

---

## 7. IA para testes

Prompt útil:

```text
Crie uma tabela de testes para definir_situacao(media), considerando os
limites 4 e 7. Inclua valores nos limites, imediatamente abaixo e acima,
além de valores inválidos. Para cada caso, informe o resultado esperado.
Não escreva a implementação.
```

Revise se os testes incluem:

- caminho comum;
- limites;
- coleção vazia;
- ausência de item;
- entrada inválida;
- estado antes e depois;
- defeitos corrigidos anteriormente.

Teste gerado por IA também pode estar errado. Calcule manualmente exemplos críticos.

---

## 8. Revisão e auditoria

Peça revisão com critérios específicos:

```text
Revise este módulo sem reescrevê-lo. Liste achados por prioridade:
correção, segurança, tratamento de erros, legibilidade e testes ausentes.
Para cada achado, cite o trecho, explique o impacto e proponha a menor
mudança. Se não houver evidência, declare a incerteza.
```

Classifique achados:

| Prioridade | Significado |
| --- | --- |
| alta | erro, perda de dados, vazamento ou regra incorreta |
| média | comportamento frágil ou manutenção difícil |
| baixa | melhoria de clareza ou consistência |

Uma auditoria útil distingue fato, hipótese e preferência de estilo.

---

## 9. Privacidade, segurança e autoria

Nunca compartilhe:

- senhas, tokens e chaves;
- `.env`;
- dados pessoais reais;
- históricos acadêmicos identificáveis;
- código proprietário sem autorização;
- documentos confidenciais.

Use exemplos fictícios e minimize o trecho enviado.

### Dependências e comandos

Antes de executar algo sugerido:

- compreenda a finalidade;
- confira caminhos e arquivos afetados;
- verifique se instala pacotes;
- desconfie de comandos destrutivos;
- não conceda privilégios sem necessidade;
- consulte documentação oficial para detalhes críticos.

### Transparência

Quando a instituição ou equipe exigir, registre:

- ferramenta utilizada;
- finalidade;
- partes influenciadas;
- verificações realizadas;
- decisões que você modificou ou rejeitou.

A responsabilidade pelo código entregue continua sendo do autor humano.

---

## 10. Prática guiada — comparar prompts

Use a mesma função problemática em três rodadas.

### Rodada 1

```text
Conserte isso.
```

### Rodada 2

Adicione objetivo, código e erro observado.

### Rodada 3

Adicione restrições, resultado esperado, casos de teste e pedido de explicação.

Compare:

- precisão;
- mudanças fora do escopo;
- clareza da explicação;
- qualidade dos testes;
- esforço necessário para verificar.

Conclusão esperada: mais contexto útil e critérios verificáveis tendem a produzir respostas mais aproveitáveis, mas não garantem correção.

---

## 11. Desafio principal — melhoria assistida e auditada

Use o sistema acadêmico da Aula 8. Crie:

```bash
git switch -c feature/melhoria-assistida
```

Escolha uma funcionalidade:

- editar notas;
- filtrar alunos por situação;
- ranking por média;
- relatório de frequência;
- exportação de resumo sem dados pessoais reais.

### Etapas obrigatórias

1. Escreva requisitos e critérios de aceite sem IA.
2. Peça à IA uma decomposição, ainda sem código.
3. Revise e ajuste o plano.
4. Solicite apenas uma unidade de implementação.
5. Leia e explique a resposta.
6. Solicite ou crie casos de teste.
7. Execute e registre os resultados.
8. Faça auditoria de qualidade, segurança e privacidade.
9. Revise `git diff` e remova mudanças indevidas.
10. Registre commits coerentes.

### Diário de uso da IA

Crie `USO_IA.md`:

```markdown
# Registro de uso de IA

## Objetivo

## Contexto fornecido

## Prompt principal

## Sugestões aceitas

## Sugestões rejeitadas e motivo

## Testes realizados

## Riscos verificados

## Decisão final do autor
```

Não inclua dados sensíveis nem uma transcrição desnecessariamente longa.

### Avaliação da resposta

| Critério | Pergunta |
| --- | --- |
| correção | os testes confirmam o comportamento? |
| aderência | respeitou escopo e restrições? |
| compreensão | o aluno explica todas as mudanças? |
| qualidade | reduziu ou aumentou complexidade? |
| segurança | introduziu risco ou segredo? |
| autoria | decisões humanas estão registradas? |

### Checklist

- [ ] Requisitos foram escritos antes da geração.
- [ ] Nenhum dado sensível foi enviado.
- [ ] A tarefa foi decomposta.
- [ ] Todo código aceito foi compreendido.
- [ ] Testes cobrem limites e falhas.
- [ ] O diff foi revisado.
- [ ] Sugestões inadequadas foram rejeitadas.
- [ ] O uso de IA foi documentado.
- [ ] O projeto continua executando.
- [ ] A branch possui commits claros.

---

## 12. Exercícios de fixação

1. Transforme três pedidos vagos em prompts verificáveis.
2. Solicite duas explicações do mesmo código para públicos diferentes e compare.
3. Dê à IA uma função com defeito, mas não revele a causa; avalie as hipóteses.
4. Solicite testes e identifique pelo menos um caso importante que faltou.
5. Audite um código gerado procurando segurança, erros e mudanças fora do escopo.
6. Compare uma solução própria com uma sugerida e justifique qual é mais adequada.

---

## 13. Erros comuns

- aceitar a primeira resposta sem executar;
- pedir um projeto inteiro em um único prompt;
- omitir restrições e critérios;
- enviar dados reais ou credenciais;
- executar comandos sem compreender;
- confundir explicação convincente com evidência;
- usar testes criados apenas para confirmar a solução;
- permitir alterações fora do escopo;
- não registrar a contribuição da IA quando exigido;
- atribuir à ferramenta a responsabilidade pela entrega.

---

## 14. Fechamento

### Revisão oral

1. Qual é o papel correto da IA no desenvolvimento?
2. Quais elementos tornam um prompt verificável?
3. Por que decompor tarefas?
4. Como usar IA no debugging sem aceitar palpites?
5. Por que testes gerados também precisam ser revisados?
6. Quais dados nunca devem ser compartilhados?
7. O que observar no `git diff`?
8. Como demonstrar autoria e responsabilidade?

### Avaliação formativa

| Critério | Evidência esperada |
| --- | --- |
| Prompt | fornece contexto, escopo e critérios |
| Decomposição | trabalha em unidades verificáveis |
| Verificação | lê, executa, testa e compara |
| Debugging | usa evidências e valida hipóteses |
| Auditoria | identifica riscos e mudanças indevidas |
| Privacidade | remove dados sensíveis |
| Autoria | registra decisões próprias |

Sugestão de pontuação: 2 pontos para requisitos e prompts, 2 para verificação, 2 para testes, 2 para auditoria, 1 para documentação e 1 para histórico Git.

## Tarefa para casa

Finalize `USO_IA.md`, prepare uma demonstração de três minutos e selecione uma sugestão da IA que foi rejeitada. Explique por que rejeitá-la melhorou o projeto.

## Ponte para a Aula 10

Na aula final, cada equipe combinará lógica, coleções, funções, POO, Git, tratamento de erros e uso responsável de IA para concluir, documentar, testar e apresentar uma aplicação Python completa.
