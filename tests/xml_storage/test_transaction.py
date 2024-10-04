from kmy.xml_storage.kmy import Kmy


def test_read_accounts_count(mm_simple: Kmy) -> None:
    assert 5 == len(mm_simple.transactions)


def test_read_postdate(mm_simple: Kmy) -> None:
    assert "2020-01-01" == mm_simple.transactions[0].post_date


def test_read_memo(mm_simple: Kmy) -> None:
    assert "" == mm_simple.transactions[0].memo


def test_read_commodity(mm_simple: Kmy) -> None:
    assert "USD" == mm_simple.transactions[0].commodity


def test_read_entrydate(mm_simple: Kmy) -> None:
    assert "2020-12-13" == mm_simple.transactions[0].entry_date


def test_read_id(mm_simple: Kmy) -> None:
    assert "T000000000000000001" == mm_simple.transactions[0].id


def test_read_splits(mm_simple: Kmy) -> None:
    assert 2 == len(mm_simple.transactions[0].splits)
