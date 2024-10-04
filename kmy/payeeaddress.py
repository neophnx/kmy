from xml.etree.ElementTree import Element

from .entity import Entity


class PayeeAddress(Entity):
    entity_name = "ADDRESS"

    def __init__(self) -> None:
        super().__init__()
        self.telephone: str = ""
        self.state: str = ""
        self.city: str = ""
        self.street: str = ""
        self.post_code: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.telephone = node.attrib["telephone"]
        self.state = node.attrib["state"]
        self.city = node.attrib["city"]
        self.street = node.attrib["street"]
        self.post_code = node.attrib["postcode"]

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["telephone"] = self.telephone
        node.attrib["state"] = self.state
        node.attrib["city"] = self.city
        node.attrib["street"] = self.street
        node.attrib["postcode"] = self.post_code
        return node

    def __repr__(self) -> str:
        return (
            f"InstitutionAddress({self.city=}, {self.street=},"
            f" {self.telephone=}, {self.post_code=}, {self.state=})"
        )
