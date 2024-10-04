from xml.etree.ElementTree import Element

from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.common.key_value_pair import KeyValuePairContainer
from kmy.xml_storage.institution.account_id import AccountIdContainer
from kmy.xml_storage.institution.institution_address import InstitutionAddress


class Institution(Entity):
    entity_name = "INSTITUTION"

    def __init__(self) -> None:
        self.sort_code: str = ""
        self.manager: str = ""
        self.name: str = ""
        self.id: str = ""
        self.address: InstitutionAddress = InstitutionAddress()
        self.account_ids: AccountIdContainer = AccountIdContainer()
        self.key_value_pairs: KeyValuePairContainer = KeyValuePairContainer()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"

    def init_from_xml(self, node: Element) -> None:
        self.id = node.attrib["id"]
        self.sort_code = node.attrib["sortcode"]
        self.name = node.attrib["name"]
        self.manager = node.attrib["manager"]
        address_node = node.find(InstitutionAddress.entity_name)
        if address_node is not None:
            self.address = InstitutionAddress.from_xml(address_node)
        self.account_ids = AccountIdContainer.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["sortcode"] = self.sort_code
        node.attrib["manager"] = self.manager
        node.attrib["name"] = self.name
        node.attrib["id"] = self.id
        node.append(self.address.to_xml())
        node.append(self.account_ids.to_xml())

        return node


class InstitutionContainer(Container[Institution]):
    entity_name = "INSTITUTIONS"
    entity_class = Institution
