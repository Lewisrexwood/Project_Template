# .claude/skills/

Reusable slash-command prompts. A file here called `foo.md` becomes
`/foo` inside Claude Code and can be invoked by the user to expand
into a full prompt.

## When to add a skill

- You find yourself typing the same instruction to Claude repeatedly
- A task has a standard procedure you want one-command access to
  (e.g. `/commit`, `/review-pr`, `/run-tests-and-report`)

## Format

Each skill is a Markdown file. The file contents are the prompt that
gets expanded when the user types `/skill-name`. It can reference
files, shell commands, and project conventions.

## Built-in user-invocable skills (for reference)

The Claude Code harness ships with skills like `/commit`, `/review-pr`,
`/loop`, `/schedule`. You do not need to redefine these — just add
your own project-specific ones here.

## Examples (add your own here)

- `run-full-test-suite.md` — {{run tests, summarize failures, suggest fixes}}
- `phase-kickoff.md` — {{read phase spec, propose implementation plan,
  wait for approval}}
