# Spec 004 — Features: Busca, Taxonomias e Giscus

**Status:** done  
**Data:** 2026-05-04 (padronização)  
**Objetivo:** Ativar busca, taxonomias úteis, comentários Giscus e metadados de publicação (sitemap/robots).

## Contexto

O blog precisava de recursos editoriais além da renderização básica: busca client-side, organização por taxonomias e comentários por post.

## Escopo

1. Habilitar busca no site em PT e EN.
2. Configurar taxonomias no Hugo.
3. Integrar comentários com Giscus.
4. Garantir geração de `robots.txt` e `sitemap.xml`.

## Fora de escopo

- Moderação automática de comentários.
- Busca semântica com backend dedicado.

## Decisões aprovadas

- Busca baseada em output JSON da home + páginas `search` por idioma.
- Giscus como mecanismo de comentários por ser gratuito e integrado ao GitHub.
- Refinamento posterior removeu `tags` da navegação e da taxonomia ativa.

## Critérios de aceitação

1. Busca funcional em PT e EN.
2. Comentários renderizados quando configuração do Giscus estiver completa.
3. Taxonomias configuradas sem gerar páginas não desejadas (`/tags/` removida).
4. Build gera `robots.txt` e `sitemap.xml`.

## Riscos e mitigação

- **Risco:** IDs do Giscus ausentes no `hugo.toml`.  
  **Mitigação:** orientar preenchimento via `giscus.app`.

## Artefatos previstos

- `hugo.toml`
- `content/search/index.md`
- `content/en/search/index.md`
- `layouts/partials/comments.html`

## Validação

- Build local e inspeção das páginas de busca/comentários.

## Referência de tarefas

- Ver `specs/004-features/tasks.md`.
