# .claude/rules/

Topic-scoped instruction files that supplement `CLAUDE.md`. Use these
when a set of rules is large enough to deserve its own file, or when
the rules apply only to work on a specific part of the codebase.

## When to add a rules file

- A single topic (e.g. "testing conventions", "database migrations",
  "API design") has more than ~10 lines of guidance
- The guidance only applies when working on specific files (in which
  case rules files can be scoped)
- `CLAUDE.md` is getting long and topic-specific content wants to move
  out

## Naming

Use kebab-case, descriptive filenames: `testing.md`, `api-design.md`,
`database-migrations.md`. The filename becomes the rule's identity.

## Format

Each rules file is plain Markdown. Start with a one-line description
of when the rule applies, then the rules themselves.

## Examples (add your own here)

- `testing.md` — {{conventions for writing pytest tests in this project}}
- `data-handling.md` — {{rules for handling raw data, PII, etc.}}
