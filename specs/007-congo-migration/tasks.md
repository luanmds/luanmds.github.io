## Migração do tema — CONCLUÍDO

- [x] Adicionar tema Congo como submódulo git em `themes/congo` e atualizar `.gitmodules`
- [x] Alterar `theme` no `hugo.toml` de `PaperMod` para `congo`
- [x] Remover ou desativar parâmetros exclusivos do PaperMod no `hugo.toml`
- [x] Adicionar parâmetros compatíveis com Congo para aparência, busca, metadados de artigo, comentários e comportamento da homepage

## Multilinguismo e estabilidade de URLs — CONCLUÍDO

- [x] Manter estrutura bilíngue (`content/` e `content/en/`) e preservar links de menu em PT/EN
- [x] Manter rotas e slugs atuais sem adicionar mudanças de permalink que alterem URLs
- [x] Validar URLs representativas em PT e EN após a migração (home, about, posts, tags, busca)

## Customização de Home + About — CONCLUÍDO (paleta atualizada no 10.3)

- [x] Criar arquivo CSS de override em `assets/` com tokens da paleta
- [x] Adicionar overrides moderados de layout em `layouts/` para home (hero curto + destaque + recentes)
- [x] Reescrever `content/about/index.md` com seções estruturadas em PT baseadas em dados públicos de LinkedIn/GitHub
- [x] Reescrever `content/en/about/index.md` com seções equivalentes em EN

## Seletor de idioma no artigo — CONCLUÍDO

- [x] Verificar presença do bloco `.IsTranslated` + `.Translations` no layout de artigo individual
- [x] Manter seletor global de idioma no header ativo (verificar funcionamento)
- [x] Adicionar `translationKey` nos pares PT/EN existentes com slugs diferentes (verificar pares existentes)
- [x] Garantir que posts sem tradução não renderizem o bloco de troca de idioma

## Verificação de paridade de recursos — CONCLUÍDO

- [x] Verificar se as páginas de busca (`content/search/index.md`, `content/en/search/index.md`) existem e funcionam
- [x] Verificar se o partial do Giscus em `layouts/partials/comments.html` renderiza quando `showComments` está habilitado
- [x] Verificar se as listagens de tags/categorias funcionam em PT e EN
- [x] Verificar se o toggle de dark mode funciona no novo tema
- [x] Verificar se RSS, sitemap e robots.txt são gerados no build

## Refinamento 10.1 — Responsividade mobile — CONCLUÍDO

- [x] Criar branch `fix/mobile-responsiveness` a partir de `main`
- [x] Alterar `[params.header] layout` de `basic` para `hybrid` no `hugo.toml`
- [x] Adicionar CSS em `assets/css/custom.css` para limitar altura da imagem nos cards de post no mobile
- [x] Alterar `layouts/_partials/article-link.html`: `flex-row` → `flex-col sm:flex-row` no elemento `<article>`
- [x] Ajustar classes de imagem em `article-link.html` para largura total quando empilhadas verticalmente no mobile
- [x] Executar build de produção e verificar ausência de erros
- [x] Fazer commit e abrir PR — https://github.com/luanmds/luanmds.github.io/pull/5

## Refinamento 10.2 — Favicon com logo — CONCLUÍDO

- [x] Criar branch `fix/favicon-logo` a partir de `main`
- [x] Gerar `static/favicon-32x32.png`, `static/favicon-16x16.png` e `static/apple-touch-icon.png`
- [x] Verificar se o Congo detecta os arquivos automaticamente
- [x] Executar build de produção e verificar ausência de erros
- [x] Fazer commit e abrir PR

## Refinamento 10.3 — Paleta Crimson Circuitry (branch: style/crimson-palette)

- [ ] Criar branch `style/crimson-palette` a partir de `main`
- [ ] Renomear `assets/css/schemes/graphite.css` → `assets/css/schemes/crimson.css`
- [ ] Atualizar `colorScheme = "crimson"` no `hugo.toml`
- [ ] Escrever escala primary (vermelhos: 50–950) em `crimson.css`
- [ ] Escrever escala neutral (base branca, cinza quente, Mine Shaft em 700) em `crimson.css`
- [ ] Escrever escala secondary (pedra quente: 50–950) em `crimson.css`
- [ ] Substituir 7 valores `rgba` hardcoded de ciano em `assets/css/custom.css` por equivalentes crimson
- [ ] Executar build de produção: `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify`
- [ ] Verificar manualmente light e dark mode em home, about e um artigo via `docker compose up`
- [ ] Perguntar ao usuário: "Deseja validar com Playwright?"
- [ ] Se aprovado, executar validação com Playwright e corrigir problemas encontrados
- [ ] Fazer commit e abrir PR

## Validação e documentação

- [ ] Atualizar `AGENTS.md` se houver mudanças arquiteturais
- [ ] Marcar spec 007 como `concluído` após todas as tarefas finalizadas
