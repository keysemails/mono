# /plan-continue skill

Resume work on an existing plan file.

## Usage
```
/plan-continue [plan-name]
```

## Instructions

### 1. Find Active Plans

Search `memory/` for `plan - *.md` files. Identify incomplete plans by checking:
- Actions without "Done" or completion markers
- Missing "Created Artifacts" that should exist
- Progress Log entries that indicate in-progress work

### 2. Auto-Select or Present Options

**Single incomplete plan:**
```
Only one incomplete plan found: [[plan - 2026-01-24-1030 - add user auth]]

Next action: Implement login endpoint

continue? (Enter/n)
```

**Multiple incomplete plans:**
Use [[meta - numbered lists for instructions]] pattern:
```
Active plans found:

1 - [[plan - 2026-01-24-1030 - add user auth]]
  - 3/5 actions complete
  - Next: Implement login endpoint

2 - [[plan - 2026-01-23-1500 - refactor database layer]]
  - 1/4 actions complete
  - Next: Add connection pooling

Which plan would you like to continue?
```

**No incomplete plans:**
```
No incomplete plans found.

Options:
1 - Create a new plan with /sprint-start
2 - View completed plans
```

### 3. Load Plan Context

When a plan is selected:

1. **Read the plan file** - Understand actions and progress
2. **Read linked spec** - Refresh on requirements
3. **Read linked goal** - Understand desired outcome
4. **Check Progress Log** - See where we left off
5. **Check Learnings** - Apply discovered insights

### 4. Present Current State

```markdown
## Resuming: [[plan - 2026-01-24-1030 - add user auth]]

**Goal:** [[goal - 2026-01-24-1000 - add user auth]]
**Spec:** [[spec - user authentication]]

### Progress
- [x] Set up auth middleware
- [x] Create user model
- [ ] Implement login endpoint
- [ ] Implement logout endpoint
- [ ] Add session management

### Learnings So Far
- JWT tokens need 15-minute expiry per security policy
- Found existing password hashing utility in utils/crypto.ts

### Next Action
Implement login endpoint

Ready to continue?
```

### 5. Continue Work

When user confirms:
1. Begin work on next incomplete action
2. Follow normal work patterns (commit after each logical change)
3. Update plan file as work progresses
4. Add to Progress Log with timestamps

### 6. Quick Continuation

After completing each action, prompt:

```
Completed: Implement login endpoint

Next: Implement logout endpoint
continue?
```

This aligns with the [[c - an action is a logical unit of work]] pattern.

## Output

- Resumes work on selected plan
- Updates plan file with progress

## When to Use

- Starting a new session to continue previous work
- Returning to a paused plan
- Checking status of active work

## Related

- [[meta - coding project structure]] - Plan workflow
- [[meta - git workflow]] - Commit strategy
- [[sprint-start]] - Creating new plans
