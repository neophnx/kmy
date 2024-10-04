from xml.etree.ElementTree import Element

from kmy.xml_storage.common.entity import Entity


class AccountGroup(Entity):
    entity_name = "ACCOUNTGROUP"

    def __init__(self) -> None:
        self.group: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.group = node.attrib.get("group", "")

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["group"] = self.group
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.group!r})"
