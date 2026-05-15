## Planejamento

- [x] Validar objetivo, escopo e critérios de aceitação com o usuário
- [x] Registrar decisões: Goatcounter (vs GA/Plausible/Hits.sh), partial override (vs modificar tema)

## Implementação

### JSON-LD

- [x] ~~Criar/atualizar `layouts/_partials/head/custom.html` com template `BlogPosting` para artigos~~ — **Descartado:** Congo gera JSON-LD nativo via `schema.html` (`Article`, `WebSite`, `BreadcrumbList`). O arquivo `head/custom.html` era dead code e foi removido.
- [x] ~~Adicionar template `WebSite` + `SearchAction` na home em `layouts/_partials/head/custom.html`~~ — idem acima.
- [x] Confirmar JSON-LD nativo do Congo renderizando corretamente no `<head>` de artigos e home

### Goatcounter — Tracking

- [x] Criar conta no Goatcounter em [goatcounter.com](https://www.goatcounter.com) (manual — usuário)
- [x] Adicionar script de tracking em `layouts/_partials/extend-head.html` (ponto de extensão correto do Congo)
- [x] Confirmar que o script não carrega em `localhost` (`hugo.IsServer` retorna `true` no servidor de desenvolvimento)

### Goatcounter — Exibição de Views

- [x] Criar `layouts/_partials/article-views.html` com fetch à API do Goatcounter
- [x] Suporte bilíngue: texto "N visualizações" (pt) / "N views" (en) via `{{ if eq .Lang "pt" }}`
- [x] Adicionar estilos discretos em `assets/css/custom.css`
- [x] Incluir o partial em `layouts/single.html` no local correto (após metadados)

### Botões de Compartilhamento

- [x] Injetar array `sharingLinks = ["linkedin", "x-twitter", "threads", "bluesky", "telegram", "email"]` em `[params.article]` no `hugo.toml`

## Correção pós-implementação

- [x] Identificar que `_partials/head/custom.html` nunca era chamado pelo Congo (ponto de extensão errado)
- [x] Remover `layouts/_partials/head/custom.html` (dead code)
- [x] Criar `layouts/_partials/extend-head.html` com o tracking script (ponto correto: `head.html:149`)
- [x] Substituir `.Site.IsServer` por `hugo.IsServer` (compatível com todos os contextos de template)
- [x] Verificar build `hugo --minify` sem erros após a correção
- [x] Habilitar "Allow adding visitor counts on your website" nas configurações do Goatcounter

## Validação

- [x] Build `hugo --minify` sem erros
- [ ] JSON-LD válido no Google Rich Results Test
- [x] Confirmar `git diff themes/` vazio (nenhum arquivo do tema modificado)

## Encerramento

- [ ] Confirmar aceite com o usuário
- [ ] Perguntar sobre validação automatizada com Playwright (quando aplicável)
