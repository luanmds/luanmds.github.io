# Spec 002 — Configuração Multilíngue

**Status:** ✅ done  
**Objetivo:** Configurar suporte bilíngue pt (padrão) + en com seletor de idioma.

## Contexto

O blog é bilíngue. O idioma padrão é **Português (pt)**, acessível na raiz `/`.
O inglês fica em `/en/` com seu próprio `contentDir` (`content/en/`).

## Decisões

- **Idioma padrão:** `pt` na raiz `/` (sem subdiretório)
- **Inglês:** `/en/` com `contentDir = "content/en"`
- **Seletor de idioma:** nativo do PaperMod (aparece no header automaticamente)
- **i18n:** arquivos `i18n/pt.yaml` e `i18n/en.yaml` com strings de UI

## Estrutura de URLs

| Conteúdo | URL pt | URL en |
|----------|--------|--------|
| Home | `/` | `/en/` |
| Posts | `/posts/` | `/en/posts/` |
| Tags | `/tags/` | `/en/tags/` |
| Busca | `/search/` | `/en/search/` |
| Sobre | `/about/` | `/en/about/` |

## Artefatos produzidos

| Arquivo | Descrição |
|---------|-----------|
| `hugo.toml` (bloco `[languages]`) | Configuração pt e en |
| `i18n/pt.yaml` | Strings de UI em português |
| `i18n/en.yaml` | Strings de UI em inglês |

## Tasks concluídas

- [x] Bloco `[languages.pt]` e `[languages.en]` no `hugo.toml`
- [x] `i18n/pt.yaml` e `i18n/en.yaml` criados
- [x] Menus separados por idioma configurados no `hugo.toml`
- [x] Build gera páginas PT e EN corretamente
