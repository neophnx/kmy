from kmy import Kmy


def test_read_institutions_count(mm_simple: Kmy) -> None:
    assert 1 == len(mm_simple.institutions)


def test_read_institution_sortcode(mm_simple: Kmy) -> None:
    assert "Routing number" == mm_simple.institutions[0].sort_code


def test_read_institution_manager(mm_simple: Kmy) -> None:
    assert "" == mm_simple.institutions[0].manager


def test_read_institution_name(mm_simple: Kmy) -> None:
    assert "Name of the institution" == mm_simple.institutions[0].name


def test_read_institution_id(mm_simple: Kmy) -> None:
    assert "I000001" == mm_simple.institutions[0].id


def test_read_institution_accountids(mm_simple: Kmy) -> None:
    assert 2 == len(mm_simple.institutions[0].account_ids)
    assert "A000001" == mm_simple.institutions[0].account_ids[0].id
    assert "A000003" == mm_simple.institutions[0].account_ids[1].id
