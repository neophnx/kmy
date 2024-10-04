from xml.etree.ElementTree import Element

from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class SubAccount(Entity):
    entity_name = "SUBACCOUNT"

    def __init__(self) -> None:
        self.id: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.id = node.attrib["id"]

    def to_xml(self) -> "Element":
        node = Element(self.entity_name)
        node.attrib["id"] = self.id
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id})"


class SubAccountContainer(Container[SubAccount]):
    entity_name = "SUBACCOUNTS"
    entity_class = SubAccount

    def __init__(self) -> None:
        super().__init__(
            export_counts=False,
        )
