# features.md

O que existe no projeto hoje. Não é roadmap — apenas o que está implementado e funcional.

---

## Publicação de conteúdo

- **Posts em Markdown** organizados como Page Bundles (pasta com `index.md` + assets co-localizados)
- **Imagens de capa** co-localizadas com o post (`cover.png`)
- **Front matter** com título, data, tags, categorias, summary e cover
- **Rascunhos** (draft: true) — não publicados no build de produção
- **Datas de publicação futura** — não publicados antes da data

## Bilinguismo

- **Dois idiomas:** pt (padrão, URLs `/`) e en (URLs `/en/`)
- **Seletor de idioma** no header (ação `locale` no menu)
- **Seletor contextual de idioma** dentro do artigo (`layouts/_partials/article-language-switch.html`) — aparece apenas em posts com `translationKey` correspondente no outro idioma
- **Conteúdo independente por idioma** — um post em pt não precisa ter versão en

## Navegação e menus

- **Menu principal** com: Posts, Tags, Buscar, Sobre, seletor de idioma, seletor de aparência
- **Breadcrumbs** nos artigos
- **Paginação** entre posts (anterior / próximo)
- **Listagem de posts** agrupada por ano com summary

## Busca

- **Busca client-side** via Fuse.js (nativo do Congo)
- Página dedicada `/search/` (e `/en/search/`)
- Índice gerado pelo Hugo em JSON no build

## Taxonomias

- **Tags** — listagem em `/tags/`, exibidas nos artigos e na listagem
- **Categorias** — taxonomia configurada, mas sem menu de navegação dedicado

## Visual e tema

- **Dark mode** — nativo do Congo, com seletor de aparência no menu
- **Auto-switch** baseado na preferência do sistema (`autoSwitchAppearance = true`)
- **Color scheme:** graphite
- **Logo customizado** para tema claro e escuro (`assets/img/logo_blog.png`, `logo_blog_dark.png`)
- **Layout da home** customizado (`layouts/_partials/home/custom.html`)
- **Layout de artigo** customizado (`layouts/single.html`) com suporte a cover, TOC e comentários

## Artigo

- **Table of Contents** lateral (sticky em desktop) para posts com `h2`–`h4`
- **Metadados do artigo:** data, autor, tempo de leitura, contagem de palavras
- **Heading anchors** — links clicáveis nos títulos
- **Code copy** — botão de copiar em blocos de código
- **Lazy loading de imagens**
- **Conversão automática para WebP** das imagens no build
- **Suporte a LaTeX** via passthrough delimiters (bloco `$$` e inline `\(`)
- **Syntax highlighting** com classes CSS (não inline styles)

## Autor

- **Box de autor** no rodapé de cada post com: nome, headline, bio e links sociais
- Links: GitHub, LinkedIn, Medium, Dev.to

## Comentários (DISABLED FOR NOW)

- **Giscus** configurado no `layouts/_partials/comments.html` e `hugo.toml`
- **Status: DISABLED FOR NOW** — `repoId` e `categoryId` estão vazios; nenhum widget é renderizado
- Instruções para ativar em `.docs/integrations.md`

## SEO e descoberta

- **RSS Feed** — gerado automaticamente pelo Hugo (`/index.xml`)
- **Sitemap** — gerado automaticamente pelo Hugo (`/sitemap.xml`)
- **robots.txt** — gerado pelo Hugo (`enableRobotsTXT = true`)
- **Fingerprint SHA-256** em assets CSS/JS

## CI/CD

- **Deploy automático** para GitHub Pages a cada push em `main`
- **Build com minificação** (`hugo --minify`)
- **Trigger manual** via `workflow_dispatch`

## Desenvolvimento local

- **Servidor de dev com live reload** via `docker compose up` (porta 1313)
- **Archetypes** para criação de novos posts com front matter pré-preenchido

## Code review

- **CodeRabbit** configurado via `.coderabbit.yaml` para review automatizado em PRs
