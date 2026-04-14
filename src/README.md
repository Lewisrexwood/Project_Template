# src/

All import-able project code. Organised by responsibility, **not** by
phase — a single module may be used in multiple phases.

## Adding a module

Create a subpackage with an `__init__.py` and a README. The README
lists every file in the subpackage with a one-line description of what
it does.

## Module boundaries

Defined in `CLAUDE.md` under "Module boundaries". Keep responsibilities
clean:

- `data_pipeline/` — ingestion only (read files, join datasets)
- `feature_engineering/` — anything that changes the shape or columns
  of data (cleaning, aggregation, derived features)
- `models/` — model definitions
- `training/` — training / calibration loops
- `evaluation/` — metrics, diagnostics, reports
- `utils/` — shared helpers (logging, config loading)

**Rule of thumb:** if it creates new columns or changes the
shape/granularity of the data it is feature engineering; if it reads
files or joins datasets it is pipeline.

## Running code

Code in `src/` should be importable from notebooks and tests. It
should **not** have a `if __name__ == "__main__":` entry point for the
main pipeline — that is the notebook's job. One-off verification
scripts are fine as top-level `_verify_*.py` files in the project
root.
