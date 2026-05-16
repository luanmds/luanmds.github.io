# AGENTS.md — luanmds.github.io

> Contrato operacional do repositório para agentes e para o mantenedor. Atualize este arquivo quando regras do projeto, arquitetura, validação ou skills locais mudarem.

---

## Project Overview

Blog estático bilíngue (português brasileiro como idioma padrão e inglês em `/en/`) para publicação de artigos com imagens em page bundles.
Hospedado no GitHub Pages em `https://luanmds.github.io/`.

Este arquivo é a referência de entrada. Para contexto durável e aprofundado, use a tabela de roteamento para `.docs/` no final.

---

## Role of This File

`AGENTS.md` define o que é obrigatório para trabalhar neste repositório:

- resumo do projeto
- guardrails obrigatórios
- como as skills locais são descobertas e quando elas ajudam
- onde fica a documentação de contexto durável em `.docs/`

Ele não impõe um workflow único para todo tipo de mudança. Quando houver mais de uma abordagem válida, alinhe a decisão com o usuário em vez de presumir uma política rígida.

---

## Mandatory Guardrails

As regras abaixo valem independentemente do workflow escolhido:

- Use Hugo **extended** para builds e validações.
- Nunca edite arquivos dentro de `themes/congo/`; overrides devem ficar no projeto.
- Valide mudanças relevantes com o build de produção antes de encerrar o trabalho:
  `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify`
- Preserve as convenções bilíngues e a estrutura de page bundles em `content/` e `content/en/`.
- Mantenha `AGENTS.md` e `.docs/` sincronizados quando regras, arquitetura, validação ou skills mudarem.
- Para mudanças com impacto em browser, ofereça validação automatizada com a skill `playwright-skill`.
- Não faça commit direto em `main`.
- Siga Conventional Commits para todos os commits.

---

## Workflow Guidance

O repositório aceita trabalho direto e também fluxos orientados por artefatos do Compozy. A escolha depende do escopo:

- Mudanças pequenas, localizadas ou puramente editoriais podem seguir trabalho direto, desde que respeitem os guardrails e a validação necessária.
- Mudanças que se beneficiam de exploração estruturada podem usar os artefatos do Compozy em `.compozy/tasks/`.
- Se houver 2 ou mais opções válidas de direção, pare e pergunte ao usuário.

Antes de fechar um trabalho:

1. Execute a validação técnica apropriada ao escopo.
2. Se houver impacto em browser, pergunte ao usuário:
   "Would you like to validate the implementation with automated browser tests using the Playwright skill?"
3. Confirme a aceitação do usuário quando isso fizer parte do fluxo combinado.
4. Atualize os artefatos de tracking correspondentes se o trabalho estiver usando PRD/tasks do Compozy.
5. Só então prepare commit e Pull Request.

---

## Local Skills

Skills locais vivem em `.agents/skills/`. O OpenCode descobre `.agents/skills/<name>/SKILL.md` nativamente.

### Compozy reference

| Skill | Path | Purpose |
|---|---|---|
| `compozy` | `.agents/skills/compozy/` | Referência do fluxo, CLI, artefatos e comandos do Compozy |

### Compozy workflow skills

| Skill | Path | Purpose |
|---|---|---|
| `cy-create-prd` | `.agents/skills/cy-create-prd/` | Criar PRDs com foco em requisitos e escopo |
| `cy-create-techspec` | `.agents/skills/cy-create-techspec/` | Traduzir PRD em especificação técnica |
| `cy-create-tasks` | `.agents/skills/cy-create-tasks/` | Decompor PRD/TechSpec em tasks executáveis |
| `cy-execute-task` | `.agents/skills/cy-execute-task/` | Executar uma task de PRD end-to-end |
| `cy-review-round` | `.agents/skills/cy-review-round/` | Fazer rodada de review manual estruturada |
| `cy-fix-reviews` | `.agents/skills/cy-fix-reviews/` | Corrigir issues exportadas de review |
| `cy-final-verify` | `.agents/skills/cy-final-verify/` | Exigir evidência fresca antes de claims de conclusão |
| `cy-workflow-memory` | `.agents/skills/cy-workflow-memory/` | Manter memória compartilhada por workflow |

### Project utility skills

| Skill | Path | Purpose |
|---|---|---|
| `playwright-skill` | `.agents/skills/playwright-skill/` | Automação de browser e validação UI contra `http://localhost:1313` |
| `content-review` | `.agents/skills/content-review/` | Revisão editorial de artigos PT-BR/EN |
| `github-branch-pr` | `.agents/skills/github-branch-pr/` | Criar branch e abrir draft PR para `main` seguindo convenções do repo |

---

## Notes for Agents

- `baseURL` em `hugo.toml` é `https://luanmds.github.io/`.
- Giscus continua desabilitado enquanto `repoId` e `categoryId` estiverem vazios.
- Docker pode criar arquivos como `root`; prefira `--user $(id -u):$(id -g)` ou ajuste permissões depois.
- GitHub Actions usa `peaceiris/actions-hugo@v3` com `extended: true`.
- CodeRabbit está configurado para auto review com `drafts: false`; a expectativa prática é review em PRs abertos que já estejam `Ready for review`.

---

## Context Routing Table

Contexto detalhado do projeto fica em `.docs/`. Use a tabela abaixo para ir direto à fonte certa.

| Topic | File | What it covers |
|---|---|---|
| What is the project, purpose, author | [`.docs/project.md`](.docs/project.md) | Identidade do projeto, propósito e audiência |
| Technologies, dependencies, runtime | [`.docs/stack.md`](.docs/stack.md) | Hugo, Congo, Docker, GitHub Pages, OpenCode, CodeRabbit |
| Architecture decisions and why | [`.docs/architecture.md`](.docs/architecture.md) | Modelo SSG, bilinguismo, theme overrides, CI/CD |
| Naming, commits, guardrails, and what to avoid | [`.docs/conventions.md`](.docs/conventions.md) | Conventional Commits, branches, slugs, regras editoriais |
| Folder structure and responsibilities | [`.docs/structure.md`](.docs/structure.md) | Estrutura de diretórios, `.agents/skills/`, `.compozy/`, `specs/` |
| Testing strategy and how to validate | [`.docs/testing.md`](.docs/testing.md) | Hugo build, Playwright manual, lacunas conhecidas |
| External services and APIs | [`.docs/integrations.md`](.docs/integrations.md) | GitHub Pages, Actions, Giscus, CodeRabbit |
| Known risks, technical debt, fragile parts | [`.docs/concerns.md`](.docs/concerns.md) | Riscos operacionais e débito técnico |
| What features exist today | [`.docs/features.md`](.docs/features.md) | Inventário do que já existe no blog |
| Article format, front matter, images, migration | [`.docs/articles.md`](.docs/articles.md) | Page bundles, front matter, imagens, compressão |
