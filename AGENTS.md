# AGENTS.md — luanmds.github.io

> Operational repository contract for agents and maintainers. Update this file whenever project rules, architecture, validation, or local skills change.

## MANDATORY GUARDRAILS

The rules below apply regardless of the chosen workflow:

- Use Hugo **extended** for builds and validations.
- Never edit files inside `themes/congo/`; overrides must stay in the project.
- Validate relevant changes with the production build before closing work:
  `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify`
- Preserve bilingual conventions and the page bundle structure in `content/` and `content/en/`.
- Keep `AGENTS.md` and `.docs/` synchronized whenever rules, architecture, validation, or skills change.
- For browser-facing changes, offer automated validation with the `playwright-skill`.
- When starting any work branch, use the `github-branch-pr` skill.
- Do not commit directly to `main`.
- Follow Conventional Commits for all commits.

## Project Overview

Bilingual static blog (Brazilian Portuguese as default language and English under `/en/`) for publishing articles with images in page bundles.
Hosted on GitHub Pages at `https://luanmds.github.io/`.

This file is the starting reference. For durable and deeper context, use the routing table to `.docs/` at the end.

## Workflow Guidance

The repository supports direct work and Compozy artifact-driven flows. The choice depends on scope:

- Small, localized, or purely editorial changes can follow direct work, as long as guardrails and required validation are respected.
- Changes that benefit from structured exploration can use Compozy artifacts under `.compozy/tasks/`.
- If there are 2 or more valid direction options, stop and ask the user.

Before closing work:

1. Execute technical validation appropriate to the scope.
2. If there is browser impact, ask the user:
   "Would you like to validate the implementation with automated browser tests using the Playwright skill?"
3. Confirm user acceptance when that is part of the agreed flow.
4. Update corresponding tracking artifacts if the work uses Compozy PRD/tasks.
5. Only then prepare commit and Pull Request.

## Skills

Local skills live in `.agents/skills/`. OpenCode discovers `.agents/skills/<name>/SKILL.md` natively.

### Compozy reference

| Skill | Path | Purpose |
|---|---|---|
| `compozy` | `.agents/skills/compozy/` | Reference for Compozy workflow, CLI, artifacts, and commands |

### Compozy workflow skills

| Skill | Path | Purpose |
|---|---|---|
| `cy-create-prd` | `.agents/skills/cy-create-prd/` | Create PRDs focused on requirements and scope |
| `cy-create-techspec` | `.agents/skills/cy-create-techspec/` | Translate PRD into technical specification |
| `cy-create-tasks` | `.agents/skills/cy-create-tasks/` | Decompose PRD/TechSpec into executable tasks |
| `cy-execute-task` | `.agents/skills/cy-execute-task/` | Execute a PRD task end-to-end |
| `cy-review-round` | `.agents/skills/cy-review-round/` | Run a structured manual review round |
| `cy-fix-reviews` | `.agents/skills/cy-fix-reviews/` | Resolve exported review issues |
| `cy-final-verify` | `.agents/skills/cy-final-verify/` | Require fresh evidence before completion claims |
| `cy-workflow-memory` | `.agents/skills/cy-workflow-memory/` | Maintain shared memory per workflow |

### Project utility skills

| Skill | Path | Purpose |
|---|---|---|
| `playwright-skill` | `.agents/skills/playwright-skill/` | Browser automation and UI validation against `http://localhost:1313` |
| `content-review` | `.agents/skills/content-review/` | Editorial review of PT-BR/EN articles |
| `github-branch-pr` | `.agents/skills/github-branch-pr/` | Create branch and open draft PR to `main` following repository conventions |

## Notes for Agents

- `baseURL` in `hugo.toml` is `https://luanmds.github.io/`.
- Giscus remains disabled while `repoId` and `categoryId` are empty.
- Docker may create files as `root`; prefer `--user $(id -u):$(id -g)` or fix permissions afterward.
- GitHub Actions uses `peaceiris/actions-hugo@v3` with `extended: true`.
- CodeRabbit is configured for auto review with `drafts: false`; practical expectation is review on open PRs already in `Ready for review`.

## Context Routing Table

Detailed project context lives in `.docs/`. Use the table below to jump to the right source.

| Topic | File | What it covers |
|---|---|---|
| What is the project, purpose, author | [`.docs/project.md`](.docs/project.md) | Project identity, purpose, and audience |
| Technologies, dependencies, runtime | [`.docs/stack.md`](.docs/stack.md) | Hugo, Congo, Docker, GitHub Pages, OpenCode, CodeRabbit |
| Architecture decisions and why | [`.docs/architecture.md`](.docs/architecture.md) | SSG model, bilingual strategy, theme overrides, CI/CD |
| Naming, commits, guardrails, and what to avoid | [`.docs/conventions.md`](.docs/conventions.md) | Conventional Commits, branches, slugs, editorial rules |
| Folder structure and responsibilities | [`.docs/structure.md`](.docs/structure.md) | Directory structure, `.agents/skills/`, `.compozy/`, `specs/` |
| Testing strategy and how to validate | [`.docs/testing.md`](.docs/testing.md) | Hugo build, manual Playwright, known gaps |
| External services and APIs | [`.docs/integrations.md`](.docs/integrations.md) | GitHub Pages, Actions, Giscus, CodeRabbit |
| Known risks, technical debt, fragile parts | [`.docs/concerns.md`](.docs/concerns.md) | Operational risks and technical debt |
| What features exist today | [`.docs/features.md`](.docs/features.md) | Inventory of implemented blog capabilities |
| Article format, front matter, images, migration | [`.docs/articles.md`](.docs/articles.md) | Page bundles, front matter, images, compression |
