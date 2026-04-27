## Implementação inicial

- [x] Busca Fuse.js ativa (JSON output + página search)
- [x] Tags e categorias configuradas
- [x] `layouts/partials/comments.html` com embed Giscus
- [x] `enableRobotsTXT = true` e sitemap.xml gerados no build

## Refinamento — Remover página de Tags (branch: fix/remove-tags)

- [x] Create branch `fix/remove-tags` from `main`
- [x] Remove `[[languages.pt.menus.main]]` block with `identifier = "tags"` from `hugo.toml`
- [x] Remove `[[languages.en.menus.main]]` block with `identifier = "tags"` from `hugo.toml`
- [x] Remove `tag = "tags"` from `[taxonomies]` section in `hugo.toml`
- [x] Run production build and verify no errors and no `/tags/` pages generated (PT: 33→25 pages, EN: 22→14 pages)
- [x] Commit and open PR — https://github.com/luanmds/luanmds.github.io/pull/7
