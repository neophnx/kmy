from xml.etree.ElementTree import Element

from .entity import Entity


class InstitutionAddress(Entity):
    entity_name = "ADDRESS"

    def __init__(self) -> None:
        self.telephone: str = ""
        self.city: str = ""
        self.zip: str = ""
        self.street: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.telephone = node.attrib["telephone"]
        self.city = node.attrib["city"]
        self.zip = node.attrib["zip"]
        self.street = node.attrib["street"]

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["telephone"] = self.telephone
        node.attrib["city"] = self.city
        node.attrib["zip"] = self.zip
        node.attrib["street"] = self.street
        return node

    def __repr__(self) -> str:
        return f"InstitutionAddress({self.city=}, {self.street=}, {self.telephone=}, {self.zip=})"
