# data/

All project data, organised by processing stage.

## Subdirectories

- `raw/` — source data as received. **Never modified in place.** If
  you need to fix something, write a cleaning step in
  `src/feature_engineering/` that produces a file in `processed/`.
  The raw directory is append-only.
- `processed/` — cleaned, derived, or aggregated data ready for the
  modelling pipeline.

## Conventions

- Large binary files (anything > ~5 MB, and anything in `processed/`
  that can be regenerated) are gitignored by default. See the root
  `.gitignore`.
- If a dataset is reproducible from `raw/` + code, document the
  regeneration command in the relevant notebook — do not rely on
  `processed/` being present.
