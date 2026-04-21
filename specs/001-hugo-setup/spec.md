# Spec 001 — Hugo Setup

**Status:** ✅ done  
**Objetivo:** Instalar Hugo extended, inicializar o site e adicionar PaperMod como submodule.

## Contexto

O projeto usa Hugo como SSG (Static Site Generator). A versão **extended** é obrigatória pois o tema PaperMod utiliza processamento SCSS disponível apenas nessa variante.

Para não poluir o ambiente local, Hugo é executado via **Docker** (`hugomods/hugo:exts`).

## Decisões

- **Runtime:** Docker (`hugomods/hugo:exts`) em vez de instalação local → ambiente limpo e reproduzível
- **Tema:** PaperMod adicionado como `git submodule` → fácil atualização com `git submodule update --remote`
- **Dev local:** `docker-compose.yml` com `hugo server` na porta 1313

## Artefatos produzidos

| Arquivo | Descrição |
|---------|-----------|
| `hugo.toml` | Configuração principal do Hugo |
| `docker-compose.yml` | Servidor de desenvolvimento local |
| `.gitmodules` + `themes/PaperMod/` | Submodule do tema |
| `.gitignore` | Ignora `public/`, `resources/_gen/`, `.hugo_build.lock` |

## Tasks concluídas

- [x] Hugo extended disponível via Docker `hugomods/hugo:exts`
- [x] `hugo new site . --force` executado
- [x] PaperMod adicionado como submodule em `themes/PaperMod`
- [x] `hugo.toml` base criado
- [x] Build `hugo --minify` validado sem erros
