# docs/reports/

Generated reports and diagnostic plots from phase notebooks. Unlike
`docs/plan/`, content here is **output**, not input.

## Conventions

- One subdirectory per report type:
  `docs/reports/{{report_name}}/`
- Each report subdirectory should have a `README.md` summarising what
  is in it and which phase / notebook produced it.
- Plots are committed if they are small (< ~200 KB each) and
  load-bearing for a decision. Large plot dumps should live outside
  the repo.

## Examples

- `distribution_report/` — {{per-catchment distribution diagnostics from phase 0}}
- `evaluation/phase1a/` — {{model performance plots from phase 1a}}
