# Spec 007 — Migração para Congo + About estruturado + link PT/EN no artigo

**Status:** proposed  
**Data:** 2026-04-22  
**Objetivo:** Migrar tema PaperMod -> Congo, preservar URLs atuais, manter recursos existentes, personalizar Home/About (direcao B1: Grafite + Ciano), e adicionar link de traducao dentro do artigo.

## Contexto

Spec de migração de tema com preservação de URLs e paridade funcional entre PT/EN.

## Escopo

- Migração PaperMod -> Congo
- Preservação de rotas existentes
- Ajustes de Home/About
- Link contextual PT/EN dentro de artigos traduzidos

## Fora de escopo

- Fork profundo do Congo
- Troca da tipografia padrão do tema
- Mudanças amplas de arquitetura além da migração

## 1) Objetivo

Migrar o blog para o tema Congo sem quebrar rotas atuais nem funcionalidades existentes, modernizando Home/About com personalizacao moderada e adicionando troca de idioma contextual dentro de cada post.

## 2) Decisoes aprovadas

1. Tema alvo: **Congo**
2. Estrategia: **Opcao 2** (migracao com overrides moderados em `layouts/`)
3. Visual: base **B1** (paleta Grafite + Ciano)
4. Tipografia: manter tipografia padrao do Congo
5. Troca de idioma no artigo: automatica via Hugo (`.IsTranslated` + `.Translations`)
6. Seletor global de idioma no header: **mantido**
7. URLs atuais: **preservadas**
8. About: estruturado com base em informacoes publicas de LinkedIn e GitHub
9. Recursos a manter: busca, Giscus, tags/categorias, dark mode, RSS, sitemap e robots

## 3) Estado atual relevante

- Tema atual: `PaperMod` em `hugo.toml`
- Site bilingue ativo (`pt` padrao, `en` em `content/en`)
- About atual simples em:
  - `content/about/index.md`
  - `content/en/about/index.md`
- Giscus via `layouts/partials/comments.html`
- Busca e i18n ativos no arranjo atual do PaperMod

## 4) Arquitetura proposta

### 4.1 Migracao do tema

- Adicionar/ativar Congo no projeto e ajustar `hugo.toml` para parametros do novo tema.
- Manter configuracoes base de multilingual, menus pt/en, taxonomias e outputs necessarios.
- Atualizar configuracoes que hoje sao especificas do PaperMod para equivalentes do Congo.

### 4.2 Preservacao de URLs

- Nao alterar estrutura de content paths nem slugs existentes.
- Evitar mudancas em permalink/sections que alterem rotas publicas.
- Validar no build local se rotas antigas continuam resolvendo.

### 4.3 Home e About (customizacao moderada)

- Criar overrides pontuais de layout para:
  - Home com estrutura B1: hero curto + destaque de conteudo + lista/grade de posts
  - About com secoes estruturadas (bio, foco tecnico, experiencia/impacto, links)
- Aplicar paleta Grafite + Ciano via CSS custom em `assets/` (sem fork completo do tema).

### 4.4 Link de traducao dentro do artigo

- No template single de post, renderizar bloco de linguagem quando houver traducao:
  - condicao: `.IsTranslated`
  - destino: item de `.Translations` correspondente ao outro idioma
- Manter seletor global de idioma no header.
- Para posts com slugs diferentes entre idiomas, usar `translationKey` para mapear pares.
- Para posts novos, padrao recomendado: mesmo slug nos dois idiomas.

### 4.5 Busca, comentarios e recursos globais

- Busca: habilitar no Congo com pagina e output exigidos pelo tema/estrategia escolhida.
- Comentarios: portar/ajustar partial de Giscus para continuar em paginas de post.
- Manter tags/categorias, dark mode, RSS, sitemap e robots no comportamento esperado.

## 5) Dados para pagina About

- Fonte de verdade: informacoes publicas de LinkedIn e GitHub do autor.
- Criar versoes PT e EN equivalentes em intencao e conteudo.
- Nao incluir afirmacoes nao verificaveis.

## 6) Tratamento de erros e fallback

- Se post nao tiver traducao pareada, nao mostrar link PT/EN no artigo.
- Se algum recurso do Congo nao tiver equivalencia direta, criar override local focado e documentado.
- Se a migracao impactar rota existente, bloquear merge ate corrigir compatibilidade.

## 7) Criterios de aceitacao

1. Tema ativo passa a ser Congo sem quebrar build.
2. URLs existentes continuam funcionando.
3. Home e About refletem direcao visual B1 (Grafite + Ciano).
4. About PT/EN estruturados e consistentes.
5. Cada post com traducao exibe link para o idioma alternativo.
6. Posts sem traducao nao exibem link de troca contextual.
7. Seletor global de idioma no header continua ativo.
8. Busca, Giscus, tags/categorias, dark mode, RSS, sitemap e robots continuam operacionais.

## 8) Validacao

- Build local de producao com Hugo extended sem erros.
- Verificacao manual das principais rotas PT e EN, incluindo About/Home e post com traducao.
- Verificacao funcional dos recursos obrigatorios mantidos.
- Opcional apos implementacao: validacao automatizada com Playwright (mediante confirmacao do usuario).

## 10) Refinamentos pós-implementação

### 10.1 Responsividade mobile (fix/mobile-responsiveness)

**Problema:** Layout `basic` do header não colapsa em telas pequenas; cards de post usam `flex-row` fixo, ficando espremidos no mobile.

**Solução aprovada:**
- Mudar `layout = "basic"` para `layout = "hybrid"` no `hugo.toml`. O layout `hybrid` nativo do Congo exibe links horizontais no desktop e hamburger collapsible no mobile — sem necessidade de override manual.
- `assets/css/custom.css`: adicionar CSS para altura da imagem dos cards no mobile.
- `layouts/_partials/article-link.html`: mudar `flex-row` → `flex-col sm:flex-row` no `<article>` e ajustar classes de imagem para empilhar verticalmente no mobile.

### 10.2 Favicon com logo (fix/favicon-logo)

**Problema:** `static/` vazia; Congo usa favicon padrão (quadrado roxo/violeta).

**Solução aprovada:**
- Gerar `static/favicon.png` derivado de `assets/img/logo_blog.png` via ImageMagick (crop quadrado centralizado, 64×64px).
- Congo detecta `static/favicon.png` automaticamente e injeta nos `<link rel="icon">`.
- Nenhuma mudança em partials ou `hugo.toml`.

## 11) Referência de tarefas

- Ver `specs/007-congo-migration/tasks.md`.
