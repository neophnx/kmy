from pathlib import Path
from typing import Iterator  # pylint: disable=unused-import

import pytest

from kmy import Kmy

TEST_DIR = Path(__file__).parent


SIMPLE: Path = TEST_DIR / "files" / "Test.kmy"
FULL: Path = TEST_DIR / "files" / "Test-full.kmy"

TEST_CASES = [SIMPLE, FULL]


@pytest.fixture()
def mm_simple() -> "Iterator[Kmy]":
    yield Kmy.from_kmy_file(SIMPLE)


@pytest.fixture()
def mm_full() -> "Iterator[Kmy]":
    yield Kmy.from_kmy_file(FULL)
