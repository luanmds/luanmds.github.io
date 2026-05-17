# conventions.md

## Commits

Seguir [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <descrição curta no imperativo>

[corpo opcional]

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

**Tipos válidos:**

| Tipo | Uso |
|---|---|
| `feat` | Novo post ou nova funcionalidade |
| `fix` | Correção de conteúdo ou bug |
| `chore` | Manutenção, configs, dependências |
| `docs` | Documentação do repositório, contexto durável e artefatos de workflow |
| `style` | CSS, visual, sem mudança de comportamento |
| `refactor` | Reestruturação sem mudança de comportamento |
| `ci` | Mudanças em workflows do GitHub Actions |

**Proibido:** commitar diretamente em `main`.

---

## Branches

```
<tipo>/<escopo-curto>
```

Exemplos: `feat/post-intro-go`, `fix/giscus-config`, `chore/update-congo`, `docs/harness-docs-governance`.

**Regra operacional:** ao abrir qualquer branch de trabalho, use a skill `github-branch-pr` para padronizar criação da branch e abertura de PR.

## Nomenclatura de slugs (URLs)

- Kebab-case: `meu-artigo-sobre-golang`
- Em português por padrão (a versão en usa o mesmo slug, estrutura espelhada)
- Slugs devem ser descritivos mas concisos
- Evitar datas no slug (a data está no front matter)

## Conteúdo editorial

- Para front matter, `translationKey`, tags, categorias, imagens e criação de artigos, use `.docs/articles.md` como fonte canônica.
- Posts bilíngues devem manter paridade estrutural entre `content/` e `content/en/`.

## Customizações de layout

- Nunca editar arquivos dentro de `themes/congo/` — mudanças seriam perdidas no próximo update
- Overrides ficam em `layouts/` (partials em `layouts/_partials/`)
- Seguir o padrão de nomenclatura do Congo para que o lookup order funcione

## O que evitar

- Commitar diretamente em `main`
- Editar arquivos dentro de `themes/congo/`
- Criar posts sem Page Bundle (sem pasta dedicada)
- Commits sem mensagem Conventional Commits
- Arquivos temporários ou de build (`public/`, `resources/`) versionados (já no `.gitignore`)
