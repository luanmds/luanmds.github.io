---
name: github-branch-pr
description: "Create a branch and open a GitHub PR in this repo. Use when starting a change that follows Conventional Commits (branch) and opens a draft PR to main."
---

# GitHub Branch + PR (main)

Skill to create a branch that follows AGENTS.md conventions and open a draft PR on GitHub.

## When to use

- Start a change that needs a branch and PR
- Prepare a PR for review while still in draft

## Required inputs

- Branch type: feat|fix|chore|docs|style|refactor|ci
- Short scope: kebab-case slug, no spaces, no accents
- PR title (if missing, derive from the change goal)

## Flow

1. **Confirm requirements**
   - If there are 2+ valid options (e.g., branch type or scope), stop and ask the user.
   - The main branch is always `main`.

2. **Ensure a clean workspace**
   - Run `git status`.
   - If there are uncommitted files, ask whether to commit, stash, or continue.

3. **Update main**
   - `git checkout main`
   - `git pull --ff-only`

4. **Create the branch**
   - Format: `<type>/<short-scope>` (see AGENTS.md).
   - Example: `feat/post-introducao-ao-go`.
   - `git checkout -b <type>/<short-scope>`

5. **Make changes and commits**
   - Commits must follow Conventional Commits.
   - If needed, suggest a short, imperative commit message.

6. **Push the branch**
   - `git push -u origin <type>/<short-scope>`

7. **Open a draft PR**
   - Base: `main`.
   - Head: `<type>/<short-scope>`.
   - If `gh` is available:
     - `gh pr create --draft --base main --head <type>/<short-scope> --title "<title>" --body "<body>"`
   - Otherwise, open GitHub compare in a browser and create the PR.

8. **Switch to ready**
   - When there are no more updates, suggest changing the PR from draft to ready.

## Suggested PR body

```
## Summary
- [Short goal summary]

## Changes
- [Objective list of changes]

## Testing
- [How to validate: e.g., docker compose up, hugo --minify]

## Notes
- [Risks, follow-ups, or pending items]
```

## Quality criteria

- Branch follows the `<type>/<short-scope>` pattern.
- PR is in draft and targets `main`.
- PR title and body reflect the actual change goal.
- No pending decisions without user validation.
