from typing import List
from xml.etree.ElementTree import Element

from .key_value_pair import KeyValuePairContainer
from .account_id import AccountIdContainer
from .entity import Entity
from .container import Container
from .institutionaddress import InstitutionAddress


class Institution(Entity):
    entity_name = "INSTITUTION"

    def __init__(self) -> None:
        self.sortCode: str = ""
        self.manager: str = ""
        self.name: str = ""
        self.id: str = ""
        self.address: InstitutionAddress = InstitutionAddress()
        self.accountIds: AccountIdContainer = AccountIdContainer()
        self.keyValuePairs: KeyValuePairContainer = KeyValuePairContainer()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"

    def init_from_xml(self, node: Element) -> None:
        self.id = node.attrib["id"]
        self.sortCode = node.attrib["sortcode"]
        self.name = node.attrib["name"]
        self.manager = node.attrib["manager"]
        address_node = node.find(InstitutionAddress.entity_name)
        if address_node is not None:
            self.address = InstitutionAddress.from_xml(address_node)
        self.accountIds = AccountIdContainer.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["sortcode"] = self.sortCode
        node.attrib["manager"] = self.manager
        node.attrib["name"] = self.name
        node.attrib["id"] = self.id
        node.append(self.address.to_xml())
        node.append(self.accountIds.to_xml())

        return node


class InstitutionContainer(Container[Institution]):
    entity_name = "INSTITUTIONS"
    entity_class = Institution
