# architecture.md

## Modelo: Static Site Generator (SSG)

O blog é um site **100% estático**. Não existe servidor de aplicação, banco de dados ou lógica de backend. O Hugo compila Markdown + templates em arquivos HTML/CSS/JS puros, que são servidos diretamente pelo GitHub Pages como assets estáticos.

```
Markdown + Templates → Hugo build → HTML/CSS/JS → GitHub Pages → Browser
```

Não há estado compartilhado, sessões ou autenticação. Cada página é um arquivo HTML gerado em tempo de build.

---

## Bilinguismo: contentDir split

**Decisão:** pt e en usam `contentDir` separados, não o sistema de `translationKey` por arquivo dentro de um único diretório.

```toml
# hugo.toml
[languages.pt]
  # contentDir padrão: content/
[languages.en]
  contentDir = "content/en"
```

**Por quê:** Mantém os arquivos de cada idioma organizados em pastas distintas, sem misturar `index.md` e `index.en.md` no mesmo diretório. Facilita navegação e criação de posts parcialmente traduzidos (nem todo post em pt precisa ter equivalente em en).

**Trade-off:** Cria duplicação de estrutura de pastas (`content/posts/` e `content/en/posts/`). Posts que existem em ambos os idiomas precisam do `translationKey` igual no front matter para o Hugo identificar que são o mesmo artigo e exibir o seletor de idioma.

---

## Page Bundles (Leaf Bundles)

Cada post é uma **Leaf Bundle**: uma pasta com `index.md` e assets co-localizados.

```
content/posts/meu-artigo/
├── index.md      ← conteúdo + front matter
└── cover.png     ← imagem junto ao artigo
```

**Por quê:** Permite referenciar imagens com caminhos relativos (`image: cover.png`) sem precisar de paths absolutos. Hugo processa as imagens do bundle (WebP, lazy loading, fingerprint) como parte do build.

---

## Theme Override Pattern

O Congo é um submodule em `themes/congo/`. Customizações **nunca são feitas dentro do submodule** — seriam perdidas no próximo `git submodule update`.

O Hugo usa lookup order: arquivos em `layouts/` do projeto têm precedência sobre `themes/congo/layouts/`. O mesmo vale para `assets/` e `static/`.

```
layouts/_partials/comments.html  ← override do partial de comentários do Congo
layouts/single.html              ← override do template de artigo
assets/img/                      ← logos e imagens do projeto
```

---

## CI/CD: Build e Deploy via GitHub Actions

O deploy é **automático** no push para `main`. O workflow `.github/workflows/deploy.yml`:

1. Faz checkout com `submodules: recursive` (inclui o tema Congo)
2. Instala Hugo extended 0.154.5 via `peaceiris/actions-hugo@v3`
3. Executa `hugo --minify --baseURL <pages-url>`
4. Faz upload do artifact `./public`
5. Deploy para GitHub Pages via `actions/deploy-pages@v4`

**Não há staging, não há deploy preview.** O que vai para `main` vai direto para produção.

---

## Busca: Client-side com Fuse.js

O Hugo gera um `index.json` com todos os posts (configurado em `outputs.home = ["HTML", "RSS", "JSON"]`). O Congo consome esse JSON via Fuse.js no browser. Não existe chamada de API — tudo roda localmente no cliente.

---

## Comentários: Giscus (DISABLED FOR NOW)

Os comentários via Giscus estão desabilitados — `repoId` e `categoryId` estão vazios no `hugo.toml`. O partial `layouts/_partials/comments.html` verifica essa condição; se os valores estiverem vazios, nenhum script externo é carregado e o bloco de comentários não é renderizado.

Para ativar no futuro, veja `.docs/integrations.md`.

---

## Decisões-chave

| Decisão | Alternativa descartada | Razão da escolha |
|---|---|---|
| Hugo (SSG) | Next.js, Gatsby, WordPress | Markdown-first sem CMS, zero runtime, sem NPM ecosystem |
| Congo theme | PaperMod (legado), outros | Suporte nativo a bilinguismo, busca, TOC, dark mode com menos configuração |
| GitHub Pages | Netlify, Vercel | Gratuito, sem vendor lock-in além do GitHub já usado |
| contentDir split | translationKey no mesmo dir | Clareza de organização por idioma |
| Git submodule para tema | Copiar theme direto | Facilita updates do upstream Congo com `git submodule update` |
