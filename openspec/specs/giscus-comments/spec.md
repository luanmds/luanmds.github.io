# giscus-comments Specification

## Purpose

Enable a Giscus discussion area on blog articles so readers can leave feedback directly on posts in either language without adding a custom backend.

## Requirements

### Requirement: Article pages show the comments widget
The blog MUST render a Giscus comments widget on published article pages when comments are enabled for that page or site.

#### Scenario: Published article displays comments
- **WHEN** a visitor opens a published article page
- **THEN** the page shows a Giscus widget after the article content and footer
- **AND** the widget is not shown on the homepage, list pages, taxonomy pages, or other non-article pages

### Requirement: Widget uses the configured GitHub Discussions source
The blog MUST load Giscus using the configured GitHub repository and discussion category values.

#### Scenario: Configured source loads successfully
- **WHEN** the site has the required Giscus repository and category identifiers configured
- **THEN** the page loads the Giscus client script
- **AND** the widget connects to the configured GitHub Discussions source

### Requirement: Missing Giscus identifiers do not break the site
The blog MUST remain buildable and MUST omit the comments widget when the required Giscus identifiers are missing or empty.

#### Scenario: Unconfigured site omits the widget
- **WHEN** the site is built without the required Giscus identifiers
- **THEN** the article page still builds normally
- **AND** no broken comments container or external Giscus script is rendered

### Requirement: Widget language matches the page language
The blog MUST present the comments widget in the active page language so Portuguese and English articles provide a consistent localized experience.

#### Scenario: English article uses English widget text
- **WHEN** a visitor opens an English article page
- **THEN** the comments widget appears in English

#### Scenario: Portuguese article uses Portuguese widget text
- **WHEN** a visitor opens a Portuguese article page
- **THEN** the comments widget appears in Portuguese
