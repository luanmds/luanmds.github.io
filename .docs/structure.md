# structure.md

## Visão geral da raiz

```
luanmds.github.io/
├── .docs/              ← documentação de contexto do projeto (este diretório)
├── .github/            ← GitHub Actions workflows
├── .opencode/          ← configuração do agente OpenCode (skills customizadas)
├── .superpowers/       ← plugins/skills do sistema de superpowers
├── .vscode/            ← configurações do editor
├── archetypes/         ← templates para novos posts
├── assets/             ← CSS, JS e imagens (overrides do tema)
├── content/            ← conteúdo em pt (idioma padrão)
├── data/               ← dados JSON/YAML consumidos por templates Hugo
├── i18n/               ← strings de UI por idioma
├── layouts/            ← overrides de templates do Congo
├── specs/              ← specs SDD (uma pasta por spec numerada)
├── static/             ← arquivos estáticos copiados diretamente para public/
├── themes/             ← submodules dos temas
├── docker-compose.yml  ← servidor local de desenvolvimento
├── hugo.toml           ← configuração principal do Hugo
├── AGENTS.md           ← referência para agentes AI
└── opencode.json       ← configuração do OpenCode
```

---

## content/

Todo o conteúdo em pt fica aqui (idioma padrão, sem subdiretório de idioma na URL).

```
content/
├── _index.md           ← front matter da home page
├── about/
│   └── index.md        ← página "Sobre"
├── posts/
│   ├── _index.md       ← front matter da listagem de posts
│   └── <slug>/
│       ├── index.md    ← conteúdo do post em pt
│       └── cover.png   ← imagem de capa (co-localizada)
├── search/
│   └── index.md        ← página de busca (necessária para o Fuse.js do Congo)
└── en/                 ← conteúdo em inglês (contentDir alternativo)
    ├── about/
    │   └── index.md
    ├── posts/
    │   └── <slug>/
    │       ├── index.md
    │       └── cover.png
    └── search/
        └── index.md
```

**Regra:** `content/en/` é o `contentDir` do idioma `en`. A estrutura interna deve espelhar `content/` para que as URLs sejam simétricas (`/posts/slug/` em pt, `/en/posts/slug/` em en).

---

## layouts/

Overrides de templates do Congo. Apenas arquivos que diferem do tema.

```
layouts/
├── _partials/
│   ├── article-language-switch.html  ← seletor de idioma dentro do artigo
│   ├── article-link.html             ← card de link de artigo customizado
│   ├── comments.html                 ← embed Giscus (override do Congo)
│   ├── logo.html                     ← logo customizado no header
│   └── home/
│       └── custom.html               ← layout customizado da home page
└── single.html                       ← template de artigo único (override)
```

---

## assets/

```
assets/
├── css/      ← CSS customizado (overrides e extensões do Congo)
└── img/
    ├── logo_blog.png       ← logo para tema claro
    └── logo_blog_dark.png  ← logo para tema escuro
```

---

## i18n/

Strings de UI por idioma. O Congo tem os seus próprios i18n; estes arquivos sobrescrevem ou complementam.

```
i18n/
├── pt.yaml   ← strings em português
└── en.yaml   ← strings em inglês
```

---

## archetypes/

Templates usados ao criar novos conteúdos via `hugo new`.

```
archetypes/
└── post/
    ├── index.md      ← template de post em pt
    └── index.en.md   ← template de post em en
```

---

## specs/

Specs do SDD. Uma pasta numerada por spec.

```
specs/
├── 001-hugo-setup/
├── 002-multilingual/
├── 003-content-structure/
├── 004-features/
├── 005-deployment/
├── 006-coderabbit/
└── 007-congo-migration/
```

Cada pasta contém `spec.md` (ou similar) e `tasks.md` com checklist.

---

## themes/

Submodules dos temas Hugo.

```
themes/
├── congo/      ← tema ativo (jpanther/congo)
└── PaperMod/   ← legado, não usado (mantido para rollback)
```

---

## .github/workflows/

```
.github/workflows/
└── deploy.yml  ← build Hugo + deploy GitHub Pages (trigger: push em main)
```

---

## Arquivos de configuração na raiz

| Arquivo | Propósito |
|---|---|
| `hugo.toml` | Configuração completa do Hugo: idiomas, tema, menus, params |
| `docker-compose.yml` | Servidor de dev local (porta 1313) |
| `opencode.json` | Config do agente OpenCode |
| `AGENTS.md` | Referência de arquitetura e convenções para agentes AI |
| `.coderabbit.yaml` | Configuração de review automatizado (CodeRabbit) |
| `.gitmodules` | Declaração dos submodules (congo, PaperMod) |
