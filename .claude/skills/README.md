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

## Included with this template

- `phase-kickoff.md` → `/phase-kickoff` — read the plan, check open
  issues, propose an implementation plan for a new phase, and wait
  for approval before writing any code. Use at the start of each
  phase.
- `status-update.md` → `/status-update` — refresh `PROJECT_STATUS.md`
  at the end of a working session. Summarises activity from git +
  current state, shows a diff for approval, then writes. Use before
  closing out a session so the next agent picks up cleanly.

## Adding your own

Drop a new `.md` file in this folder. Optional YAML frontmatter can
define `description`, allowed `tools`, and more — see the Claude Code
docs linked in `.claude/README.md`.
