---
created: 2026-01-23T13:55:09
changed: 2026-01-24T05:51:40
prior_commit: 278c6c5
---

# File Prefixes

Standard prefixes for the flat file naming convention. See [[meta - file conventions]] for dated vs non-dated naming.

## Dated Prefixes

These use `prefix - yyyy-mm-dd-hhmm - claim.md`:

| Prefix | Purpose |
|--------|---------|
| `architecture` | Codebase architecture snapshots - structure and component documentation |
| `bug` | Bug reports (discovered at a specific time) |
| `codereview` | Code review reports - codebase quality analysis with severity ratings |
| `consistency` | Consistency reports - project structure and inconsistency analysis |
| `drift` | Drift analysis - comparing documented intent to current reality |
| `goal` | Sprint/feature goals - problem, desired outcome, preferences snapshot |
| `next` | Actionable items snapshots - aggregated view of what to work on |
| `plan` | Task plans (capture intent at a specific time) |
| `proposal` | Suggested changes or improvements for discussion |
| `reflect` | Reflection snapshots - extracted learnings, tasks, incoherences |
| `research` | Research findings (point-in-time knowledge capture) |
| `session` | Chat session exports (from /tomd) |
| `todo` | Individual actionable tasks |
| `solved` | Completed todos (renamed from `todo` when work is done) |
| `videoplan` | Scene-by-scene video structure |

## Video Planning Prefixes

Used by `/tomanim` skill for planning workflow:

| Prefix | Purpose |
|--------|---------|
| `analysis` | Deep content analysis for visualization |
| `brainstorm` | Visualization options exploration |
| `videoplan` | Scene-by-scene video structure (also in dated above) |

## Standard Prefixes

These use `prefix - claim.md`:

| Prefix | Purpose |
|--------|---------|
| `c` | Concepts - claims written as prose (see [[meta - claim prose]]) |
| `idea` | Ideas and brainstorms |
| `incoherence` | Contradictions or unclear areas identified during reflection |
| `learning` | Extracted learnings/insights from reflection |
| `meta` | Meta/system files |
| `moc` | Map of Content - hierarchy/index files |
| `problem` | Problems identified |
| `question` | Questions to explore |
| `spec` | Specifications |
| `sprint` | Sprint plans |

## Todo → Solved Workflow

When a todo is complete, rename it from `todo - ...` to `solved - ...`:
- Preserves the timestamp and claim
- Use [[meta - handle renames for wiki link files]] to update references
- `/consistency` will detect implemented todos and prompt for renaming

## Adding New Prefixes

If you discover a file type that doesn't fit existing prefixes:
1. Propose the new prefix to the user
2. Add it to this table with a clear purpose description
3. Keep prefixes short and descriptive

**Principle:** Prefer domain-specific prefixes over overloading generic ones. For example, use `incoherence` for contradictions found during reflection rather than stuffing them into `bug`. Each prefix should have a clear, distinct purpose.

## Related

- [[meta - file conventions]] - Full naming and structure conventions
