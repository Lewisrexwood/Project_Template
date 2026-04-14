---
description: Refresh PROJECT_STATUS.md at the end of a working session by summarising what changed, then wait for approval before writing.
---

You are closing out a working session. Your job is to update
`PROJECT_STATUS.md` so that the next agent (or future-you) can pick
up cleanly.

Do **not** overwrite `PROJECT_STATUS.md` until the user approves the
proposed update.

## 1. Gather session activity

Run in parallel:

- `git log --oneline -20` — recent commits
- `git diff HEAD~N` where N = commits-since-last-PROJECT_STATUS-update
  (usually safe to look at the last 5–10 commits; ask if unclear)
- `git status` — uncommitted work in progress
- Read the current `PROJECT_STATUS.md`
- Read `outstanding_issues.md` for anything that changed state

If you cannot reliably determine N, ask the user: "When was the last
status update you are happy with?"

## 2. Propose the update

Summarize back to the user (in chat, before writing):

- **Current state** — a one-paragraph rewrite of the top section,
  reflecting what is actually true right now
- **What is done** — items to tick off / add since the last update
- **What is in progress** — current work, with the sub-item actually
  being worked on
- **What is blocked** — changes vs. the previous update; if nothing
  is blocked, say so explicitly
- **Immediate next task** — one or two sentences pointing to the
  concrete next action (usually pointing into
  `docs/plan/NEXT_TASK.md`)
- **Recent decisions worth flagging** — anything decided this session
  that a new agent would not pick up from the code alone

Show a **diff-style summary** so the user can see what lines will
change — not the full file, just the deltas.

## 3. Check for drift

Flag anything that smells stale:

- Items listed as "in progress" in `PROJECT_STATUS.md` that have been
  there for more than one session
- `outstanding_issues.md` entries marked OPEN that were actually
  resolved in a recent commit
- A `docs/plan/NEXT_TASK.md` that no longer matches reality

Raise these to the user as part of your proposal — do not silently
"fix" them.

## 4. Wait for approval

Only after the user says "go ahead" (or equivalent) do you:

- Edit `PROJECT_STATUS.md`
- Update the `Last updated: YYYY-MM-DD` line to today's date
- Update `outstanding_issues.md` if any status transitions were
  approved
- Update `docs/plan/NEXT_TASK.md` if the next task changed
