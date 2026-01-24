---
created: 2026-01-23T13:15:00
changed: 2026-01-24T05:12:43
prior_commit: 8955e5e
---

# Memory System for Code Projects

This guide explains how to use the `/memory` folder pattern in source code repositories to externalize knowledge discovered during development. The system supports AI-assisted coding by providing persistent context across sessions.

**Skills available:** `/goal`, `/proposal`, `/spec`, `/sprint-start` orchestrate the workflow described here.

This guide explains how to use the `/memory` folder pattern in source code repositories to externalize knowledge discovered during development. The system supports AI-assisted coding by providing persistent context across sessions.

## Purpose

The `/memory` folder captures:
- **Goals and requirements** before implementation
- **Proposals** exploring approaches and decision points
- **Specs** that evolve as understanding deepens
- **Plans** that track actions and link to created artifacts
- **Learnings** discovered during development
- **Decisions** and their rationale

This enables AI assistants to maintain context across sessions and reduces repetition ("we discussed this before...").

## Quick Start

To bootstrap the memory system in a new project:

1. Create the folder structure:
   ```
   project/
     memory/
       meta - file conventions.md   # (optional) Project-specific overrides
     CLAUDE.md                      # Project instructions
   ```

2. Add to `CLAUDE.md`:
   ```markdown
   ## Memory System

   See [[meta - coding project structure]] for the full workflow.
   ```

3. Create your first goal file when starting a feature.

## Core File Types

### Goal Files

**Format**: `goal - yyyy-mm-dd-hhmm - claim.md`

A snapshot capturing the problem, rough goal, and user preferences. Created at sprint/feature start.

```markdown
---
created: timestamp
changed: timestamp
prior_commit: hash
---

# Goal: [Brief description]

## Problem
[What problem are we solving?]

## Desired Outcome
[What does success look like?]

## Preferences
[User preferences, constraints, priorities]

## Related
- [[proposal - yyyy-mm-dd-hhmm - claim]] (created after goal)
- [[plan - yyyy-mm-dd-hhmm - claim]] (created after planning)
```

### Proposal Files

**Format**: `proposal - yyyy-mm-dd-hhmm - claim.md`

A document exploring approaches and decision points for achieving a goal. Created after goal, before spec.

```markdown
---
created: timestamp
changed: timestamp
prior_commit: hash
---

# Proposal: [Brief description]

## Goal
[[goal - yyyy-mm-dd-hhmm - claim]]

## Approaches

### 1 - [Approach A]
[Description, pros, cons]

### 2 - [Approach B]
[Description, pros, cons]

## Decision Points
[Numbered decisions using [[meta - numbered lists for instructions]]]

## Selected Approach
[Added after user selection]

## Related
- [[spec - claim]]
- [[plan - yyyy-mm-dd-hhmm - claim]]
```

### Spec Files

**Format**: `spec - claim.md`

A living document capturing requirements and known state. Linked from the plan, updated during replanning.

```markdown
---
created: timestamp
changed: timestamp
prior_commit: hash
---

# Spec: [Feature name]

## Requirements
[What must be true when done]

## Known Constraints
[Technical limitations, dependencies]

## Open Questions
[Unknowns to resolve during implementation]
```

### Plan Files

**Format**: `plan - yyyy-mm-dd-hhmm - claim.md`

A collection of actions to be taken. Updated while progressing - not immutable.

```markdown
---
created: timestamp
changed: timestamp
prior_commit: hash
---

# Plan: [What we're building]

## Goal
[[goal - yyyy-mm-dd-hhmm - claim]]

## Proposal
[[proposal - yyyy-mm-dd-hhmm - claim]]

## Spec
[[spec - claim]]

## Actions
1. [Action 1]
2. [Action 2]
   - Progress: ✓ Done
3. [Action 3]
   - Progress: In progress
   - [[learning - discovered constraint]]

## Created Artifacts
- [[learning - discovered constraint]]
- [[research - api investigation]]

## Learnings

<!-- Insights discovered during sprint execution -->
<!-- These can later be elevated to `learning -` files via /reflect -->

## Progress Log

<!-- Timestamped entries tracking work done -->
```

### Other File Types

See [[meta - prefixes]] for the complete list. Key types:
- `learning - claim.md` - Insights discovered during implementation
- `research - claim.md` - Investigation findings
- `bug - yyyy-mm-dd-hhmm - claim.md` - Bug reports
- `question - claim.md` - Open questions to explore

## Sprint Workflow

Sprints are **goal-driven chunks** - they end when the goal is achieved, not by calendar.

### Sprint Start

