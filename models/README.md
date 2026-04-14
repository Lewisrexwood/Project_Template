# models/

Saved model artifacts. **Gitignored by default** — contents are
reproducible from code + data + config, so we do not commit binaries
here.

## Conventions

- One subdirectory per training run: `models/{{phase}}/{{run_id}}/`
- Each run directory should contain:
  - model weights (`.pt`, `.pkl`, etc.)
  - a copy of the config used for the run (`config.yaml`)
  - a hash or git commit of the code that produced it (`run_info.json`)
- Regenerating a model from scratch should require only the config
  and the raw data.

## Inspecting models

Loading and evaluating a model is done through the evaluation notebook
for the phase that produced it, or via helpers in `src/evaluation/`.
