## Why

The blog currently has no built-in discussion layer on article pages, which makes it harder for readers to leave feedback or continue conversations after publishing. Giscus adds comments without introducing a custom backend, so this is a lightweight way to make the site more interactive now.

## What Changes

- Add Giscus-powered comments to blog post pages.
- Configure the site to load the comments widget only where it belongs, without affecting the homepage or list pages.
- Preserve bilingual content structure so comments work consistently for both Portuguese and English articles.
- Rely on the existing GitHub-backed Giscus model instead of introducing a separate comment service.

## Capabilities

### New Capabilities
- `giscus-comments`: Enable and render Giscus comments on article pages, including the required site configuration and page-level integration.

### Modified Capabilities
- 

## Impact

Affected areas include Hugo theme overrides, site configuration, and the blog post layout used for article pages. The change also depends on the GitHub repository being configured as a Giscus discussion source.
