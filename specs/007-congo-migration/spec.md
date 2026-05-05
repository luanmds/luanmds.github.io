# Spec 007 — Migração para Congo + About estruturado + link PT/EN no artigo

**Status:** em andamento
**Data:** 2026-04-22
**Atualização:** 2026-05-05
**Objetivo:** Migrar o tema PaperMod para Congo, preservar URLs atuais, manter recursos existentes, personalizar Home/About com a paleta Crimson Circuitry e adicionar link de tradução contextual dentro dos artigos.

## Contexto

O blog utilizava o tema PaperMod. A migração para o Congo moderniza o visual e abre espaço para customizações moderadas de layout e paleta de cores, mantendo paridade funcional completa entre PT e EN.

## Escopo

1. Migração PaperMod → Congo
2. Preservação de rotas existentes
3. Ajustes de Home/About com paleta Crimson Circuitry
4. Link contextual PT/EN dentro de artigos traduzidos

## Fora de escopo

- Fork profundo do Congo
- Troca da tipografia padrão do tema
- Mudanças amplas de arquitetura além da migração

## Decisões aprovadas

- Tema alvo: **Congo** (submodulo git em `themes/congo`)
- Estratégia: overrides moderados em `layouts/` sem fork do tema
- Visual: paleta **Crimson Circuitry** (vermelho + cinza quente) via `assets/css/schemes/crimson.css`
- Tipografia: manter padrão do Congo
- Troca de idioma no artigo: automática via Hugo (`.IsTranslated` + `.Translations`)
- Seletor global de idioma no header: mantido
- URLs atuais: preservadas (sem alteração de slugs ou permalinks)
- About: estruturado com base em informações públicas de LinkedIn e GitHub
- Recursos a manter: busca, Giscus, tags/categorias, dark mode, RSS, sitemap e robots
- `showComments = false` até `repoId`/`categoryId` do Giscus serem preenchidos pelo usuário

## Critérios de aceitação

1. Tema ativo é o Congo; build sem erros.
2. URLs existentes continuam funcionando.
3. Home e About refletem a paleta Crimson Circuitry em light e dark mode.
4. About PT/EN estruturados e consistentes.
5. Cada post com tradução exibe link para o idioma alternativo.
6. Posts sem tradução não exibem link de troca contextual.
7. Seletor global de idioma no header continua ativo.
8. Busca, tags/categorias, dark mode, RSS, sitemap e robots operacionais.

## Riscos e mitigação

- **Risco:** atualização do Congo quebrar overrides locais em `layouts/`.
  **Mitigação:** manter overrides focados e documentados; revisar ao atualizar o submodulo.
- **Risco:** paleta com contraste insuficiente em dark mode.
  **Mitigação:** Congo usa automaticamente `primary-300/400` (tons claros) no dark mode; verificar visualmente após implementação.
- **Risco:** Giscus inativo enquanto IDs não forem preenchidos.
  **Mitigação:** `showComments = false` como padrão explícito; não é bloqueante para o merge.

## Artefatos previstos

- `hugo.toml`
- `assets/css/schemes/crimson.css`
- `assets/css/custom.css`
- `layouts/` (overrides de home, artigo e partials)
- `content/about/index.md`
- `content/en/about/index.md`
- `static/` (favicons)

## Validação

- Build de produção: `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify`
- Verificação manual das principais rotas PT e EN via `docker compose up` (`http://localhost:1313`)
- Verificação visual de light e dark mode em home, about e post com tradução
- Opcional: validação automatizada com Playwright (mediante confirmação do usuário)

## Referência de tarefas

- Ver `specs/007-congo-migration/tasks.md`.

---

## Refinamentos pós-implementação

### 10.1 — Responsividade mobile (fix/mobile-responsiveness) — CONCLUÍDO

- Layout `hybrid` ativo no header (hamburger no mobile, links no desktop).
- CSS mobile para altura dos cards de post em `assets/css/custom.css`.
- PR #5 merged.

### 10.2 — Favicon com logo (fix/favicon-logo) — CONCLUÍDO

- Favicons gerados em `static/` a partir de `assets/img/logo_blog.png`.
- Congo detecta automaticamente os arquivos.
- PR merged.

### 10.3 — Paleta Crimson Circuitry (style/crimson-palette)

Substituição da paleta Grafite + Ciano pela Crimson Circuitry.

- Renomear `assets/css/schemes/graphite.css` → `assets/css/schemes/crimson.css`
- Atualizar `colorScheme = "crimson"` em `hugo.toml`
- Escala **primary** (vermelhos): âncoras em `#ff6e61` (400), `#c93b3b` (600), `#8a0009` (800)
- Escala **neutral** (cinza quente, base branca): branco em 50, Gallery `#f0f0f0` em ~200, Mine Shaft `#3b3b3b` em 700
- Escala **secondary** (pedra quente): complemento terroso sem hue contrastante
- Substituir 7 valores `rgba` hardcoded de ciano no `custom.css` por equivalentes crimson
- Dark mode: Congo usa `primary-300/400` automaticamente em modo escuro — comportamento "lean lighter" sem override manual

#### Escala Primary (vermelhos)

| Step | Hex | RGB |
|---|---|---|
| 50 | #fff2f1 | 255, 242, 241 |
| 100 | #ffe4e2 | 255, 228, 226 |
| 200 | #ffc3be | 255, 195, 190 |
| 300 | #ff9b91 | 255, 155, 145 |
| 400 | #ff6e61 | 255, 110, 97 |
| 500 | #e4544e | 228, 84, 78 |
| 600 | #c93b3b | 201, 59, 59 |
| 700 | #a91d22 | 169, 29, 34 |
| 800 | #8a0009 | 138, 0, 9 |
| 900 | #600006 | 96, 0, 6 |
| 950 | #370004 | 55, 0, 4 |

#### Escala Neutral (cinza quente, base branca)

| Step | RGB |
|---|---|
| 50 | 255, 255, 255 |
| 100 | 250, 250, 249 |
| 200 | 240, 240, 238 |
| 300 | 214, 212, 209 |
| 400 | 168, 165, 161 |
| 500 | 120, 117, 111 |
| 600 | 83, 80, 80 |
| 700 | 59, 59, 59 |
| 800 | 38, 36, 36 |
| 900 | 23, 21, 21 |
| 950 | 13, 11, 11 |

#### Escala Secondary (pedra quente)

| Step | RGB |
|---|---|
| 50 | 250, 248, 245 |
| 100 | 245, 241, 235 |
| 200 | 232, 224, 213 |
| 300 | 212, 200, 184 |
| 400 | 184, 168, 152 |
| 500 | 154, 136, 120 |
| 600 | 125, 108, 92 |
| 700 | 99, 84, 72 |
| 800 | 71, 60, 52 |
| 900 | 46, 39, 32 |
| 950 | 26, 21, 16 |
