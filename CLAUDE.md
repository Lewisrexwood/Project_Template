# Claude Project Instructions — {{PROJECT_NAME}}

This is a standalone project. Do not pull conventions from sibling
projects unless a document in this repo explicitly says so.

> **Template note:** Replace `{{PROJECT_NAME}}` and any other
> `{{PLACEHOLDER}}` markers throughout this file. Delete this blockquote
> when you are done. Delete any sections that do not apply to your
> project (e.g. "Data Decisions" if this is not a data project).

---

## Read this before anything else

If you are a fresh agent picking up this project, your reading order is:

1. **[`PROJECT_STATUS.md`](PROJECT_STATUS.md)** in the project root —
   tells you where the project is right now, what is done, what is
   blocked, and what the immediate next task is. This is the single
   most load-bearing handoff doc in the project.
2. **This file (`CLAUDE.md`)** — workflow rules, tech stack, things
   not to do. Binding.
3. **[`outstanding_issues.md`](outstanding_issues.md)** — open
   decisions and deferred items, tracked per-issue.
4. **[`docs/plan/00_summary.md`](docs/plan/00_summary.md)** — the full
   plan. Architecture, locked decisions, phase structure,
   out-of-scope list.
5. **[`docs/plan/NEXT_TASK.md`](docs/plan/NEXT_TASK.md)** — concrete
   instructions for the immediate next task the user will want you to
   execute.

**Do not start writing any code** until you have read these files and
the current task has been confirmed with the user.

---

## Workflow: Clarification First, Always

Before writing any code or making changes, Claude must:

1. **Ask clarifying questions** to understand the full requirement
2. **Summarise the plan** — what will be built, how, and why
3. **Wait for explicit approval** before proceeding ("yes", "go ahead",
   "looks good", etc.)

If a request is clear and small (e.g., "fix this typo"), a
single-sentence plan summary is enough — but approval is still
required.

**No exceptions** — even when the user reports an error or warning,
Claude must explain the issue and proposed fix, then wait for
approval before editing any code. Do not jump straight to fixing.

---

## What this project is

{{ONE_PARAGRAPH_PROJECT_DESCRIPTION}}

{{EXPAND_ARCHITECTURE_OR_GOALS_HERE_IF_USEFUL}}

**Read `docs/plan/00_summary.md` before doing ANY implementation
work.** That document is the entry point into the full plan. It lists
decisions that are locked, decisions that are open, and the phase
structure. Do not skip it.

**Also read `outstanding_issues.md`** before starting work. It tracks
deferred decisions and open questions that the plan does not repeat.

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python (3.11+) |
| Core libraries | {{numpy, pandas, ...}} |
| Testing | pytest |
| Config | YAML via PyYAML |
| Visualisation | matplotlib / seaborn / plotly as appropriate |
| {{domain layer, e.g. Deep learning}} | {{e.g. PyTorch}} |

Add packages to `requirements.txt` when introducing new dependencies.
Pin versions.

---

## Project Structure

```
{{PROJECT_NAME}}/
├── CLAUDE.md                       # this file
├── README.md                       # top-level project readme
├── PROJECT_STATUS.md               # current state + next task (handoff doc)
├── outstanding_issues.md           # open issues and decisions, do not delete
├── requirements.txt                # pinned dependencies
├── .gitignore
│
├── .claude/                        # Claude Code project settings
│   ├── settings.json               # team-shared (committed)
│   ├── settings.local.json         # personal overrides (gitignored)
│   ├── rules/                      # topic-scoped instruction files
│   ├── skills/                     # reusable slash-command prompts
│   └── agents/                     # subagent definitions
│
├── config/                         # YAML configs (paths, hyperparameters, splits)
│
├── data/
│   ├── raw/                        # source data, never modified in place
│   └── processed/                  # cleaned / derived data
│
├── src/                            # all import-able code lives here
│   └── __init__.py
│
├── tests/                          # pytest, unit + validation
│   └── conftest.py
│
├── notebooks/                      # phase entry-point notebooks (one per phase)
│
├── models/                         # saved model artifacts (gitignored)
│
└── docs/
    ├── plan/                       # the plan (read this first)
    │   ├── 00_summary.md
    │   ├── NEXT_TASK.md
    │   └── completion_notes/       # per-phase retros, written on phase close
    ├── source_data/                # verbatim provider docs (do not modify)
    └── reports/                    # phase output reports and diagnostic plots
```

### Module boundaries

Give every top-level module in `src/` a single responsibility and
document it here. A rule-of-thumb sentence per module is enough — if
you cannot summarise the module in one sentence, the module is doing
too much.

