# /toscript skill

Export code from the conversation to a script file.

## Usage
```
/toscript [optional filename or language hint]
```

## Instructions

When invoked, use the AskUserQuestion tool to ask what should be exported:

**Question:** "What would you like to export as a script?"

**Options:**
1. **All code blocks** - Extract all code from the conversation into one file
2. **Specific code** - Let me select which code blocks to include
3. **Composite script** - Combine related snippets into a working script with proper structure

## After Selection

### All Code Blocks
- Extract every code block from the conversation
- Separate with comments indicating source/context
- Detect language from code block annotations or content

### Specific Code
- Ask a follow-up: "Which code? Describe what it does or paste a snippet to identify it."
- Extract only the matching code blocks

### Composite Script
- Identify related code snippets
- Combine into a coherent, runnable script
- Add imports, main guard, error handling as appropriate
- Add brief comments for clarity

## File Naming & Location

- If user provided a filename hint, use it
- Otherwise, derive name from script purpose (e.g., `process-files.sh`, `convert-data.py`)
- Ask user for preferred location if unclear
- Default to project root or a `scripts/` directory if one exists

## Language Detection

Infer from:
1. Code block language annotations (```python, ```bash, etc.)
2. Shebang lines
3. Syntax patterns
4. User's hint in the command

## Output Format

Include appropriate:
- Shebang line for shell scripts
- Encoding declaration for Python
- Brief header comment describing purpose
- Make executable if shell script (`chmod +x`)
