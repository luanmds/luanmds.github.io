# AGENTS.md

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

Bilingual static blog on Hugo, published on GitHub Pages, with Brazilian Portuguese as default language and English under `/en/`.

This file is the starting reference. For durable and deeper context, use the routing table to `.docs/` at the end.

## Workflow Guidance

Use the lightest workflow that fits the scope:

- Small, localized, or purely editorial changes can follow direct work, as long as guardrails and required validation are respected.
- Larger or riskier changes can use temporary planning, tracking, or review artifacts when helpful.
- Durable project knowledge should be consolidated into `.docs/` rather than left in tool-specific workflow artifacts.
- If there are 2 or more valid direction options, stop and ask the user.

Before closing work:

1. Execute technical validation appropriate to the scope.
2. If there is browser impact, ask the user:
   "Would you like to validate the implementation with automated browser tests using the Playwright skill?"
3. Confirm user acceptance when that is part of the agreed flow.
4. Update any tracking artifacts in use and consolidate durable context into `.docs/` when needed.
5. Only then prepare commit and Pull Request.

## Skills

Local skills live in `.agents/skills/`. OpenCode discovers `.agents/skills/<name>/SKILL.md` natively.

Skills are optional helpers for local workflows and validation. Their presence does not define the repository's official process or durable documentation model.

### Project skills

| Skill | Path | Purpose |
|---|---|---|
| `playwright-skill` | `.agents/skills/playwright-skill/` | Browser automation and UI validation against `http://localhost:1313` |
| `content-review` | `.agents/skills/content-review/` | Editorial review of PT-BR/EN articles |
| `github-branch-pr` | `.agents/skills/github-branch-pr/` | Create branch and open draft PR to `main` following repository conventions |
| `cy-create-prd` | `.agents/skills/cy-create-prd/` | Create PRDs focused on requirements and scope |
| `cy-create-techspec` | `.agents/skills/cy-create-techspec/` | Translate PRD into technical specification |
| `cy-create-tasks` | `.agents/skills/cy-create-tasks/` | Decompose PRD/TechSpec into executable tasks |
| `cy-execute-task` | `.agents/skills/cy-execute-task/` | Execute a PRD task end-to-end |
| `cy-review-round` | `.agents/skills/cy-review-round/` | Run a structured manual review round |
| `cy-fix-reviews` | `.agents/skills/cy-fix-reviews/` | Resolve exported review issues |
| `cy-final-verify` | `.agents/skills/cy-final-verify/` | Require fresh evidence before completion claims |
| `cy-workflow-memory` | `.agents/skills/cy-workflow-memory/` | Maintain shared memory per workflow |

## Notes for Agents

- `baseURL` in `hugo.toml` is `https://luanmds.github.io/`.
- Docker may create files as `root`; prefer `--user $(id -u):$(id -g)` or fix permissions afterward.

## Context Routing Table

Detailed project context lives in `.docs/`. Use the table below to jump to the right source.

| Topic | File | What it covers |
|---|---|---|
| What is the project, purpose, author | [`.docs/project.md`](.docs/project.md) | Project identity, purpose, and audience |
| Technologies, dependencies, runtime | [`.docs/stack.md`](.docs/stack.md) | Stack and development tools |
| Architecture decisions and why | [`.docs/architecture.md`](.docs/architecture.md) | SSG model, bilingual strategy, theme overrides, CI/CD |
| Naming, commits, guardrails, and what to avoid | [`.docs/conventions.md`](.docs/conventions.md) | Conventions and repository guardrails |
| Folder structure and responsibilities | [`.docs/structure.md`](.docs/structure.md) | Directory structure, `.agents/skills/`, `.docs/`, `specs/` |
| Testing strategy and how to validate | [`.docs/testing.md`](.docs/testing.md) | Validation workflow and known gaps |
| External services and APIs | [`.docs/integrations.md`](.docs/integrations.md) | External integrations and configuration |
| Known risks, technical debt, fragile parts | [`.docs/concerns.md`](.docs/concerns.md) | Operational risks and technical debt |
| What features exist today | [`.docs/features.md`](.docs/features.md) | Inventory of implemented blog capabilities |
| Article format, front matter, images, migration | [`.docs/articles.md`](.docs/articles.md) | Editorial format and article workflow |
