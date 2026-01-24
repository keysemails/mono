# /done skill

End the current session with export and merge offer.

## Usage
```
/done
```

## Instructions

### 1. Detect Project Context

**First, check for `.PROJECT` file:**

```bash
cat .PROJECT 2>/dev/null
```

If `.PROJECT` exists and specifies a project, use that as the default target (unless session activity clearly indicates work in a different project).

**Then run the detection script:**

```bash
.claude/scripts/detect-project.sh
```

**Determine the target project:**

1. **Use `.PROJECT` default if set**: If `.PROJECT` specifies a project and session work matches, use it without prompting.

2. **Check if working in a subproject branch**: Look at the subprojects' `uncommitted` and `branch` fields. If a subproject has a non-main branch or uncommitted changes, work was likely done there.

3. **Review session activity**: Consider what files were created/modified during the session. If work was done in `repo/<subproject>/`, that's the target.

4. **If ambiguous**, ask:
   ```
   This session touched multiple projects. Where should I export?
   1 - mono (memory/)
   2 - <subproject> (repo/<subproject>/memory/)
   ```

5. **Set target paths** based on selection:
   - **mono**: `memory/` and current git context
   - **subproject**: `repo/<subproject>/memory/` and `cd repo/<subproject>` for git operations

### 2. Export Session

Run the export script with the correct path:

**For mono:**
```bash
python3 .claude/scripts/jsonl-to-md.py -o "memory/session - $(date '+%Y-%m-%d-%H%M') - <brief-claim>.md"
```

**For subproject:**
```bash
python3 .claude/scripts/jsonl-to-md.py -o "repo/<subproject>/memory/session - $(date '+%Y-%m-%d-%H%M') - <brief-claim>.md"
```

The `<brief-claim>` should summarize what was accomplished in the session.

### 3. Check for Sensitive Data

Scan the export for sensitive patterns:
```bash
grep -iE "(api.?key|token|secret|password|credential|bearer)" "<export-path>" | head -5
```

If API keys, tokens, credentials, or private paths were discussed, ask what to redact before committing.

### 4. Commit Export

**For mono:**
```bash
git add "memory/session - ..." && git commit -m "Add session export: <claim>"
```

**For subproject:**
```bash
cd repo/<subproject> && git add "memory/session - ..." && git commit -m "Add session export: <claim>"
```

Follow [[meta - git workflow]] for commit format.

### 5. Merge

If in a task branch, ask: "Should I merge the branch?"

For subprojects, ensure you're in the correct repo before merging:
```bash
cd repo/<subproject> && git checkout <main-branch> && git merge --no-ff <task-branch> -m "Merge <task-branch>: <description>"
```

## Output

- Creates: `<project>/memory/session - <timestamp> - <claim>.md`
- Optionally: Merges task branch to main/master

## Related

- `/change-project` - Switch project context mid-session
- `/detect-project` - Initial project detection
- `/reflect @<session-file>` - Analyze a session export
