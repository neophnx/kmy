from xml.etree.ElementTree import Element

from .entity import Entity


class Period(Entity):
    entity_name = "PERIOD"

    def __init__(self) -> None:
        self.start: str = ""
        self.amount: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.start = node.attrib.get("start", "")
        self.amount = node.attrib.get("amount", "")

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["start"] = self.start
        node.attrib["amount"] = self.amount
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.start}, {self.amount})"
