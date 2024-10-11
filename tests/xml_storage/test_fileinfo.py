from copy import deepcopy
from datetime import date
from xml.etree.ElementTree import fromstring

from kmy.kmy import Kmy
from kmy.xml_storage.file_info.creation_date import CreationDate
from kmy.xml_storage.file_info.file_info import FileInfo
from tests.xml_storage.test_write import compare_xml


def test_creation_date_xml_invariant():
    xml = fromstring(
        """
  <CREATION_DATE date="2020-12-13"/>
"""
    )

    creation_date = CreationDate.from_xml(xml)

    assert creation_date.date == "2020-12-13"
    test = creation_date.to_xml(None)

    assert test is not None
    compare_xml(xml, test)


def test_file_info_xml_invariant():
    xml = fromstring(
        """
<FILEINFO>
  <CREATION_DATE date="2020-12-13"/>
  <LAST_MODIFIED_DATE date="2020-12-13"/>
  <VERSION id="1"/>
  <FIXVERSION id="5"/>
</FILEINFO>
"""
    )
    file_info = FileInfo.from_xml(xml)

    test = file_info.to_xml(None)

    assert test is not None
    compare_xml(xml, test)


def test_read_creation_date(mm_simple: Kmy) -> None:

    assert "2020-12-13" == mm_simple.file_info.creation_date.date


def test_read_last_modified_date(mm_simple: Kmy) -> None:
    assert "2020-12-13" == mm_simple.file_info.last_modified_date.date


def test_write_last_modified_date(mm_simple: Kmy) -> None:
    mm = deepcopy(mm_simple)
    mm.file_info.last_modified_date.date.value = date(2024, 10, 9)

    assert "2024-10-09" == mm.file_info.last_modified_date.date


def test_read_version(mm_simple: Kmy) -> None:
    assert "1" == mm_simple.file_info.version.id


def test_read_fix_version(mm_simple: Kmy) -> None:
    assert "5" == mm_simple.file_info.fix_version.id
