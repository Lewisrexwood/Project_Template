# PROJECT_STATUS — {{PROJECT_NAME}}

> **The single most load-bearing handoff doc in the project.** A fresh
> agent reads this first, before `CLAUDE.md`. Keep it up to date at
> the end of every working session. If this file is stale, the next
> agent will start from the wrong place.

Last updated: {{YYYY-MM-DD}}

---

## Current state — one paragraph

{{Where is the project right now? One paragraph, plain English. "We
just finished phase 0. All pipeline tests pass. Distribution report is
written. About to start phase 1a." Aim for enough context that an
agent who has never seen this project can tell you what week it is
in.}}

---

## What is done

- [ ] {{Phase 0 — infrastructure — COMPLETE (YYYY-MM-DD)}}
- [ ] {{Verification scripts run, outputs in _verify_outputs/}}
- [ ] {{...}}

---

## What is in progress

- {{Phase 1a — {{short description}} — started YYYY-MM-DD}}
  - {{sub-item currently being worked on}}
  - {{next sub-item}}

---

## What is blocked

- {{Blocker 1 — what is blocked, what we are waiting on, who owns
  unblocking it. Link to the outstanding_issues.md entry.}}

If nothing is blocked, write "Nothing is blocked."

---

## Immediate next task

One or two sentences pointing to the concrete next action. Usually
this should point at `docs/plan/NEXT_TASK.md` for detail.

> **Next:** {{short imperative — e.g. "Run the distribution report on
> the full 10-catchment dataset and review outputs with user."}} See
> [`docs/plan/NEXT_TASK.md`](docs/plan/NEXT_TASK.md) for details.

---

## Recent decisions worth flagging

Decisions made in the last session or two that a new agent would not
pick up by reading the code alone. Move them into
`docs/plan/00_summary.md` once they are "locked".

- {{YYYY-MM-DD — Decision — Reason}}
