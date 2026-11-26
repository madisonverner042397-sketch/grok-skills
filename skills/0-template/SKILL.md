---
name: 0-template
description: Template for creating a new Agent Skill. Copy this folder, rename it to your skill's kebab-case name, and fill in every section. Use this as the starting point whenever you author a new skill for the AgentSkills library.
license: MIT
---

# Skill Template

> Copy this folder to `skills/<your-skill-name>/`, rename it, and replace this content. Delete this blockquote when done.

## Overview

One short paragraph: what this skill does and the situations it applies to.

**Keywords**: comma, separated, discovery, terms

## Inputs and Access

- What the user must provide (files, links, IDs, a goal).
- Which apps, logins, or permissions the agent needs, and what to do if one is missing.

## Workflow

1. First step — what to do.
2. Second step.
3. Third step.
4. Verify the result: what to check before returning it, and what counts as a failure.

## Output

What to return and in what format (a draft, a table, a file, a link).

## Approval Boundaries

- Actions that need the user's OK first, such as sending, purchasing, deleting, publishing, or changing production systems.
- What to do when a source is missing or stale: report it instead of guessing.

## Decision Framework

Use a table or bullet heuristics to help the agent choose between options.

| If… | Then… |
| --- | --- |
| condition A | action A |
| condition B | action B |

## Worked Example

Show a concrete input and the expected output. See `examples/sample.md` for a fuller example.

## Best Practices

- Do this.
- Prefer that.

## Common Pitfalls

- Avoid this.
- Watch out for that.

## Supporting Files

- `references/guide.md` — deep reference material (loaded only when needed).
- `scripts/run.py` — runnable helper.
- `examples/sample.md` — worked example.
