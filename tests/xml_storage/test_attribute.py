from datetime import date
from decimal import Decimal

import pytest

from kmy.xml_storage.common.attribute.amount_attribute import AmountAttribute
from kmy.xml_storage.common.attribute.attribute import Attribute
from kmy.xml_storage.common.attribute.bool_attribute import BoolAttribute
from kmy.xml_storage.common.attribute.date_attribute import DateAttribute


def test_abstract_attribute():
    with pytest.raises(TypeError):
        Attribute("foo")


def test_date_read():
    d = DateAttribute("date", value="2011-12-13")
    assert d.value == date(2011, 12, 13)


def test_date_write():
    d = DateAttribute("date", value="2011-12-13")
    d.value = date(2021, 1, 3)

    assert d.value == date(2021, 1, 3)
    assert d.raw_value == "2021-01-03"


def test_date_eq():
    assert DateAttribute("date", value="2011-12-13") == DateAttribute(
        "date", value="2011-12-13"
    )

    assert DateAttribute("date", value="2011-12-13") == "2011-12-13"
    assert DateAttribute("date", value="2011-12-13") == date(2011, 12, 13)


def test_date_unexpected_format():
    d = DateAttribute("date", value="2011/12/13")
    with pytest.raises(ValueError):
        d.value


def test_bool_read():
    d = BoolAttribute("date", value="1")
    assert d.value


def test_bool_write():
    d = BoolAttribute("date", value="1")
    d.value = False

    assert not d.value
    assert d.raw_value == "0"


def test_bool_unexpected_format():
    d = BoolAttribute("date", value="true")
    with pytest.raises(ValueError):
        assert d.value


def test_amount_read():
    d = AmountAttribute("date", value="3/25")
    assert d.value == Decimal("0.12")


def test_amount_write():
    d = AmountAttribute("date", value="3/25")
    d.value = Decimal("1.23")

    assert d.value == Decimal("1.23")
    assert d.raw_value == "123/100"


def test_amount_unexpected_format():
    d = AmountAttribute("date", value="12.23")
    with pytest.raises(ValueError):
        d.value
