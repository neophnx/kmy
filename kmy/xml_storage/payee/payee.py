from xml.etree.ElementTree import Element

from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.payee.payee_address import PayeeAddress


class Payee(Entity):
    entity_name = "PAYEE"

    def __init__(self) -> None:
        self.reference: str = ""
        self.name: str = ""
        self.email: str = ""
        self.notes: str = ""
        self.id: str = ""
        self.matching_enabled: bool = False
        self.usingmatchkey: str | None = None
        self.matchkey: str | None = None
        self.matchignorecase: str | None = None
        self.address: PayeeAddress = PayeeAddress()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"

    def init_from_xml(self, node: Element) -> None:
        self.reference = node.attrib["reference"]
        self.name = node.attrib["name"]
        self.email = node.attrib["email"]
        self.notes = node.attrib.get("notes", "")
        self.id = node.attrib["id"]
        self.matching_enabled = node.attrib["matchingenabled"] != "0"
        self.usingmatchkey = node.attrib.get("usingmatchkey", None)
        self.matchkey = node.attrib.get("matchkey", None)
        self.matchignorecase = node.attrib.get("matchignorecase", None)
        address_node = node.find("ADDRESS")
        if address_node is not None:
            self.address = PayeeAddress.from_xml(address_node)

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["reference"] = self.reference
        node.attrib["name"] = self.name
        node.attrib["email"] = self.email
        if self.notes:
            node.attrib["notes"] = self.notes
        node.attrib["id"] = self.id
        node.attrib["matchingenabled"] = str(int(self.matching_enabled))
        if self.usingmatchkey:
            node.attrib["usingmatchkey"] = self.usingmatchkey
        if self.matchkey:
            node.attrib["matchkey"] = self.matchkey
        if self.matchignorecase:
            node.attrib["matchignorecase"] = str(self.matchignorecase)
        node.append(self.address.to_xml())
        return node


class PayeeContainer(Container[Payee]):
    entity_name = "PAYEES"
    entity_class = Payee
