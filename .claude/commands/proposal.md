# /proposal skill

Create a proposal file to explore approaches and decision points for a goal.

## Usage
```
/proposal [@goal-file]
```

## Instructions

### 1. Reference Goal

A proposal must connect to a goal. Resolve the goal reference:

- If `@goal-file` provided, use it
- If only one recent goal exists, auto-select it and confirm:
  > Found goal: [[goal - timestamp - claim]]
  >
  > Create proposal for this goal? (y/n)
- Otherwise, list recent goals for selection using [[meta - numbered lists for instructions]]

### 2. Explore Approaches

Based on the goal, identify possible approaches:

- What are the options for solving this?
- What are the trade-offs of each approach?
- What research or exploration might be needed?
- What decisions need to be made before proceeding?

Ask clarifying questions if needed to understand the solution space.

### 3. Create Proposal File

Create `memory/proposal - <timestamp> - <claim>.md`:

```markdown
---
created: <timestamp>
changed: <timestamp>
prior_commit: <hash>
---

# Proposal: [Brief description]

## Goal

[[goal - timestamp - claim]]

[Brief summary of the problem and desired outcome]

## Approaches

### 1 - [Approach A]

[Description]

**Pros:**
- [Advantage 1]
- [Advantage 2]

**Cons:**
- [Disadvantage 1]

### 2 - [Approach B]

[Description]

**Pros:**
- [Advantage 1]

**Cons:**
- [Disadvantage 1]
- [Disadvantage 2]

## Decision Points

<!-- Use [[meta - numbered lists for instructions]] pattern -->

1 - [Decision 1 description]
  - 1.1 - [Option A]
  - 1.2 - [Option B]

2 - [Decision 2 description]
  - 2.1 - [Option A]
  - 2.2 - [Option B]

## Open Questions

- [Question that needs research or exploration]
- [Uncertainty that affects approach selection]

## Related

<!-- Links added after decisions -->
```

The claim should describe what's being proposed, e.g.:
- `proposal - 2026-01-23-1420 - user authentication approaches.md`
- `proposal - 2026-01-23-1420 - terrain rendering optimization options.md`

### 4. Present for Selection

After creating the proposal, present decisions using [[meta - numbered lists for instructions]]:

```markdown
## Proposal Created

[[proposal - timestamp - claim]]

### Select Approach

1 - [Approach A] (Recommended)
2 - [Approach B]

### Decision Points

[Present each decision point for selection]
```

User selects approach and makes decisions.

### 5. Update Proposal with Selections

After user selects:

1. Add a `## Selected Approach` section with the chosen approach
2. Mark decisions as resolved with chosen option
3. Update `changed` timestamp

### 6. Commit

Per [[meta - git workflow]], commit after creating the proposal file.

### 7. Offer Next Steps

After selections are made:

> Proposal complete: [[proposal - timestamp - claim]]
>
> Selected: [Approach name]
>
> Next steps:
> 1 - Create spec based on selected approach
> 2 - Jump to planning (skip spec)
> 3 - Need more research first

For most cases, recommend creating a spec to capture requirements for the selected approach.

## Linking

When a spec or plan is created from this proposal, update the Related section:

```markdown
## Related

- [[spec - feature name]]
- [[plan - timestamp - claim]]
```

Also update the goal's Related section to include the proposal.

## Output

- Creates: `memory/proposal - <timestamp> - <claim>.md`
- Updates: Goal file's Related section

## Related

- [[meta - coding project structure]] - Full workflow context
- [[meta - file conventions]] - Naming and frontmatter standards
- [[meta - git workflow]] - Commit strategy
- [[/goal]] - Goal creation skill (precedes proposal)
- [[/spec]] - Spec creation skill (follows proposal)
