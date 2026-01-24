# /spec skill

Create or update a spec file to capture requirements, constraints, and open questions for a feature.

## Usage
```
/spec [feature name]
/spec @existing-spec   # Update existing spec
```

## Instructions

### 1. Check for Existing Spec

If `@existing-spec` is provided, resolve it per [[meta - processing]] and update that spec. Otherwise, create a new one.

### 2. Gather Spec Information

Ask the user or extract from context:

- **Requirements** - What must be true when done?
- **Known Constraints** - Technical limitations, dependencies
- **Open Questions** - Unknowns to resolve during implementation

If a goal file exists for this work, read it first to inform the spec.

### 3. Create Spec File

Create `memory/spec - <feature name>.md`:

```markdown
---
created: <timestamp>
changed: <timestamp>
prior_commit: <hash>
---

# Spec: [Feature name]

## Requirements

- [Requirement 1]
- [Requirement 2]

## Known Constraints

- [Constraint 1]
- [Constraint 2]

## Open Questions

- [Question 1]
- [Question 2]

## Related

<!-- Link to goal if exists -->
```

The claim should be the feature name, e.g.:
- `spec - user authentication.md`
- `spec - terrain brush system.md`

### 4. Commit

Per [[meta - git workflow]], commit after creating or updating the spec.

### 5. If Linked to Goal

If this spec was created for an existing goal, update the goal's Related section:

```markdown
## Related

- [[spec - feature name]]
```

## Updating Specs

Specs are **living documents**. Update them when:

- Requirements change or clarify
- New constraints are discovered
- Open questions are answered
- Implementation reveals new information

When updating, always:
1. Update the `changed` timestamp and `prior_commit`
2. Commit the change

### Answering Open Questions

When an open question is resolved, move it from "Open Questions" to either:
- **Requirements** (if it became a requirement)
- **Known Constraints** (if it became a constraint)
- Or simply remove it if no longer relevant

Add a brief note about the resolution:

```markdown
## Requirements

- API must use JWT tokens (resolved from: "What auth method?")
```

## Output

- Creates: `memory/spec - <feature name>.md`
- Or updates an existing spec file

## Related

- [[meta - coding project structure]] - Full workflow context
- [[meta - file conventions]] - Naming and frontmatter standards
- [[meta - git workflow]] - Commit strategy
