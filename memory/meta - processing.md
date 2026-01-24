---
created: 2026-01-23T13:15:00
changed: 2026-01-24T06:42:00
prior_commit: 55d4281
---

# Processing Files

Use `/process @file` to process files with embedded prompts.

## File Resolution

When given `@(some file name)`:
1. Try exact path first
2. Search current directory for matching filename
3. Search recursively with glob
4. Try fuzzy matching for typos
5. Report each failed approach: "Could not find with approach X, trying Y..."
6. If multiple matches found, present as numbered options and ask user to select

## Embedded Prompts `{{ }}`

Files may contain prompts in double brackets:

```
{{
some prompt or instruction
}}
```

These can be:
- **Nested:** `{{ outer {{ inner }} }}`
- **Date-tagged:** `{{2026-01-23 12:00 some prompt }}`

**Rules:**
- Process prompts that are NOT yet tagged with a date
- After processing, tag with current timestamp
- Skip date-tagged prompts unless user specifies a date range

## Version Management

Git handles versioning - no need for backup folders or file renaming.

When processing a file:
1. **Keep the filename unchanged** - do NOT rename or update dates in filename
2. Update YAML frontmatter:
   - Set `changed` to current timestamp
   - Set `prior_commit` to current HEAD before committing
3. Edit the file in place with processed changes
4. Commit immediately per [[meta - git workflow]]

To recover previous versions, use `git show <prior_commit>:<filepath>`

## Related

- [[meta - file conventions]] - Naming and frontmatter standards
- [[meta - git workflow]] - Commit and branch strategy
