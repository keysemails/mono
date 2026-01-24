# /consistency skill

Generate a consistency report analyzing project structure and checking for inconsistencies.

## Usage
```
/consistency [focus-area]
```

## Instructions

When invoked, create a `consistency - <date>-<time> - <claim>.md` file in `memory/` that contains:

### 1. Project Structure Map (optional for focused analyses)

For full analysis, list all files as a nested bullet list organized by prefix. After each file, add a `#` followed by a brief explanation (one phrase).

**Note:** When using a `[focus-area]`, the structure map can be omitted to keep the report focused on the specific concern.

```markdown
## Project Structure

- **meta** (system/conventions)
  - [[meta - file conventions]] # naming, YAML frontmatter, flat hierarchy rules
  - [[meta - git workflow]] # branching, commit strategy
  - [[meta - prefixes]] # list of standard file prefixes
- **plan** (multi-phase work)
  - [[plan - session automation]] # automate context collection
- **idea** (brainstorms)
  - [[idea - terrain brushes]] # procedural terrain editing concept
- **c** (concepts)
  - [[c - an action is a logical unit of work]] # defines action granularity
```

Group by prefix, then list files alphabetically within each group.

### 2. Inconsistency Analysis

Scan files for these types of inconsistencies:

#### a) Planned but not done
- Find `plan` and `idea` files
- Check if their described work exists (implementations, follow-up files)
- List incomplete plans with their outstanding items

#### b) Principle violations
- Extract principles/rules from `meta` files
- Check if other files respect those principles
- Examples:
  - YAML frontmatter missing when meta says it's required
  - Nested folders when meta says flat hierarchy
  - Files without proper prefixes

#### c) Orphaned references
- Wiki links that point to non-existent files
- Files not referenced by any MOC

#### d) Stale content
- Files with old `changed` dates that reference "upcoming" work
- Plans marked complete but referencing incomplete items

#### e) Implemented todos
- Scan `todo - *.md` files (ignore `solved - *.md` files)
- For each todo:
  - Read the todo's description/summary
  - Check if the described work already exists (skill created, feature implemented, etc.)
  - If work appears complete, report as "possibly implemented"
- When user confirms a todo is solved:
  - Rename from `todo - ...` to `solved - ...` per [[meta - handle renames for wiki link files]]
  - Update all wiki links pointing to the old name

### 3. Report Format

Use the [[meta - numbered lists for instructions]] pattern so users can select which issues to act upon.

```markdown
---
created: <timestamp>
changed: <timestamp>
prior_commit: <hash>
---

# Consistency Report - <date>

## Project Structure

<nested bullet list with explanations>

## Inconsistencies Found

1 - Planned But Not Done
  - 1.1 - <plan/idea file> - <outstanding item>
  - 1.2 - ...

2 - Principle Violations
  - 2.1 - <file> - <violation description> (per [[meta - x]])
  - 2.2 - ...

3 - Orphaned References
  - 3.1 - [[link]] in <file> - target not found

4 - Stale Content
  - 4.1 - <file> - <issue>

5 - Implemented Todos
  - 5.1 - [[todo - timestamp - claim]] - <evidence of completion>

## Summary

- X files analyzed
- Y inconsistencies found
- Highest priority: <recommendation>

Which items would you like to address? (e.g., "1.1, 2.3")
```

## Workflow

1. **Scan** - Read all files in `memory/` directory
2. **Map** - Build the structure tree grouped by prefix
3. **Analyze** - Check for each inconsistency type
4. **Report** - Create the consistency file with findings
5. **Commit** - Per [[meta - git workflow]]
6. **Act** - When user selects items to address, fix them
7. **Link** - After fixing, add nested wiki link under the item per [[meta - numbered lists for instructions]]

### Updating Report After Fixes

When an issue is addressed, update the consistency report to link the result:

**Before:**
```markdown
1 - Principle Violations
  - 1.1 - [[session - old name]] - missing timestamp in filename
```

**After fixing (renaming the file):**
```markdown
1 - Principle Violations
  - 1.1 - [[session - old name]] - missing timestamp in filename
    - [[session - 2026-01-23-1400 - descriptive claim]]
```

This creates a traceable record of what was found and how it was resolved.

## Options

If `[focus-area]` is provided:
- `meta` - Focus on convention compliance
- `plans` - Focus on plan completion status
- `links` - Focus on orphaned references
- `readme` - Focus on README completeness vs actual project state
- `todos` - Focus on implemented todos that should be renamed to `solved`
- (omit) - Full analysis (includes project structure map)

Focused analyses may omit the project structure map to keep reports concise.

## Output

Creates: `memory/consistency - <date>-<time> - <claim>.md`

The claim should summarize findings, e.g.:
- `consistency - 2026-01-23-1420 - 3 incomplete plans found.md`
- `consistency - 2026-01-23-1420 - no major issues.md`
