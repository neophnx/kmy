import gzip
from itertools import zip_longest
from pathlib import Path
from xml.etree.ElementTree import (
    parse,
    Element,
    dump,
)

import pytest

from kmy import Kmy

test_dir = Path(__file__).parent

VERBOSE = False


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
    assert node1.attrib == node2.attrib

    for sub_node1, sub_node2 in zip_longest(node1, node2):
        compare_xml(sub_node1, sub_node2)


@pytest.mark.parametrize("file_name", ["Test.kmy", "Test-full.kmy"])
def test_to_xml(file_name) -> None:

    path = test_dir / file_name

    mm = Kmy.from_kmy_file(path)

    with gzip.open(path, "rb") as file:
        ref = parse(file)
        test = mm.to_xml()

        compare_xml(ref.getroot(), test.getroot())
