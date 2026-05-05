# Spec 005 — Deploy GitHub Pages

**Status:** done  
**Data:** 2026-05-04 (padronização)  
**Objetivo:** Automatizar build e deploy no GitHub Pages via GitHub Actions.

## Contexto

O repositório publica o blog no GitHub Pages usando pipeline de CI/CD em vez do modo clássico com branch dedicada.

## Escopo

1. Criar workflow de build com Hugo extended.
2. Publicar artefato no GitHub Pages.
3. Garantir paridade de versão do Hugo entre local e CI.

## Fora de escopo

- Provisionamento de infraestrutura fora do GitHub.
- Estratégias multi-ambiente (staging/prod).

## Decisões aprovadas

- Deploy via GitHub Actions.
- Uso de `peaceiris/actions-hugo@v3` com `extended: true`.
- Publicação com `actions/deploy-pages@v4`.

## Critérios de aceitação

1. Workflow `deploy.yml` executa em push para `main`.
2. Build Hugo finaliza sem erro.
3. Artefato é publicado no GitHub Pages.

## Artefatos previstos

- `.github/workflows/deploy.yml`
- `hugo.toml` (baseURL e parâmetros de publicação)

## Validação

- Build local de produção sem erros.
- Verificação do site publicado após push para `main`.

## Referência de tarefas

- Ver `specs/005-deployment/tasks.md`.
