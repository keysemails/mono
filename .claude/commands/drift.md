# /drift skill

Detect drift between documented intent and current reality.

## Usage
```
/drift [target]
```

## Target Options

- `(no argument)` - Analyze all active plans and specs
- `plan` - Focus on plan files
- `spec` - Focus on spec files
- `architecture` - Focus on architecture documentation
- `@filename` - Analyze specific file for drift

## Philosophy

Drift occurs when reality diverges from documented intent. This skill surfaces discrepancies so they can be consciously addressed - either by updating the documentation or by fixing the implementation.

## Instructions

### 1. Identify Sources of Truth

Gather documented intent from:
- Active `plan - *.md` files
- `spec - *.md` files
- `architecture - *.md` files
- `learning - *.md` files (expected patterns)

### 2. Analyze Drift Categories

#### Priority Drift
Are we working on what we said we'd work on?

- Compare current branch/commits to active plan
- Check if work aligns with stated priorities
- Identify scope creep or tangential work

#### Specification Drift
Does implementation match spec?

- Compare code behavior to spec requirements
- Check if all requirements are implemented
- Identify features that exist but aren't in spec

#### Knowledge Application Drift
Are documented learnings being applied?

- Cross-reference `learning -` files against recent code
- Check if known pitfalls are being avoided
- Identify repeated mistakes

#### Architectural Drift
Does code match documented architecture?

- Compare actual file structure to architecture docs
- Check if modules follow documented patterns
- Identify undocumented components

### 3. Create Drift Report

Create `memory/drift - <timestamp> - <claim>.md`:

```markdown
---
created: <timestamp>
changed: <timestamp>
prior_commit: <hash>
category: Drift Analysis
target: <what was analyzed>
---

# Drift Analysis: [Target Description]

## Summary

**Drift Level:** [Low/Moderate/Significant]

| Category | Status | Details |
|----------|--------|---------|
| Priority | [icon] | [brief] |
| Specification | [icon] | [brief] |
| Knowledge | [icon] | [brief] |
| Architectural | [icon] | [brief] |

## Priority Drift

### Current Work vs Planned Work

**Active Plan:** [[plan - timestamp - claim]]

**Planned:**
1. Action X
2. Action Y

**Actual (recent commits):**
- abc1234: Did Z instead
- def5678: Tangential work on W

**Assessment:** [Are we on track? Scope creeping? Blocked and pivoting?]

### Recommendations
1 - [Action to realign]
2 - [Or update plan to reflect new priorities]

## Specification Drift

### [[spec - claim]]

**Implemented but not in spec:**
- Feature X exists in code but isn't documented

**In spec but not implemented:**
- Requirement Y is specified but missing

**Divergent implementation:**
- Spec says A, code does B

### Recommendations
1 - [Update spec to match reality]
2 - [Fix implementation to match spec]

## Knowledge Application Drift

### Learnings Not Applied

**[[learning - claim]]** says: [principle]
- But [file:line](path#L42) does the opposite

### Recommendations
1 - [Apply the learning]
2 - [Or update learning if it's outdated]

## Architectural Drift

### Undocumented Components
- `src/new-module/` exists but isn't in architecture docs

### Pattern Violations
- Architecture says use pattern X
- But [file.ts](path/file.ts) uses pattern Y

### Recommendations
1 - [Update architecture docs]
2 - [Refactor to match architecture]

## Next Steps

Which drift items would you like to address? (e.g., "1.1, 2.2")
```

### 4. Drift Level Guide

- **Low** - Minor discrepancies, mostly documentation updates needed
- **Moderate** - Some implementation fixes needed, or intentional pivots not documented
- **Significant** - Major divergence between intent and reality, needs discussion

### 5. Commit

Per [[meta - git workflow]], commit after creating the drift report.

## Integration with /consistency

`/consistency` can invoke `/drift` for the drift-related portion of its analysis. The difference:

- `/consistency` - Broad project structure and inconsistency analysis
- `/drift` - Focused on intent vs reality across plans, specs, architecture

## Output

- Creates: `memory/drift - <timestamp> - <claim>.md`

The claim should summarize findings:
- `drift - 2026-01-24-1030 - significant spec drift in auth module.md`
- `drift - 2026-01-24-1030 - low drift all plans on track.md`

## When to Use

- Mid-sprint check-in
- Before major milestones
- When work feels unfocused
- After extended work sessions
- When returning to a project after time away

## Related

- [[meta - coding project structure]] - Plan and spec context
- [[meta - numbered lists for instructions]] - Selection pattern
- [[consistency]] - Broader project analysis
