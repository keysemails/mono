# Project Instructions

## CRITICAL: Read Context Before Acting

**BEFORE taking any action** in this project, you MUST read the relevant context files from the `memory/` folder. Do not skip this step.

### Always Read at Session Start (handled by hook)

The session-start hook automatically loads these files before your first message:
- `INIT.md` - This file (project instructions)
- `memory/meta - file conventions.md` - Naming, YAML frontmatter, linking standards

**You don't need to read these files manually** - they're already in your context when the session begins.

### Multiproject Structure

This is a **mono-repo with nested git repositories**:

```
mono/                      # Meta repo (workflow rules, conventions)
  .git/
  memory/                  # Shared conventions and meta knowledge
  repo/                    # Subprojects live here (gitignored by mono)
    project-a/
      .git/                # Independent git repo
      memory/              # Project-specific knowledge
    project-b/
      .git/
      memory/
```

**Key points:**
- Each subproject in `repo/` is its own git repo with independent history
- Subprojects are gitignored by mono - they don't appear in mono's git status
- The **active project** determines which `.git` receives commits
- Workflow rules from `mono/memory/` apply to all subprojects

**External memory repos**: For projects where memory can't be committed (e.g., work repos), use a sibling `<project>.memory/` folder as a separate git repo. See [[meta - subproject integration]] for details.

**Memory cascade** (in order of precedence):
1. `mono/memory/` - Workflow rules (always applied)
2. `<project>.memory/memory/` - External personal memory (if exists)
3. `<project>/memory/` - Local project memory (if exists)

**Project skills:**
- `/detect-project` - Initial detection at session start
- `/change-project` - Switch projects mid-session
- `/default-project` - Set persistent default (creates `.PROJECT` file)

**Cross-project work**: When a task touches both mono and a subproject:
1. Identify which work belongs where (meta vs domain-specific)
2. Complete work in one project first (commit, potentially merge)
3. Use `/change-project` to switch context
4. Complete work in the other project

Don't mix commits across repos in a single flow - finish one project's work before switching.

**For complex cross-project work**, suggest splitting into separate sessions:
> "This work spans both [subproject] and mono. I recommend we finish [subproject] work first, run `/done` to export, then start a new session for the mono changes using that export as context."

This keeps each session focused and avoids context confusion between repos.

See [[meta - subproject integration]] for the full multi-project workflow.

### Default Project (.PROJECT file)

If a `.PROJECT` file exists at mono root, it contains the default project context. This file is:
- Created by `/default-project` skill
- Read by session-start hook and included in context
- User-specific (gitignored)

When `.PROJECT` exists, **skip project detection prompts** and use its settings unless the user's request clearly involves a different project.

### Dynamic Context Flow

**After responding to the user's first message**, follow this flow:

1. **Check for default project**: If `.PROJECT` file was loaded (shown in session context), use it. Skip to step 3.

2. **Detect project context** from the first message (only if no default):
   - Current working directory
   - Sibling `<dirname>.memory/` folder (external memory)
   - Local `memory/` folder
   - `repo/` subprojects

3. **Ask user**: "Should I run collect-context for [detected project]?"
   - If project is ambiguous, present options:
     - 1 - Use external memory (if sibling `.memory/` found)
     - 2 - Use local memory (if exists)
     - 3 - Use mono memory only
     - 4 - Create new external memory repo (if none found)

4. **If user says yes**:
   - Run `.claude/scripts/collect-context.py` for the selected project
   - Read the generated `memory/meta - dynamic context.md`
   - This file contains: recent changes, last session info

5. **Then proceed** with the user's actual request

The selected project determines:
- Which `.git` to use for branches and commits
- Where memory files should go
- Which memory sources to combine (mono + external/local)

See [[meta - subproject integration]] for full details on multi-project sessions and external memory repos.

### Read Before Specific Operations

