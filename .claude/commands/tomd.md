# /tomd skill

Export conversation content to a markdown file.

## Usage
```
/tomd [optional topic hint]
```

## Instructions

When invoked, use the AskUserQuestion tool to ask what should be exported:

**Question:** "What would you like to export to markdown?"

**Options:**
1. **Full chat** - Export the entire conversation as-is
2. **Specific part** - Let me select which messages/topics to include
3. **Summary** - Generate a condensed summary of key points and learnings

## After Selection

### Full Chat
- Export all user and assistant messages
- Preserve code blocks and formatting
- Use headers to separate turns

### Specific Part
- Ask a follow-up: "Which part? Describe the topic or paste a snippet to identify the section."
- Extract only the relevant exchanges

### Summary
- Identify main topics discussed
- Extract key decisions, learnings, and conclusions
- Condense into a readable document

## File Naming

Follow [[file-conventions]] for naming:
- Determine appropriate prefix based on content (`research -`, `idea -`, `question -`, etc.)
- Use a descriptive claim that captures the main content
- If user provided a topic hint in the command, use it to inform the name

## Output Format

```markdown
---
created: <current-timestamp>
changed: <current-timestamp>
prior_commit: <current-HEAD>
---

# <Title based on content>

<Exported content here>
```

## File Location

Write to `memory/` directory unless user specifies otherwise.
