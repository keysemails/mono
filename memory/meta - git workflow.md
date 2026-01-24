---
created: 2026-01-23T13:15:00
changed: 2026-01-24T01:04:16
prior_commit: e336701
---

# Git Workflow

## Branching Strategy

**One branch per task.**

When work begins that will change files, immediately create a branch. The branch IS the work unit.

```
main
 └── task/add-terrain-brushes
 └── task/fix-spell-targeting
 └── task/refactor-memory-system
```

Branch naming: `task/<brief-description>`

**When to create a branch:**
- As soon as it's clear a change is needed
- Before making any edits
- Do not wait for user confirmation - create the branch proactively

## Commit Strategy

**One commit per action.**

[[c - an action is a logical unit of work]] - typically what you do before asking the user for feedback or moving to the next todo item.

```
task/add-terrain-brushes
 ├── commit: "Add terrain brush base class"           (may touch multiple files)
 ├── commit: "Add grass and rock brush implementations"
 └── commit: "Fix type errors from brush registry"
```

**Commit timing:**
- After completing each action/change, commit immediately
- Don't batch up multiple actions into one commit
- Don't wait for user approval to commit
- If working through a todo list, one commit per todo item

This enables:
- Clear history of what was done
- Easy rollback of specific actions
- User can see progress via commit log

## Workflow

1. **Create branch immediately** when work starts: `git checkout -b task/<description>`
2. Make changes (may touch multiple files for one logical action)
3. Update YAML frontmatter (`changed`, `prior_commit`) on modified files
4. Commit with descriptive message
5. If user requests changes, stay in branch and repeat 2-4
6. Merge branch when task complete: `git checkout main && git merge --no-ff task/<branch>`

**IMPORTANT: Do NOT delete branches after merging.** Branch references are part of the project history. The `--no-ff` merge preserves the branch structure, and keeping the reference preserves the name for future inspection.

## Initializing New Repos

For brand new repositories, the first commit naturally establishes `main`. The task branch workflow applies to *subsequent* work, not the initial commit.

**New repo setup:**
1. `git init`
2. First commit goes directly to `main` (establishes the baseline)
3. From then on, create task branches for all changes

**Don't create an orphan main and merge into it** - this creates "unrelated histories" (branches with no common ancestor) which complicates merging.

## Merge Strategy

**Always use `--no-ff` (no fast-forward) merges.**

This preserves branch structure in history so you can see what work was done in each task branch, even after merging. Fast-forward merges flatten history and lose this context.

## Commit Messages

Brief, descriptive, focused on what changed:
- "Add terrain brush base class"
- "Fix spell targeting for area effects"
- "Update file-conventions with new prefixes"

## Status Reporting

After completing an action and before asking for feedback, report:

1. **Branch status** - Current branch name and commit count
2. **Recent commits** - Hash, message, and files changed (always list actual filenames)
3. **Summary** - Brief description of what was done

**Use nested bullet lists. Do NOT use tables.**

Example format:

**Branch:** `task/my-feature` (3 commits)
- `abc1234` First commit
  - [file1.md](memory/file1.md)
  - [file2.md](src/file2.md)
- `def5678` Second commit
  - [file3.md](memory/file3.md)
- `ghi9012` Third commit
  - [file1.md](memory/file1.md)

**Summary:** Renamed X to Y and added Z to file conventions.

Ready to merge, or any changes needed?

**Before "continue?"**, always preview what comes next:

- **Next:** Add unit tests for the new convention
  continue?

- **Next:** Merge to main
  continue?

- **Next:** Update documentation with new API
  continue?

**File path format:** Use `[filename](relative/path/to/file)` - this creates clickable links in VSCode. The path must be relative from the repo root.

Then ask questions or suggest next steps.

## Multi-Repo Commits

When using external memory repos (see [[meta - subproject integration]]), a session may touch multiple git repositories:
- The project repo (code changes)
- The external memory repo (memory changes)
- Possibly mono repo (convention changes)

### Handling Split Commits

When changes span multiple repos:

1. **Identify which files belong where**
   - Code files → project repo
   - Memory files → external memory repo (or local memory if no external)
   - Convention/workflow changes → mono repo

2. **Commit to each repo separately**
   - Stage and commit project changes from project directory
   - Stage and commit memory changes from external memory directory
   - Each repo gets its own branch lifecycle

3. **Report per-repo status**
   - Show commits for each affected repo
   - Clarify which repo each commit went to

### Example Status Report

**Project repo** (`work-project/`):
- Branch: `task/add-feature` (2 commits)
  - `abc1234` Add new feature
    - [feature.ts](src/feature.ts)

**External memory** (`work-project.memory/`):
- Branch: `task/add-feature` (1 commit)
  - `def5678` Add session notes for feature work
    - [session - 2026-01-23-2300.md](memory/session%20-%202026-01-23-2300.md)

### Coordination

- Use the same branch name across repos for related work
- Merge both repos when the task is complete
- See [[todo - 2026-01-23-2329 - git repo discovery]] for planned auto-discovery

## External Changes

When files are modified outside of your direct edits (by the user, linters, or IDE), respond immediately:

1. **Safe changes** (settings, configs, formatting) → commit automatically
2. **Potentially sensitive** (secrets, credentials added) → ask before committing
3. **Unclear intent** → ask user what the change was for

Watch for notifications about modified files (e.g., `settings.local.json`) and act on them - don't leave changes uncommitted.

## Related

- [[meta - file conventions]] - YAML frontmatter with `prior_commit`
- [[meta - processing]] - How `/process` handles versioning
