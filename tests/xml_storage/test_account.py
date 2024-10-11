from kmy.kmy import Kmy


def test_read_accounts_count(mm_simple: Kmy) -> None:
    assert 11 == len(mm_simple.accounts)


def test_read_number(mm_simple) -> None:
    assert "" == mm_simple.accounts[0].number


def test_read_last_modified(mm_simple) -> None:
    assert "" == mm_simple.accounts[0].last_modified


def test_read_institution(mm_simple) -> None:
    assert "" == mm_simple.accounts[0].institution


def test_read_name(mm_simple) -> None:
    assert "Asset" == mm_simple.accounts[0].name


def test_read_currency(mm_simple) -> None:
    assert "USD" == mm_simple.accounts[0].currency


def test_read_parentaccount(mm_simple) -> None:
    assert "" == mm_simple.accounts[0].parent_account


def test_read_lastreconciled(mm_simple) -> None:
    assert "" == mm_simple.accounts[0].last_reconciled


def test_read_description(mm_simple) -> None:
    assert "" == mm_simple.accounts[0].description


def test_read_type(mm_simple) -> None:
    assert "9" == mm_simple.accounts[0].type


def test_read_opened(mm_simple) -> None:
    assert "" == mm_simple.accounts[0].opened


def test_read_id(mm_simple) -> None:
    assert "AStd::Asset" == mm_simple.accounts[0].id


def test_read_subaccounts(mm_simple) -> None:
    assert 1 == len(mm_simple.accounts[0].sub_accounts)


def test_read_subaccount_id(mm_simple) -> None:
    assert "A000001" == mm_simple.accounts[0].sub_accounts[0].id


def test_repr(mm_simple) -> None:
    assert "Account(name='Asset', currency='USD')" == repr(mm_simple.accounts[0])
