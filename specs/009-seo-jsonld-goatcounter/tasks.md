## Planejamento

- [x] Validar objetivo, escopo e critérios de aceitação com o usuário
- [x] Registrar decisões: Goatcounter (vs GA/Plausible/Hits.sh), partial override (vs modificar tema)

## Implementação

### JSON-LD

- [x] Criar/atualizar `layouts/_partials/head/custom.html` com template `BlogPosting` para artigos
- [x] Adicionar template `WebSite` + `SearchAction` na home em `layouts/_partials/head/custom.html`
- [x] Testar renderização do JSON-LD com `hugo server` (inspecionar `<head>`)

### Goatcounter — Tracking

- [x] Criar conta no Goatcounter em [goatcounter.com](https://www.goatcounter.com) (manual — usuário)
- [x] Adicionar script de tracking no `layouts/_partials/head/custom.html` com o site code do Goatcounter
- [x] Confirmar que o script não carrega em `localhost` (Goatcounter ignora por padrão)

### Goatcounter — Exibição de Views

- [x] Criar `layouts/_partials/article-views.html` com fetch à API do Goatcounter
- [x] Suporte bilíngue: texto "N visualizações" (pt) / "N views" (en) via `{{ if eq .Lang "pt" }}`
- [x] Adicionar estilos discretos em `assets/css/custom.css`
- [x] Incluir o partial em `layouts/single.html` no local correto (após metadados)

### Botões de Compartilhamento

- [x] Injetar array `sharingLinks = ["linkedin", "x-twitter", "threads", "bluesky", "telegram", "email"]` em `[params.article]` no `hugo.toml`

## Validação

- [x] Build `hugo --minify` sem erros
- [ ] JSON-LD válido no Google Rich Results Test
- [x] Confirmar `git diff themes/` vazio (nenhum arquivo do tema modificado)

## Encerramento

- [ ] Confirmar aceite com o usuário
- [ ] Perguntar sobre validação automatizada com Playwright (quando aplicável)
