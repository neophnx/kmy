import gzip
from itertools import zip_longest
from xml.etree.ElementTree import (
    parse,
    Element,
    dump,
    indent,
)

import pytest

from kmy.kmy import Kmy
from tests.conftest import TEST_CASES

VERBOSE = True


def compare_xml(node1: Element, node2: Element) -> None:
    if node1 is None and node2 is None:
        return
    if VERBOSE:
        print("=" * 50)
        print(
            "== node1",
        )
        if node1 is not None:
            indent(node1)
            dump(node1)
        else:
            print("   Empty node")
        print("== node2")
        if node2 is not None:
            indent(node2)
            dump(node2)
        else:
            print("   Empty node")
    assert node1 is not None, f"node1 is None {node2}"
    assert node2 is not None, f"node2 is None {node2}"
    assert node1.tag == node2.tag, (node1, node2)

    if node1.text is not None and node1.text.strip() == "":
        node1.text = None
    if node2.text is not None and node2.text.strip() == "":
        node2.text = None
    assert node1.text == node2.text, (node1, node2)

    if node1.tail is not None and node1.tail.strip() == "":
        node1.tail = None
    if node2.tail is not None and node2.tail.strip() == "":
        node2.tail = None

    assert node1.tail == node2.tail, (node1, node2)

    for key in set(node1.attrib.keys()).union(set(node2.attrib.keys())):
        if VERBOSE:
            print(
                f"  attrib {key=} | {node1.attrib.get(key, None)!r} {node2.attrib.get(key, None)!r}"
            )
        assert str(node1.attrib.get(key, None)) == str(node2.attrib.get(key, None)), (
            node1,
            node2,
        )

    assert node1.attrib == node2.attrib

    for sub_node1, sub_node2 in zip_longest(node1, node2):
        compare_xml(sub_node1, sub_node2)


@pytest.mark.parametrize("path", TEST_CASES)
def test_to_xml(path) -> None:

    mm = Kmy.from_kmy_file(path)

    with gzip.open(path, "rb") as file:
        ref = parse(file)
        test = mm.to_xml_tree()

        compare_xml(ref.getroot(), test.getroot())
