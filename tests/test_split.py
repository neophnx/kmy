import pytest

from kmy import Kmy, Split


@pytest.fixture(name="splits")
def fixture_splits(mm_simple: Kmy):
    yield mm_simple.transactions[0].splits


def test_read_splits_count(splits: "list[Split]") -> None:
    assert 2 == len(splits)


def test_read_payee(splits: "list[Split]") -> None:
    assert "" == splits[0].payee


def test_read_memo(splits: "list[Split]") -> None:
    assert "" == splits[0].memo


def test_read_shares(splits: "list[Split]") -> None:
    assert "42/1" == splits[0].shares


def test_read_number(splits: "list[Split]") -> None:
    assert "" == splits[0].number


def test_read_action(splits: "list[Split]") -> None:
    assert "" == splits[0].action


def test_read_price(splits: "list[Split]") -> None:
    assert "1/1" == splits[0].price


def test_read_account(splits: "list[Split]") -> None:
    assert "A000001" == splits[0].account


def test_read_reconcileflag(splits: "list[Split]") -> None:
    assert "0" == splits[0].reconcile_flag


def test_read_bankid(splits: "list[Split]") -> None:
    assert "" == splits[0].bank_id


def test_read_value(splits: "list[Split]") -> None:
    assert "42/1" == splits[0].value


def test_read_reconciledate(splits: "list[Split]") -> None:
    assert "" == splits[0].reconcile_date


def test_read_id(splits: "list[Split]") -> None:
    assert "S0001" == splits[0].id
