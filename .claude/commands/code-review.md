# /code-review skill

Systematic codebase quality analysis with actionable findings.

## Usage
```
/code-review [scope]
```

## Scope Options

- `(no argument)` - Review entire codebase
- `path/to/dir` - Review specific directory
- `path/to/file.ts` - Review specific file
- `recent` - Review files changed in recent commits

## Instructions

### 1. Analyze Codebase

Examine the specified scope for:

**Critical Issues**
- Security vulnerabilities (injection, XSS, exposed secrets)
- Data loss risks
- Race conditions
- Unhandled error paths that could crash

**Warnings**
- Performance bottlenecks
- Memory leaks
- Missing error handling
- Deprecated API usage
- Code duplication

**Suggestions**
- Readability improvements
- Better naming
- Documentation gaps
- Test coverage opportunities

### 2. Identify Patterns

Look for:
- **Positive patterns** - Good practices being followed consistently
- **Concerning patterns** - Anti-patterns or bad habits spreading
- **Inconsistencies** - Mixed approaches to same problem

### 3. Create Review File

Create `memory/codereview - <timestamp> - <claim>.md`:

```markdown
---
created: <timestamp>
changed: <timestamp>
prior_commit: <hash>
category: Code Review
scope: <what was reviewed>
---

# Code Review: [Scope Description]

## Executive Summary

**Health Rating:** [emoji] [rating]
- Good: Solid codebase, minor issues only
- Fair: Some concerns need attention
- Needs Attention: Critical issues or significant technical debt

**Key Findings:**
- [1-3 sentence summary of most important findings]

## Findings by Severity

### Critical

1 - [Finding title]
  - **Location:** [file:line](path/to/file.ts#L42)
  - **Issue:** [Description of the problem]
  - **Risk:** [What could go wrong]
  - **Recommendation:** [How to fix]

### Warnings

2 - [Finding title]
  - **Location:** [file:line](path/to/file.ts#L100)
  - **Issue:** [Description]
  - **Recommendation:** [How to address]

### Suggestions

3 - [Finding title]
  - **Location:** [file.ts](path/to/file.ts)
  - **Observation:** [What could be better]
  - **Suggestion:** [Improvement idea]

## Pattern Analysis

### Positive Patterns
- [Pattern observed and where it's used well]

### Concerning Patterns
- [Anti-pattern and examples]

### Inconsistencies
- [Mixed approaches to same problem]

## Appendix: File-by-File Findings

### [filename.ts](path/to/filename.ts)
- Line 42: [Brief finding]
- Line 100-105: [Brief finding]

### [other-file.ts](path/to/other-file.ts)
- Line 15: [Brief finding]

## Summary

- **Files reviewed:** X
- **Critical issues:** Y
- **Warnings:** Z
- **Suggestions:** W

Which items would you like to address? (e.g., "1, 2.1")
```

### 4. Health Rating Guide

Use these ratings:

- **Good** - No critical issues, few warnings, codebase follows good practices
- **Fair** - No critical issues but multiple warnings, or inconsistent patterns
- **Needs Attention** - Has critical issues, or many warnings suggesting systemic problems

### 5. Commit

Per [[meta - git workflow]], commit after creating the review file.

### 6. Acting on Findings

When user selects items to address:
1. Fix the issue
2. Update the review file with a nested link showing the fix:

```markdown
1 - SQL injection in user query
  - **Location:** [db.ts:42](src/db.ts#L42)
  - **Issue:** User input concatenated into SQL
  - **Fixed:** [commit abc1234](link) - Converted to parameterized query
```

## Output

- Creates: `memory/codereview - <timestamp> - <claim>.md`

The claim should summarize findings:
- `codereview - 2026-01-24-1030 - 2 critical issues in auth module.md`
- `codereview - 2026-01-24-1030 - healthy codebase minor suggestions.md`

## When to Use

- Before major releases
- After acquiring or inheriting a codebase
- Periodic quality checks
- Before significant refactoring
- When onboarding to understand code quality

## Related

- [[meta - file conventions]] - Naming and frontmatter standards
- [[meta - numbered lists for instructions]] - Selection pattern for actionable items
- [[meta - prefixes]] - codereview prefix documentation
