# .claude/agents/

Custom subagent definitions. Subagents run with isolated context
windows and their own system prompt — useful for parallelising
independent queries or for keeping the main context clean.

## When to add a subagent

- A task is well-defined enough to prompt once and reuse many times
  (e.g. "research agent for this codebase", "pytest failure
  triager")
- You want to run multiple independent queries in parallel without
  interleaving them in the main conversation
- A task produces a large volume of output that would otherwise fill
  the main context (e.g. exhaustive file searches)

## Format

Each subagent is a Markdown file with YAML frontmatter:

```markdown
---
name: researcher
description: Use this agent to do deep investigation across the codebase without filling the main context.
tools: [Glob, Grep, Read, WebFetch]
---

You are a research agent. When asked a question:
1. {{instructions}}
2. {{instructions}}
...
```

## Examples (add your own here)

- `phase-reviewer.md` — {{read a phase's spec + completion notes and
  critique whether acceptance criteria were actually met}}
