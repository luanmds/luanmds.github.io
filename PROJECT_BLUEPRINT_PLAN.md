# 🚀 Project Blueprint: luanmds-blog (SDD Version)

This repository follows the **Spec-Driven Development (SDD)** methodology. All implementation must be preceded by a technical specification to ensure consistency, context optimization, and performance.

## 1. Project Summary

A personal blog and technical content hub focused on high performance and SEO, built with Astro. The repository centralizes code (Astro) and content assets (Markdown + Images).

- **Repo Name:** `luanmds-blog`
    - Still not created
- **Framework:** Astro
- **Hosting:** Vercel (CI/CD via GitHub)
- **Methodology:** Spec-Driven Development (SDD)
- **Project Management Tool:** Github Projects
    - Link: https://github.com/users/luanmds/projects/4

---

## 2. Structured Planning (SDD Focus)

| **Section** | **Definition** |
| --- | --- |
| **Objective** | Migrate Medium articles to a self-owned platform optimized for AI-assisted development. |
| **Business Case** | Full data ownership, high-performance SEO, and a professional technical showcase. |
| **SDD Workflow** | Spec (What) -> Design (How) -> Tasks (Action) -> Impl (Code). |
| **Core Stack** | Astro, Markdown/MDX, Tailwind CSS, Vercel. |
| **Success Metrics** | 100 Lighthouse Score; Zero build errors; 100% image migration success. |

---

## 3. Context Architecture (Repo Structure)

To enable effective SDD, the repository is structured to provide immediate context to AI agents:

Plaintext

`luanmds-blog/
├── specs/                  # "Source of Truth" documentation
│   ├── blog-spec.md        # Feature specifications
│   └── tech-design.md      # Architecture decisions (Astro/Tailwind)
├── apps/
│   └── web/                # Astro Project (Back + Front)
│       ├── src/content/    # Articles in Markdown
│       └── src/assets/     # Optimized images
├── AGENTS.md               # Global instructions for AI Agents (Cursor/Copilot/Claude)
├── package.json            # Build scripts and workspace config
└── README.md               # Instructions for humans`

---

## 4. SDD Implementation Roadmap

### Phase 1: Context Initialization (Discovery)

- [ ]  Create `AGENTS.md` defining coding standards (e.g., "Always use functional components", "Images must have alt text").
- [ ]  Create `specs/blog-spec.md` detailing how Medium articles should be rendered.
- [ ]  Define the **Astro Content Collections** schema (tags, date, author).

### Phase 2: Technical Setup & Infra

- [ ]  Initialize monorepo structure within `apps/web`.
- [ ]  Configure **Astro Image Service** to process local images.
- [ ]  Set up Vercel + GitHub integration.

### Phase 3: Assisted Migration (Optimized)

- [ ]  Develop/run a migration script to convert Medium HTML to Markdown.
- [ ]  Ensure the script extracts image URLs and saves them locally in `src/assets/`.
- [ ]  Validate generated files against the defined **Spec**.

### Phase 4: UI Development & SEO

- [ ]  Implement responsive layout based on the Tech Design Doc.
- [ ]  Generate Sitemap and RSS Feed (critical for Medium migration).
- [ ]  Deploy and validate Core Web Vitals.

---

## 5. PM Notes & Next Steps

> **PM Alert:** Since Medium images may vary in resolution, it is crucial to keep the assets folder organized by subfolders (e.g., `src/assets/images/post-slug/`) for easier maintenance.
> 

**Immediate Next Task:**

1. Initialize the Astro project using the structure above.
2. Provide the `AGENTS.md` and `specs/blog-spec.md` files to your AI agent to begin the automated implementation.