# /architecture skill

Create comprehensive codebase snapshots for historical reference and onboarding.

## Usage
```
/architecture [focus-area or question]
```

## Philosophy

Act as a **documentarian, not an evaluator**. Document what exists without suggesting improvements or optimizations. The goal is to capture the codebase "as-is" for future reference.

## Instructions

### 1. Determine Mode

**Full Snapshot Mode** (no arguments):
- Comprehensive documentation of the entire codebase
- Use for onboarding, major milestones, or periodic snapshots

**Focused Query Mode** (with arguments):
- Answer specific questions about architecture
- Examples: `/architecture how does auth work?`, `/architecture database layer`

### 2. Gather Information

For full snapshots, document:

1. **Git State**
   - Current branch and commit
   - Recent significant commits
   - Active branches

2. **Directory Structure**
   - Top-level organization
   - Key directories and their purposes

3. **Tech Stack**
   - Languages and frameworks
   - Key dependencies
   - Build tools

4. **Module Breakdown**
   - Major components/modules
   - How they connect
   - Data flow patterns

5. **Entry Points**
   - Where execution begins
   - Key configuration files
   - Environment requirements

For focused queries, document only what's relevant to the question.

### 3. Create Architecture File

Create `memory/architecture - <timestamp> - <claim>.md`:

```markdown
---
created: <timestamp>
changed: <timestamp>
prior_commit: <hash>
category: Architecture
---

# Architecture: [Project Name or Focus Area]

## Git State

- **Branch:** main
- **Commit:** abc1234 - "Recent commit message"
- **Active branches:** feature/x, bugfix/y

## Directory Structure

```
project/
  src/
    components/    # UI components
    services/      # Business logic
    utils/         # Shared utilities
  tests/
  config/
```

## Tech Stack

- **Language:** TypeScript 5.x
- **Framework:** React 18
- **Build:** Vite
- **Key deps:** react-query, zustand, tailwind

## Modules

### Authentication
[Description of auth module, files involved, how it works]

### Data Layer
[Description of data handling, API calls, state management]

<!-- Add more modules as needed -->

## Entry Points

- `src/main.tsx` - Application bootstrap
- `vite.config.ts` - Build configuration
- `.env` - Environment variables (AUTH_URL, API_BASE)

## Notes

<!-- Any additional context or observations -->
```

The claim should describe what was documented:
- `architecture - 2026-01-24-1030 - full codebase snapshot.md`
- `architecture - 2026-01-24-1030 - authentication flow.md`

### 4. Follow-up Questions

If user asks follow-up questions about the same architecture:
1. **Append to existing file** rather than creating a new one
2. Add a new section with timestamp
3. Update the `changed` timestamp

```markdown
## Follow-up: How does session refresh work?
_Added: 2026-01-24 11:30_

[Answer to the follow-up question]
```

### 5. Commit

Per [[meta - git workflow]], commit after creating/updating the architecture file.

## Output

- Creates/updates: `memory/architecture - <timestamp> - <claim>.md`

## When to Use

- Onboarding to a new codebase
- After major refactors or architectural changes
- Before starting significant new work
- Periodic snapshots for historical reference
- Answering "how does X work?" questions

## Related

- [[meta - file conventions]] - Naming and frontmatter standards
- [[meta - coding project structure]] - Sprint workflow context
