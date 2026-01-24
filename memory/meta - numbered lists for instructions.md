---
created: 2026-01-23T18:14:06
changed: 2026-01-24T05:52:54
prior_commit: 278c6c5
---

# Numbered Lists for Instructions

A pattern for presenting structured information to users with selectable actions.

## Structure

Use a nested numbered list where:
- Top-level numbers represent categories (1, 2, 3...)
- Sub-items use decimal notation (1.1, 1.2, 2.1...)

**Output as plain markdown, not in a code block:**

1 - Category Name
  - 1.1 - First item in category
  - 1.2 - Second item in category
2 - Another Category
  - 2.1 - Item in second category

## Presenting for User Selection

After displaying the list, prompt for selection:

```
Which items would you like to act upon? (e.g., "1.1, 2.3 optional comment")
```

## Processing User Responses

User can respond with:
- Single item: `1.1`
- Multiple items: `1.1, 2.3, 3.2`
- Item with comment: `2.1 (add deadline)` or `2.1 - with extra context`

## Linking Results

When acting on a selection creates a file, add a nested wiki link under the original item:

**Before action:**
```markdown
1 - Principle Violations
  - 1.1 - Session file missing timestamp
  - 1.2 - Meta file missing frontmatter
```

**After fixing 1.1 (which renamed the file):**
```markdown
1 - Principle Violations
  - 1.1 - Session file missing timestamp
    - [[session - 2026-01-23-1400 - git workflow setup]]
  - 1.2 - Meta file missing frontmatter
```

This creates a traceable record:
- The original issue remains visible
- The resulting file is wiki-linked for navigation
- Unaddressed items stay as plain bullet points

For skills that create new files from selections (like `/reflect` creating `todo` or `learning` files), the same pattern applies:

**After creating a todo from item 2.1:**
```markdown
2 - Potential Tasks
  - 2.1 - Audit meta files for trigger gaps
    - [[todo - 2026-01-23-1933 - audit meta files for trigger gaps in CLAUDE.md]]
  - 2.2 - Another task (not yet acted upon)
```

## Auto-Selection for Single Options

When only one option exists, auto-select it instead of presenting a list. This reduces friction while still giving the user control.

**Pattern:**
```
Only one incomplete plan found: [[plan - 2026-01-24-1030 - add user auth]]

Next action: Implement login endpoint

continue? (Enter/n)
```

**Guidelines:**
- State what was found and that it's the only option
- Show relevant context (next action, status, etc.)
- Prompt for confirmation with a simple yes/no
- Accept Enter as confirmation for flow

**When to apply:**
- `/plan-continue` with one incomplete plan
- Task selection from a single-item list
- File selection when only one matches

**When NOT to apply:**
- Destructive actions (always require explicit confirmation)
- Actions with significant side effects
- When context suggests user wants to see options

## Use Cases

| Skill | Categories | Action on Selection |
|-------|------------|---------------------|
| `/consistency` | Planned But Not Done, Principle Violations, Orphaned References, Stale Content | Fix selected issues |
| `/reflect` | Learnings, Tasks, Incoherences, Questions | Create appropriate file type |
| `/showrules` | Rule sources by file | Read and cite selected rules |

## Benefits

- Clear visual hierarchy
- Unambiguous references
- Supports batch selection
- Allows inline comments
- Works well in terminal/chat interfaces

## Related

- [[meta - file conventions]] - File naming standards
- [[meta - processing]] - Processing workflows
