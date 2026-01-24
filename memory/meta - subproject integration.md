---
created: 2026-01-23T18:42:56
changed: 2026-01-24T00:16:32
prior_commit: 252f078
---

# Subproject Integration

How Claude should behave when working in a mono-repo with nested projects.

## Session Start: Project Context

At the start of a session, Claude needs to know which project is the focus. This determines which git repository to use.

**If clear from the first message**: The user mentions a specific project or file path that identifies it.

**If unclear**: List all projects in `repo/` and ask the user to select:

```
Which project are you working on?

1 - my-cool-tool
2 - [other projects...]
3 - Meta (mono repo itself)
```

The selected project becomes the **active project** for the session:
- Git operations use that project's `.git`
- Task branches are created there
- Memory files go in that project's `memory/` folder

**Limitation**: Files in `repo/` are gitignored by the mono repo, so IDE @ autocomplete won't find them. Users need to specify paths manually or work from within the subproject directory.

## Switching Projects Mid-Session

Use `/change-project` to switch the active project during a session. This skill:

1. **Shows current context** - Which project is active, which git repo, which memory sources
2. **Lists available projects** - All subprojects in `repo/` plus the meta repo
3. **Handles the transition** - Warns about uncommitted work, confirms new context

**When to switch:**
- Completing work in one project, starting work in another
- Moving from meta work (conventions, workflows) to subproject work (implementation)
- Needing to commit changes to a different repo

**Before switching**, the skill checks for uncommitted changes in the current project and warns you. Changes remain in that project's working directory - they don't follow you to the new context.

**After switching**, all git operations (branch, commit, status) apply to the new project's repository.

## Core Principles

1. **Skills must work in subprojects** - Skill discovery respects current working directory
2. **Project-specific configuration is respected** - Each subproject can have its own CLAUDE.md, settings, memory
3. **Search can span all projects** - Global search across the mono-repo is allowed
4. **Insight isolation** - Don't track domain insights about nested projects in the meta project's memory
5. **Workflow rules are inherited** - The git workflow from the mono repo's `memory/` applies to subprojects

## Workflow Inheritance

Subprojects have their own `.git` but follow the same workflow conventions defined in the mono repo's `memory/` folder. When working in a subproject:

- Read [[meta - git workflow]] from the mono repo
- Apply those rules to the subproject's git (task branches, `--no-ff` merges, commit conventions)
- Commits go to the subproject's `.git`, but the workflow pattern is the same

This means the mono repo's `memory/` serves two purposes:
1. **Meta knowledge** - How projects relate, shared conventions
2. **Workflow rules** - Applied consistently across all repos in the structure

## Memory Folder Scope

Subprojects live in the `/repo` folder, each with its own `memory/` for project-specific knowledge:

```
mono/
  memory/               # Meta-level: how projects relate, shared conventions
  CLAUDE.md
  repo/                 # All subprojects live here
    subproject-a/
      .git/             # Each subproject is its own git repo
      memory/           # Domain knowledge for subproject-a
      CLAUDE.md
    subproject-b/
      .git/
      memory/           # Domain knowledge for subproject-b
      CLAUDE.md
```

**What goes where:**
- **Meta project memory**: Conventions, workflow, cross-project patterns
- **Subproject memory**: Domain insights, project-specific decisions, local patterns

## Wiki Links

Wiki links resolve within the current project's memory folder. Cross-project references should use explicit paths rather than wiki links to avoid ambiguity.

## External Memory Repos

For projects where memory can't be committed to the main repo (e.g., work projects), use an external memory repo as a sibling folder.

### Convention

- **Location**: `<project>.memory/` sibling to project folder
- **Structure**: Same flat hierarchy as subproject memory

Example:

    ~/repos/
      work-project/           # The actual project (no memory committed)
        .git/
        src/
      work-project.memory/    # Personal memory (separate git repo)
        .git/
        memory/
          session - ...
          meta - ...

### Memory Cascade

When working in a project, memory sources are combined in order:

1. `mono/memory/` - Workflow rules, conventions (always applied)
2. `<project>.memory/memory/` - External personal memory (if sibling exists)
3. `<project>/memory/` - Local project memory (if exists)

External takes precedence over local when both exist and conflict.

### Detection

After the first user message each session:

