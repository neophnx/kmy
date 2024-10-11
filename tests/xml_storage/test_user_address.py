from typing import Iterator  # pylint: disable=unused-import

import pytest

from kmy.kmy import Kmy
from kmy.xml_storage.user.useraddress import UserAddress


@pytest.fixture(name="useraddress")
def fixture_useraddress(mm_simple: Kmy) -> "Iterator[UserAddress]":
    yield mm_simple.user.address


def test_read_telephone(useraddress: UserAddress) -> None:
    assert "Telephone" == useraddress.telephone


def test_read_county(useraddress: UserAddress) -> None:
    assert "CountyState" == useraddress.county


def test_read_city(useraddress: UserAddress) -> None:
    assert "Town" == useraddress.city


def test_read_zipcode(useraddress: UserAddress) -> None:
    assert "PostalCode" == useraddress.zip_code


def test_read_street(useraddress: UserAddress) -> None:
    assert "Street" == useraddress.street
