# Spec 009 — SEO: JSON-LD Structured Data + Contador de Visualizações (Goatcounter)

**Status:** proposed  
**Data:** 2026-05-09  
**Objetivo:** Melhorar a indexação do blog com dados estruturados JSON-LD e adicionar rastreamento de visualizações com exibição por artigo via Goatcounter.

## Contexto

O blog atualmente gera sitemap, robots.txt e RSS, mas não possui dados estruturados (Schema.org/JSON-LD), o que limita a indexação semântica pelo Google (rich results, knowledge graph). Adicionalmente, não há analytics nem contador de visualizações visível ao leitor.

O Congo não gera JSON-LD por padrão. A solução deve ser implementada via partial override sem modificar o tema diretamente.

Como o blog é 100% estático (Hugo + GitHub Pages), um contador de views requer um serviço externo. O Goatcounter foi escolhido por ser: gratuito para uso pessoal, open source, GDPR-friendly (sem cookies), com API pública que permite exibir a contagem no artigo.

## Escopo

1. Adicionar JSON-LD do tipo `BlogPosting` em cada artigo via partial Hugo
2. Adicionar JSON-LD do tipo `WebSite` na home page para habilitar o Sitelinks Search Box
3. Criar conta no Goatcounter e adicionar o script de tracking
4. Exibir o contador de visualizações no rodapé de cada artigo (via API JS do Goatcounter)
5. Suporte bilíngue: JSON-LD deve usar o idioma correto do artigo

## Fora de escopo

- Modificar arquivos dentro de `themes/congo/` diretamente
- Implementar analytics avançados (funis, events, heatmaps)
- Dashboard público de analytics
- Integração com Google Analytics

## Decisões aprovadas

- **JSON-LD via partial override** em `layouts/_partials/head/custom.html` — padrão do Congo para extensões sem alterar o tema
- **Goatcounter** como solução de analytics/views — rejeitado Google Analytics (coleta dados excessivos), Plausible (pago), Hits.sh (sem API para exibição inline)
- **Exibição de views via JS fetch** na API pública do Goatcounter — a contagem de cada artigo é pública, o que é aceitável para um blog pessoal
- **Partial dedicado para views** em `layouts/_partials/article-views.html` — incluído no `layouts/single.html` existente

## Critérios de aceitação

1. `<script type="application/ld+json">` com tipo `BlogPosting` presente no `<head>` de cada artigo publicado
2. JSON-LD da home com tipo `WebSite` + `SearchAction` apontando para `/search/`
3. Script do Goatcounter carregado em todas as páginas (tracking invisível)
4. Contador de views exibido no artigo com texto "N visualizações" / "N views" conforme o idioma
5. Build `hugo --minify` sem erros após as mudanças
6. Nenhum arquivo em `themes/congo/` modificado

## Riscos e mitigação

- **Risco:** A API pública do Goatcounter pode ter rate limit ou instabilidade.  
  **Mitigação:** Exibir "—" ou ocultar o elemento quando a API retornar erro; usar `async` no fetch para não bloquear a página.

- **Risco:** Goatcounter gratuito tem limite de 100k pageviews/mês.  
  **Mitigação:** Aceitável para um blog pessoal no início. Revisar se o volume crescer.

- **Risco:** Adblockers podem bloquear o script do Goatcounter.  
  **Mitigação:** Comportamento esperado e documentado; o contador simplesmente não incrementa para esses usuários.

- **Risco:** O `layouts/single.html` já possui customizações — adicionar o partial de views pode quebrar o layout.  
  **Mitigação:** Verificar o arquivo atual antes de modificar; adicionar o partial no local correto (após metadados do artigo).

## Artefatos previstos

- `layouts/_partials/head/custom.html` — JSON-LD para artigos e home
- `layouts/_partials/article-views.html` — exibição do contador de views
- `layouts/single.html` — incluir o partial `article-views`
- `assets/css/custom.css` — estilos para o contador de views (discreto, alinhado com o design do tema)
- `specs/009-seo-jsonld-goatcounter/tasks.md`

## Validação

- `docker compose up` e inspecionar `<head>` de um artigo no browser (DevTools > View Source)
- Verificar JSON-LD com [Google Rich Results Test](https://search.google.com/test/rich-results)
- Verificar JSON-LD com [Schema.org Validator](https://validator.schema.org/)
- `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify` sem erros
- Confirmar que nenhum arquivo em `themes/` foi alterado com `git diff themes/`

## Referência de tarefas

- Ver `specs/009-seo-jsonld-goatcounter/tasks.md`.
