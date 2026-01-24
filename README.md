# A Simple Claude Code Memory System for Your Projects

I have `/memory` folders for all my projects to `externalise` into.

No matter the project, i want claude code to accumulate context for future use. Always.

Instead of letting insights, decisions, or learnings stay implicit and get lost over time, just persist everything to markdown files.

With this, ephemeral clues from prior conversations easily persist across sessions, allowing future claude instances to build on past work even more. 

For the human in the loop this is obviously also very helpful, and can even give new surfaces to work on.

## Knowledge Capture as a workflow automation

All this should happen naturally, without you having to worry about it.

The system is biased toward capture over curation.
Reconstructing "damn i think we had this a few sessions ago" is much harder than "well i dont need any of this".
Better yet, keep it via git and you can even go back to those deleted parts if needed.

`mono` is a persistent knowledge layer that sits above your projects.
you work from within `mono`, having your actual projects in a `repo/` subfolder.

With things like `/change-project` or `/default-project` you can tell claude to focus on a specific project.
It then auto-handles feature branches, git commits per action and the `/memory` folder automatically (in the scope of the sub repo), while you direct claude to do the actual work at the same time.

If you notice that something in the session did not meet your expectations, you can e.g. use `/toclaude` to update the workflow to your liking.
This can either be project specific settings that `mono` should honour, or config changes in `mono` itself.

(Note that sub-project integration and local claude rule conflict resolution is not perfect yet. Im still playing around with it a lot, but its good enough to play with)

## Types of Memory files and prefixes
Here are some of the files I have in my `/memory` (both in `mono`, and in other `repo/`s)

### Dated files (prefix - yyyy-mm-dd-hhmm - claim.md):

Many types of files are snapshots that help externalise things to act upon in the moment.
They can be used as basis for new sessions, and also capture decisions.

- `architecture` - Overview of a coding project currents state
- `bug` - Bug reports
- `codereview` - Ranked review of the current code base with suggestions on what to do next
- `consistency` - Notice unclosed todos, open tasks, content that is inconsitent between files
- `drift` - Compares documented intent to the current state
- `goal` - This should really be named more like problem and preferences
- `next` - Collects what tasks could be done next
- `plan` - Implementation plans for complex changes, tracking progress and learnings (can use to reflect or act upon in a later step)
- `proposal` - Suggested changes before making a plan
- `reflect` - Extracted learnings, tasks, incoherences
- `research` - Collected websearch or file search results
- `session` - Chat exports (from `/tomd` or `/done`)
- `spec` - Specifications as part of plans (underused)
- `todo` - Actionable tasks
- `solved` - Completed todos (renamed from todo)
- `videoplan` - Scene-by-scene video structure (playing around with a manim skill)

### Non-Dated Files (prefix - claim.md):

- `c` - Concepts as prose claims
- `idea` - Ideas and brainstorming
- `learning` - Insights from reflection
- `meta` - System/workflow files
- `moc` - Maps of Content (hierarchy indexes, underexplored still)
- `problem` - Problems identified
- `question` - Questions to explore


## Skills/Commands

### Sprint/Planning Workflow:

- `/sprint-start` - Orchestrates goal -> proposal -> spec -> plan creation and approval
- `/goal` - Captures problem, desired outcome, and preferences
- `/proposal` - Explore approaches and decision points for a goal
- `/spec` - Define requirements, constraints, and open questions
- `/plan-continue` - Resume work on an existing plan

### Analysis/Snapshots:

- `/reflect` - Analyse files, extract learnings, tasks, incoherences, questions
- `/consistency` - Check project structure for inconsistencies and violations
- `/drift` - Detect divergence between documented intent and current state
- `/architecture` - Create codebase structure snapshots
- `/code-review` - Code quality analysis with severity ratings
- `/next` - Collect, store and present things to work on next

### Knowledge/Research:

- `/research` - Research and document topics via websearch or from local sources
- `/todo` - Quickly create todo files from input or extract from files

### Sub-Project Management:

- `/detect-project` - Check which project we should be wokring on (git and memory management)
- `/change-project` - Switch active project
- `/default-project` - Set default project (.PROJECT file)

### Export/Conversion:

- `/done` - End session with export (`session-`) and offer to merge (can follow with `/reflect` manually)
- `/tomd` - Export conversation to markdown
- `/toscript` - Export code blocks to script file (untested)
- `/toclaude` - Extract learnings to CLAUDE.md etc
- `/tomanim` - Convert markdown to manim-animated video (wip)

### Utility:

- `/process` - Process in-file prompts ({ ... } blocks)
- `/human-sort` - Reorganize human.md sections without modifying content
- `/showrules` - Toggle citation of rules before each response (should be debug tool but is broken rn)
- `/toskill` - Create a new skill from conversation

## The Structure

```
mono/
  memory/           # Knowledge that persists
  .claude/commands/ # Your custom workflows (skills)
  repo/             # Your actual projects live here
    project-a/
      .claude
      memory/
      src/
      ...
    project-b/
```


### Flat files and wiki links
`memory/` uses a flat file structure, no nested folders.
Most of it works through `[[wiki links]]` that link to other documents.
Its all just markdown files.
(need to make much more use of MOCs etc)

### Working on sub projects

Open e.g. VSCode in `mono/` and then use `/change-project` or `/default-project` to start working on the sub-repo.

```
!!!
you should probably test things out first, e.g. copy paste your git repo as new git repo, since mono uses git automatically

once you are happy with the workflow (go ham on changing stuff),
then you may want to give it a real shot.

or better yet start with new toy projects to test this out.
```

## The Session Workflow
(Example generated based on my `session - ` files)

When you start Claude Code, hooks automatically load:
- `INIT.md` - Project instructions
- `.PROJECT` - Default project context (if set)

**Claude's first question** (if no default project):
> "Should I run collect-context for [detected project]?"

This gathers recent changes and session history for context. (lots to improve on dynamic-context creation)

```
User: /consistency

Claude: I'll generate a consistency report. Let me check the current branch first.

[reads: git branch --show-current]

I'm on main, so I need to create a task branch first.

[runs: git checkout -b task/consistency-report]

Now let me scan the memory directory...

[reads multiple files, analyzes for issues]

[creates: memory/consistency - 2026-01-24-0430 - 12 issues found.md]
[commits the file]

**Branch:** `task/consistency-report` (1 commit)
- `6c433c9` Add consistency report: 12 issues found
  - [consistency - 2026-01-24-0430 - 12 issues found.md](memory/...)

**Summary:** Found 12 inconsistencies across 72 files.

Which items would you like to address? (e.g., "1.1, 2.3")
```

```
User: 2.1, 3

Claude: [fixes the selected items]
[commits the fixes]
[updates the consistency report with wiki links to results]

**Branch:** `task/consistency-report` (2 commits)
- `6c433c9` Add consistency report
- `60c62bb` Address consistency items 2.1 and 3.x

Merge to main?
```

```
User: /done

Claude: [exports session to memory/session - 2026-01-24-0440 - consistency report and fixes.md]
[commits the export]

Merged to main. Session complete.
```



## Try It

`mono` on GitHub:
https://github.com/ltOgt/mono



### /research
Consider running `/research` on `mono` itself to learn more.
Then use `mono` to change `mono` to your liking.


# Disclaimer

`mono` was developed organically over a few days, by using `mono`.
Note that pretty much all of the docs in the repo are written by claude itself using mono.

# Future
All of this barely scratches the surface and can be improved immensly.
Next ill have to evolve `mono` by running `/research` on the mindblowing stuff @arscontexta has found out about @arscontexta using @arscontexta


