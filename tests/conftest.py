from pathlib import Path
from typing import Iterator  # pylint: disable=unused-import

import pytest

from kmy.kmy import Kmy

TEST_FILE_DIR = Path(__file__).parent / "files"


SIMPLE: Path = TEST_FILE_DIR / "Test.kmy"
FULL: Path = TEST_FILE_DIR / "Test-full.kmy"

TEST_CASES = [SIMPLE, FULL]


@pytest.fixture()
def mm_simple() -> "Iterator[Kmy]":
    yield Kmy.from_kmy_file(SIMPLE)


@pytest.fixture()
def mm_full() -> "Iterator[Kmy]":
    yield Kmy.from_kmy_file(FULL)
