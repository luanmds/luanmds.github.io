# AGENTS.md — luanmds.github.io

> Reference file for AI agents. Always keep it up to date after architectural changes.

---

## Project Overview

Bilingual static blog (Brazilian Portuguese as default + English) for publishing articles with images.
Hosted for free on GitHub Pages at `https://luanmds.github.io/`.

> For full context on the project, stack, architecture, conventions, and known concerns, see the **Context Routing Table** at the bottom of this file.

---

## Methodology: Spec-Driven Development (SDD)

**Mandatory flow:** `Spec (PLAN mode) → Verify and Validate → Create Tasks (Markdown) → Implement (code + tests)`

- **NEVER write code without an approved spec and tasks** in PLAN mode
- Tasks must be stored as `tasks.md` inside each spec folder (Markdown checklist format)
- MANDATORY: Create the spec in `specs/` folder, Verify and Validate the spec with user before continue 
- Any decision with 2+ valid options: **stop and ask the user**
- This file (`AGENTS.md`) must be updated whenever there are architectural changes
- After Implement phase, Validate the changes with user. If all ok, commit the changes and create a Pull Request in repository.


### Updating Specs and Tasks

- When update specs ALWAYS update the `tasks.md` in it.
- Check with all tasks from a specific spec are done. Else, ask the user if he wants to implement or to remove them. 

### Implement phase — Testing with Playwright

After completing the implementation of a spec, **always ask the user**:

> "Would you like to validate the implementation with automated browser tests using the Playwright skill?"

- If **yes**: invoke the `playwright-skill` skill immediately and run tests against the local dev server (`http://localhost:1313` via `docker compose up`). Fix any failures before proceeding.
- If **no**: skip and proceed to the validation/commit step.

The Playwright skill is located at `.opencode/skills/playwright/`. The dev server must be running before executing tests (`docker compose up -d`).

---

## SDD Specs

All specs are in `specs/` folder. Verify them when necessary.

| Spec | Description                 | Status    |
|------|-----------------------------|-----------|
| 001  | Hugo Setup                  | ✅ done   |
| 002  | Multilingual Configuration  | ✅ done   |
| 003  | Content Structure           | ✅ done   |
| 004  | Features (search/tags/etc.) | ✅ done   |
| 005  | Deploy GitHub Pages         | ✅ done   |
| 006  | CodeRabbit Configuration    | ✅ done   |

---

## Notes for Agents

- Hugo **extended** is required (Congo uses extended-only features)
- `baseURL` in `hugo.toml` is `https://luanmds.github.io/`
- Giscus `repoId` and `categoryId` are placeholders — user fills them in at [giscus.app](https://giscus.app)
- Docker creates files as `root` — always use `--user $(id -u):$(id -g)` or fix permissions afterwards
- Run `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify` to validate before committing
- GitHub Actions uses `peaceiris/actions-hugo@v3` with `extended: true`

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
