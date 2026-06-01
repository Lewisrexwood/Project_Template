# Superpowers Minimalist Refactor — Design

**Date:** 2026-04-27 (revised 2026-06-01 to broaden scope)
**Owner:** Lewis Rexwood
**Status:** Draft, awaiting user approval

## Goal

Refactor `Project_Template` so that it ships **what every project Lewis runs needs** — both data-heavy and software-engineering projects — with the workflow delegated entirely to the `superpowers` skills. Optimise for: minimum surface area, zero duplication with what the skills already enforce, and a fresh agent being productive in one read.

## Scope (2026-06-01 revision)

The original draft punted data/ML scaffolding to per-project setup. That was too aggressive: Lewis's projects split roughly evenly between data work and software engineering, and the cost of an unused empty directory is one `.gitkeep` while the cost of a missing convention is friction at phase 1. Revised scope: ship the union of universal needs for both project types.

## Non-goals

- Preserving custom skills (`phase-kickoff`, `status-update`) that duplicate `brainstorming`, `writing-plans`, or built-in handoff patterns.
- Backwards compatibility with the previous template's file paths.
- Domain-specific subdirectories beyond the universal set (e.g. `docs/source_data/`, `docs/reports/`, project-specific config schemas). Those remain a first-phase job.

## Principle

Ship what every project needs and nothing else. "Every project" here means *every project Lewis runs*, which spans data and SE work. Domain-specific scaffolding (analysis taxonomies, report templates, ETL stages) is still created by the brainstorm of the first phase.

## Final layout

```
project_template/
├── CLAUDE.md                        # ~50 lines, mostly placeholders
├── README.md                        # ~15 lines: setup, run, where docs live
├── .gitignore
├── requirements.txt                 # commented-out hints only
├── .claude/
│   ├── settings.json                # permissions only
│   └── settings.local.json.example
├── docs/
│   └── superpowers/
│       ├── specs/.gitkeep
│       └── plans/.gitkeep
├── src/
│   └── __init__.py
├── tests/
│   └── conftest.py
├── scripts/.gitkeep                 # CLI entrypoints, one-off utilities (SE projects)
├── notebooks/.gitkeep               # exploratory analysis (data projects)
├── config/.gitkeep                  # experiment/runtime configs (both)
├── data/
│   ├── raw/.gitkeep                 # raw inputs, not committed (gitignored)
│   └── processed/.gitkeep           # derived data, not committed (gitignored)
├── models/.gitkeep                  # trained artefacts, not committed (gitignored)
└── visuals/.gitkeep                 # generated plots and figures
```

17 files, 15 directories. Universal needs across Lewis's projects:
- `data/`, `models/` — contents gitignored, `.gitkeep` tracked
- `visuals/`, `notebooks/`, `config/`, `scripts/` — contents tracked by default

A pure-SE project will leave `notebooks/` and `data/` empty; a pure-data project will leave `scripts/` empty. Cost of one unused dir < cost of inventing the convention mid-phase.

## What gets removed

| Path | Reason |
|---|---|
| `PROJECT_STATUS.md` | The most recent unfinished plan in `docs/superpowers/plans/` *is* the current state. A separate handoff doc duplicates it and goes stale faster. |
| `outstanding_issues.md` | GitHub issues do this better. Design-relevant questions belong in the spec's "Open Questions" section. |
| `docs/plan/00_summary.md`, `NEXT_TASK.md`, `completion_notes/` | Superseded by `docs/superpowers/specs/` and `plans/`. The most recent unfinished plan is `NEXT_TASK`. Phase outcomes go in a `## Outcome` appendix on the plan or in the PR body. |
| `.claude/skills/phase-kickoff.md` | Duplicates `brainstorming` + `writing-plans`. |
| `.claude/skills/status-update.md` | Once `PROJECT_STATUS.md` is gone, this skill has no target. The plan's `## Status` line covers the same ground. |
| `.claude/skills/README.md` | Empty placeholder for empty directory. |
| `.claude/rules/README.md`, `.claude/agents/README.md` (and their dirs) | Empty placeholders. The convention can be re-introduced via a one-line note in `CLAUDE.md` if/when needed. |
| `docs/source_data/`, `docs/reports/` and their READMEs | Domain scaffolding. Per-project structure for source data documentation and analysis reports is too varied to pre-decide. Recreated by phase 1 when the domain is known. |

## What stays