1. Detect working directory
2. Check for sibling `<dirname>.memory/` folder
3. Check for local `memory/` folder
4. Prompt user to confirm/select which memory source to use

This happens after the first message so user intent can inform detection.

### Git Operations

External memory repos require split commits:
- Code changes → project repo
- Memory changes → external memory repo

See [[todo - 2026-01-23-2329 - git repo discovery]] for the auto-discovery enhancement.

## Skill Discovery

When in a subproject directory:
1. First look in `subproject/.claude/commands/`
2. Fall back to parent `mono/.claude/commands/` for shared skills

## Configuration Cascade

Project-specific CLAUDE.md files should supplement, not replace, parent instructions. The cascade:
1. User global (`~/.claude/CLAUDE.md`)
2. Mono-repo root (`mono/CLAUDE.md`)
3. Subproject (`mono/subproject/CLAUDE.md`)

Later files can override earlier ones for project-specific needs.

**Important**: Do not blindly prefer meta repo rules. Subproject context matters - when rules conflict, surface the conflict to the user rather than silently choosing.

## Conflict Detection

When working in a subproject, conflicts may arise between:
- Meta repo conventions and subproject conventions
- Parent CLAUDE.md instructions and subproject CLAUDE.md instructions
- Memory files with differing guidance

**Before starting work in a subproject**:
1. Check `sub-conflict-resolution/` for unresolved conflicts for that subproject
2. If conflicts exist, surface them to the user before proceeding
3. If you detect a new conflict, create a conflict file rather than silently choosing one rule

## Conflict Resolution Workflow

When a rule conflict is detected:

### 1. Create a conflict file

Location: `sub-conflict-resolution/conflict - yyyy-mm-dd-hhmm - <subproject>.md`

```markdown
---
created: timestamp
subproject: name
status: unresolved
---

# Conflict: [Brief description]

## Meta Rule
[What the meta repo says]
Source: [file path]

## Subproject Rule
[What the subproject says]
Source: [file path]

## Options
[Present using numbered list pattern]
```

### 2. Present options to user

Use the [[meta - numbered lists for instructions]] pattern:

```
1 - Follow meta repo rule
  - 1.1 - [Reasoning for meta rule]
2 - Follow subproject rule
  - 2.1 - [Reasoning for subproject rule]
3 - Create hybrid approach
  - 3.1 - [Describe compromise]
```

### 3. Record resolution

After user selects, update `sub-conflict-resolution/resolve - <subproject>.md`:

```markdown
---
created: timestamp
changed: timestamp
subproject: name
prior_commit: hash
---

# Resolutions for [subproject]

## yyyy-mm-dd - [Conflict topic]
**Decision**: Follow [meta/sub/hybrid]
**Reasoning**: ...
**Conflict file**: [[conflict - yyyy-mm-dd-hhmm - subproject]]
```

Also update the conflict file's status to `resolved`.

## Git Commit Handling

Commits in subprojects go to the subproject's git repository:
- The working directory determines which `.git` receives the commit
- This is standard git behavior - no special handling needed

**Cross-repo operations**: If a task touches files in both meta and subproject:
- Split into separate commits
- Commit subproject changes from within the subproject directory
- Commit meta changes from the meta repo root

## Session End: Multi-Project Sessions

When `/done` is run and the session touched multiple projects (meta + subproject):

### 1. Identify what belongs where

Review the session for:
- **Meta-relevant**: Workflow improvements, convention changes, cross-project patterns
- **Subproject-relevant**: Domain insights, project-specific decisions, implementation details

### 2. Inform the user

```
This session touched both meta and [subproject]. I'll need to:
- Export meta-relevant content to mono/memory/
- Export [subproject]-relevant content to repo/[subproject]/memory/
- Handle git separately for each repo
```

### 3. Handle git flows separately

After splitting content:
1. Complete git flow for the subproject (commit, merge offer)
2. Complete git flow for the meta repo (commit, merge offer)

Each repo gets its own branch lifecycle.

### 4. Advise on complexity

If the session involved significant work in both repos, suggest:

> "This session touched multiple projects substantially. For complex cross-project work, consider separate sessions for each project to keep context focused."

## Working Directory Awareness

Claude should track which directory operations are happening in:
- Commands from `mono/` root → mono repo git
- Commands from `repo/subproject/` → subproject git

When switching context, be explicit:

> "Switching to [subproject] - git operations will now use that repo."
