---
description: Start a new phase by reading the plan, checking open issues, and proposing an implementation plan before writing any code.
---

You are starting a new phase of this project. Do **not** write any
code yet. Your job right now is to orient, then propose a plan.

Follow this procedure:

## 1. Identify the phase

Ask the user which phase they want to start, unless they have already
said. Confirm the phase doc filename (e.g.
`docs/plan/02_phase1a_something.md`) and the matching notebook name
(e.g. `notebooks/02_phase1a_something.ipynb`).

## 2. Read the inputs, in this order

1. `PROJECT_STATUS.md` — current state, what is done, what is blocked
2. `docs/plan/00_summary.md` — locked decisions, out-of-scope,
   and how this phase fits into the whole
3. `docs/plan/<phase_doc>.md` — the spec for the phase being started
4. `outstanding_issues.md` — filter to issues that touch this phase;
   flag any that are OPEN and block this phase
5. `docs/plan/completion_notes/` — notes from prior completed phases;
   look for "For the next phase" gotchas

## 3. Propose an implementation plan

Summarize back to the user:

- **Goal of this phase** (one sentence, from the phase doc)
- **Inputs it depends on** (prior-phase outputs, data, configs)
- **Deliverables** (files to create, reports to generate, tests to pass)
- **Blocking open issues** (if any — list them; ask how to proceed)
- **Proposed task breakdown** (3–7 bullets, the order you will tackle
  them)
- **Tests you will write** (brief — what behaviour each test covers)
- **Open questions** (things the spec does not pin down that you need
  a decision on before writing code)

## 4. Wait for approval

Do not edit any file until the user says "go ahead", "approved", "yes",
or equivalent. If the user pushes back on the plan, revise and
re-summarize.

## 5. Once approved

- Create the phase notebook in `notebooks/` if it does not exist yet
  (empty stub is fine — the notebook is the operational entry point,
  you will fill it in as you implement)
- Use `TodoWrite` to track the task breakdown
- Start work on the first task
