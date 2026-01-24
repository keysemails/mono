# mono

A personal knowledge management system designed for Claude Code. Uses flat file organization, wiki-style linking, and embedded prompts to create an evolving knowledge base that persists across AI sessions.

## Why mono?

AI coding assistants forget everything between sessions. Every conversation starts fresh - you re-explain your codebase, re-establish conventions, re-discover the same insights.

mono solves this by creating a persistent knowledge layer:
- **Memory files** capture decisions, learnings, and context
- **Skills** (slash commands) encode workflows you'd otherwise repeat manually
- **Wiki links** connect ideas so Claude can follow threads
- **Session exports** preserve conversations for later reflection

The result: each session builds on previous work instead of starting over.

## Project Structure

**mono is designed to be used from its root folder.** Your subprojects (other git repos, coding projects, etc.) live in the `/repo` subfolder:

```
mono/                     # ← Work from here
  memory/                 # Meta-level knowledge, conventions, session exports
  CLAUDE.md               # Behavior rules
  .claude/commands/       # Skills (slash commands)
  repo/                   # ← Your subprojects go here
    project-a/            # A separate git repo
      .git/
      memory/             # Project-specific knowledge
      CLAUDE.md           # Project-specific rules
    project-b/            # Another git repo
      .git/
      ...
```

This structure allows:
- **Unified context** - Claude reads mono's CLAUDE.md and memory/ regardless of which subproject you're working in
- **Project isolation** - Each subproject has its own git history, memory, and optional CLAUDE.md overrides
- **Skill inheritance** - Subprojects can have their own `.claude/commands/` while inheriting mono's skills
- **Cross-project search** - Search across all repos from the mono root

See [meta - subproject integration.md](memory/meta%20-%20subproject%20integration.md) for conflict handling between meta and subproject rules.

## Core Concepts

### Flat File Hierarchy

All files live at the root of `memory/` - no nested folders. Organization happens through **MOC (Map of Content)** files that link related documents together.

```
memory/
  meta - file conventions.md
  meta - git workflow.md
  moc - research.md           # Links to research files
  research - terrain heightmaps.md
  session - 2026-01-23-1549 - improved export.md
```

### Wiki Links

Files reference each other using `[[wiki-links]]`:

```markdown
Follow the [[meta - git workflow]] for commits.
See [[meta - prefixes]] for naming conventions.
```

### File Naming

Files follow `prefix - claim.md` where the claim is written as readable prose.

**Standard prefixes** (no date in filename):

| Prefix | Purpose |
|--------|---------|
| `meta` | System/workflow documentation |
| `c` | Concepts - claims as prose |
| `idea` | Ideas and brainstorms |
| `incoherence` | Contradictions or unclear areas found during reflection |
| `learning` | Extracted insights from reflection |
| `moc` | Maps of content (indexes) |
| `problem` | Problems identified |
| `question` | Questions to explore |
| `research` | Research findings |
| `spec` | Specifications |
| `sprint` | Sprint plans |

**Dated prefixes** (use `prefix - yyyy-mm-dd-hhmm - claim.md`):

| Prefix | Purpose |
|--------|---------|
| `bug` | Bug reports |
| `consistency` | Project consistency reports |
| `goal` | Sprint/feature goals |
| `next` | Actionable items snapshots |
| `plan` | Task plans |
| `reflect` | Extracted learnings from sessions |
| `session` | Exported chat sessions |
| `todo` | Individual tasks |

See [meta - prefixes.md](memory/meta%20-%20prefixes.md) for the full list.

### YAML Frontmatter

Every file has metadata:

```yaml
---
created: 2026-01-23T13:15:00
changed: 2026-01-23T16:08:11
prior_commit: c8b5be9
---
```

## Skills (Slash Commands)

Custom commands in `.claude/commands/`:

| Command | Purpose |
|---------|---------|
| `/goal` | Create a goal file for a sprint or feature |
| `/proposal` | Explore approaches with trade-offs before committing |
| `/spec` | Create or update a requirements specification |
| `/sprint-start` | Initialize a sprint: goal, spec, plan, then approval |
| `/plan-continue` | Resume work on an existing incomplete plan |
| `/process @file` | Process embedded `{{ }}` prompts in a file |
| `/reflect @file` | Extract learnings, tasks, and questions from a file |
| `/research` | Research topics into scannable knowledge documents |
| `/todo` | Quick create todo files from input or extract from files |
| `/next` | Show actionable items (todos, ideas, pending prompts) to decide what to work on |
| `/consistency` | Check project for structural issues |
| `/architecture` | Document codebase structure as-is |
| `/code-review` | Full codebase quality analysis with severity ratings |
| `/drift` | Compare documented intent vs current reality |
| `/done` | End session - export, commit, and offer to merge branch |
| `/detect-project` | Detect and select project context at session start |
| `/change-project` | Switch active project context mid-session |
| `/showrules` | Display relevant rules for a topic |
| `/toclaude` | Update CLAUDE.md with new behaviors |
| `/toskill` | Create a new skill command |
| `/tomd` | Export current session to markdown |
| `/toscript` | Export code from conversation to a script file |
| `/tomanim` | Convert markdown files to manim-animated videos |
| `/default-project` | Set persistent default project for session start |
| `/human-sort` | Reorganize human notes file sections |

