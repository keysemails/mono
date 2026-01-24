# /change-project skill

Switch the active project context mid-session. Lists available projects and lets you select a new focus.

## Usage
```
/change-project
```

## Instructions

### 1. Gather Project Context

Run the detection script to get all project information in one call:

```bash
.claude/scripts/detect-project.sh
```

This outputs current context (pwd, git root, branch, uncommitted changes), all subprojects with their properties, and mono status.

### 2. Present Options

From the script output, present options using [[meta - numbered lists for instructions]] pattern:

```
Available projects:

1 - mono (meta repo)
  - 1.1 - Memory: mono/memory/
  - 1.2 - For: workflow rules, conventions, cross-project work
2 - [subproject-a]
  - 2.1 - Location: repo/[subproject-a]/
  - 2.2 - Memory: repo/[subproject-a]/memory/
3 - [subproject-b]
  - 3.1 - Location: repo/[subproject-b]/
  - 3.2 - Memory: repo/[subproject-b]/memory/

Which project should we switch to?
```

Mark the current project with `(current)` in the list.

### 3. Handle Selection

When user selects a project:

1. **Confirm the switch**:
   ```
   Switching to [project name]...
   ```

2. **Check for uncommitted work** (already in script output):
   If uncommitted changes exist (uncommitted > 0), warn:
   ```
   Warning: You have uncommitted changes in [current project].
   - [list of changed files]

   Continue switching? The changes will remain in [current project].
   ```

3. **Set new context**:
   - Update working directory awareness
   - Note which `.git` will receive future commits
   - Identify active memory source(s)

4. **Confirm new context**:
   ```
   Now working in: [project name]
   - Git repo: [path]
   - Memory: [memory path(s)]
   - Branch: [current branch in new project]
   ```

### 4. Handle External Memory

If the selected project has a sibling `<project>.memory/` folder:
- Include it in the memory sources
- Note that commits will be split between project repo and memory repo

If no external memory exists, offer to create one (per [[meta - subproject integration]]).

## When to Use

- Switching focus between subprojects mid-session
- Moving from meta work to subproject work (or vice versa)
- After completing work in one project, starting work in another

## Difference from /detect-project

- `/detect-project` - Initial detection at session start, sets up context
- `/change-project` - Explicit switch mid-session, handles transition

## Related

- [[meta - subproject integration]] - Full multi-project documentation
- `/detect-project` - Initial project detection
- [[meta - git workflow]] - Commit handling across repos