| Operation                                | MUST Read First                                           |
| ---------------------------------------- | --------------------------------------------------------- |
| Any git operation (commit, branch, etc.) | `memory/meta - git workflow.md`                           |
| Creating or editing files                | `memory/meta - file conventions.md`                       |
| Using `/process` command                 | `memory/meta - processing.md`                             |
| Entering plan mode                       | `memory/meta - file conventions.md`                       |
| Starting a sprint (`/sprint-start`)      | `memory/meta - coding project structure.md`               |
| Working in a subproject                  | `memory/meta - subproject integration.md`                 |
| Working in a subproject                  | Check `sub-conflict-resolution/` for unresolved conflicts |
| Presenting selectable items to user      | `memory/meta - numbered lists for instructions.md`        |

### Branch Before Editing

**Before creating or editing any file for work**, ensure you're in a task branch:

1. If on `main`, create a branch: `git checkout -b task/<description>`
2. Make changes
3. Commit immediately after each logical action

This applies to ALL file changes - not just when you think about git. Creating a README, editing a config, writing code - all require a branch first. See [[meta - git workflow]] for details.

**ENFORCEMENT: Before every Write or Edit tool call, verify you are NOT on main.** This is a hard rule - no exceptions. If you find yourself about to create/edit a file while on main, stop and create a branch first.

### IMPORTANT: Never Delete Branches

**Do NOT delete branches after merging.** Branch references are part of the project history. Use `--no-ff` merges to preserve structure, and keep the branch reference so it can be inspected later. See [[meta - git workflow]] for details.

### New Work in Existing Branch

When starting work that's distinct from the current branch's purpose, ask:

> "We're in `task/X` but this is new work (Y). Should I:
> 1. Merge the current branch first and create `task/Y`?
> 2. Continue in this branch?"

Don't silently continue in a branch whose name no longer matches the work. See [[meta - branch scope]] for rationale and examples.

## CRITICAL: Externalisation

Capture context for future use - see [[meta - externalise]] for details.

## Proactive Context Gathering

When starting work that may benefit from additional context, ask:

> "Should I search for more context before proceeding?"

Suggest specific questions the search could help answer. For example:

> "I could search for:
> - How authentication is currently handled in this codebase
> - Whether there are existing patterns for API error handling
> - What testing conventions are used here"

This applies especially to:
- Tasks touching unfamiliar areas of the codebase
- Work requiring domain knowledge not yet established in the conversation
- Changes that might conflict with existing patterns or conventions

## Sprint Workflow

For structured development work, use the goal → spec → plan flow:

1. **`/goal`** - Capture problem, desired outcome, and preferences
2. **`/spec`** - Define requirements, constraints, and open questions
3. **`/sprint-start`** - Orchestrate all three: goal, spec, plan, then approval

Use `/sprint-start` for new features or non-trivial work. It creates the full structure and waits for approval before implementation.

Use `/plan-continue` to resume work on an existing plan in a new session.

See [[meta - coding project structure]] for the complete workflow guide.

## Plan Mode

**For non-trivial features, create a plan first before implementing.** Don't jump straight to implementation - planning ensures alignment and prevents wasted effort.

Plan mode is **only for creating the plan** - no implementation work.

- Create a plan document in `memory/` using naming: `plan - <descriptive claim>.md`
- Include YAML frontmatter
- The plan file is the only output - actual work happens in a new session
- This is in addition to any system plan file - the memory/ plan becomes the persistent record

### Wiki Links

This project uses `[[wiki-links]]` to connect files. When you encounter a wiki link:
1. Resolve it to a file in `memory/` directory (e.g., `[[meta - file conventions]]` → `memory/meta - file conventions.md`)
2. Read the linked file
3. Follow any wiki links within that file as needed

## Snapshot Skills

Skills that aggregate or analyze information (like `/reflect`, `/consistency`, `/next`, `/architecture`, `/code-review`, `/drift`) should create a **snapshot file** in `memory/`:

