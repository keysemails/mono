# /human-sort skill

Reorganize the human notes file - regroup content and manage sections without changing any human-written text.

## Usage
```
/human-sort
/human-sort @(section-name)
```

## Critical Rule

**NEVER modify human-written text.** You may only:
- Add, rename, or remove section headers (`## Section Name`)
- Move blocks of text between sections
- Add the horizontal rule separators (`---`)

The actual notes (everything that isn't a section header or separator) must remain exactly as written, including typos, formatting, and punctuation.

## Instructions

### 1. Read Human Notes

Read `memory/human.md` to understand current structure.

### 2. Present Current Structure

Display sections using [[meta - numbered lists for instructions]] pattern:

```
Current sections in human.md:

1 - Mono / Workflow (12 items)
2 - Plan Mode (1 item)
3 - Showrules / Debug (2 items)
4 - Subprojects (5 items)
5 - Session / UI (3 items)
6 - tomanim (4 items)
7 - vtt (1 item)

Actions:
- m - Move items (e.g., "m 1.3 -> 4" moves item 3 from section 1 to section 4)
- n - New section (e.g., "n Hooks" creates new section)
- r - Rename section (e.g., "r 3 Debug" renames section 3)
- d - Delete empty section
- v - View section contents
- done - Finish and save
```

### 3. Handle View Request

If user requests `v <number>`, show that section's contents with item numbers:

```
## Mono / Workflow

1.1 - (new)
      should have top level file for human notes
      and then use those in sessions...

1.2 - ? do we need the session start hook
        . ah we may be doing some dynamic stuff
        . check again

1.3 - better support for in file adding of {{feedback}}
```

Items are separated by blank lines in the original. Each contiguous block of text is one item.

### 4. Handle Move Request

When user says `m 1.3 -> 4`:
1. Identify the text block (item 1.3)
2. Remove it from section 1
3. Add it to section 4
4. Preserve exact text, only change location

### 5. Handle New Section

When user says `n <name>`:
1. Create new empty section with `## <name>` header
2. Add separator `---` before it
3. Present updated structure

### 6. Handle Rename

When user says `r <number> <new-name>`:
1. Change only the section header text
2. Keep all contents unchanged

### 7. Handle Delete

When user says `d <number>`:
1. Only allow if section is empty
2. Remove the header and separator
3. Refuse if section has content

### 8. Save Changes

When user says `done`:
1. Rewrite `memory/human.md` with new structure
2. Preserve the YAML frontmatter (update `changed` timestamp)
3. Preserve the header block explaining fleeting notes
4. Commit per [[meta - git workflow]]

### 9. Argument Shortcut

If called with `@(section-name)`:
1. Jump directly to viewing that section
2. Allow moving items out of it

## Integrity Check

Before saving, verify:
- All original text blocks are present
- No text has been modified (character-for-character match)
- Only structural elements (headers, separators) changed

If verification fails, abort and show what would have been lost.

## Output

- Updates: `memory/human.md` (structure only)
- Commits changes with message describing reorganization

## Related

- [[meta - file conventions]] - File standards
- [[meta - numbered lists for instructions]] - Selection pattern
