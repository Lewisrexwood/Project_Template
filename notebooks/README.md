# notebooks/

**Phase entry points.** One notebook per phase, matching the phase's
spec document in `docs/plan/` by number prefix.

## Rules (from CLAUDE.md)

- The notebook is the single operational entry point for running its
  phase.
- The notebook imports from `src/` and calls into it. **No processing
  logic lives in the notebook itself** — if you find yourself writing
  a function in a notebook, move it to `src/`.
- Results are presented inline for user review. Plots, tables,
  summary statistics — everything the user needs to decide whether
  the phase's output is acceptable.

## Naming

Match the phase doc in `docs/plan/`:

| Phase doc | Notebook |
|---|---|
| `01_phase0_infrastructure.md` | `01_phase0_infrastructure.ipynb` |
| `02_phase1_{{x}}.md` | `02_phase1_{{x}}.ipynb` |

## Committing notebooks

- Clear cell outputs before committing large notebooks, **unless** the
  inline results are the deliverable (in which case commit the
  outputs so reviewers can see them without executing).
- Large plot outputs → consider saving to `docs/reports/` and linking
  from the notebook instead of embedding.
