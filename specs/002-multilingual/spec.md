# Spec 002 — Configuração Multilíngue

**Status:** done  
**Data:** 2026-05-04 (padronização)  
**Objetivo:** Configurar suporte bilíngue pt (padrão) + en com seletor de idioma.

## Contexto

O blog é bilíngue. O idioma padrão é **Português (pt)** na raiz `/`, e o inglês é servido em `/en/`.

## Escopo

1. Configurar idiomas no `hugo.toml`.
2. Separar conteúdo PT e EN mantendo URLs previsíveis.
3. Garantir menus e i18n para os dois idiomas.

## Fora de escopo

- Tradução completa de todos os artigos existentes.
- Alterações visuais profundas de tema.

## Decisões aprovadas

- Idioma padrão em `pt` na raiz `/`.
- Inglês em `/en/` com conteúdo em `content/en/`.
- Uso de arquivos `i18n/pt.yaml` e `i18n/en.yaml` para strings de interface.

## Critérios de aceitação

1. Páginas PT e EN geradas corretamente.
2. Rotas de home, posts, busca e about funcionando em ambos idiomas.
3. Menus por idioma configurados sem conflitos.

## Artefatos previstos

- `hugo.toml` (bloco `[languages]`)
- `i18n/pt.yaml`
- `i18n/en.yaml`

## Validação

- Build local confirmando geração bilíngue.

## Referência de tarefas

- Ver `specs/002-multilingual/tasks.md`.
