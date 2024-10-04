from xml.etree.ElementTree import Element

from kmy.xml_storage.common.entity import Entity


class UserAddress(Entity):
    entity_name = "ADDRESS"

    def __init__(self) -> None:
        super().__init__()
        self.telephone: str = ""
        self.county: str = ""
        self.city: str = ""
        self.zip_code: str = ""
        self.street: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.telephone = node.get("telephone", "")
        self.county = node.attrib.get("county", "")
        self.city = node.attrib.get("city", "")
        self.zip_code = node.attrib.get("zipcode", "")
        self.street = node.attrib.get("street", "")

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["telephone"] = self.telephone
        node.attrib["county"] = self.county
        node.attrib["city"] = self.city
        node.attrib["zipcode"] = self.zip_code
        node.attrib["street"] = self.street
        return node

    def __repr__(self) -> str:
        return (
            f"InstitutionAddress({self.city=}, {self.street=}, "
            f"{self.telephone=}, {self.zip_code=}, {self.county=})"
        )
