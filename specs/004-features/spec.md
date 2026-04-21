# Spec 004 — Features: Busca, Tags, Giscus

**Status:** ✅ done  
**Objetivo:** Ativar busca Fuse.js, taxonomia de tags/categorias, comentários Giscus, sitemap e robots.txt.

## Busca (Fuse.js)

PaperMod integra busca client-side via [Fuse.js](https://fusejs.io/). Requer:
1. Output `JSON` na home (`outputs = ["HTML", "RSS", "JSON"]` no `hugo.toml`)
2. Página `content/search/index.md` com `layout: search`

A busca filtra por título, tags, categorias e sumário dos artigos.

## Tags e Categorias

Configuradas como taxonomias nativas do Hugo:
```toml
[taxonomies]
  tag = "tags"
  category = "categories"
```

Páginas de listagem geradas automaticamente em `/tags/` e `/categories/`.

## Giscus (Comentários)

Sistema de comentários baseado em **GitHub Discussions** — gratuito e open source.

**Configuração necessária pelo usuário:**
1. Acesse [giscus.app](https://giscus.app)
2. Configure o repositório `luanmds/luanmds.github.io`
3. Copie `repoId` e `categoryId`
4. Preencha em `hugo.toml` nos campos `params.giscus.repoId` e `params.giscus.categoryId`

## Sitemap e Robots.txt

Gerados automaticamente pelo Hugo com `enableRobotsTXT = true`.

## Artefatos produzidos

| Arquivo | Descrição |
|---------|-----------|
| `hugo.toml` (outputs, taxonomies) | Configuração de busca e taxonomias |
| `content/search/index.md` | Página de busca pt (layout: search) |
| `content/en/search/index.md` | Página de busca en (layout: search) |
| `layouts/partials/comments.html` | Embed Giscus configurável via hugo.toml |

## Tasks concluídas

- [x] Busca Fuse.js ativa (JSON output + página search)
- [x] Tags e categorias configuradas
- [x] `layouts/partials/comments.html` com embed Giscus
- [x] `enableRobotsTXT = true` e sitemap.xml gerados no build
