---
created: 2026-01-23T18:28:22
changed: 2026-01-23T20:18:40
prior_commit: 9b176e1
---

# Externalise

Capture context for future use. Don't let insights, decisions, or learnings stay only in conversation - persist them to files.

## Why Externalise

- Conversations are ephemeral; files persist across sessions
- Future Claude instances can build on past work
- Reduces repetition ("we discussed this before...")
- Creates a searchable knowledge base

## What to Externalise

| Content Type | Where to Put It |
|--------------|-----------------|
| Workflow/behavior changes | CLAUDE.md or [[meta - git workflow]] |
| Conventions discovered | [[meta - file conventions]] or new meta file |
| Learnings from a session | Use `/reflect` to extract to learning files |
| Decisions made | Document in relevant meta file or create new one |
| Reusable patterns | Create a skill in `.claude/commands/` |
| Questions to explore | Create `question - <claim>.md` |
| Ideas for later | Create `idea - <claim>.md` |
| Rule conflicts between repos | `sub-conflict-resolution/conflict - date - subrepo.md` |

## When to Externalise

- **During work**: When you establish a pattern or make a decision
- **At session end**: Use `/reflect` on the session export
- **When corrected**: If the user corrects behavior, update docs via `/toclaude`
- **When something "should have happened"**: Per [[CLAUDE.md#meta-feedback-loop]]

## How to Externalise

1. **Identify** what should persist beyond this conversation
2. **Choose** the right file type (see [[meta - prefixes]])
3. **Write** with proper frontmatter (see [[meta - file conventions]])
4. **Link** using wiki links to connect related concepts
5. **Commit** per [[meta - git workflow]]

## Principle

When in doubt, externalise. It's easier to delete unnecessary files than to recreate lost context.

## Related

- [[meta - coding project structure]] - Full workflow for sprints, planning, and knowledge capture
- [[meta - file conventions]] - How to structure files
- [[meta - prefixes]] - Which prefix to use
- [[meta - git workflow]] - Commit immediately after creating
