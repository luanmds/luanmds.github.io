## 1. Giscus setup

- [x] 1.1 Enable GitHub Discussions for the repository and collect the Giscus repository and category identifiers.
- [x] 1.2 Update `hugo.toml` to enable article comments by default and fill in the Giscus configuration values.

## 2. Template verification

- [x] 2.1 Confirm the existing comments partial still renders only on article pages when the Giscus configuration is complete.
- [x] 2.2 Ensure the comments widget follows the active page language for both Portuguese and English articles.

## 3. Docs and validation

- [x] 3.1 Update `.docs/features.md`, `.docs/integrations.md`, and `.docs/architecture.md` so the repo documentation reflects that Giscus is enabled.
- [x] 3.2 Run the Hugo production build and verify the comments widget on both PT and EN article pages in a browser.
