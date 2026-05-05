# Spec 001 — Hugo Setup

**Status:** done  
**Data:** 2026-05-04 (padronização)  
**Objetivo:** Instalar Hugo extended, inicializar o site e adicionar PaperMod como submodule.

## Contexto

O projeto usa Hugo como SSG (Static Site Generator). A versão **extended** é obrigatória porque temas utilizados no projeto dependem de recursos de processamento avançado (como SCSS).

## Escopo

1. Disponibilizar Hugo extended em ambiente reproduzível.
2. Inicializar a estrutura base do site.
3. Versionar um tema como submodule.
4. Garantir build local sem erros.

## Fora de escopo

- Publicação em produção.
- Configuração de conteúdo bilíngue.

## Decisões aprovadas

- Runtime via Docker (`hugomods/hugo:exts`) para evitar dependência local.
- Tema PaperMod versionado como `git submodule`.
- Ambiente de desenvolvimento local via `docker-compose` na porta `1313`.

## Critérios de aceitação

1. Hugo extended disponível via container.
2. Estrutura inicial do site criada com sucesso.
3. Submodule do tema presente no repositório.
4. Build `hugo --minify` executa sem erro.

## Artefatos previstos

- `hugo.toml`
- `docker-compose.yml`
- `.gitmodules`
- `themes/PaperMod/`
- `.gitignore`

## Validação

- Build local com Hugo extended sem erros.

## Referência de tarefas

- Ver `specs/001-hugo-setup/tasks.md`.
