from typing import Iterator  # pylint: disable=unused-import

import pytest

from kmy.xml_storage.institution.institution_address import InstitutionAddress
from kmy.kmy import Kmy


@pytest.fixture(name="address")
def fixture_address(mm_simple: Kmy) -> "Iterator[InstitutionAddress]":
    yield mm_simple.institutions[0].address


def test_read_telephone(address: InstitutionAddress) -> None:
    assert "" == address.telephone


def test_read_city(address: InstitutionAddress) -> None:
    assert "" == address.city


def test_read_zip(address: InstitutionAddress) -> None:
    assert "" == address.zip


def test_read_street(address: InstitutionAddress) -> None:
    assert "" == address.street
