# /toskill skill

Create a new Claude Code skill from the current conversation.

## Usage
```
/toskill [skill-name]
```

## Instructions

When invoked, use the AskUserQuestion tool to gather skill details:

**Question:** "What should this skill do?"

**Options:**
1. **Capture this workflow** - Turn what we just did into a repeatable skill
2. **New skill from scratch** - Define a new skill based on an idea discussed
3. **Refine existing skill** - Improve a skill based on learnings from this session

## After Selection

### Capture This Workflow
- Analyze the conversation for the pattern/workflow performed
- Identify inputs, steps, and outputs
- Generalize into reusable instructions

### New Skill From Scratch
- Ask follow-up: "Describe what the skill should do and when to use it."
- Draft skill based on description

### Refine Existing Skill
- Ask: "Which skill? What should change?"
- Read the existing skill from `.claude/commands/`
- Apply improvements

## Skill Structure

Follow the established format:

```markdown
# /<skill-name> skill

<One-line description>

## Usage
\```
/<skill-name> [arguments]
\```

## Instructions

<Detailed instructions for Claude to follow>

## Options/Workflow

<Any user choices or decision points>

## Output

<What the skill produces>
```

## File Location

Write to `.claude/commands/<skill-name>.md`

## Snapshot Skills

If the skill aggregates or analyzes information (like `/reflect`, `/consistency`, `/next`), it should:

1. **Create a snapshot file** in `memory/` with dated prefix (e.g., `next - yyyy-mm-dd-hhmm - claim.md`)
2. **Add the prefix** to [[meta - prefixes]] and [[meta - file conventions]]
3. **Use numbered lists** per [[meta - numbered lists for instructions]] for user selection
4. **Update the file** with wiki links as items are acted upon

This creates traceable records of what was presented and what actions were taken.

## After Creation

- Confirm the new skill name to user
- Mention they can invoke it with `/<skill-name>`
- Offer to test it immediately
