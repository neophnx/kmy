from xml.etree.ElementTree import Element

from .container import Container
from .entity import Entity


class AccountId(Entity):
    entity_name = "ACCOUNTID"

    def __init__(self) -> None:
        self.id: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.id = node.attrib.get("id", "")

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["id"] = self.id
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id})"


class AccountIdContainer(Container[AccountId]):
    entity_name = "ACCOUNTIDS"
    entity_class = AccountId

    def __init__(self) -> None:
        super().__init__(export_counts=False)
