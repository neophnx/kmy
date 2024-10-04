from typing import Iterator  # pylint: disable unused-import

import pytest

from kmy.xml_storage.kmy import Kmy
from kmy.xml_storage.payee.payee_address import PayeeAddress


@pytest.fixture(name="address")
def fixture_address(mm_simple: Kmy) -> "Iterator[PayeeAddress]":
    yield mm_simple.payees[0].address


def test_read_telephone(address: PayeeAddress) -> None:
    assert "+1 312 123 4567" == address.telephone


def test_read_state(address: PayeeAddress) -> None:
    assert "WH" == address.state


def test_read_city(address: PayeeAddress) -> None:
    assert "Whoville" == address.city


def test_read_street(address: PayeeAddress) -> None:
    assert "123 Street\n42 Something" == address.street


def test_read_postcode(address: PayeeAddress) -> None:
    assert "WHO 123" == address.post_code
