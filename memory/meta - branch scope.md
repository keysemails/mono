---
created: 2026-01-23T19:25:33
changed: 2026-01-23T19:25:33
prior_commit: 322fae4
---

# Branch Scope

How to handle work that doesn't match the current branch's purpose.

## The Problem

A branch like `task/add-readme` has a clear scope. But during work, the user might request something unrelated (e.g., "fix the numbered list output format"). Silently continuing in the mismatched branch creates confusing git history.

## When to Check

Before starting new work, compare:
- **Current branch name**: What does `task/X` describe?
- **New work**: What is the user actually asking for?

If they don't match, the scope has changed.

## What to Do

Ask the user:

> "We're in `task/X` but this is new work (Y). Should I:
> 1. Merge the current branch first and create `task/Y`?
> 2. Continue in this branch?"

Then follow their choice.

## Why This Matters

- **Clear git history**: Each branch represents one logical task
- **Easy rollback**: Can revert a feature without touching unrelated work
- **Better PR reviews**: Reviewers see focused changesets

## Exceptions

Minor follow-up work directly related to the branch is fine to continue. Use judgment - if the work is a natural extension of the branch's purpose, no need to ask.

## Related

- [[meta - git workflow]] - Branch and commit strategy
- [[c - an action is a logical unit of work]] - What constitutes one commit
