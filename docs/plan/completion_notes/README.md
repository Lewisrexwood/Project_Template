# completion_notes/

One file per completed phase. File naming: `phaseN_notes.md` (e.g.
`phase0_notes.md`, `phase1a_notes.md`), matching the phase's spec
document in `docs/plan/`.

## Why these exist

Completion notes are the retrospective for a phase. They are written
**when the phase closes** and are aimed at the next agent picking up
the project. A good completion note answers:

1. **What was built** — a short list of the artifacts that now exist,
   with paths.
2. **Deviations from the plan** — anything in the phase spec that was
   not followed, and why.
3. **Outstanding issues touched** — which entries in
   `outstanding_issues.md` were resolved, updated, or newly raised.
4. **Gotchas for the next phase** — things that were learned during
   implementation that the next phase's agent needs to know but that
   are not otherwise documented in the code.

## Template

```markdown
# Phase {{N}} — Completion Notes

Completed: {{YYYY-MM-DD}}

## What was built
- `path/to/file.py` — {{one-liner}}
- `docs/reports/{{report_name}}.md` — {{one-liner}}

## Deviations from the plan
- {{Deviation — why}}

## Outstanding issues touched
- Issue {{N}}: {{RESOLVED / updated / newly raised}} — {{note}}

## For the next phase
- {{Gotcha or piece of knowledge the next agent needs}}
```
