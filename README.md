# 📝 luanmds.github.io

A bilingual static blog (Brazilian Portuguese + English) for publishing technical articles with co-located images. Powered by Hugo extended, themed with Congo, and hosted on GitHub Pages.

**🌐 Live:** [https://luanmds.github.io](https://luanmds.github.io)  
**📦 Repository:** [github.com/luanmds/luanmds.github.io](https://github.com/luanmds/luanmds.github.io)

---

## ⚡ Quick Start

### 📋 Prerequisites

- **Hugo extended** v0.154.5+ (required — Congo uses extended-only SCSS compilation)
- **Docker** + Docker Compose (for local development)
- **Git** with submodule support

### 🚀 Local Development

Clone the repository with all submodules:

```bash
git clone --recurse-submodules https://github.com/luanmds/luanmds.github.io.git
cd luanmds.github.io
```

Start the local dev server:

```bash
docker compose up
```

Open `http://localhost:1313` in your browser. Changes to content, layouts, or styles auto-reload.

### 🏗️ Build for Production

Generate optimized static site:

```bash
hugo --minify
```

Output goes to `public/` directory.

### ✅ Validate Build

Verify the build with Hugo extended in Docker:

```bash
docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|-----------|---------|
| **Hugo extended** | ⚡ Static site generator — compiles Markdown + Go templates into HTML |
| **Congo** | 🎨 Active theme (Git submodule from `jpanther/congo`) |
| **GitHub Pages** | 🌍 Free static hosting |
| **GitHub Actions** | 🔄 CI/CD — automatic build and deploy on push to `main` |
| **Fuse.js** | 🔍 Client-side full-text search (native Congo integration) |
| **Giscus** | 💬 Comment system via GitHub Discussions (currently placeholder config) |

---

## ✨ Key Features

- **🌐 Bilingual Support** — Two language versions (PT default on `/`, EN on `/en/`) with language switching in header and article context switcher
- **🌙 Dark Mode** — Native dark/light theme toggle with system preference auto-detection
- **🔍 Client-Side Search** — Full-text search via Fuse.js, no backend required
- **🏷️ Taxonomies** — Tags (with dedicated page) and categories
- **📡 RSS Feeds** — Separate feeds for each language
- **📦 Page Bundles** — Articles organized as folders with co-located images and assets
- **📝 Markdown Authoring** — All content written in Markdown with YAML front matter
- **📱 Responsive Design** — Mobile-first layout via Congo theme
- **🔗 Breadcrumbs & Pagination** — Navigation aids in articles
- **📅 Future-Dated Posts** — Automatic handling of scheduled publications

---

## ⚙️ Configuration

### 📋 Main Config: `hugo.toml`

Core settings:
- `baseURL = "https://luanmds.github.io/"` — production URL (auto-adjusted for local dev)
- `languageCode = "pt-BR"` (default language)
- `defaultContentLanguage = "pt"`
- Menu configuration (Posts, Tags, Search, About, language/appearance switchers)
- **Giscus is currently disabled** — placeholder config (awaiting user setup at [giscus.app](https://giscus.app))

### 🎨 Theme Customizations

- **CSS overrides** in `assets/css/` (compiled via Hugo's SCSS processor)
- **Layout overrides** in `layouts/` (e.g., custom home, single post, search page)
- **Logo assets** in `assets/img/` (light/dark variants)
- **Theme color scheme** — set to `graphite` in config

### 🌍 Internationalization (`i18n/`)

Translation strings for UI elements (nav, pagination, search, etc.) in:
- `i18n/pt.yaml` — Brazilian Portuguese
- `i18n/en.yaml` — English

---

## 🔄 Development Workflow

This project follows **Spec-Driven Development (SDD)**.

### 📋 Workflow

1. **Spec** — Create spec in `specs/` folder (use `specs/000-template/spec.md` as template)
2. **Tasks** — Define implementation tasks in `specs/*/tasks.md` (Markdown checklist)
3. **Implement** — Write code, commit with Conventional Commits
4. **Test** — Validate with Playwright automated browser tests (if UI changes)
5. **Validate** — Run build, verify in local dev server, check all tasks marked Done
6. **PR** — Create pull request to `main` with task completion evidence

### 📚 Full Methodology

See `AGENTS.md` for complete Spec-Driven Development guide, including:
- When to ask the user for decisions
- How to update specs and tasks
- Testing strategy and Playwright integration
- Git worktree usage for isolated feature branches

### 🔍 Pre-Commit Validation

Always validate locally before committing:

```bash
docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify
```

### 🚀 Deployment

GitHub Actions automatically:
1. Pulls repo on push to `main`
2. Builds with Hugo extended
3. Deploys to GitHub Pages

Config: `.github/workflows/` (uses `peaceiris/actions-hugo@v3` with `extended: true`)

---

## 📚 Documentation Map

Detailed documentation is in `.docs/`. Use this table to find what you need:

| Topic | File | Contains |
|-------|------|----------|
| 📝 Project identity, author, purpose | [`.docs/project.md`](.docs/project.md) | What is the project, who built it, what problem it solves |
| 🛠️ Dependencies, versions, tools | [`.docs/stack.md`](.docs/stack.md) | Hugo version, theme, Docker setup, Fuse.js, Giscus |
| 🏗️ Architecture & design decisions | [`.docs/architecture.md`](.docs/architecture.md) | SSG model, bilingual strategy, theme overrides, CI/CD design |
| 📋 Naming, commits, front matter | [`.docs/conventions.md`](.docs/conventions.md) | Conventional Commits, slugs, article YAML fields, what to avoid |
| 📂 Folder structure & responsibilities | [`.docs/structure.md`](.docs/structure.md) | Purpose of every directory and subdirectory |
| ✅ Testing & validation strategy | [`.docs/testing.md`](.docs/testing.md) | Playwright skill usage, build-as-test, local validation process |
| 🔗 External services & integrations | [`.docs/integrations.md`](.docs/integrations.md) | GitHub Pages, Actions, Giscus setup, CodeRabbit configuration |
| ⚠️ Known risks & technical debt | [`.docs/concerns.md`](.docs/concerns.md) | Congo upgrade fragility, Giscus placeholder status, design system gaps |
| ✨ Complete feature inventory | [`.docs/features.md`](.docs/features.md) | Everything that works: search, dark mode, tags, comments, etc. |
| ✍️ Article authoring guide | [`.docs/articles.md`](.docs/articles.md) | Page bundle format, front matter fields, image handling, pngquant rules |

---

## ✍️ Writing Content

### 📦 Page Bundle Format

Articles live in `content/posts/article-slug/`:

```
content/
└── posts/
    └── my-article/
        ├── index.md        (article content + front matter)
        ├── cover.png       (cover image)
        └── [other images]
```

### 📄 Front Matter Example

```yaml
---
title: "Article Title"
description: "Short summary"
date: 2026-05-05
draft: false
tags: ["tag1", "tag2"]
categories: ["Category"]
translationKey: "my-article"  # Pair with same key in other language for switcher
---
```

### 🖼️ Image Handling

- **Cover image** — `cover.png` in the page bundle (auto-used in listings and article header)
- **Inline images** — Store in same folder, reference with `![alt text](image.png)`
- **Optimization** — Use `pngquant` to compress PNG files before committing (see `.docs/articles.md` for automation)

### 🌐 Bilingual Articles

To create a PT/EN article pair:

1. `content/posts/my-article/index.md` — Portuguese version with `translationKey: my-article`
2. `content/en/posts/my-article/index.md` — English version with same `translationKey`

Both will show language switcher in the article header.

See `.docs/articles.md` for complete authoring guide.

---

## 🧪 Testing & Validation

### 🔨 Build Validation

Test that Hugo can build without errors:

```bash
docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify
```

### 🖥️ Local Testing

Start the dev server and manually test:

```bash
docker compose up
# Visit http://localhost:1313
# Test language switching, dark mode, search, links, responsive design
```

### 🤖 Automated Browser Tests

After implementing UI changes, validate with Playwright:

1. Start dev server: `docker compose up -d`
2. Run Playwright tests: Use the `playwright-skill` (`.opencode/skills/playwright/`)
3. Fix any failures before committing

See `.docs/testing.md` for detailed test strategy.

### 👀 Code Review

CodeRabbit automatically reviews pull requests. Config in `.coderabbit.yaml`.

---

## ⚠️ Important Notes for Developers

- **⭐ Hugo extended is mandatory** — Congo theme requires SCSS transpilation, which only works with extended version
- **🔒 Docker user permissions** — Use `--user $(id -u):$(id -g)` flag or fix file ownership afterwards (Docker creates files as root by default)
- **📦 Git submodules** — Update after clone: `git submodule update --init --recursive`
- **💬 Giscus comments — DISABLED FOR NOW** — Currently uses placeholder config. To enable in the future: go to [giscus.app](https://giscus.app), configure repo, and update `repoId` and `categoryId` in `hugo.toml`
- **🔄 GitHub Actions** — Uses `peaceiris/actions-hugo@v3` with `extended: true` for CI/CD

---

## 🔗 Links

**👤 Author:** Luan Mello (Backend engineer, .NET specialist, distributed systems)

- 🐙 GitHub: [@luanmds](https://github.com/luanmds)
- 💼 LinkedIn: [luanmds](https://www.linkedin.com/in/luanmds/)
- ✍️ Medium: [@luanmds](https://luanmds.medium.com/)
- 📰 Dev.to: [@luanmds](https://dev.to/luanmds)

**🌐 Live Blog:** [https://luanmds.github.io](https://luanmds.github.io)  
**📦 GitHub Repo:** [github.com/luanmds/luanmds.github.io](https://github.com/luanmds/luanmds.github.io)

---

## 📄 License

This project is open source. The blog content (articles in `content/`) is authored by Luan Mello. The template, configurations, and customizations are available for reference and adaptation.
