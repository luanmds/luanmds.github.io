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

---

## Refinamento — Remover página de Tags (branch: fix/remove-tags)

**Decisão:** Tags não serão utilizadas no blog. A página `/tags/` e os itens de menu de Tags devem ser removidos.

**Solução aprovada:**
- `hugo.toml`: remover `[[languages.pt.menus.main]]` com `identifier = "tags"`.
- `hugo.toml`: remover `[[languages.en.menus.main]]` com `identifier = "tags"`.
- `hugo.toml`: remover `tag = "tags"` da seção `[taxonomies]` para impedir geração de páginas `/tags/`.
- Posts com `tags:` no front matter não causam erro — Hugo ignora taxonomias não configuradas.

### Tasks (branch: fix/remove-tags)

- [x] Create branch `fix/remove-tags` from `main`
- [x] Remove `[[languages.pt.menus.main]]` block with `identifier = "tags"` from `hugo.toml`
- [x] Remove `[[languages.en.menus.main]]` block with `identifier = "tags"` from `hugo.toml`
- [x] Remove `tag = "tags"` from `[taxonomies]` section in `hugo.toml`
- [x] Run production build and verify no errors and no `/tags/` pages generated (PT: 33→25 pages, EN: 22→14 pages)
- [x] Commit and open PR
