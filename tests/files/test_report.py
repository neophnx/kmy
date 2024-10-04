from kmy.kmy import Kmy


def test_read_reports_count_simple(mm_simple: Kmy) -> None:
    assert 0 == len(mm_simple.reports)


def test_read_reports_count_full(mm_full: Kmy) -> None:
    assert 1 == len(mm_full.reports)


def test_read_reports_full(mm_full: Kmy) -> None:
    assert (
        "Copie de Diagramme circulaire des revenus et dépenses"
        == mm_full.reports[0].name
    )
