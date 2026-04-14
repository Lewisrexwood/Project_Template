# Plan Summary — {{PROJECT_NAME}}

> **Read this before doing any implementation work.** It is the entry
> point for the whole plan: locked decisions, open decisions, phase
> structure, and out-of-scope items.

---

## 1. Project goal

{{One paragraph. What is the successful end state? What does "done"
look like?}}

---

## 2. Architecture / approach

{{Two or three paragraphs describing how the project gets from inputs
to outputs. Diagrams in ASCII are welcome. Reference specific modules
in `src/` when their role is load-bearing.}}

---

## 3. Phase structure

The project is broken into phases. Each phase has its own spec
document in this folder and a corresponding notebook in
[`notebooks/`](../../notebooks/).

| # | Phase | Spec | Notebook | Status |
|---|---|---|---|---|
| 0 | {{Infrastructure}} | `01_phase0_infrastructure.md` | `01_phase0_infrastructure.ipynb` | {{planned / in progress / complete}} |
| 1 | {{...}} | `02_phase1_{{x}}.md` | `02_phase1_{{x}}.ipynb` | |
| 2 | {{...}} | `03_phase2_{{x}}.md` | `03_phase2_{{x}}.ipynb` | |

Each phase doc should include:
- Goal and success criteria
- Inputs (data, configs, prior-phase outputs)
- Outputs (artifacts, reports, notebook deliverables)
- Test specifications — what tests must pass to call the phase complete
- Dependencies on other phases

---

## 4. Locked decisions

Decisions that are fixed. Changing any of these requires explicit user
approval. Each entry should give the decision and a one-line reason.

1. {{Decision — reason}}
2. {{Decision — reason}}
3. {{...}}

---

## 5. Open decisions

Decisions that still need to be made. These are typically also tracked
in [`outstanding_issues.md`](../../outstanding_issues.md) — link them.

- {{Question — what is blocked by it — link to issue}}

---

## 6. Out of scope

Things that were considered and intentionally excluded. Listing them
here stops them drifting back in.

- {{Thing — why excluded}}
- {{Thing — why excluded}}

---

## 7. Data / inputs (if applicable)

{{Describe the project's inputs — what data, where it lives, in what
format, with what known caveats. Reference verification scripts if
any have been run.}}

---

## 8. Evaluation (if applicable)

{{How will we know if the system is working? Metrics, holdouts,
baselines, acceptance thresholds.}}
