# /goal skill

Create a goal file to capture the problem, desired outcome, and preferences for a sprint or feature.

## Usage
```
/goal [brief description]
```

## Instructions

### 1. Gather Goal Information

If a brief description was provided, use it as a starting point. Otherwise, ask the user:

> What problem are we solving?

Then gather:
- **Problem** - What's wrong or missing?
- **Desired Outcome** - What does success look like?
- **Preferences** - Constraints, priorities, user preferences

Use the [[meta - numbered lists for instructions]] pattern if presenting options for any of these.

### 2. Create Goal File

Create `memory/goal - <timestamp> - <claim>.md`:

```markdown
---
created: <timestamp>
changed: <timestamp>
prior_commit: <hash>
---

# Goal: [Brief description]

## Problem

[What problem are we solving?]

## Desired Outcome

[What does success look like?]

## Preferences

[User preferences, constraints, priorities]

## Related

<!-- Links added after planning -->
```

The claim should be a brief description of the goal, e.g.:
- `goal - 2026-01-23-1420 - add user authentication.md`
- `goal - 2026-01-23-1420 - improve terrain rendering performance.md`

### 3. Commit

Per [[meta - git workflow]], commit after creating the goal file.

### 4. Offer Next Steps

After creating the goal, offer:

> Goal created: [[goal - <timestamp> - <claim>]]
>
> Next steps:
> 1 - Create a proposal to explore approaches (Recommended)
> 2 - Jump to spec (approach is already clear)
> 3 - Start work immediately (small task)

For larger features, recommend creating a proposal first to explore approaches and make decisions before defining requirements. For well-understood small tasks with clear approaches, spec or immediate work may be appropriate.

## Linking to Proposal and Plan

When a proposal or plan is created for this goal (via `/sprint-start` or manually), update the goal's Related section:

```markdown
## Related

- [[proposal - 2026-01-23-1430 - user authentication approaches]]
- [[plan - 2026-01-23-1500 - add user authentication]]
```

## Output

- Creates: `memory/goal - <timestamp> - <claim>.md`

## Related

- [[meta - coding project structure]] - Full workflow context
- [[meta - file conventions]] - Naming and frontmatter standards
- [[meta - git workflow]] - Commit strategy
- [[/proposal]] - Proposal creation skill (follows goal)
