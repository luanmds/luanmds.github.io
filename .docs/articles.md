# articles.md

## Page Bundle

Cada artigo é um **Page Bundle** — uma pasta dedicada com `index.md` e todos os assets co-localizados.

```
content/posts/<slug>/
├── index.md      ← conteúdo e front matter
├── cover.png     ← imagem de capa (obrigatória)
└── imageN.png    ← imagens do corpo do artigo (opcional)
```

Para artigos bilíngues, a estrutura é espelhada:

```
content/posts/<slug-pt>/       ← versão em pt
content/en/posts/<slug-en>/    ← versão em en
```

---

## Front Matter

```yaml
---
title: "Título do Artigo"
date: 2026-04-27
draft: true
tags: ["tag1", "tag2"]
categories: ["categoria"]
summary: "Resumo do artigo exibido na listagem e em metatags."
cover:
  image: cover.png
  alt: "Descrição acessível da imagem de capa"
  relative: true
translationKey: "chave-unica"   # apenas em artigos bilíngues
---
```

### Campos

| Campo | Obrigatório | Descrição |
|---|---|---|
| `title` | sim | Título exibido no artigo e no `<title>` HTML |
| `date` | sim | Data de publicação (ISO 8601: `YYYY-MM-DD`) |
| `draft` | sim | `true` enquanto não publicado; `false` para publicar |
| `tags` | sim | Lista inline: `["tag1", "tag2"]` — minúsculas, sem acentos |
| `categories` | sim | Lista inline com uma categoria principal |
| `summary` | sim | Texto curto (~150 chars) para listagem e Open Graph |
| `cover.image` | sim | Nome do arquivo da capa co-localizado no bundle |
| `cover.alt` | sim | Texto alternativo acessível da capa |
| `cover.relative` | sim | Sempre `true` (resolve relativo ao bundle) |
| `translationKey` | condicional | Obrigatório se o artigo tiver par em outro idioma |

### Regras de tags e categorias

- Tags em kebab-case sem acentos: `dotnet`, `system-design`, `boas-praticas`
- Uma categoria por artigo; categorias são mais amplas que tags
- Não criar tags/categorias com um único post — consolidar nas existentes

---

## Bilinguismo

Artigos com par nos dois idiomas devem ter o mesmo valor de `translationKey` em ambos os arquivos. O Congo usa essa chave para exibir o seletor de idioma e para ligar as páginas entre si.

```
content/posts/saga-pattern-resumo/index.md   → translationKey: "saga-pattern"
content/en/posts/saga-pattern-overview/index.md → translationKey: "saga-pattern"
```

Artigos sem par (somente pt ou somente en) **não usam** `translationKey`.

---

## Imagens

### Cover

- Arquivo: `cover.png` no bundle do artigo
- Dimensões recomendadas: **1200×630 px** (proporção Open Graph 1.91:1)
- O Hugo gera WebP automaticamente no build para navegadores modernos

### Imagens do corpo

- Nomeadas sequencialmente: `image1.png`, `image2.png`, …
- Referenciadas no Markdown por nome simples: `![alt](image1.png)`
- Não usar caminhos absolutos — `relative: true` garante a resolução pelo bundle

### Compressão

Antes de commitar, comprimir todos os PNGs com **pngquant** (via Docker):

```bash
docker run --rm -v $(pwd)/content:/imgs alpine sh -c "
  apk add --no-cache pngquant -q
  find /imgs -name '*.png' | xargs -I{} pngquant --force --ext .png --quality 80-95 --skip-if-larger {}
"
```

Redução típica: **40–70%** em diagramas. Imagens fotográficas/complexas podem não comprimir (o `--skip-if-larger` preserva o original nesses casos).

---

## Conteúdo Markdown

### Formatação

- Uma linha por parágrafo (sem quebras de linha manuais dentro do parágrafo)
- Listas tight: sem linhas em branco entre os itens
- Links inline: `[texto](url)` — nunca URLs nuas no meio do texto
- Negrito: `**termo**` — usar com moderação para termos técnicos relevantes
- Itálico: `*termo*` — para estrangeirismos e ênfase suave
- Código inline: `` `func()` `` — para qualquer trecho de código ou nome de símbolo

### Blocos de código

Sempre especificar a linguagem na abertura da fence:

````markdown
```csharp
public class Exemplo { }
```
````

Linguagens mais usadas: `csharp`, `bash`, `yaml`, `json`, `sql`, `go`

### Headings

- `## H2` — seções principais do artigo
- `### H3` — subseções
- Nunca usar `# H1` no corpo (o título já vem do front matter)
- Não pular níveis (H2 → H4)

---

## Criando um novo artigo

```bash
# 1. Criar o bundle via archetype
hugo new posts/<slug>/index.md

# 2. Para a versão em inglês (se bilíngue)
hugo new --contentDir content/en posts/<slug-en>/index.md

# 3. Adicionar imagens no bundle e comprimir
docker run --rm -v $(pwd)/content/posts/<slug>:/imgs alpine sh -c "
  apk add --no-cache pngquant -q
  find /imgs -name '*.png' | xargs -I{} pngquant --force --ext .png --quality 80-95 --skip-if-larger {}
"

# 4. Validar o build
docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify
```
