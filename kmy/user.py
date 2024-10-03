from xml.etree.ElementTree import Element

from .entity import Entity
from .useraddress import UserAddress


class User(Entity):
    entity_name = "USER"

    def __init__(self) -> None:
        self.name: str = ""
        self.email: str = ""
        self.address: UserAddress = UserAddress()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"

    def init_from_xml(self, node: Element) -> None:
        self.email = node.attrib["email"]
        self.name = node.attrib["name"]
        self.address = UserAddress.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["name"] = self.name

        node.attrib["email"] = self.email
        node.append(self.address.to_xml())
        return node
