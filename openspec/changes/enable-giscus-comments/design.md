## Context

See `proposal.md` for the motivation. The repository already has Congo’s comments hook in place through `layouts/single.html` and `layouts/_partials/comments.html`, and `hugo.toml` already contains a `params.giscus` block with the repository name plus placeholder identifiers. The current blocker is that `repoId` and `categoryId` are empty, so the widget never renders.

## Goals / Non-Goals

**Goals:**
- Turn on Giscus for blog articles without changing the theme submodule.
- Keep the site build-safe when Giscus is not configured or is partially misconfigured.
- Preserve a bilingual experience so Portuguese and English posts both show a localized widget.
- Keep the change compatible with the current static-site, GitHub Pages deployment model.

**Non-Goals:**
- Building a custom comment backend or moderation system.
- Adding comments to home, list, taxonomy, or search pages.
- Reworking article layouts beyond the comment integration boundary.

## Decisions

- Use the existing Congo comment partial override instead of editing `themes/congo/`.
  - Rationale: the repo already follows the override pattern documented in `.docs/architecture.md`, and this keeps the integration upgrade-safe.
  - Alternative considered: patching the theme submodule directly. Rejected because it would be fragile and violate the repository’s non-negotiables.

- Enable comments through repository config and article-level defaults rather than hard-coding the widget into content files.
  - Rationale: comments are a site capability, not a per-post content concern for this blog.
  - Alternative considered: adding `showComments` to every post front matter. Rejected because it would create repetitive maintenance for a global feature.

- Keep the widget gated by the existing `repoId` and `categoryId` checks.
  - Rationale: the current partial already treats missing IDs as a safe no-op, which prevents broken pages and preserves build success while configuration is incomplete.
  - Alternative considered: rendering a placeholder or warning block in production. Rejected because it would expose an incomplete integration to readers.

- Let the widget language follow the active page language.
  - Rationale: the site is bilingual, so the comments UI should match the article language instead of forcing a single locale.
  - Alternative considered: using one fixed language for all visitors. Rejected because it would make one half of the site feel translated incorrectly.

- Use Giscus’ hosted client script.
  - Rationale: this keeps the implementation lightweight and avoids shipping or maintaining a local fork of the widget.
  - Alternative considered: self-hosting the client. Rejected because it adds complexity without a clear benefit for this blog.

## Risks / Trade-offs

- [External dependency on GitHub Discussions and giscus.app] → Keep the integration isolated behind the existing config gate so the site still works if the service is unavailable or misconfigured.
- [Client-side comments add a browser request on article pages] → Load the widget only on article pages where comments are enabled.
- [Localized widget behavior can drift if the page language config is wrong] → Verify the PT and EN article routes during browser validation.
- [Discussion threads depend on stable permalinks] → Preserve current post URL structure and avoid changing permalinks as part of this work.

## Migration Plan

1. Enable GitHub Discussions for the repository and choose the target discussion category in Giscus.
2. Populate the Giscus identifiers in `hugo.toml` and ensure article comments are enabled by default.
3. Build the site and verify that article pages render the widget only where expected.
4. If a rollback is needed, clear the Giscus identifiers or disable article comments in config and rebuild.
