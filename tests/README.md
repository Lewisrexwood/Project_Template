# tests/

pytest suite. See `CLAUDE.md` → "Testing Guidelines" for the two
categories of tests (unit/functional and validation) and the default
philosophy (smallest set of tests that gives meaningful confidence).

## Running tests

```bash
pytest tests/ -v
```

Run a single file:

```bash
pytest tests/test_config_loader.py -v
```

Run with a marker (e.g. to skip slow/full-data tests):

```bash
pytest tests/ -v -m "not full_data"
```

## Conventions

- File naming: `test_<module_under_test>.py`
- One test class per function / behaviour under test, if grouping helps
- Use markers (`@pytest.mark.full_data`, `@pytest.mark.slow`) to gate
  tests that are expensive; register the markers in `pytest.ini` or
  `pyproject.toml`
- Fixtures shared across the suite go in `conftest.py`
