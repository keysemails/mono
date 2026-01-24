# /toclaude skill

Extract learnings from the current conversation and add them to the project's CLAUDE.md.

## Usage
```
/toclaude [optional: specific instruction to add]
```

## Instructions

### If argument provided
- Use the provided text as the instruction to add
- Read `./CLAUDE.md` to find the appropriate section
- Add the instruction and show the diff

### If no argument (conversation analysis)
Analyze the preceding conversation to identify:

1. **Corrections made** - Did the user correct Claude's approach? That's a rule.
2. **Preferences expressed** - Did the user say "I prefer X" or "always do Y"?
3. **Patterns established** - Did we establish a workflow that should be repeated?
4. **Project conventions** - Did we discover or create naming/structure conventions?
5. **Tool usage** - Did we learn how to use a project-specific tool or command?

Use the AskUserQuestion tool to confirm findings:

**Question:** "I found these potential instructions from our conversation. Which should be added to CLAUDE.md?"

**Options:** Present 2-4 extracted learnings as multi-select options (set `multiSelect: true`)

Each option should be a concise, actionable instruction written in imperative form (e.g., "Always run tests before committing" not "We discussed running tests").

## After Selection

Decide whether to add directly or create a linked file:

### Add directly to CLAUDE.md when:
- It's a simple rule or preference (1-3 bullet points)
- It fits naturally into an existing section

### Create a separate file and wiki-link when:
- The topic is substantial (would need its own `##` section with multiple subsections)
- It's a workflow or process with multiple steps
- It might grow over time as we learn more
- It's a reference document (conventions, patterns, templates)

**If creating a linked file:**
1. Create `memory/meta - <topic>.md` with the full instructions
2. Add a wiki-link reference in CLAUDE.md: `- [[meta - <topic>]] - <one-line description>`
3. Place the link in the "Core References" section or create an appropriate section

**If adding directly:**
1. Read `./CLAUDE.md`
2. Determine the best section for each instruction:
   - Match to existing sections if appropriate
   - Create a new section if the topic is distinct
3. Edit the file to add the selected instructions
4. Show the diff of changes made

## Output Format

Instructions should be:
- Written as bullet points under the appropriate `##` section
- Imperative and direct ("Do X" not "You should do X")
- Specific enough to be actionable
- General enough to apply beyond this one conversation

## File Location

Always updates: `./CLAUDE.md` (project root)
