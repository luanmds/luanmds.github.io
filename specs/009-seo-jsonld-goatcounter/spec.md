# Spec 009 — SEO: JSON-LD + Goatcounter + Botões de Compartilhamento

**Status:** done  
**Data:** 2026-05-09  
**Objetivo:** Melhorar a indexação do blog com dados estruturados JSON-LD, adicionar rastreamento de visualizações via Goatcounter e habilitar os botões nativos de compartilhamento.

## Contexto

O blog atualmente gera sitemap, robots.txt e RSS, mas não possui dados estruturados (Schema.org/JSON-LD), o que limita a indexação semântica pelo Google (rich results, knowledge graph). Adicionalmente, não há analytics nem contador de visualizações visível ao leitor.

O Congo gera JSON-LD nativamente via `_partials/schema.html` (tipos `Article`, `WebSite`, `BreadcrumbList`). A implementação customizada foi descartada após verificação — o JSON-LD customizado em `head/custom.html` era redundante e nunca foi renderizado (ver Correção abaixo).

Como o blog é 100% estático (Hugo + GitHub Pages), um contador de views requer um serviço externo. O Goatcounter foi escolhido por ser: gratuito para uso pessoal, open source, GDPR-friendly (sem cookies), com API pública que permite exibir a contagem no artigo.

## Escopo

1. Adicionar JSON-LD do tipo `BlogPosting` em cada artigo via partial Hugo
2. Adicionar JSON-LD do tipo `WebSite` na home page para habilitar o Sitelinks Search Box
3. Criar conta no Goatcounter e adicionar o script de tracking
4. Exibir o contador de visualizações no rodapé de cada artigo (via API JS do Goatcounter)
5. Suporte bilíngue: JSON-LD deve usar o idioma correto do artigo
6. Ativar botões de compartilhamento (LinkedIn, X, Threads, Bluesky, Telegram, Email) via configuração `sharingLinks` no tema.

## Fora de escopo

- Modificar arquivos dentro de `themes/congo/` diretamente
- Implementar analytics avançados (funis, events, heatmaps)
- Dashboard público de analytics
- Integração com Google Analytics

## Decisões aprovadas

- **JSON-LD via Congo nativo** — `_partials/schema.html` do Congo já gera `Article`, `WebSite` e `BreadcrumbList`. Nenhuma customização necessária.
- **Goatcounter tracking via `extend-head.html`** — o ponto de extensão correto do Congo para scripts no `<head>` é `_partials/extend-head.html` (chamado em `head.html` linha 149). **Correção aplicada:** o script estava em `_partials/head/custom.html` (não chamado por nenhum template), movido para `_partials/extend-head.html`.
- **Goatcounter** como solução de analytics/views — rejeitado Google Analytics (coleta dados excessivos), Plausible (pago), Hits.sh (sem API para exibição inline)
- **Exibição de views via JS fetch** na API pública do Goatcounter — a contagem de cada artigo é pública, o que é aceitável para um blog pessoal
- **Partial dedicado para views** em `layouts/_partials/article-views.html` — incluído no `layouts/single.html` existente

## Critérios de aceitação

1. JSON-LD `Article`, `WebSite` e `BreadcrumbList` gerado pelo Congo nativo em todas as páginas relevantes
2. Script do Goatcounter carregado em todas as páginas via `_partials/extend-head.html` (tracking invisível)
3. Contador de views exibido no artigo com texto "N visualizações" / "N views" conforme o idioma
4. Build `hugo --minify` sem erros após as mudanças
5. Nenhum arquivo em `themes/congo/` modificado
6. Botões de compartilhamento visíveis ao final do artigo com os links corretamente gerados.

## Riscos e mitigação

- **Risco:** A API pública do Goatcounter pode ter rate limit ou instabilidade.  
  **Mitigação:** Exibir "—" ou ocultar o elemento quando a API retornar erro; usar `async` no fetch para não bloquear a página.

- **Risco:** Goatcounter gratuito tem limite de 100k pageviews/mês.  
  **Mitigação:** Aceitável para um blog pessoal no início. Revisar se o volume crescer.

- **Risco:** Adblockers podem bloquear o script do Goatcounter.  
  **Mitigação:** Comportamento esperado e documentado; o contador simplesmente não incrementa para esses usuários.

- **Risco:** O `layouts/single.html` já possui customizações — adicionar o partial de views pode quebrar o layout.  
  **Mitigação:** Verificar o arquivo atual antes de modificar; adicionar o partial no local correto (após metadados do artigo).

## Artefatos gerados

- `layouts/_partials/extend-head.html` — script de tracking do Goatcounter (ponto de extensão correto do Congo)
- `layouts/_partials/article-views.html` — exibição do contador de views
- `layouts/single.html` — inclui o partial `article-views`
- `assets/css/custom.css` — estilos para o contador de views (discreto, alinhado com o design do tema)
- `specs/009-seo-jsonld-goatcounter/tasks.md`

> **Nota:** `layouts/_partials/head/custom.html` foi criado durante a implementação mas removido na correção — era dead code (nunca chamado pelo Congo) e o JSON-LD que continha era redundante com o `schema.html` nativo do tema.

## Correção pós-implementação

**Problema:** O script de tracking do Goatcounter estava em `_partials/head/custom.html`, que não é um ponto de extensão do Congo. O Congo só chama `_partials/extend-head.html` como hook do `<head>` (ver `themes/congo/layouts/_partials/head.html:149`). O resultado foi que o tracking nunca carregou em produção, o GoatCounter não registrou pageviews e o endpoint `/counter/<path>.json` retornava 404.

**Correção (PR `fix/goatcounter-tracking-script`):**
- Removido `layouts/_partials/head/custom.html` (dead code)
- Criado `layouts/_partials/extend-head.html` com o tracking script
- Substituído `.Site.IsServer` por `hugo.IsServer` (compatível com todos os contextos de template do Congo)
- JSON-LD customizado descartado — Congo já gera esquemas equivalentes via `schema.html`

## Validação

- `docker compose up` e inspecionar `<head>` de um artigo no browser (DevTools > View Source)
- Verificar JSON-LD com [Google Rich Results Test](https://search.google.com/test/rich-results)
- Verificar JSON-LD com [Schema.org Validator](https://validator.schema.org/)
- `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify` sem erros
- Confirmar que nenhum arquivo em `themes/` foi alterado com `git diff themes/`

## Referência de tarefas

- Ver `specs/009-seo-jsonld-goatcounter/tasks.md`.