- `{{src/data_pipeline/}}` — {{ingestion only: read files, join datasets, no transforms}}
- `{{src/feature_engineering/}}` — {{cleaning, aggregation, derived features — anything that changes the shape or columns of the data}}
- `{{src/models/}}` — {{model definitions}}
- `{{src/training/}}` — {{training / calibration loops}}
- `{{src/evaluation/}}` — {{metrics, diagnostics, reports}}
- `{{src/utils/}}` — {{logging, config loading, shared helpers}}

**Rule of thumb:** if it creates new columns or changes the
shape/granularity of the data it is feature engineering; if it reads
files or joins datasets it is pipeline.

---

## Testing Guidelines

Use **pytest** for all tests. Keep tests minimal unless complexity
warrants more.

### Two categories of tests

**1. Unit / functional tests** — test individual functions and pipelines

- Does the function return the right shape/type?
- Does it handle edge cases (empty input, nulls, wrong dtype)?
- Do data loaders return exactly the expected columns?

**2. Validation tests** — test dataset and system behaviour

- Does the dataset meet expected schema and value ranges?
- Does the pipeline produce deterministic outputs given a fixed seed?
- Does the trained model meet a minimum performance threshold?

### Before writing tests, Claude will

- Briefly explain what each test covers and why
- Ask if you want additional coverage or a different approach
- Default to the smallest set of tests that gives meaningful confidence

Run tests with:

```bash
pytest tests/ -v
```

### Phase acceptance criteria include tests

Every phase document in `docs/plan/` should include a "Test
specifications" section. A phase is **not** complete until all listed
tests exist and pass. Do not mark a phase complete in
`completion_notes/` if any test is failing or missing.

---

## Data / Domain Decisions (locked)

List decisions that are fixed for this project and must not be changed
without explicit user approval. Cross-reference `docs/plan/00_summary.md`
where the decision is explained in full.

- {{Decision 1 — one sentence. See 00_summary.md Section X.}}
- {{Decision 2 — one sentence.}}
- {{...}}

---

## Documentation

Each folder in the project must contain a `README.md` that documents
every file within that folder. These READMEs describe **what** each
file does, and a high-level summary of **how** it works (enough context
for a new agent to orient without reading every line of code). Keep
them updated as files are added, renamed, or removed.

Source data documents (verbatim from external providers) live in
`docs/source_data/`. Reference them from the plan when physical
definitions are load-bearing. Never modify them.

### Notebook entry points

Every phase must produce a **Jupyter notebook** in `notebooks/` that
serves as the single operational entry point for running that phase's
pipelines. The notebook imports and calls `src/` modules — **no
processing logic lives in the notebook itself**. The notebook should
present results inline for user review. This makes the phase's outputs
reproducible and inspectable in one place.

**Naming convention:** notebooks mirror the phase doc filenames with
the same number prefix:

| Phase doc (`docs/plan/`) | Notebook (`notebooks/`) |
|---|---|
| `01_phaseN_description.md` | `01_phaseN_description.ipynb` |

---

## Code Style

- Clear variable names over clever ones
- Short functions — one responsibility each
- Comments only where logic is non-obvious
- No speculative abstractions — build for the task at hand
- Fix security issues immediately if spotted
- Avoid wildcard imports; use explicit `from x import y` or `import x`
- Use type hints for function signatures where it helps clarity, but
  do not retrofit hints into code that is about to be rewritten
- Use `pathlib.Path`, not string concatenation, for filesystem paths
- Use `PyYAML` with `sort_keys=False, default_flow_style=False` for
  human-readable config files

---

## Explanations

The user is comfortable reviewing code but may need step-by-step
explanations for unfamiliar packages or setup. When introducing a new
library or pattern, briefly explain what it does and why it is being
used.

When the user asks clarifying questions about the plan, answer them
grounded in the project's own verification data and source-data docs.
Do not invent explanations that are not backed by the documents or
the data.

---

## Things NOT to do without explicit user approval

> **Template note:** populate this list with project-specific
> guardrails as decisions get locked. Every entry should be a decision
> the user has already made — this is not a general list of bad
> practices, it is a list of *this project's* tripwires.

- {{Change any locked decision listed in docs/plan/00_summary.md}}
- {{Swap the tech stack / model family / data source without approval}}
- {{Add "just one more" feature or architecture "for comparison"}}
- Delete issues from `outstanding_issues.md` — mark RESOLVED with a
  short note instead
- Modify files in `docs/source_data/` — those are verbatim from the
  source provider

---

## Things to do proactively

- Use `TodoWrite` to track multi-step work when a task has 3+ sequential
  steps
- When completing a phase, write a `docs/plan/completion_notes/phaseN_notes.md`
  covering what was built, deviations from the plan and why,
  outstanding issues touched, and what the next phase should know
- When encountering a blocker, raise it explicitly and update
  `outstanding_issues.md` rather than silently working around it
- When a verification script output contradicts a planning assumption,
  stop and surface the contradiction before continuing
