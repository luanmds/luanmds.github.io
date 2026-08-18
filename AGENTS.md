# AGENTS.md

Short operational entry point for agents working in this repository. Keep this file simple and always update it; durable project context belongs in `.docs/`.

## Project

Personal bilingual Hugo blog published on GitHub Pages.

- Default language: Brazilian Portuguese at `/`
- English content: `/en/`
- Production URL: `https://luanmds.github.io/`
- Canonical context: `.docs/`

## Non-Negotiables

- Use Hugo **extended** for builds and validation.
- Do not edit `themes/congo/`; customize through project overrides such as `layouts/`, `assets/`, and `static/`.
- Preserve bilingual structure and Page Bundles under `content/` and `content/en/`.
- Keep durable rules, architecture, validation, and workflow knowledge synchronized between this file and `.docs/`.
- Do not commit directly to `main`.
- Use Conventional Commits.

## Work Flow

- Prefer the lightest process that safely fits the change.
- If two or more valid implementation directions exist, ask before choosing.
- For content work, follow `.docs/articles.md`.
- For layout, theme, or browser-facing changes, check `.docs/architecture.md`, `.docs/structure.md`, and `.docs/testing.md`.
- When starting a work branch, use the `github-branch-pr` skill.
- Before a commit or PR, validate the relevant scope and update `.docs/` if durable project knowledge changed.

## Required Validation

Run the production build before closing relevant changes:

```bash
docker run --rm --user $(id -u):$(id -g) -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify
```

For browser-impacting changes, offer automated validation:

> Would you like to validate the implementation with automated browser tests using the Playwright skill?

## Local Skills

Project skills live in `.agents/skills/`.

| Skill | Use |
|---|---|
| `playwright-skill` | Browser automation and UI validation against `http://localhost:1313` |
| `content-review` | Editorial review of PT-BR/EN articles |
| `github-branch-pr` | Create a branch and draft PR to `main` following repo conventions |

## Docs Map

| Need | Read |
|---|---|
| Project identity and audience | `.docs/project.md` |
| Stack and tools | `.docs/stack.md` |
| Architecture and major decisions | `.docs/architecture.md` |
| Repository conventions | `.docs/conventions.md` |
| Folder responsibilities | `.docs/structure.md` |
| Validation strategy | `.docs/testing.md` |
| External integrations | `.docs/integrations.md` |
| Known risks and debt | `.docs/concerns.md` |
| Current features | `.docs/features.md` |
| Article format and workflow | `.docs/articles.md` |
