# AGENTS.md — luanmds.github.io

> Reference file for AI agents. Always keep it up to date after architectural changes.

---

## Project Overview

Bilingual static blog (Brazilian Portuguese as default + English) for publishing articles with images.
Hosted for free on GitHub Pages at `https://luanmds.github.io/`.

---

## Methodology: Spec-Driven Development (SDD)

**Mandatory flow:** `Spec (PLAN mode) → Tasks (SQL) → Implement (code)`

- **NEVER write code without an approved spec and tasks** in PLAN mode
- Any decision with 2+ valid options: **stop and ask the user**
- This file (`AGENTS.md`) must be updated whenever there are architectural changes

---

## Tech Stack

| Layer          | Technology                             |
|----------------|----------------------------------------|
| SSG            | Hugo extended v0.154.5                 |
| Theme          | PaperMod (git submodule)               |
| Content        | Markdown + Hugo Page Bundles           |
| Languages      | pt (default `/`) + en (`/en/`)         |
| Search         | Fuse.js (PaperMod native, client-side) |
| Comments       | Giscus (GitHub Discussions)            |
| Local dev      | Docker (hugomods/hugo:exts)            |
| Hosting        | GitHub Pages                           |
| CI/CD          | GitHub Actions                         |
| Repository     | luanmds/luanmds.github.io              |

---

## Architecture and Project Structure

```
luanmds.github.io/
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD: build Hugo extended → deploy GitHub Pages
├── archetypes/
│   └── post/                   # Template for new posts (Page Bundle)
│       ├── index.md            # pt template
│       └── index.en.md         # en template
├── assets/                     # Custom CSS/JS (theme overrides)
├── content/                    # pt content (default language)
│   ├── posts/
│   │   └── <slug>/
│   │       ├── index.md        # pt content
│   │       └── cover.png       # Co-located image
│   ├── about/index.md
│   ├── search/index.md
│   └── en/                     # en content (contentDir for English)
│       ├── posts/
│       │   └── <slug>/
│       │       ├── index.md    # en content
│       │       └── cover.png
│       ├── about/index.md
│       └── search/index.md
├── i18n/
│   ├── pt.yaml                 # UI strings in Portuguese
│   └── en.yaml                 # UI strings in English
├── layouts/
│   └── partials/
│       └── comments.html       # Giscus embed
├── static/                     # Static files (favicon, etc.)
├── themes/
│   └── PaperMod/               # Submodule: adityatelange/hugo-PaperMod
├── docker-compose.yml          # Local dev: hugo server on port 1313
├── hugo.toml                   # Main Hugo configuration
├── AGENTS.md                   # This file
└── specs/                      # SDD specs (one folder per spec)
    ├── 001-hugo-setup/
    ├── 002-multilingual/
    ├── 003-content-structure/
    ├── 004-features/
    └── 005-deployment/
```

---

## Content Pattern: Page Bundles

Each post is a **Leaf Bundle** (a folder with `index.md`):

```
content/posts/my-article/
├── index.md        # pt — front matter + content
└── cover.png       # Co-located cover image

content/en/posts/my-article/
├── index.md        # en — front matter + content
└── cover.png
```

**Default front matter (`index.md`):**
```yaml
---
title: "Article Title"
date: 2026-04-21
draft: false
tags: ["tag1", "tag2"]
categories: ["category"]
summary: "Article summary"
cover:
  image: cover.png
  alt: "Image description"
  relative: true
---
```

---

## Language Configuration

- **pt** → base URL `/` (default), contentDir: `content/`
- **en** → base URL `/en/`, contentDir: `content/en/`
- Language switcher available in the header (PaperMod native)
- UI strings: `i18n/pt.yaml` and `i18n/en.yaml`

---

## Configured Features

| Feature       | Implementation                   | Status       |
|---------------|----------------------------------|--------------|
| Search        | Fuse.js + JSON index             | ✅ active    |
| Tags          | Hugo native taxonomy             | ✅ active    |
| Comments      | Giscus (GitHub Discussions)      | ✅ partial*  |
| Dark mode     | PaperMod native                  | ✅ active    |
| RSS Feed      | Hugo native                      | ✅ active    |
| Sitemap       | Hugo native                      | ✅ active    |
| Robots.txt    | Hugo native                      | ✅ active    |

> *Giscus: `repoId` and `categoryId` must be filled in `hugo.toml` after setting up at [giscus.app](https://giscus.app).

---

## SDD Specs

| Spec | Description                 | Status    |
|------|-----------------------------|-----------|
| 001  | Hugo Setup                  | ✅ done   |
| 002  | Multilingual Configuration  | ✅ done   |
| 003  | Content Structure           | ✅ done   |
| 004  | Features (search/tags/etc.) | ✅ done   |
| 005  | Deploy GitHub Pages         | ✅ done   |

---

## Git — Branching and Commits

### Main branch

The repository's principal branch is **`main`**. Every deployment is triggered by a push to it.

### Branch naming

Branches must follow the **Conventional Commits** pattern:

```
<type>/<short-scope>
```

| Type | Use | Example |
|------|-----|---------|
| `feat` | New feature or content | `feat/post-intro-to-go` |
| `fix` | Bug fix or incorrect content | `fix/broken-link-about` |
| `chore` | Maintenance, configs, dependencies | `chore/update-papermod` |
| `docs` | Documentation (AGENTS.md, specs) | `docs/spec-006-seo` |
| `style` | Visual tweaks / CSS overrides | `style/heading-font` |
| `refactor` | Restructuring without behavior change | `refactor/reorganize-content` |
| `ci` | GitHub Actions workflow changes | `ci/add-link-checker` |

### Commit messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description in imperative mood>

[optional body]

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

**Examples:**
```
feat(posts): add article about docker networking
fix(i18n): correct portuguese translation for read_time key
chore(theme): update PaperMod submodule to latest
docs(agents): translate AGENTS.md to English
```

---

## Local Development

```bash
# Start development server (port 1313)
docker compose up

# Production build
docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify

# New pt post
mkdir -p content/posts/my-article
# Create content/posts/my-article/index.md using archetypes/post/index.md as base

# Update theme submodule
git submodule update --remote themes/PaperMod
```

---

## Notes for Agents

- Hugo **extended** is required (PaperMod uses extended-only features)
- `baseURL` in `hugo.toml` is `https://luanmds.github.io/`
- Giscus `repoId` and `categoryId` are placeholders — user fills them in at [giscus.app](https://giscus.app)
- Docker creates files as `root` — always use `--user $(id -u):$(id -g)` or fix permissions afterwards
- Run `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify` to validate before committing
- GitHub Actions uses `peaceiris/actions-hugo@v3` with `extended: true`

