# AGENTS.md — luanmds.github.io

> Reference file for AI agents. Keep it updated after architectural or workflow changes.

---

## Project Overview

Bilingual static blog (Brazilian Portuguese as default + English) for publishing articles with images.
Hosted on GitHub Pages at `https://luanmds.github.io/`.

For full project context, use the Context Routing Table at the end of this file.

---

## Methodology: Spec-Driven Development (SDD)

Default flow:

`Align scope → Validate decisions → Spec (when applicable) → tasks.md → Implement → Technical validation → User validation → Playwright offer (when applicable) → Commit → Pull Request`

### Core rules

- SDD is the default for any task that changes behavior, architecture, templates, UX, content structure, or automation.
- Create specs in `specs/` and always start from `specs/000-template/spec.md` plus `specs/000-template/tasks.md`.
- Never write implementation code before the user validates the direction when a spec is required.
- Keep `tasks.md` synchronized with the real state of the work.
- Any decision with 2+ valid options: stop and ask the user.
- Update this file (`AGENTS.md`) whenever architecture, workflow, or local skill conventions change.
- When a task from `tasks.md` is completed, mark it as done before commit.

### Exceptions

- Content-only article creation is exempt from spec creation. Go directly to branch and PR flow.
- Low-risk maintenance or documentation work may skip spec creation only when the user explicitly approves that exception. In that case, work from an agreed plan and keep affected docs consistent.

### Validation and closure order

1. Run the technical validation defined in the spec or agreed plan.
2. Ask the user whether they want Playwright validation when the change affects browser behavior.
3. Confirm acceptance with the user.
4. Mark completed items in `tasks.md` when a spec exists.
5. Only then create the commit and Pull Request.

### Updating specs and tasks

- When a spec changes, update its `tasks.md` too.
- If a spec still has open tasks, ask the user whether to implement or remove them.

---

## Playwright Validation

After implementation that affects browser behavior, always ask the user:

> "Would you like to validate the implementation with automated browser tests using the Playwright skill?"

- If yes: invoke `playwright-skill`, run against `http://localhost:1313`, and fix failures before proceeding.
- If no: continue with the remaining validation and acceptance steps.
- Start the local server first with `docker compose up -d` when Playwright validation is requested.

The local Playwright skill lives at `.agents/skills/playwright-skill/`.

---

## Skills

Project skills live in `.agents/skills/`. OpenCode discovers `.agents/skills/<name>/SKILL.md` natively, so no `opencode.json` change is required for local skill discovery in this repository.

| Skill | Path | Purpose |
|---|---|---|
| `playwright-skill` | `.agents/skills/playwright-skill/` | Browser automation and UI validation against the local dev server |
| `content-review` | `.agents/skills/content-review/` | Review article drafts against the author's PT-BR/EN voice, structure, and SEO expectations |
| `github-branch-pr` | `.agents/skills/github-branch-pr/` | Create a branch following conventions and open a draft PR to `main` |

---

## SDD Specs

All specs are in `specs/`.

| Spec | Description                 | Status    |
|------|-----------------------------|-----------|
| 001  | Hugo Setup                  | ✅ done   |
| 002  | Multilingual Configuration  | ✅ done   |
| 003  | Content Structure           | ✅ done   |
| 004  | Features (search/tags/etc.) | ✅ done   |
| 005  | Deploy GitHub Pages         | ✅ done   |
| 006  | CodeRabbit Configuration    | ✅ done   |
| 007  | Congo Migration             | ✅ done   |
| 008  | Spec Template + Branding    | ✅ done   |
| 009  | SEO: JSON-LD + Goatcounter  | 🔲 proposed |

---

## Notes for Agents

- Hugo **extended** is required because Congo uses extended-only features.
- `baseURL` in `hugo.toml` is `https://luanmds.github.io/`.
- Giscus `repoId` and `categoryId` are placeholders that the user fills at `https://giscus.app/`.
- Docker can create files as `root`; prefer `--user $(id -u):$(id -g)` or fix permissions afterwards.
- Use `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify` before committing when you need a production build check.
- GitHub Actions uses `peaceiris/actions-hugo@v3` with `extended: true`.

---

## Context Routing Table

Detailed context documentation is in `.docs/`. Use the table below to find the right file for each topic.

| Topic | File | What it covers |
|---|---|---|
| What is the project, purpose, author | [`.docs/project.md`](.docs/project.md) | Project identity, domain, problem it solves |
| Technologies, dependencies, runtime | [`.docs/stack.md`](.docs/stack.md) | Hugo, Congo, Docker, GitHub Pages, tools |
| Architecture decisions and why | [`.docs/architecture.md`](.docs/architecture.md) | SSG model, bilingualism strategy, theme overrides, CI/CD |
| Naming, commits, conventions, what to avoid | [`.docs/conventions.md`](.docs/conventions.md) | Conventional Commits, SDD flow, front matter, slugs |
| Folder structure and responsibilities | [`.docs/structure.md`](.docs/structure.md) | Every directory and its purpose |
| Testing strategy and how to validate | [`.docs/testing.md`](.docs/testing.md) | Playwright skill, build-as-test, local validation |
| External services and APIs | [`.docs/integrations.md`](.docs/integrations.md) | GitHub Pages, Actions, Giscus, CodeRabbit |
| Known risks, technical debt, fragile parts | [`.docs/concerns.md`](.docs/concerns.md) | Congo updates, CI alerts, Giscus, design system |
| What features exist today | [`.docs/features.md`](.docs/features.md) | Complete inventory of implemented functionality |
| Article format, front matter, images, migration | [`.docs/articles.md`](.docs/articles.md) | Page bundle structure, front matter fields, image rules, pngquant |