1. **Create goal file** - Define problem, desired outcome, preferences
2. **Create proposal** - Explore approaches, identify decision points
3. **Select approach** - User chooses from proposal options
4. **Draft spec** - Capture requirements based on selected approach
5. **Create plan** - List actions, link goal, proposal, and spec
6. **Get approval** - User reviews plan before implementation

### During Sprint

1. **Work in phases** - Report progress before moving to next phase
2. **Surface issues** - Missing knowledge or blockers → tell user immediately
3. **Update plan** - Link created artifacts, mark progress
4. **Capture findings** - Present via numbered list, user decides what to persist
5. **Log progress** - Add timestamped entries to Progress Log section
6. **Record learnings** - Add inline discoveries to Learnings section

#### Learnings Section

During sprint execution, record insights discovered:

```markdown
## Learnings

- API requires auth header even for public endpoints
- Batch processing >100 items causes timeout; need pagination
- Found existing utility in utils/string.ts that handles edge case
```

These inline learnings can later be elevated to `learning -` files via `/reflect` at sprint end.

#### Progress Log Section

Add timestamped entries tracking work done:

```markdown
## Progress Log

### 2026-01-24 10:30

Completed user authentication flow. Tests passing.
Discovered need for refresh token handling - added to open questions.

### 2026-01-24 14:15

Implemented refresh token. Ran into CORS issues - see [[learning - cors preflight for auth headers]].
```

Use `/progress` to auto-generate entries from recent commits, or write manually.

### Sprint End

1. **Verify goal achieved** - Does current state match desired outcome?
2. **Run /reflect** - Extract remaining learnings from session
3. **Retrospective** - What worked, what didn't, what to improve

## Planning Mode

### When to Plan

**Always plan for**:
- New features
- Non-trivial changes (multiple files, architectural decisions)

**Skip planning for**:
- Bug fixes with obvious solutions
- Single-line changes
- Documentation typos

### Scope Warnings

If a plan seems too large (many actions, touches many areas), warn the user:

> "This plan covers [X actions across Y areas]. Consider splitting into:
> 1. [Subset A] - focused on [goal A]
> 2. [Subset B] - focused on [goal B]
>
> Would you like to proceed as one plan or split?"

User decides whether to proceed or split.

### Plan Updates

During implementation, if issues arise:
1. **Surface immediately** - Don't silently proceed with assumptions
2. **Present options** - Use [[meta - numbered lists for instructions]] pattern
3. **Update plan** - If approach changes, update the plan file
4. **Link artifacts** - New learnings, research, etc. get linked in the plan

## Knowledge Capture

### During Implementation

When you discover something worth persisting:

1. **Present findings** via numbered list pattern:
   ```
   1 - Learning: API requires auth header even for public endpoints
     - 1.1 - Create learning file
     - 1.2 - Skip (keep in session only)
   ```

2. **User selects** which items to persist
3. **Create files** for selected items
4. **Link back to plan** - Update plan's "Created Artifacts" section

### At Session End

1. Run `/reflect` on the session export
2. Review extracted learnings, questions, incoherences
3. Approve which items to persist

### What to Capture

- **Learnings**: "API X requires Y" - things you'd want to know next time
- **Research**: Investigation results that inform future decisions
- **Questions**: Things that need exploration but weren't resolved
- **Incoherences**: Contradictions found between files or expectations

## AI Guidance

### Proactive Behavior

The AI should:
- **Read context at session start** - Check `meta - dynamic context.md` for recent activity overview
- **Create a plan** before implementing features
- **Report phase completion** before moving to next phase
- **Surface issues immediately** - Don't assume or proceed silently
- **Present findings** for user decision via numbered lists

### What NOT to Do

- Don't create learning files without user approval
- Don't proceed when blocked - surface the blocker
- Don't update plans silently - inform user of changes
- Don't assume user intent - ask when uncertain

## Inline Summaries and Consistency

**Principle**: It's acceptable to duplicate key info as inline summaries when the full detail lives in a linked file.

**Example**:
```markdown
## Planning Mode

Always plan for new features and non-trivial changes.
See [[meta - planning triggers]] for edge cases and examples.
```

**Benefit**: Quick reference without navigating. The `/consistency` skill can detect when summaries drift from their source files.

## Subprojects

Each project has its own `/memory` folder. See [[meta - subproject integration]] for:
- How subproject memory stays independent
- When root can link to subproject memory
- Cross-project reference conventions (explicit paths, not wiki links)

## Related

- [[meta - file conventions]] - Naming, YAML frontmatter, wiki links
- [[meta - prefixes]] - Complete list of file prefixes
- [[meta - externalise]] - When and how to capture context
- [[meta - numbered lists for instructions]] - User selection pattern
- [[meta - subproject integration]] - Multi-project setup
