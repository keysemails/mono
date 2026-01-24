---
created: 2026-01-23T13:15:00
changed: 2026-01-24T05:54:34
prior_commit: 04feba3
---

# File Conventions

## Flat Hierarchy

This project uses a **flat file structure** - no nested folders. All files live at the same level.

Instead of organizing with folders like:
```
knowledge/research/terrain/heightmaps.md
```

We use **MOC (Map of Content)** files to represent hierarchies:
```
moc - knowledge.md
moc - research.md
research - terrain heightmaps.md
```

Where `moc - knowledge.md` contains:
```markdown
# Knowledge

- Research
  - [[moc - research]]
- Bugs
  - [[bug - player clips through walls]]
  - [[bug - lighting flickers on terrain edges]]
```

And `moc - research.md` contains:
```markdown
# Research

- Terrain
  - [[research - terrain heightmaps]]
  - [[research - terrain brush mapping]]
- Audio
  - [[research - spatial audio implementation]]
```

For deep structures, use nested MOCs - each MOC links to sub-MOCs and leaf files.

## Naming

Files follow: `prefix - claim.md`

**Prefixes:** See [[meta - prefixes]] for the full list of standard prefixes.

**Claim:** See [[meta - claim prose]] for how to write claims as readable prose.

For larger resources (sprint plans, research results), use descriptive names:
- `sprint - terrain research sprint.md`
- `research - terrain brush heightmap mapping.md`

## Dated Filenames

Files that represent **point-in-time snapshots** include dates in the filename:

| Prefix | Format | Reason |
|--------|--------|--------|
| `architecture` | `architecture - yyyy-mm-dd-hhmm - claim.md` | Codebase snapshots capture structure at a point in time |
| `bug` | `bug - yyyy-mm-dd-hhmm - claim.md` | Bugs are discovered at a specific time |
| `codereview` | `codereview - yyyy-mm-dd-hhmm - claim.md` | Code reviews capture quality analysis at a moment |
| `consistency` | `consistency - yyyy-mm-dd-hhmm - claim.md` | Reports capture state at a moment |
| `drift` | `drift - yyyy-mm-dd-hhmm - claim.md` | Drift analysis compares intent vs reality at a moment |
| `goal` | `goal - yyyy-mm-dd-hhmm - claim.md` | Goals capture intent at sprint/feature start |
| `next` | `next - yyyy-mm-dd-hhmm - claim.md` | Actionable items snapshots capture state at a moment |
| `plan` | `plan - yyyy-mm-dd-hhmm - claim.md` | Plans capture intent at a specific time |
| `proposal` | `proposal - yyyy-mm-dd-hhmm - claim.md` | Proposals capture suggested changes at a point in time |
| `reflect` | `reflect - yyyy-mm-dd-hhmm - claim.md` | Reflections capture extracted findings at a moment |
| `research` | `research - yyyy-mm-dd-hhmm - claim.md` | Research captures knowledge at a point in time |
| `session` | `session - yyyy-mm-dd-hhmm - claim.md` | Chat exports are immutable snapshots |
| `todo` | `todo - yyyy-mm-dd-hhmm - claim.md` | Tasks are identified at a specific time |

All other files use just `prefix - claim.md` without dates. The YAML frontmatter tracks `created` and `changed` timestamps.

**Exception:** `human.md` - A special file for fleeting human notes that doesn't follow the prefix convention. It's a scratch space that Claude should never modify directly (only via `/human-sort` for reorganization).

## YAML Frontmatter

Every file must have:

```yaml
---
created: yyyy-mm-ddThh:mm:ss
changed: yyyy-mm-ddThh:mm:ss
prior_commit: <commit-hash or null>
---
```

- `created` - When file was first created
- `changed` - Last modification timestamp
- `prior_commit` - The commit hash before making changes (for rollback reference)

Update `changed` and `prior_commit` on every edit.

## Wiki Links

Use `[[filename]]` to reference other files:
- `[[meta - file conventions]]` - Links to this file
- `[[meta - processing]]` - Links to processing instructions
- `[[meta - git workflow]]` - Links to git workflow

When encountering a wiki link, resolve and read the linked file.

### Inline Links over Related Sections

Prefer wiki links **inline where the concept is mentioned** rather than collecting them in a "Related" section at the bottom.

**Preferred:**
```markdown
Follow the [[meta - git workflow]] for commits. Use the
[[meta - numbered lists for instructions]] pattern when presenting options.
```

**Avoid:**
```markdown
Follow the git workflow for commits. Use the numbered list pattern.

## Related
- [[meta - git workflow]]
- [[meta - numbered lists for instructions]]
```

Inline links provide context at point of use. Related sections are acceptable for truly supplementary references that don't fit naturally in the prose.
