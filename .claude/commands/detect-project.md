# /detect-project skill

Detect and select project context, including external memory repos. Run automatically after first message or manually to switch projects.

## Usage
```
/detect-project
```

## Instructions

### 1. Detect Current Context

Run the detection script to gather all project information in one call:

```bash
.claude/scripts/detect-project.sh
```

This outputs:
- Current context (pwd, git root, branch, uncommitted changes)
- All subprojects with their properties (git, branch, memory, external memory)
- Mono status

### 2. Build Options List

Present discovered options using [[meta - numbered lists for instructions]] pattern:

```
Detected project context for [current directory name]:

1 - Use external memory
  - 1.1 - Location: [sibling .memory path]
  - 1.2 - Status: [found/not found]
2 - Use local memory
  - 2.1 - Location: [./memory]
  - 2.2 - Status: [found/not found]
3 - Use mono memory only
  - 3.1 - Location: [mono/memory path]
4 - Create new external memory repo
  - 4.1 - Will create: [project].memory/ sibling folder
```

Omit options that don't apply (e.g., if no sibling found, adjust option 4).

### 3. Handle User Selection

| Selection | Action |
|-----------|--------|
| 1 - External | Set context to use external memory repo |
| 2 - Local | Set context to use project's local memory |
| 3 - Mono only | Only use mono/memory for this session |
| 4 - Create new | Run setup steps from [[meta - external memory template]] |

### 4. Set Active Context

After selection, confirm:

```
Active project context:
- Working directory: [path]
- Git repo: [which .git]
- Memory source(s): [list of memory locations]
```

Store this context for the session - all subsequent operations use these settings.

### 5. Creating External Memory Repo

If user selects option 4:

1. Create sibling folder: `<project>.memory/`
2. Initialize git: `git init`
3. Create memory folder: `mkdir memory`
4. Confirm creation and set as active

## When This Runs

**Automatically**: After responding to user's first message each session (per INIT.md)

**Manually**: User runs `/detect-project` to:
- Switch to different project mid-session
- Create new external memory repo
- Verify current context

## Output

No file created - this skill sets session context and reports status.

## Related

- [[meta - subproject integration]] - Full external memory documentation
- [[meta - external memory template]] - External memory repo structure
- [[meta - git workflow]] - Multi-repo commit handling
