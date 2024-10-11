from xml.etree.ElementTree import fromstring

from kmy.kmy import Kmy
from kmy.xml_storage.institution.institution import InstitutionContainer
from tests.xml_storage.test_write import compare_xml


def test_institution_xml_invariant():
    xml = fromstring(
        """
<INSTITUTIONS count="1">
    <INSTITUTION sortcode="Routing number" manager="" name="Name of the institution" id="I000001">
        <ADDRESS telephone="" city="" zip="" street=""/>
        <ACCOUNTIDS>
            <ACCOUNTID id="A000001"/>
            <ACCOUNTID id="A000003"/>
        </ACCOUNTIDS>
    </INSTITUTION>
</INSTITUTIONS>
"""
    )
    institutions = InstitutionContainer.from_xml(xml)
    test = institutions.to_xml(None)

    assert test is not None
    compare_xml(xml, test)


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
