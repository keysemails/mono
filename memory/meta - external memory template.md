---
created: 2026-01-23T23:34:58
changed: 2026-01-23T23:34:58
prior_commit: da80eac
---

# External Memory Template

Structure for external memory repos used with projects where memory can't be committed.

## Required Structure

    <project>.memory/
      .git/                 # Initialized as separate repo
      memory/               # Flat structure, same conventions as mono/memory

## Optional Structure

    <project>.memory/
      .git/
      memory/
      .claude/
        commands/           # Project-specific skills
        settings.local.json # Project-specific permissions
      CLAUDE.md             # Project-specific instructions

## Setup Steps

1. Create the memory repo folder as sibling to project:

       mkdir ~/repos/work-project.memory
       cd ~/repos/work-project.memory
       git init

2. Create the memory folder:

       mkdir memory

3. (Optional) Add project-specific configuration:

       mkdir -p .claude/commands

4. Register in external-memory-map (in mono repo):

   Add entry to `sub-conflict-resolution/external-memory-map.md`

## File Conventions

Follow the same conventions as [[meta - file conventions]]:

- Flat hierarchy (no nested folders)
- Prefixes indicate file purpose (session, meta, todo, etc.)
- YAML frontmatter with created, changed, prior_commit
- Wiki links resolve within the memory folder

## Git Remote

External memory repos can have their own remote for backup:

    git remote add origin git@github.com:username/work-project-memory.git

This keeps personal notes separate from the work project while still version-controlled.
