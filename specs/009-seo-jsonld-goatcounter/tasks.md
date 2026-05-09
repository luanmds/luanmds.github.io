## Planejamento

- [x] Validar objetivo, escopo e critérios de aceitação com o usuário
- [x] Registrar decisões: Goatcounter (vs GA/Plausible/Hits.sh), partial override (vs modificar tema)

## Implementação

### JSON-LD

- [ ] Criar/atualizar `layouts/_partials/head/custom.html` com template `BlogPosting` para artigos
- [ ] Adicionar template `WebSite` + `SearchAction` na home em `layouts/_partials/head/custom.html`
- [ ] Testar renderização do JSON-LD com `hugo server` (inspecionar `<head>`)

### Goatcounter — Tracking

- [ ] Criar conta no Goatcounter em [goatcounter.com](https://www.goatcounter.com) (manual — usuário)
- [ ] Adicionar script de tracking no `layouts/_partials/head/custom.html` com o site code do Goatcounter
- [ ] Confirmar que o script não carrega em `localhost` (Goatcounter ignora por padrão)

### Goatcounter — Exibição de Views

- [ ] Criar `layouts/_partials/article-views.html` com fetch à API do Goatcounter
- [ ] Suporte bilíngue: texto "N visualizações" (pt) / "N views" (en) via `{{ if eq .Lang "pt" }}`
- [ ] Adicionar estilos discretos em `assets/css/custom.css`
- [ ] Incluir o partial em `layouts/single.html` no local correto (após metadados)

## Validação

- [ ] Build `hugo --minify` sem erros
- [ ] JSON-LD válido no Google Rich Results Test
- [ ] Confirmar `git diff themes/` vazio (nenhum arquivo do tema modificado)

## Encerramento

- [ ] Confirmar aceite com o usuário
- [ ] Perguntar sobre validação automatizada com Playwright (quando aplicável)
