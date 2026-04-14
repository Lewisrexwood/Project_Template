# config/

YAML configuration files. Everything that is a tunable parameter,
path, or run-specific setting belongs here rather than hardcoded in
`src/`.

## Conventions

- YAML only. Write with
  `yaml.safe_dump(..., sort_keys=False, default_flow_style=False)` so
  diffs stay readable.
- One file per concern. Prefer many small configs to one mega-config.
- Commit configs; do not commit secrets. Secrets belong in a gitignored
  `.env` or similar.

## Typical files

- `data_paths.yaml` — filesystem locations for source data
- `splits.yaml` — train / val / test date ranges (hashed if reproducibility matters)
- `training.yaml` — optimizer, learning rate, epochs
- `{{model}}_defaults.yaml` — per-model hyperparameters

Add an entry here every time you create a new config file.
