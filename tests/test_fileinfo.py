from kmy import Kmy


def test_read_creation_date(mm_simple: Kmy) -> None:
    assert "2020-12-13" == mm_simple.file_info.creation_date.date


def test_read_last_modified_date(mm_simple: Kmy) -> None:
    assert "2020-12-13" == mm_simple.file_info.last_modified_date.date


def test_read_version(mm_simple: Kmy) -> None:
    assert "1" == mm_simple.file_info.version.id


def test_read_fix_version(mm_simple: Kmy) -> None:
    assert "5" == mm_simple.file_info.fix_version.id
