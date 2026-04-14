"""Shared pytest fixtures.

Keep fixtures minimal. Project-wide fixtures (e.g. `project_root`,
`sample_config`) live here; module-specific fixtures live next to the
tests that use them.
"""

from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Absolute path to the repo root."""
    return Path(__file__).resolve().parent.parent
