# {{PROJECT_NAME}}

{{One-sentence tagline describing what this project is.}}

## What it does

{{Two or three sentences describing the project's purpose at a high
level. Link to the plan for depth.}}

## Status

See [`PROJECT_STATUS.md`](PROJECT_STATUS.md) for the current state
and immediate next task.

## For Claude agents picking up this project

Start with [`CLAUDE.md`](CLAUDE.md). It defines the reading order and
the workflow rules.

## Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Running the pipeline

Every phase has a corresponding notebook in [`notebooks/`](notebooks/)
that serves as the operational entry point. Open the notebook for the
phase you want to run; the notebook imports from `src/` and presents
its results inline.

## Tests

```bash
pytest tests/ -v
```

## Layout

See the "Project Structure" section of [`CLAUDE.md`](CLAUDE.md) for the
full folder tree and module boundaries.
