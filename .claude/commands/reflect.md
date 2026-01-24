# /reflect skill

Analyze a file and extract learnings, tasks, incoherences, and questions into a reflection snapshot.

## Usage
```
/reflect @file [additional files...]
```

## Instructions

### 1. Resolve Files

Resolve `@file` references per [[meta - processing]]:
- Try exact path first
- Search for matching filename
- Report failed approaches
- If multiple matches, ask user to select

### 2. Analyze Content

Read the file(s) and extract:
- **Learnings** - Insights, knowledge, or understanding gained
- **Potential Tasks** - Actionable items that could be done
- **Incoherences** - Contradictions, unclear areas, or inconsistencies
- **Questions** - Open questions that emerged

### 3. Create Reflect File

Create `memory/reflect - <timestamp> - <claim>.md`:

```markdown
---
created: <timestamp>
changed: <timestamp>
prior_commit: <hash>
---

# Reflection on [[source-file]]

## Learnings
- 1.1 - <learning>
- 1.2 - <learning>

## Potential Tasks
- 2.1 - <task>
- 2.2 - <task>

## Incoherences
- 3.1 - <issue>

## Questions
- 4.1 - <question>
```

If reflecting on multiple files, list them all with wiki links.

### 4. Present to User

Display using the [[meta - numbered lists for instructions]] pattern as **plain markdown** (not in a code block):

1 - Learnings
  - 1.1 - \<learning\>
  - 1.2 - \<learning\>
2 - Potential Tasks
  - 2.1 - \<task\>
3 - Incoherences
  - 3.1 - \<issue\>
4 - Questions
  - 4.1 - \<question\>

Which items would you like to act upon? (e.g., "1.1, 2.3 optional comment")

### 5. Process User Selection

User responds with index numbers and optional comments:
- `1.1` - act on learning 1.1
- `2.3 (add deadline)` - act on task 2.3 with comment

### 6. Create Files for Selected Items

For each selected item, create the appropriate file:

| Category | Selection | Creates |
|----------|-----------|---------|
| Learning (1.x) | `1.1` | `memory/learning - <claim>.md` |
| Task (2.x) | `2.1` | `memory/todo - <timestamp> - <claim>.md` |
| Incoherence (3.x) | `3.1` | `memory/incoherence - <claim>.md` |
| Question (4.x) | `4.1` | `memory/question - <claim>.md` |

Each created file should:
- Have proper YAML frontmatter
- Wiki link back to the reflect file
- Include user's comment if provided
- Expand on the bullet point with more detail

### 7. Update Reflect File

For each acted-upon item, update the reflect file to include a wiki link:

Before: `- 1.1 - insight about X`
After: `- 1.1 - [[learning - insight about X]]`

Items not acted upon remain as plain bullet points.

### 8. Commit

Per [[meta - git workflow]], commit after each logical action.

## Output

- Creates: `memory/reflect - <timestamp> - <claim>.md`
- Optionally creates: learning, todo, incoherence, or question files based on user selection
- Updates reflect file with wiki links to created files

## Related

- [[meta - prefixes]] - File prefix reference
- [[meta - file conventions]] - Naming and frontmatter standards
- [[meta - git workflow]] - Commit strategy
- [[meta - numbered lists for instructions]] - Numbered list pattern for user selection
