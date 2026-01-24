# /showrules skill

Toggle "cite rules" mode. When active, Claude cites relevant rules before every response.

## Usage
```
/showrules
```

## Instructions

### 1. Detect Current State

Check if the phrase `showrules mode is currently ACTIVE` appears earlier in this conversation.

### 2. Toggle

**If mode is currently ACTIVE:**
- Output: `showrules mode is currently INACTIVE`
- Stop following the citation rules below

**If mode is currently INACTIVE (or not set):**
- Output: `showrules mode is currently ACTIVE`
- Follow the citation rules below for all subsequent responses

### 3. Citation Rules (When Active)

For every response while showrules mode is ACTIVE:

**Start with a `# Rules Applied` section:**

```markdown
# Rules Applied

- [Section Name](CLAUDE.md#section-anchor) - brief summary
- [meta - file conventions](memory/meta - file conventions.md) - brief summary

<actual response follows>
```

**Use VSCode-clickable markdown links:**
- For CLAUDE.md sections: `[Section Name](CLAUDE.md#section-anchor)`
- For memory files: `[filename](memory/filename.md)`

**If no rules apply:** Still include the header with `- (none directly applicable)`

### 4. Rule Sources

Present rule sources using the [[meta - numbered lists for instructions]] pattern:

```
1 - CLAUDE.md
  - 1.1 - [Read Context Before Acting](CLAUDE.md#critical-read-context-before-acting)
  - 1.2 - [Externalisation](CLAUDE.md#critical-externalisation)
  - 1.3 - [Plan Mode](CLAUDE.md#plan-mode)
  - 1.4 - [Wiki Links](CLAUDE.md#wiki-links)
  - 1.5 - [Flat Hierarchy](CLAUDE.md#flat-hierarchy)
  - 1.6 - [Settings File Safety](CLAUDE.md#settings-file-safety)
  - 1.7 - [Questions vs Work](CLAUDE.md#questions-vs-work)
  - 1.8 - [Todos as Actions](CLAUDE.md#todos-as-actions)
  - 1.9 - [Ratifying Behavior Changes](CLAUDE.md#ratifying-behavior-changes)
  - 1.10 - [Session End](CLAUDE.md#session-end)
2 - Meta Files
  - 2.1 - [meta - file conventions](memory/meta - file conventions.md)
  - 2.2 - [meta - git workflow](memory/meta - git workflow.md)
  - 2.3 - [meta - processing](memory/meta - processing.md)
  - 2.4 - [meta - prefixes](memory/meta - prefixes.md)
  - 2.5 - [meta - claim prose](memory/meta - claim prose.md)
  - 2.6 - [meta - dynamic context](memory/meta - dynamic context.md)
  - 2.7 - [meta - numbered lists for instructions](memory/meta - numbered lists for instructions.md)
3 - Embedded Rules (not yet externalized)
  - 3.1 - Session startup hook in ~/.claude/CLAUDE.md → propose: meta - session hooks.md
  - 3.2 - Skill-specific rules in .claude/commands/*.md → propose: meta - skills.md
```

**Operation-specific rule mapping:**

| Operation | Primary Sources |
|-----------|-----------------|
| Git operations | 1.1, 2.2 |
| Creating/editing files | 1.1, 2.1 |
| `/process` command | 2.3 |
| Plan mode | 1.3, 2.1 |
| Session end | 1.10 |

### 5. Citation Judgment

- Only cite rules that actually apply to the current request
- Include a brief summary (5-10 words) explaining relevance
- List most relevant rules first
- Don't over-cite - be selective
- If a file isn't loaded in context, read it first, then cite relevant rules

## Output

- Activation: `showrules mode is currently ACTIVE`
- Deactivation: `showrules mode is currently INACTIVE`

## Related

- [[CLAUDE.md]] - Main project instructions
- [[meta - file conventions]] - File naming standards
- [[meta - git workflow]] - Git conventions
- [[meta - numbered lists for instructions]] - Numbered list pattern
