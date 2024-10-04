from kmy.xml_storage.kmy import Kmy


def test_read_costcenters_count_simple(mm_simple: Kmy):
    assert 0 == len(mm_simple.cost_centers)


def test_read_costcenters_count_full(mm_full: Kmy):
    assert 0 == len(mm_full.cost_centers)
