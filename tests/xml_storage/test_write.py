import gzip
from itertools import zip_longest
from xml.etree.ElementTree import (
    parse,
    Element,
    dump,
)

import pytest

from kmy.xml_storage.kmy import Kmy
from tests.conftest import TEST_CASES

VERBOSE = True


def compare_xml(node1: Element, node2: Element) -> None:
    if node1 is None and node2 is None:
        return
    assert node1 is not None
    assert node2 is not None
    if VERBOSE:
        print(node1.tag, node2.tag)
        dump(node1)
        dump(node2)
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
                f"  attrib {key=} | {node1.attrib.get(key, None)} {node2.attrib.get(key, None)}"
            )
        assert node1.attrib.get(key, None) == node2.attrib.get(key, None), (
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
        test = mm.to_xml()

        compare_xml(ref.getroot(), test.getroot())
