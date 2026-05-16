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

Exemplos: `feat/post-intro-go`, `fix/giscus-config`, `chore/update-congo`, `docs/compozy-docs-governance`.

---

## Forma de trabalhar

O repositório não exige um único processo para toda mudança. O que é obrigatório é respeitar os guardrails e convenções vigentes do projeto.

- Trabalho direto é aceitável para mudanças pequenas, localizadas ou puramente editoriais.
- Fluxos com artefatos do Compozy são úteis quando o escopo pede PRD, TechSpec, task breakdown, review rounds ou tracking mais explícito.
- Qualquer decisão com 2+ opções válidas: parar e perguntar ao usuário.
- Antes de encerrar trabalho relevante, rodar o build de produção do Hugo.
- Após mudanças com impacto em browser, oferecer validação com Playwright.

### Artefatos de planejamento

- `specs/` contém specs históricos do projeto e pode continuar servindo como referência de decisões anteriores.
- `.compozy/tasks/` contém workflows orientados por artefatos quando o Compozy é usado.
- Se um workflow com tracking estiver em uso, mantenha seus arquivos sincronizados com o estado real do trabalho.

---

## Nomenclatura de slugs (URLs)

- Kebab-case: `meu-artigo-sobre-golang`
- Em português por padrão (a versão en usa o mesmo slug, estrutura espelhada)
- Slugs devem ser descritivos mas concisos
- Evitar datas no slug (a data está no front matter)

---

## Front matter padrão

```yaml
---
title: "Título do Artigo"
translationKey: "chave-unica-de-traducao"   # igual em pt e en para ligar os idiomas
date: 2026-04-21
draft: false
tags: ["tag1", "tag2"]
categories: ["categoria"]
summary: "Resumo do artigo (aparece na listagem)"
cover:
  image: cover.png
  alt: "Descrição acessível da imagem"
  relative: true
---
```

**`translationKey`** é obrigatório em posts que têm versão nos dois idiomas. Deve ser igual em `content/posts/<slug>/index.md` e `content/en/posts/<slug>/index.md`.

---

## Tags e categorias

- Tags em minúsculas, sem acentos quando possível: `dotnet`, `arquitetura`, `ia`
- Categorias mais amplas: `backend`, `carreira`, `ferramentas`, `meta`
- Evitar criar tags ou categorias com apenas um post — prefira consolidar

---

## Imagens

- Cover padrão: `cover.png` (co-localizada no Page Bundle)
- Usar `relative: true` no front matter para referenciar por nome simples
- Dimensões recomendadas: 1200×630px (proporção Open Graph)
- Formato PNG ou JPEG; o Hugo gera WebP automaticamente no build

---

## Customizações de layout

- Nunca editar arquivos dentro de `themes/congo/` — mudanças seriam perdidas no próximo update
- Overrides ficam em `layouts/` (partials em `layouts/_partials/`)
- Seguir o padrão de nomenclatura do Congo para que o lookup order funcione

---

## O que evitar

- Commitar diretamente em `main`
- Editar arquivos dentro de `themes/congo/`
- Criar posts sem Page Bundle (sem pasta dedicada)
- Omitir `translationKey` em posts bilíngues
- Commits sem mensagem Conventional Commits
- Arquivos temporários ou de build (`public/`, `resources/`) versionados (já no `.gitignore`)
