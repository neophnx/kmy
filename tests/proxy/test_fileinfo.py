from datetime import date

from tests.conftest import SIMPLE
from kmy.kmy import Kmy
from kmy.proxy.common import DateProxy


def test_fileinfo_read_creation_date() -> None:
    proxy = Kmy(SIMPLE)

    assert proxy.file_info.creation_date.date == date(2020, 12, 13)


def test_fileinfo_write_creation_date() -> None:
    proxy = Kmy(SIMPLE)
    assert not proxy.file_info.creation_date.date._dirty
    assert (
        not proxy.file_info.creation_date._dirty
    ), proxy.file_info.creation_date._dirty

    proxy.file_info.creation_date.date = date(2020, 12, 14)

    assert isinstance(proxy.file_info.creation_date.date, DateProxy)
    assert proxy.file_info.creation_date.date == date(2020, 12, 14)

    assert proxy.file_info.creation_date.date._dirty
    assert proxy.file_info.creation_date._dirty
    assert proxy.file_info._dirty
    assert proxy._dirty
