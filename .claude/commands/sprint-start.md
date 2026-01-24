# /sprint-start skill

Orchestrate sprint initialization: create goal, proposal, spec, and plan, then get user approval before implementation.

## Usage
```
/sprint-start [brief description]
```

## Instructions

### 1. Create Goal

If a goal doesn't already exist for this work, use the [[/goal]] skill pattern:

1. Ask what problem we're solving (if not provided)
2. Gather desired outcome and preferences
3. Create the goal file

If user provides a brief description, use it to bootstrap the goal.

### 2. Create Proposal

After goal creation, use the [[/proposal]] skill pattern:

1. Explore possible approaches to achieve the goal
2. Identify trade-offs for each approach
3. List decision points that need resolution
4. Create the proposal file
5. Present approaches for user selection

### 3. Draft Spec

After proposal decisions are made, use the [[/spec]] skill pattern:

1. Extract requirements based on the selected approach
2. Identify known constraints
3. List open questions
4. Create the spec file

### 4. Create Plan

Create `memory/plan - <timestamp> - <claim>.md`:

```markdown
---
created: <timestamp>
changed: <timestamp>
prior_commit: <hash>
---

# Plan: [What we're building]

## Goal

[[goal - <timestamp> - <claim>]]

## Proposal

[[proposal - <timestamp> - <claim>]]

## Spec

[[spec - <feature name>]]

## Actions

1. [Action 1]
2. [Action 2]
3. [Action 3]

## Created Artifacts

<!-- Links added during implementation -->
```

Break down the work into concrete actions. Each action should be:
- Specific and achievable
- One logical unit of work (one commit)
- Ordered by dependency

### 5. Present for Approval

Display the plan to the user:

```markdown
## Sprint Ready for Approval

**Goal:** [[goal - <timestamp> - <claim>]]
**Proposal:** [[proposal - <timestamp> - <claim>]]
**Spec:** [[spec - <feature name>]]
**Plan:** [[plan - <timestamp> - <claim>]]

### Actions

1. [Action 1]
2. [Action 2]
3. [Action 3]

---

Ready to start? (y/n/adjust)
```

### 6. Handle Response

| Response | Action |
|----------|--------|
| `y` / `yes` | Begin implementation with first action |
| `n` / `no` | Ask what changes are needed |
| `adjust` | Allow user to modify plan, spec, or goal |
| Specific feedback | Update the relevant file and re-present |

### 7. Scope Warning

If the plan has many actions (>5) or touches many areas, warn:

> This plan covers [X actions across Y areas]. Consider splitting into:
> 1. [Subset A] - focused on [goal A]
> 2. [Subset B] - focused on [goal B]
>
> Would you like to proceed as one plan or split?

User decides whether to proceed or split.

### 8. Link Files

Ensure all files are cross-linked:

**Goal file:**
```markdown
## Related

- [[proposal - timestamp - claim]]
- [[spec - feature name]]
- [[plan - timestamp - claim]]
```

**Proposal file:**
```markdown
## Related

- [[spec - feature name]]
- [[plan - timestamp - claim]]
```

**Spec file:**
```markdown
## Related

- [[goal - timestamp - claim]]
- [[proposal - timestamp - claim]]
```

**Plan file already links to goal, proposal, and spec via their sections.**

### 9. Commit

Per [[meta - git workflow]], commit after creating each file.

## During Sprint

After approval, work through actions:

1. **Mark progress** in the plan file:
   ```markdown
   2. [Action 2]
      - Progress: In progress
   ```

2. **Surface issues immediately** - Don't silently proceed with assumptions

3. **Update plan** if approach changes - Use [[meta - numbered lists for instructions]] to present options

4. **Link artifacts** - Add learnings, research, etc. to Created Artifacts section:
   ```markdown
   ## Created Artifacts

   - [[learning - api requires auth header]]
   ```

## Output

- Creates: `memory/goal - <timestamp> - <claim>.md`
- Creates: `memory/proposal - <timestamp> - <claim>.md`
- Creates: `memory/spec - <feature name>.md`
- Creates: `memory/plan - <timestamp> - <claim>.md`
- All files cross-linked

## Related

- [[meta - coding project structure]] - Full workflow context
- [[/goal]] - Goal creation skill
- [[/proposal]] - Proposal creation skill
- [[/spec]] - Spec creation skill
- [[meta - git workflow]] - Commit strategy
