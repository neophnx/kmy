from xml.etree.ElementTree import Element

from .entity import Entity


class Address(Entity):
    entity_name = "ADDRESS"

    def __init__(self) -> None:
        self.telephone: str = ""
        self.street: str = ""
        self.city: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.city = node.attrib["city"]
        self.street = node.attrib["street"]
        self.telephone = node.attrib["telephone"]

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["city"] = self.city
        node.attrib["street"] = self.street
        node.attrib["telephone"] = self.telephone
        return node
