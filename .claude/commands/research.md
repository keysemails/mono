---
description: Research and document techniques or industry standards
allowed-tools: Read, Write, Edit, Bash(ls:*), Bash(date:*), Bash(git*), Task, WebSearch
---

# Research: $ARGUMENTS

Research techniques and industry standards, creating a scannable knowledge document for future reference.

## Mode Detection

**Arguments required** (e.g., `/research Perlin noise algorithms`):
  Topic to research

**If no arguments**:
  Prompt for topic

---

## Implementation Steps

### 1. Get Topic

**If `$ARGUMENTS` is empty**:
```
What topic would you like to research?

Examples:
- "Perlin noise algorithms"
- "WebSocket synchronization patterns"
- "Entity Component System architecture"
- "A* pathfinding optimization"

Topic:
```

**If `$ARGUMENTS` provided**:
Use directly.

### 2. Parse Topic into Components

Extract:
- **Main topic**: Primary subject (e.g., "terrain-generation", "pathfinding")
- **Approach/Variant**: Specific technique (e.g., "perlin-noise", "a-star")

**Parsing strategy**:
- Look for technique keywords (algorithm names, pattern names, technology names)
- If specific technique mentioned, use it as variant
- Otherwise, use topic as main subject

**Examples**:
- "Perlin noise algorithms" → Main: `perlin-noise`, Variant: `algorithms`
- "A* pathfinding" → Main: `pathfinding`, Variant: `a-star`
- "ECS architecture" → Main: `ecs`, Variant: `architecture`

### 3. Check Existing Knowledge

```bash
ls memory/research\ -\ *.md 2>/dev/null
```

Check if similar topic already exists:
- Look for filenames containing main topic keywords
- If found, show to user:

```
A document on a similar topic already exists:
- memory/research - perlin noise basics.md

Options:
1. Create new document anyway
2. Read existing document first
3. Cancel

Choose (1-3):
```

### 4. Conduct Research (Quick Overview Mode)

Use Task agent with WebSearch to gather information.

**Research scope** (user preference: quick overview):
- Focus on **practical, actionable information**
- Keep it **scannable** - bullet points and short paragraphs
- Prioritize **common use cases** over edge cases
- Include **authoritative sources** for deeper reading

**Research areas**:
1. **Key Concepts**: Core ideas and definitions (2-3 concepts)
2. **Common Patterns**: Standard implementations (2-3 patterns)
3. **Best Practices**: Recommended approaches
4. **Trade-offs**: Pros/cons of different approaches (table format)
5. **Resources**: Links to official docs, tutorials, papers

**Constraint for Task agent**:
```
Research "<topic>" with focus on quick overview.
Gather practical information that's scannable.
Include:
- 2-3 key concepts with brief explanations
- 2-3 common implementation patterns
- Trade-offs table comparing approaches
- Links to authoritative resources (docs, tutorials)

Keep it concise - this is a quick reference guide.
```

### 5. Auto-Detect Category

Based on topic content, categorize as:
- **Algorithm**: If topic involves computational procedures (noise, pathfinding, sorting)
- **Pattern**: If topic involves design patterns (singleton, observer, ECS)
- **Architecture**: If topic involves system design (client-server, microservices)
- **Tool**: If topic involves specific technology (WebSocket, Redis, Docker)
- **Technique**: If topic involves development practices (TDD, profiling)

### 6. Structure Knowledge Document

Use YAML frontmatter per [[meta - file conventions]]:

```markdown
---
created: yyyy-mm-ddThh:mm:ss
changed: yyyy-mm-ddThh:mm:ss
prior_commit: <current-HEAD-or-null>
category: <Algorithm|Pattern|Architecture|Tool|Technique>
---

# <Topic>: <Approach/Variant>

## Overview

<2-3 sentence high-level summary of what this is and when to use it>

## Key Concepts

- **Concept 1**: Brief explanation (1-2 sentences)
- **Concept 2**: Brief explanation
- **Concept 3**: Brief explanation

## Common Patterns

### Pattern 1: <Name>

- **Use case**: When to use this pattern
- **Implementation**: High-level steps or approach
- **Example**: Brief code snippet or pseudocode (if applicable)

### Pattern 2: <Name>

...

## Trade-offs

| Approach    | Pros       | Cons        |
| ----------- | ---------- | ----------- |
| <Variant 1> | <benefits> | <drawbacks> |
| <Variant 2> | <benefits> | <drawbacks> |

## Best Practices

- Practice 1: Explanation
- Practice 2: Explanation
- Practice 3: Explanation

## Resources

- [Official Documentation](url) - Brief description
- [Tutorial/Article](url) - Brief description
- [Research Paper](url) - Brief description (if applicable)
- [Video/Course](url) - Brief description (if applicable)

## Related

- [[research - related topic]] - How it relates
- [[learning - related insight]] - Connection to prior learning

## When to Use

- Scenario 1: Description
- Scenario 2: Description

## When NOT to Use

- Scenario 1: Description
- Scenario 2: Description
```

### 7. Generate Filename

**Get timestamp once** (use for both filename and frontmatter):
```bash
date +"%Y-%m-%d-%H%M"
```

