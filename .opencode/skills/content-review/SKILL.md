---
name: content-review
description: Use ONLY when the user explicitly requests a content review, text improvement, writing feedback on a blog article OR when there is a new article created in content/posts folder.
---

# Content Review — luanmds.github.io

## Overview

This skill guides article content review for Luan's blog. The goal is to help improve drafts so they match the author's established tone, voice, and structure — not to rewrite them into a generic "good article" style.

**Core principle:** Preserve the author's voice. Suggest changes that make the text sound *more like Luan*, not more formal.

---

## Author Voice Profile

### Tone
- Warm and conversational, never stiff or corporate
- First person throughout ("demonstrarei", "deixo", "para mim são sempre obrigatórias rs")
- Slight humor via parenthetical asides: `(eu devo estar velho!)`, `(rs)`, `Mas…e quando`
- Treats reader as a peer developer, not a student

### Language (PT-BR — primary)
- Brazilian Portuguese, informal register
- Uses idiomatic expressions: "pulga atrás da orelha", "tudo muito bonito"
- Ellipsis for conversational pauses: `Mas…e quando`
- Exclamation marks used sparingly for emphasis: `Muito Bom né?`
- Foreign and technical terms stay in English with italics: *Stubs*, *Message Brokers*, *checkout*

### Language (EN — translation)
- More formal than PT-BR but still approachable
- Mirrors PT-BR catchphrases (if present): "Enjoy the read!" → "Boa leitura!", "This is all Folks…" → "Isso é tudo pessoal…"
- Avoid over-translating casual expressions — keep the personality

---

## Article Structure Pattern

Every published post follows this structure:

| Section | Notes |
|---|---|
| **Intro paragraph** | States what the article covers + why it matters in bold. Optionally end with "Boa leitura!" (PT) or "Enjoy the read!" (EN) if it fits the tone. |
| **Repo callout** (if applicable) | Bold label like **Hands-on:** + repo link + short description |
| **H2 sections** with H3 subsections | Clear hierarchy, section names match the topic directly |
| **Tips/Dicas** | Blockquotes: `> Dica: ...` (PT) or `> Tip: ...` (EN) |
| **Conclusion** | Wraps up, points to repo, asks for feedback. Can optionally use the header "Isso é tudo pessoal…" (PT) / "This is all Folks…" (EN) if appropriate. |
| **References** | Plain list of links, always last |

---

## Formatting Conventions

- **Bold** for key technical terms on first use, important warnings, and callout labels
- *Italics* for English terms inside PT-BR text (and vice-versa), and book/tool names
- `code` for inline code references, method names, decorators, patterns
- Code blocks with language identifier (`csharp`, `bash`, etc.)
- Images referenced as `![Alt text](filename.png)` — always in page bundle
- Numbered lists for ordered steps; bullet lists for unordered items
- H3 sections under H2 use `####` for sub-sub-sections only when needed

---

## Review Checklist

When reviewing a draft, check each area and suggest specific improvements:

### Voice & Tone
- [ ] Does the intro explain what the reader will learn *and why it matters*?
- [ ] Suggest a "Boa leitura!" or "Enjoy the read!" opening only if it fits naturally with the intro's flow.
- [ ] Does the conclusion ask for feedback / invite community interaction? (Suggest "Isso é tudo pessoal..." only if it feels right).
- [ ] Are there natural conversational asides? (if none, suggest adding 1–2)
- [ ] Does it sound like a peer talking, not a documentation page?

### Structure
- [ ] Does it follow the intro → sections → conclusion → references pattern?
- [ ] Are H2/H3 titles clear and direct (not clever, not vague)?
- [ ] Is there a hands-on repo callout if there's a companion GitHub project?
- [ ] Tips/Dicas in blockquotes where applicable?

### Language Quality (PT-BR)
- [ ] Are technical English terms in italics when embedded in PT-BR text?
- [ ] Are there any machine-translation patterns to fix? (overly formal, strange word order)
- [ ] Do sentences read naturally when read aloud?

### Language Quality (EN)
- [ ] Does it preserve the author's personality vs. sounding like a generic tech blog?
- [ ] Are PT-BR catchphrases mirrored correctly?
- [ ] Grammar and naturalness check

### Technical Content
- [ ] Are code examples syntactically correct?
- [ ] Are linked references real URLs (not placeholders)?
- [ ] Is technical depth appropriate — detailed enough to be useful without being a textbook?

---

## How to Run a Review

1. Read the full draft once without stopping.
2. Identify the **3 biggest issues** (voice, structure, or clarity).
3. Apply the checklist above and collect all findings.
4. Output a structured review, followed by an explicit Execution Plan:

```
## Review: [Article Title]

### Summary
[1–2 sentences on overall state]

### Critical (must fix)
- [item]: [specific suggestion with example]

### Suggested (improves quality)
- [item]: [specific suggestion]

### Minor
- [item]: [small fix]

### Execution Plan
[List of exact changes you plan to apply to the file]
```

5. **CRITICAL:** DO NOT apply any fixes directly to the file at this stage. You MUST present the review and the Execution Plan first, and then explicitly ask the user for permission to implement the changes.
6. Only if the user explicitly approves the plan, apply the fixes exactly as planned, preserving everything that's already working.

---

## Common Issues to Watch For

| Issue | Symptom | Fix |
|---|---|---|
| Machine-translation tone | Too formal, unnatural word order | Rewrite key sentences to sound conversational |
| Missing intro transition | Intro jumps abruptly to content | Suggest a natural transition, optionally "Boa leitura!" if appropriate |
| No conclusion CTA | Article just stops after last section | Add a conclusion section with feedback ask, optionally titled "Isso é tudo pessoal…" |
| Over-bold | Every other word bolded | Keep bold only for first use of key terms + critical callouts |
| Missing italics on EN terms in PT-BR | `Message Brokers`, `Stubs` without formatting | Add italics: *Message Brokers*, *Stubs* |
| Generic section titles | "Section 1", "Introduction", "Conclusion" | Use descriptive topic titles |
| Missing references | No sources cited | Remind author to add references section |
| Weak intro | Doesn't explain *why* this matters | Add a sentence explaining the practical impact |

---

## Example: Good Intro vs. Weak Intro

**Weak:**
> Nesse artigo falarei sobre Testes de Integração.

**Strong (matches author style):**
> Nesse artigo vamos abordar de forma compilada os conceitos, definições e boas práticas gerais em Testes de Integração. No detalhe, entenderemos em quais cenários os testes de integração se encaixam, como implementar de forma fácil de manter, além de ver quando não usar mocks em seus cenários. **Compreender isso lhe capacita a tomar decisões relacionadas a testes automatizados e a medir o esforço necessário antes mesmo de implementar, usando qualquer linguagem de programação ou framework**.
>
> Boa leitura!

Key elements: compiled overview → specific sub-topics → **bold practical impact statement** → (Optional) "Boa leitura!"
