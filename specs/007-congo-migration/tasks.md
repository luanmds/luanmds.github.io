- [ ] Create branch `style/congo-migration-home-about` from `main`
- [ ] Add `.superpowers/` to `.gitignore` to avoid committing brainstorming artifacts

## Theme migration

- [ ] Add Congo theme as git submodule at `themes/congo` and update `.gitmodules`
- [ ] Switch `theme` in `hugo.toml` from `PaperMod` to `congo`
- [ ] Remove or disable PaperMod-only params from `hugo.toml`
- [ ] Add Congo-compatible params for appearance, search, article metadata, comments, and homepage behavior

## Multilingual and URL stability

- [ ] Keep current bilingual structure (`content/` and `content/en/`) and preserve menu links in PT/EN
- [ ] Keep current routes and slugs unchanged; do not add permalink changes that alter URLs
- [ ] Validate representative URLs in PT and EN after migration (home, about, posts, tags, search)

## Home + About customization (B1 / Grafite + Ciano)

- [ ] Create CSS override file in `assets/` with B1 palette tokens (grafite + ciano)
- [ ] Add moderate layout overrides in `layouts/` for home (hero curto + destaque + recentes)
- [ ] Rewrite `content/about/index.md` with structured PT sections based on public LinkedIn/GitHub data
- [ ] Rewrite `content/en/about/index.md` with equivalent structured EN sections

## In-article language switch

- [ ] Add a post-level language switch block in single-article layout using `.IsTranslated` + `.Translations`
- [ ] Keep global language selector in header active
- [ ] Add `translationKey` for existing PT/EN post pairs with different slugs
- [ ] Ensure posts without translation do not render the in-article switch block

## Feature parity checks

- [ ] Ensure Congo search is active and search pages (`content/search/index.md`, `content/en/search/index.md`) still work
- [ ] Ensure Giscus partial at `layouts/partials/comments.html` still renders when `showComments`/equivalent is enabled
- [ ] Ensure tags/categories listings still work in PT and EN
- [ ] Ensure dark mode toggle still works in the new theme
- [ ] Ensure RSS, sitemap, and robots.txt are still generated

## Validation and docs

- [ ] Run production build: `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify`
- [ ] Manually verify key pages locally via `docker compose up` (`http://localhost:1313`)
- [ ] Ask user: "Would you like to validate the implementation with automated browser tests using the Playwright skill?"
- [ ] If approved, run Playwright validation and fix issues before completion
- [ ] Update `AGENTS.md` if the migration changes architecture, structure, or operating conventions

## Refinamento 10.1 — Mobile Responsiveness (branch: fix/mobile-responsiveness)

- [x] Create branch `fix/mobile-responsiveness` from `main`
- [x] Switch `[params.header] layout` from `basic` to `hybrid` in `hugo.toml` (native Congo layout: hamburger on mobile, links on desktop — no override needed)
- [x] Add CSS in `assets/css/custom.css` for mobile image height constraint on post cards
- [x] Change `layouts/_partials/article-link.html`: `flex-row` → `flex-col sm:flex-row` on the `<article>` element
- [x] Adjust image CSS classes in `article-link.html` to be full-width when stacked vertically on mobile
- [x] Run production build and verify no errors
- [x] Ask user about Playwright validation before committing
- [x] Commit and open PR — https://github.com/luanmds/luanmds.github.io/pull/5

## Refinamento 10.2 — Favicon com logo (branch: fix/favicon-logo)

- [x] Create branch `fix/favicon-logo` from `main`
- [x] Generate `static/favicon-32x32.png` (32×32), `static/favicon-16x16.png` (16×16) and `static/apple-touch-icon.png` (180×180) from `assets/img/logo_blog.png` via center-crop + Pillow resize
- [x] Verify Congo picks up the files (`head.html` uses `favicon-32x32.png` and `favicon-16x16.png` from `static/` by default)
- [x] Run production build and verify no errors
- [x] Commit and open PR
