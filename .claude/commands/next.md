# /next skill

Show actionable items across the project to decide what to work on next. Creates a snapshot file for tracking.

## Usage
```
/next
```

## Instructions

### 1. Scan Data Sources

Search `memory/` for actionable items:

| Source | Pattern | What to Find |
|--------|---------|--------------|
| Todos | `todo - *.md` | All todo files |
| Ideas | `idea - *.md` | All idea files |
| Incoherences | `incoherence - *.md` | All incoherence files |
| Questions | `question - *.md` | All question files |
| Unactioned reflections | `reflect - *.md` | Bullet points without wiki links |
| Pending prompts | All files | Untagged `{{ }}` blocks (no date stamp) |
| Stale plans | `plan - *.md` | Plans older than 7 days |

### 2. Check for Unactioned Reflection Items

For each reflect file, scan for bullet points that:
- Have a numbered index (e.g., `- 2.1 - some task`)
- Do NOT have a nested wiki link on the next line

These are items that were identified but not yet acted upon.

### 3. Create Next File

Create `memory/next - <timestamp> - actionable items snapshot.md`:

```markdown
---
created: <timestamp>
changed: <timestamp>
prior_commit: <hash>
---

# Actionable Items Snapshot

1 - Open Todos
  - 1.1 - [[todo - timestamp - claim]]
  - 1.2 - [[todo - timestamp - claim]]
2 - Ideas
  - 2.1 - [[idea - claim]]
3 - Incoherences
  - 3.1 - [[incoherence - claim]]
4 - Questions
  - 4.1 - [[question - claim]]
5 - Unactioned Reflections
  - 5.1 - "item text" (from [[reflect - timestamp - claim]])
6 - Pending Prompts
  - 6.1 - "prompt preview..." in [[filename]]
7 - Stale Plans
  - 7.1 - [[plan - timestamp - claim]] (N days old)
```

Omit empty categories entirely.

### 4. Present to User

Display the numbered list using the [[meta - numbered lists for instructions]] pattern as **plain markdown** (not in a code block). After the list, prompt:

Which would you like to work on? (e.g., "1.1" or "2.1 let's explore this")

### 5. Handle User Selection

When user selects an item:

| Category | Action |
|----------|--------|
| Todo (1.x) | Read the todo file and offer to start work on it |
| Idea (2.x) | Read the idea and offer to create a plan for it |
| Incoherence (3.x) | Read the issue and offer to resolve it |
| Question (4.x) | Read the question and offer to research/answer it |
| Unactioned reflection (5.x) | Offer to create the appropriate file type (todo/learning/etc) per the /reflect skill pattern |
| Pending prompt (6.x) | Read the file and offer to process the prompt |
| Stale plan (7.x) | Read the plan and offer to implement or archive it |

### 6. Update Next File with Results

Per [[meta - numbered lists for instructions]], when acting on a selection creates or modifies a file, add a nested wiki link under the original item in the next file:

**Before:**
```markdown
1 - Open Todos
  - 1.1 - [[todo - 2026-01-20-1400 - fix login redirect]]
```

**After working on 1.1 and completing it (renamed to solved):**
```markdown
1 - Open Todos
  - 1.1 - [[solved - 2026-01-20-1400 - fix login redirect]]
```

**After acting on an idea and creating a plan:**
```markdown
2 - Ideas
  - 2.1 - [[idea - automating context collection]]
    - [[plan - 2026-01-23-1800 - automate context collection]]
```

This creates a traceable record of what was addressed.

### 7. After Starting Work

Once the user confirms what to work on:
- If it requires a branch, ensure we're in a task branch
- Update the next file with results after each action
- Mark todos complete when finished
- Archive resolved incoherences

## Output

- Creates: `memory/next - <timestamp> - actionable items snapshot.md`
- Updates: The next file with wiki links as items are addressed

## Related

- [[meta - numbered lists for instructions]] - Numbered list pattern with result linking
- [[meta - processing]] - For handling pending prompts
- [[meta - file conventions]] - File patterns and naming
- [[meta - prefixes]] - The `next` prefix definition
