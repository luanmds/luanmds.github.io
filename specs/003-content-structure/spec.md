# Spec 003 — Estrutura de Conteúdo

**Status:** ✅ done  
**Objetivo:** Definir Page Bundles, archetypes e criar posts de exemplo com imagens.

## Contexto

Todo conteúdo segue o padrão **Page Bundle (Leaf Bundle)**: cada post é uma pasta com `index.md` e seus recursos (imagens) co-localizados. Isso simplifica a gestão de assets por artigo.

## Padrão de Diretórios

```
content/posts/<slug>/
├── index.md       # Conteúdo pt
└── cover.png      # Imagem co-localizada

content/en/posts/<slug>/
├── index.md       # Conteúdo en
└── cover.png
```

## Front Matter Padrão

```yaml
---
title: "Título"
date: YYYY-MM-DD
draft: false
tags: ["tag1"]
categories: ["categoria"]
summary: "Resumo"
cover:
  image: cover.png
  alt: "Descrição"
  relative: true   # obrigatório para Page Bundles
---
```

## Artefatos produzidos

| Arquivo | Descrição |
|---------|-----------|
| `archetypes/post/index.md` | Template pt para novos posts |
| `archetypes/post/index.en.md` | Template en para novos posts |
| `content/about/index.md` | Página Sobre (pt) |
| `content/en/about/index.md` | Página About (en) |
| `content/search/index.md` | Página de busca (pt) |
| `content/en/search/index.md` | Página de busca (en) |
| `content/posts/bem-vindo-ao-blog/` | Post de exemplo (pt) com cover.png |
| `content/en/posts/welcome-to-the-blog/` | Post de exemplo (en) com cover.png |

## Tasks concluídas

- [x] Archetype `archetypes/post/` criado (pt + en templates)
- [x] Páginas `about` e `search` em ambos idiomas
- [x] 2 posts de exemplo com imagens co-localizadas
- [x] Build valida imagens processadas corretamente
