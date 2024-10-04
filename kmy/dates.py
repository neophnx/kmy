from xml.etree.ElementTree import Element

from .entity import Entity


class Dates(Entity):
    entity_name = "DATES"

    def __init__(self) -> None:
        self.from_date: str = ""
        self.to_date: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.from_date = node.attrib.get("from", "")
        self.to_date = node.attrib.get("to", "")

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["from"] = self.from_date
        node.attrib["to"] = self.to_date
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.from_date!r}, {self.to_date!r})"