| Path | Why |
|---|---|
| `CLAUDE.md` | Slimmed to project-specific facts only (name, tech stack, tripwires, code style). Workflow is delegated to skills via a one-liner. |
| `README.md` | Slimmed to setup + where docs live. |
| `.gitignore` | Keep most current contents; small edits — see ".gitignore trimming" section. |
| `requirements.txt` | Keep as-is. The current file is already commented-out hints only (no actual pins) — exactly what a minimalist template should have. New projects un-comment and pin what they use. |
| `.claude/settings.json` | Keep current permissions; add `gh pr create:*` and `git push origin:*` because `finishing-a-development-branch` calls them. |
| `.claude/settings.local.json.example` | Keep — useful onboarding artefact. |
| `src/__init__.py` | Empty marker. |
| `tests/conftest.py` | Empty pytest hook file. |
| `data/raw/`, `data/processed/` | Universal need across Lewis's projects. Contents gitignored; `.gitkeep` files only. |
| `models/` | Universal need. Contents gitignored. |
| `visuals/` | Universal need (replaces the old `docs/reports/`). Contents tracked by default — users gitignore selectively if outputs get heavy. |
| `notebooks/` | Restored 2026-06-01. Universal for data work, ignorable for pure SE. Contents tracked; checkpoints gitignored. |
| `config/` | Restored 2026-06-01. Universal — both data projects (experiment configs, hyperparameters) and SE projects (runtime config, feature flags) use it. Contents tracked. |
| `scripts/` | Added 2026-06-01. Universal for SE work (CLI entrypoints, one-off utilities), useful for data work too (data-loading or migration scripts). Contents tracked. |

## CLAUDE.md, slimmed

Sections:

1. **Project name + one-paragraph description** (placeholders)
2. **Tech stack** (table, placeholders)
3. **Project-specific tripwires** ("Things NOT to do without explicit user approval" — short list, placeholder)
4. **Code style** (short bullet list — clear names, short functions, comments only where logic is non-obvious, no speculative abstractions, type hints where they help)
5. **Workflow** — single line: "Workflow is enforced by the `superpowers` skills. Invoke them per their triggers (see `using-superpowers`)."
6. **Reading order for a fresh agent** — single line: "This file, then the most recent file in `docs/superpowers/plans/`."

Target length: ~40 lines including blank lines and headings.

## README.md, slimmed

Sections:

1. **Project name + tagline** (placeholders)
2. **What it does** (one paragraph, placeholder)
3. **Setup** (venv + pip install -r requirements.txt)
4. **Tests** (`pytest tests/ -v`)
5. **For Claude agents** — one line: "Start with `CLAUDE.md`."

Target length: ~15 lines.

## .claude/settings.json additions

Add to `permissions.allow`:

```
"Bash(gh pr create:*)",
"Bash(gh pr view:*)",
"Bash(gh pr status:*)",
"Bash(git push origin:*)",
"Bash(git branch:*)",
"Bash(git checkout -b *)"
```

Rationale: `finishing-a-development-branch` and `requesting-code-review` use these. Pre-allowing avoids a permission prompt mid-workflow.

## .gitignore trimming

Keep:
- Generic Python ignores (`__pycache__`, `.venv`, `*.pyc`, `.pytest_cache`, etc.)
- `.claude/settings.local.json`
- `data/raw/*` + `!data/raw/.gitkeep` and `data/processed/*` + `!data/processed/.gitkeep`
- `models/*` + `!models/.gitkeep` (replaces the existing `!models/README.md` which is being removed)
- `.ipynb_checkpoints/` — kept now that `notebooks/` is restored.

Add nothing for `visuals/`, `notebooks/`, `config/`, or `scripts/` — those are tracked by default. Users can add a project-specific gitignore if outputs get heavy.

## Lifecycle of a phase, post-refactor

1. New phase → invoke `brainstorming` → spec saved to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`.
2. Spec approved → invoke `writing-plans` → plan saved to `docs/superpowers/plans/YYYY-MM-DD-<topic>-plan.md`.
3. Build → `executing-plans` (or `subagent-driven-development`) + `test-driven-development`; `systematic-debugging` for failures.
4. Pre-merge → `verification-before-completion` then `requesting-code-review`.
5. Phase closes → `## Outcome` appendix on the plan, then `finishing-a-development-branch`.

No project-level handoff doc. The active plan is the handoff.

## Acceptance criteria

The PR is acceptable if a fresh agent can clone the template, read `CLAUDE.md`, and start phase 1 by invoking `brainstorming` without needing any other context. We will *not* execute that walk-through inside this PR; it is the reviewer's manual check before merge.

## Risks

1. **Loss of the cross-session "where am I" doc.** Mitigation: the convention "the most recent unfinished plan is the current state" is documented in `CLAUDE.md` and reinforced by `writing-plans`' status field.
2. **Some users may want the deeper data/ML scaffolding back** (`notebooks/`, `config/`, `docs/source_data/`). Mitigation: the universal three (`data/`, `models/`, `visuals/`) are kept; the rest can be added per-project, or a separate `data-project-template` repo can be created later. Not in scope for this PR.
3. **Custom skills being deleted may have nuance worth keeping.** Mitigation: read `phase-kickoff.md` and `status-update.md` end-to-end during plan execution and surface anything not covered by superpowers before deleting.

## Out of scope

- Adding new superpowers-aware skills.
- Changing `superpowers` itself.
- Producing the data-project variant template.
- Setting up CI on the repo.
