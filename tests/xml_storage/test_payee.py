from kmy.kmy import Kmy


def test_read_payees_count(mm_simple: Kmy) -> None:
    assert 3 == len(mm_simple.payees)


def test_read_reference(mm_simple: Kmy) -> None:
    assert "" == mm_simple.payees[0].reference


def test_read_name(mm_simple: Kmy) -> None:
    assert "Some From" == mm_simple.payees[0].name


def test_read_email(mm_simple: Kmy) -> None:
    assert "who@ville.tld" == mm_simple.payees[0].email


def test_read_id(mm_simple: Kmy) -> None:
    assert "P000001" == mm_simple.payees[0].id


def test_read_matching_enabled(mm_simple: Kmy) -> None:
    assert not mm_simple.payees[0].matching_enabled