Format: `research - yyyy-mm-dd-hhmm - <claim>.md`

**Claim should be prose** per [[meta - claim prose]]:
- Readable phrase capturing the main content
- Not kebab-case keywords

**Sanitize**:
- Keep readable prose with spaces
- Remove special characters except spaces and hyphens

**Examples** (assuming timestamp `2026-01-24-1530`):
- "Perlin noise algorithms" → `research - 2026-01-24-1530 - perlin noise algorithms.md`
- "A* pathfinding" → `research - 2026-01-24-1530 - a star pathfinding.md`
- "WebSocket synchronization" → `research - 2026-01-24-1530 - websocket synchronization patterns.md`

### 8. Create Document

Write directly to: `memory/research - yyyy-mm-dd-hhmm - <claim>.md`

**No subdirectory** - this project uses a flat hierarchy per [[meta - file conventions]].

### 9. Present Summary

Show brief overview to user (example with timestamp `2026-01-24-1530`):

```
Research document created: memory/research - 2026-01-24-1530 - perlin noise algorithms.md

Topic: Perlin Noise Algorithms
Category: Algorithm

Key Takeaways:
- Perlin noise generates natural-looking gradients using gradient vectors
- Common in procedural terrain, texture, and cloud generation
- Trade-off: Quality vs performance (octaves increase detail but cost)
- Best for: Continuous, organic-looking randomness
- Alternatives: Simplex noise (faster), Worley noise (cellular patterns)

Resources:
- Original Perlin paper (1985)
- Improved noise reference implementation
- Tutorial: Understanding Perlin noise

Would you like me to:
1. Research related topics (Simplex noise, Worley noise)
2. Go deeper on a specific aspect
3. Continue with feature work
```

### 10. Offer Follow-up

Ask if user wants to:
- Research related topics
- Deep-dive into specific aspect (creates new learn doc)
- Return to feature work

---

## Example Usage

**Basic usage**:
```bash
/research Perlin noise algorithms
```

Creates: `memory/research - 2026-01-24-1530 - perlin noise algorithms.md`

**Another example**:
```bash
/research ECS architecture patterns
```

Creates: `memory/research - 2026-01-24-1530 - ecs architecture patterns.md`

**With no arguments**:
```bash
/research
> What topic would you like to research?
> A* pathfinding optimization
```

Creates: `memory/research - 2026-01-24-1530 - a star pathfinding optimization.md`

---

## Error Handling

**No topic provided and user input empty**:
```
Error: No topic specified.

Suggestion: Provide a topic to research, e.g., `/research Perlin noise`
```

**WebSearch fails**:
```
WebSearch unavailable. Using existing knowledge to create document.

Please provide key information about <topic>:
- Key concepts:
- Common use cases:
- Resources/links:
```

**Topic too broad**:
```
The topic "<topic>" is quite broad. Consider narrowing it down:

Examples:
- Instead of "terrain generation" → "terrain generation with Perlin noise"
- Instead of "networking" → "WebSocket connection patterns"
- Instead of "AI" → "A* pathfinding algorithm"

Narrow down your topic or proceed anyway? (narrow/proceed):
```

**Filename conflict**:
```
A file on this topic already exists: memory/research - 2026-01-20-1200 - perlin noise algorithms.md

Options:
1. Overwrite existing document
2. Create with different name
3. Read existing document first
4. Cancel

Choose (1-4):
```

---

## Research Quality Guidelines

**Quick overview mode** (user preference):

1. **Conciseness**: Each section should be scannable in 30 seconds
2. **Practicality**: Focus on "how to use" over "how it works internally"
3. **Examples**: Include brief code snippets where helpful
4. **Resources**: Always link to authoritative sources for deep-dives
5. **Trade-offs**: Use table format for easy comparison
6. **Actionable**: Reader should know when to use and when not to use

**What to avoid**:
- Long paragraphs (break into bullets)
- Excessive detail (save for "Resources" links)
- Jargon without definitions
- Theoretical focus without practical application

---

## Integration with Sprint Workflow

Knowledge documents support feature development per [[meta - coding project structure]]:

**During `/goal`**:
- Research techniques before defining requirements
- Reference in goal's preferences section

**During `/spec`**:
- Learn about unfamiliar concepts as needed
- Document findings for team knowledge

**Example flow**:
```bash
/goal terrain-generation
> Need to learn about noise algorithms first

/learn Perlin noise algorithms
> Creates knowledge doc

/spec terrain-generation
> References knowledge doc during specification
```

---

## Important Notes

- Knowledge docs are **reference material**, not implementation plans
- They're **version-controlled** with the project
- Future sessions can reference them via [[wiki-links]]
- **Quick overview** means scannable, not superficial
- Focus on **practical application** in the project's domain
- Link to **authoritative sources** for deeper learning
- Update docs if you find better information later

## Related

- [[meta - file conventions]] - Naming and frontmatter standards
- [[meta - prefixes]] - File prefix definitions (includes `research`)
- [[meta - externalise]] - When and how to capture context
- [[meta - coding project structure]] - Sprint workflow integration