## Sprint Workflow

For non-trivial features, mono uses a structured planning flow:

1. **`/goal`** - Capture the problem, desired outcome, and preferences
2. **`/proposal`** - Explore approaches, identify trade-offs, get user decision
3. **`/spec`** - Define requirements based on chosen approach
4. **`/sprint-start`** - Orchestrate all three, then create an action plan

This happens before any code is written. The plan file tracks progress and links to artifacts created during implementation.

Use `/plan-continue` to resume work in a new session.

```
goal → proposal → spec → plan → implement → reflect
```

See [meta - coding project structure.md](memory/meta%20-%20coding%20project%20structure.md) for the complete workflow.

## Embedded Prompts

Files can contain prompts for future processing:

```markdown
{{
Research how terrain heightmaps work
}}
```

Run `/process @file` to execute unprocessed prompts. After processing, they're tagged with timestamps to avoid re-processing.

## Subproject Support

Subprojects live in the `/repo` folder. Each can have their own `memory/`, `CLAUDE.md`, and `.claude/commands/`. The `sub-conflict-resolution/` folder tracks conflicts between meta-repo and subproject conventions - see the Project Structure section above for the full layout.

## Git Workflow

**One branch per task, one commit per action.** Claude handles this automatically - you don't need to manage git yourself.

When work begins, Claude immediately creates a task branch:

```
git checkout -b task/add-terrain-brushes
```

Commit after each logical action - don't batch changes. This creates clear history and enables easy rollback.

```
task/add-terrain-brushes
 ├── commit: "Add terrain brush base class"
 ├── commit: "Add grass and rock brush implementations"
 └── commit: "Fix type errors from brush registry"
```

**Branch scope**: If work shifts to something unrelated to the current branch, ask whether to merge and create a new branch or continue. Don't silently mix unrelated work.

Always merge with `--no-ff` to preserve branch structure in history.

See [meta - git workflow.md](memory/meta%20-%20git%20workflow.md) and [meta - branch scope.md](memory/meta%20-%20branch%20scope.md) for full details.

## Numbered Lists for Selection

When Claude presents options, tasks, or items for you to act on, they use a numbered list pattern:

```markdown
1 - Category A
  - 1.1 - First item in category A
  - 1.2 - Second item in category A
2 - Category B
  - 2.1 - First item in category B
```

Select items by number (e.g., "1.1" or "1.1, 2.1"). After acting on an item, Claude adds a nested wiki link showing the result:

```markdown
1 - Category A
  - 1.1 - First item
    - [[resulting file or action taken]]
```

This creates a traceable record of what was presented and how it was resolved. Used by `/next`, `/consistency`, `/reflect`, and conflict resolution.

## Externalising Context

Don't let insights stay only in conversation - persist them to files:

| Content Type | Where to Put It |
|--------------|-----------------|
| Workflow changes | `CLAUDE.md` or meta files |
| Learnings from sessions | Use `/reflect` to extract |
| Reusable patterns | Create a skill in `.claude/commands/` |
| Ideas for later | Create `idea - <claim>.md` |
| Questions to explore | Create `question - <claim>.md` |

Principle: When in doubt, externalise. It's easier to delete unnecessary files than recreate lost context.

See [meta - externalise.md](memory/meta%20-%20externalise.md) for the full guide.

## Behavior Rules (CLAUDE.md)

[CLAUDE.md](CLAUDE.md) defines how Claude should behave in this project:

- **Context loading** - Which files to read at session start
- **Branch before editing** - Create task branch before any file changes
- **Branch scope** - Ask before mixing unrelated work in one branch
- **Plan mode** - Create plans before implementing non-trivial features
- **Todos as actions** - Each todo is one commit, report after each
- **Meta feedback loop** - When expectations are missed, update documentation
- **Session end** - Run `/done` to export the session, commit, and merge the task branch

CLAUDE.md contains inline summaries with `[[wiki-links]]` to detailed meta files. This allows quick reference while keeping full context accessible. Use `/consistency` to detect drift between inline content and linked files.

## Getting Started

**Prerequisites:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (Anthropic's CLI tool for Claude)

1. Clone this repo
2. Add your projects to the `repo/` folder (they won't be committed to mono)
3. Run `claude` from the mono root - Claude will read `CLAUDE.md` automatically
4. Work from within mono, not from inside your subprojects

**Typical session workflow** (git is automatic - you just work):
1. Start work → Claude automatically creates a task branch
2. Make changes → Claude commits after each logical action
3. End session → Run `/done` to export, commit, and merge
