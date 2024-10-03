import gzip
from pathlib import Path
from xml.etree.ElementTree import (
    parse,
    indent,
    tostringlist,
)

from kmy import Kmy

file_name = Path(__file__).parent / "Test.kmy"


def test_to_xml() -> None:
    mm = Kmy.from_kmy_file(file_name)
    with gzip.open(file_name, "rb") as file:
        ref = parse(file)
        test = mm.to_xml()

        indent(ref)
        indent(test)
        assert (b"".join(tostringlist(ref.getroot(), encoding="utf-8"))).decode(
            "utf-8"
        ) == (b"".join(tostringlist(test.getroot(), encoding="utf-8"))).decode("utf-8")
