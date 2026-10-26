# Manual das atividades práticas

Abra o [menu de atividades](index.html) no navegador para acessar as páginas do projeto.

## Atividades disponíveis

| Atividade | Conteúdo | Arquivo |
| --- | --- | --- |
| Aula prática 1 | Estruturas de dados em Python: listas, tuplas, dicionários e conjuntos | [Abrir aula](aula-pratica-1/index.html) |
| Aula 3 — Form Food | Atividade disponível na pasta form-food | [Abrir atividade](aula%203/form-food/index.html) |

## Como abrir localmente

1. Abra a pasta `coding`.
2. Dê dois cliques no arquivo `index.html` da raiz.
3. Escolha uma atividade no menu.

A aula prática 1 apresenta exemplos Python para executar no editor ou notebook; o navegador exibe a documentação.

## Organização do Git

A pasta `aula-pratica-1` faz parte do repositório principal de `coding`. Seu repositório Git interno foi removido; os arquivos da aula foram preservados.

Para versionar o menu, este manual e a aula, execute no terminal dentro de `coding`:

```powershell
git add -- index.html MANUAL.md aula-pratica-1
git commit -m "Adiciona aula pratica de estruturas de dados e menu de atividades"
git push
```

Esses comandos não foram executados automaticamente. O envio depende do acesso ao remoto e da configuração da branch do repositório principal.

## Publicação das páginas

Para publicar o conjunto em uma hospedagem estática, use `coding` como raiz e mantenha a estrutura das pastas. O arquivo `index.html` da raiz é a entrada do menu; ele usa links relativos para acessar cada atividade.

Enviar os arquivos ao Git não ativa, por si só, uma hospedagem de páginas. Configure o serviço de hospedagem para servir esta raiz.

## Como adicionar outra atividade

1. Crie a pasta da atividade dentro de `coding`, sem inicializar outro repositório Git nela.
2. Coloque o `index.html` e os arquivos necessários nessa pasta.
3. Adicione um link relativo no `index.html` da raiz e uma linha na tabela deste manual.

O catálogo é mantido manualmente. Pastas com espaços devem usar `%20` nos links HTML, como em `aula%203/form-food/index.html`.