- Use the appropriate dated prefix (e.g., `next - yyyy-mm-dd-hhmm - claim.md`)
- Include YAML frontmatter with timestamps
- Use the [[meta - numbered lists for instructions]] pattern for user selection
- Update the snapshot file with wiki links as items are acted upon

This creates a traceable record of what was presented and what actions were taken.

## Flat Hierarchy

This project uses a flat file structure with MOC (Map of Content) files for organization. No nested folders - see [[meta - file conventions]] for details.

## Subproject Conflict Handling

Before starting work in a subproject:

1. Check `sub-conflict-resolution/conflict - * - <subproject>.md` for unresolved conflicts
2. If found, surface them to user before proceeding
3. When detecting a rule conflict between meta and subproject, create a conflict file rather than silently choosing

See [[meta - subproject integration]] for the full conflict resolution workflow.

## Settings File Safety

`.claude/settings.local.json` is tracked in git. Be careful what goes in it.

**Do NOT add to settings:**
- Secrets, tokens, or API keys
- Absolute paths specific to one machine
- Personal preferences that shouldn't apply to collaborators

**When editing settings:**
- Review existing content for anything problematic (secrets, machine-specific paths)
- If you find issues, warn the user before proceeding
- If user asks to add something problematic, explain why it's risky and suggest alternatives
- Only proceed with problematic additions if user explicitly insists after warning

## Questions vs Work

- If the user is asking a question, just answer it - don't make file changes
- Only edit files when the task is clearly work (implementing, fixing, creating)
- When uncertain, answer the question first, then offer to do the work as a follow-up

## Todos as Actions

Each todo item I create is an [[c - an action is a logical unit of work|action]] - a logical unit of work that results in one commit.

**After completing each todo/action:**
1. Commit the changes immediately
2. Present a status report using the standard git flow format (see Status Reporting section)
3. Preview next step and ask to continue:
   - **Next:** [brief description of next task]
   - continue?

**User responses:**
- **"continue"** - Do the next task, then report with the same git flow (commit → status report → ask again)
- **"continue all"** - Complete all remaining tasks without stopping, then present a combined status report at the end

This gives the user control over pacing while keeping work atomic and reviewable.

## Status Reporting

After completing work (before asking for feedback or moving to next task), report:

1. **Branch** - name and commit count
2. **Recent commits** - hash, message, and files changed
3. **Summary** - what was done

**Format requirements:**
- Use nested bullet lists, NOT tables
- File paths must be clickable: `[filename](relative/path/to/file)`

Example:
```
**Branch:** `task/my-feature` (2 commits)
- `abc1234` Add new feature
  - [feature.md](memory/feature.md)
  - [config.ts](src/config.ts)
- `def5678` Fix typo
  - [feature.md](memory/feature.md)

**Summary:** Added feature X and fixed typo.
```

See [[meta - git workflow]] for full details.

## Ratifying Behavior Changes

When the user requests a change in how Claude should behave (workflow, formatting, conventions, etc.), update the relevant documentation files to persist the decision:

- **Workflow changes** → Update `memory/meta - git workflow.md`
- **Convention changes** → Update `memory/meta - file conventions.md` or related meta files
- **Claude behavior** → Update this file (`INIT.md`)

This ensures future sessions follow the same rules. Don't just change behavior for the current session - document it.

## Meta Feedback Loop

When the user says something "should have happened" (indicating a missed expectation):

1. **Identify the gap** - What was expected but didn't occur?
2. **Check documentation** - Was this clearly specified in INIT.md or meta files?
3. **Clarify if needed** - If the rule exists but was ambiguous, update the documentation to make triggers/expectations explicit
4. **Add if missing** - If no rule existed, add one

This applies immediately - treat "should have happened" feedback as a documentation improvement task alongside fixing the immediate issue.

## Session End

**Trigger:** User runs `/done`

This is the only trigger - no interpretation of "done" or similar words needed. The `/done` skill handles export, reflection, and merge offer.
