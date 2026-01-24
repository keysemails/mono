# /todo skill

Quickly create todo files in memory folder. Can create from input or extract from files.

## Usage
```
/todo [description]
/todo @file
/todo @file "specific item to extract"
```

## Instructions

### Mode Detection

Determine which mode based on input:

| Input | Mode |
|-------|------|
| `/todo fix the bug in auth` | Quick create - single todo with given description |
| `/todo @somefile` | File scan - extract todos from file content |
| `/todo @somefile "the specific thing"` | Targeted extract - create todo for specific item in file |

### Quick Create Mode

When given a description directly:

1. Get current timestamp via `date +%Y-%m-%dT%H:%M:%S` and `date +%Y-%m-%d-%H%M`
2. Get current commit hash via `git rev-parse --short HEAD`
3. Create `memory/todo - <timestamp> - <claim>.md`:

```markdown
---
created: <ISO timestamp>
changed: <ISO timestamp>
prior_commit: <hash>
---

# <Description as title>

## Description

<Expand the brief description into actionable context>

## Related

- (add wiki links if context is known)
```

4. Confirm to user with link to created file

### File Scan Mode

When given a file reference (e.g., `@memory/_dump.gid`):

1. Resolve the file path (may need to search if not exact)
2. Read the file content
3. Look for actionable items:
   - Lines starting with `-`, `>`, `?`, or `!`
   - Lines containing `todo`, `should`, `need`, `want`
   - Nested `{{ }}` blocks (unprocessed prompts)
   - Numbered items that appear to be tasks
4. Present found items as a numbered list per [[meta - numbered lists for instructions]]:

```
Found actionable items in <filename>:

1 - "item text preview..."
2 - "another item..."
3 - "third item..."

Which items should become todos? (e.g., "1,3" or "all" or "none")
```

5. For selected items, create individual todo files
6. If file uses `{{ }}` prompts, tag processed ones with current date per session start rules

### Targeted Extract Mode

When given file + specific text (e.g., `@file "the thing"`):

1. Resolve and read the file
2. Find the line(s) matching the quoted text
3. Create a single todo from that specific item
4. Tag the source if it's a `{{ }}` block

## Claim Generation

For the `claim` portion of the filename:
- Keep it short (3-7 words)
- Use lowercase
- Capture the essence of the task
- Examples:
  - "fix auth redirect loop"
  - "add dark mode toggle"
  - "review prefixes documentation"

## Batch Creation

When creating multiple todos from a file scan:
- Create each as a separate file
- Link them to the source file in Related section
- Report summary: "Created N todos from <filename>"

## Output

- Creates: `memory/todo - yyyy-mm-dd-hhmm - claim.md` (one or more)
- May update: Source file (tagging `{{ }}` blocks with dates)

## Related

- [[meta - prefixes]] - todo prefix definition
- [[meta - file conventions]] - File naming conventions
- [[meta - numbered lists for instructions]] - Selection pattern
