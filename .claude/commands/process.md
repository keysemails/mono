# /process skill

Process a file by resolving its path and handling embedded prompts.

## Usage
```
/process @file-reference [additional instructions]
```

## Instructions

Follow the wiki-linked documentation:
- [[file-conventions]] - For naming and YAML frontmatter requirements
- [[git-workflow]] - For branch/commit strategy when making changes
- [[processing]] - For detailed processing rules

## Quick Reference

1. **Resolve** `@file` (exact → search → fuzzy, report progress)
2. **Read** file and find untagged `{{ }}` prompts
3. **Process** each prompt, tag with timestamp after
4. **Edit in place** - do NOT rename files or create version folders (git handles versioning)
5. **Update** YAML frontmatter (`changed`, `prior_commit`)
6. **Commit** the change per [[git-workflow]]
