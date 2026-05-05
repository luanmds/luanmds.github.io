# Spec 003 — Estrutura de Conteúdo

**Status:** done  
**Data:** 2026-05-04 (padronização)  
**Objetivo:** Definir Page Bundles, archetypes e criar posts de exemplo com imagens.

## Contexto

O conteúdo do blog segue padrão de **Page Bundle (Leaf Bundle)**, com cada post em pasta própria contendo `index.md` e assets co-localizados.

## Escopo

1. Definir padrão de diretórios para posts PT e EN.
2. Criar archetypes para acelerar produção de conteúdo.
3. Estruturar páginas institucionais mínimas em dois idiomas.

## Fora de escopo

- Migração de acervo legado externo.
- Otimização avançada de mídia.

## Decisões aprovadas

- Estrutura por bundle (`content/posts/<slug>/index.md` + mídia local).
- Front matter padronizado para metadados editoriais.
- Manutenção de equivalência entre conteúdo PT e EN.

## Critérios de aceitação

1. Archetypes de post disponíveis para PT e EN.
2. Páginas base (`about`, `search`) criadas em ambos idiomas.
3. Posts de exemplo com imagens renderizando corretamente no build.

## Artefatos previstos

- `archetypes/post/index.md`
- `archetypes/post/index.en.md`
- `content/about/index.md`
- `content/en/about/index.md`
- `content/search/index.md`
- `content/en/search/index.md`

## Validação

- Build local com processamento correto de imagens dos bundles.

## Referência de tarefas

- Ver `specs/003-content-structure/tasks.md`.
