# Claude Project Instructions — {{PROJECT_NAME}}

This is a standalone project. Do not pull conventions from sibling
projects unless a document in this repo explicitly says so.

---

## Read this before anything else

If you are a fresh agent picking up this project, your reading order is:

1. **This file (`CLAUDE.md`)** — workflow rules, tech stack, things to do.
2. **The most recent unfinished plan in `docs/superpowers/plans/`** —
   that *is* the current state. If there is no plan yet, the first move
   is to invoke `brainstorming` on the next phase.

Do not start implementation until the current plan is confirmed.

---

## What this project is

{{ONE_PARAGRAPH_PROJECT_DESCRIPTION}}

{{EXPAND_ARCHITECTURE_OR_GOALS_HERE_IF_USEFUL}}

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python (3.11+) |
| Testing | pytest |
| Config | YAML via PyYAML |

Add packages to `requirements.txt` when introducing new dependencies.
Pin versions.

---

## Project-specific tripwires

Things NOT to do without explicit user approval. Fill in per project.

- {{e.g. "Never re-run the data ingest against production — costs $$ and
  rate-limits downstream"}}
- {{e.g. "Do not regenerate `models/` artefacts on `main`; that's a
  release-time action"}}
- {{add more as the project teaches you}}

---

## Workflow

Workflow is enforced by the `superpowers` skills. Invoke them per
their triggers — see `using-superpowers`. In particular:

- Before any creative work → `brainstorming`
- Before writing implementation → `writing-plans` then
  `test-driven-development`
- Before merging → `verification-before-completion` then
  `requesting-code-review` then `finishing-a-development-branch`

The active plan lives in `docs/superpowers/plans/`; the spec it came
from lives in `docs/superpowers/specs/`. Keep the repo minimal —
domain-specific folders are added when the first phase needs them.

---

## Project Structure

```
{{PROJECT_NAME}}/
├── CLAUDE.md
├── README.md
├── requirements.txt
├── .gitignore
├── .claude/
│   ├── settings.json
│   └── settings.local.json.example
├── docs/
│   └── superpowers/
│       ├── specs/      # design docs per phase
│       └── plans/      # active plan per phase
├── src/                # package code
│   └── __init__.py
├── tests/              # pytest suite
│   └── conftest.py
├── scripts/            # CLI entrypoints, one-off utilities
├── notebooks/          # exploratory analysis
├── config/             # experiment / runtime configs
├── data/
│   ├── raw/            # raw inputs (gitignored)
│   └── processed/      # derived data (gitignored)
├── models/             # trained artefacts (gitignored)
└── visuals/            # generated plots and figures
```

`data/` and `models/` have gitignored contents; everything else is
tracked by default. A pure-SE project will leave `notebooks/` and
`data/` empty; a pure-data project will leave `scripts/` empty.

---

## Code style

- Clear variable names over clever ones
- Short functions, one responsibility
- Comments only when the logic is non-obvious
- Avoid speculative abstractions
- Prefer `pathlib.Path` for filesystem paths
- Type hints where they help, not as decoration
