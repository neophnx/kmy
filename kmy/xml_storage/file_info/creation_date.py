from xml.etree.ElementTree import Element

from kmy.xml_storage.common.entity import Entity


class CreationDate(Entity):
    entity_name = "CREATION_DATE"

    def __init__(
        self,
    ) -> None:
        self.date: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.date = node.attrib.get("date", "")

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["date"] = self.date
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.date})"
