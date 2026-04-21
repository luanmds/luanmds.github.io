# AGENTS.md — luanmds.github.io

> Arquivo de referência para agentes de IA. Mantenha sempre atualizado após mudanças arquiteturais.

---

## Visão Geral do Projeto

Blog estático bilíngue (Português-BR padrão + Inglês) para publicação de artigos com imagens.
Hospedado gratuitamente no GitHub Pages em `https://luanmds.github.io/`.

---

## Metodologia: Spec-Driven Development (SDD)

**Fluxo obrigatório:** `Spec (PLAN mode) → Tasks (SQL) → Implement (code)`

- **NUNCA codar sem spec e tasks aprovados** em PLAN mode
- Qualquer decisão com 2+ opções válidas: **parar e consultar o usuário**
- Este arquivo (`AGENTS.md`) deve ser atualizado sempre que houver mudanças arquiteturais

---

## Stack Tecnológica

| Camada         | Tecnologia                             |
|----------------|----------------------------------------|
| SSG            | Hugo extended v0.154.5                 |
| Tema           | PaperMod (git submodule)               |
| Conteúdo       | Markdown + Hugo Page Bundles           |
| Idiomas        | pt (default `/`) + en (`/en/`)         |
| Busca          | Fuse.js (nativo PaperMod, client-side) |
| Comentários    | Giscus (GitHub Discussions)            |
| Dev local      | Docker (hugomods/hugo:exts)            |
| Hosting        | GitHub Pages                           |
| CI/CD          | GitHub Actions                         |
| Repositório    | luanmds/luanmds.github.io              |

---

## Arquitetura e Estrutura do Projeto

```
luanmds.github.io/
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD: build Hugo extended → deploy GitHub Pages
├── archetypes/
│   └── post/                   # Template para novos posts (Page Bundle)
│       ├── index.md            # Template pt
│       └── index.en.md         # Template en
├── assets/                     # CSS/JS customizados (overrides do tema)
├── content/                    # Conteúdo pt (idioma padrão)
│   ├── posts/
│   │   └── <slug>/
│   │       ├── index.md        # Conteúdo pt
│   │       └── cover.png       # Imagem co-localizada
│   ├── about/index.md
│   ├── search/index.md
│   └── en/                     # Conteúdo en (contentDir do idioma inglês)
│       ├── posts/
│       │   └── <slug>/
│       │       ├── index.md    # Conteúdo en
│       │       └── cover.png
│       ├── about/index.md
│       └── search/index.md
├── i18n/
│   ├── pt.yaml                 # Strings de UI em português
│   └── en.yaml                 # Strings de UI em inglês
├── layouts/
│   └── partials/
│       └── comments.html       # Embed Giscus
├── static/                     # Arquivos estáticos (favicon, etc.)
├── themes/
│   └── PaperMod/               # Submodule: adityatelange/hugo-PaperMod
├── docker-compose.yml          # Dev local: hugo server na porta 1313
├── hugo.toml                   # Configuração principal do Hugo
├── AGENTS.md                   # Este arquivo
└── specs/                      # Specs SDD (uma pasta por spec)
    ├── 001-hugo-setup/
    ├── 002-multilingual/
    ├── 003-content-structure/
    ├── 004-features/
    └── 005-deployment/
```

---

## Padrão de Conteúdo: Page Bundles

Cada post é um **Leaf Bundle** (pasta com `index.md`):

```
content/posts/meu-artigo/
├── index.md        # pt — front matter + conteúdo
└── cover.png       # Imagem de capa co-localizada

content/en/posts/my-article/
├── index.md        # en — front matter + conteúdo
└── cover.png
```

**Front matter padrão (`index.md`):**
```yaml
---
title: "Título do Artigo"
date: 2026-04-21
draft: false
tags: ["tag1", "tag2"]
categories: ["categoria"]
summary: "Resumo do artigo"
cover:
  image: cover.png
  alt: "Descrição da imagem"
  relative: true
---
```

---

## Configuração de Idiomas

- **pt** → URL base `/` (padrão), contentDir: `content/`
- **en** → URL base `/en/`, contentDir: `content/en/`
- Seletor de idioma disponível no header (PaperMod nativo)
- Strings de UI: `i18n/pt.yaml` e `i18n/en.yaml`

---

## Features Configuradas

| Feature       | Implementação                    | Status      |
|---------------|----------------------------------|-------------|
| Busca         | Fuse.js + JSON index             | ✅ ativo    |
| Tags          | Taxonomia nativa Hugo            | ✅ ativo    |
| Comentários   | Giscus (GitHub Discussions)      | ✅ parcial* |
| Dark mode     | PaperMod nativo                  | ✅ ativo    |
| RSS Feed      | Hugo nativo                      | ✅ ativo    |
| Sitemap       | Hugo nativo                      | ✅ ativo    |
| Robots.txt    | Hugo nativo                      | ✅ ativo    |

> *Giscus: `repoId` e `categoryId` precisam ser preenchidos em `hugo.toml` após configurar em [giscus.app](https://giscus.app).

---

## Specs SDD

| Spec | Descrição                   | Status    |
|------|-----------------------------|-----------|
| 001  | Hugo Setup                  | ✅ done   |
| 002  | Configuração Multilíngue    | ✅ done   |
| 003  | Estrutura de Conteúdo       | ✅ done   |
| 004  | Features (busca/tags/etc.)  | ✅ done   |
| 005  | Deploy GitHub Pages         | ✅ done   |

---

## Desenvolvimento Local

```bash
# Iniciar servidor de desenvolvimento (porta 1313)
docker compose up

# Build de produção
docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify

# Novo post pt
mkdir -p content/posts/meu-artigo
# Crie content/posts/meu-artigo/index.md usando archetypes/post/index.md como base

# Atualizar submodule do tema
git submodule update --remote themes/PaperMod
```

---

## Notas para Agentes

- Hugo **extended** é obrigatório (PaperMod usa recursos extended)
- O `baseURL` em `hugo.toml` é `https://luanmds.github.io/`
- Giscus `repoId` e `categoryId` são placeholders — usuário preenche em [giscus.app](https://giscus.app)
- Docker cria arquivos como `root` — sempre usar `--user $(id -u):$(id -g)` ou corrigir permissões depois
- Rodar `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify` para validar antes de commitar
- GitHub Actions usa `peaceiris/actions-hugo@v3` com `extended: true`
