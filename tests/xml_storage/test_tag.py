from kmy.xml_storage.kmy import Kmy


def test_read_tags_count(mm_simple: Kmy) -> None:
    assert 1 == len(mm_simple.tags)


def test_read_closed(mm_simple: Kmy) -> None:
    assert not mm_simple.tags[0].closed


def test_read_tagcolor(mm_simple: Kmy) -> None:
    assert "#000000" == mm_simple.tags[0].tag_color


def test_read_name(mm_simple: Kmy) -> None:
    assert "Bar Tag" == mm_simple.tags[0].name


def test_read_id(mm_simple: Kmy) -> None:
    assert "G000001" == mm_simple.tags[0].id
