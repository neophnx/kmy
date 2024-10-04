from xml.etree.ElementTree import Element

from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class TagId(Entity):
    entity_name = "TAG"

    def __init__(self) -> None:
        self.id: str = ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id='{self.id}')"

    def init_from_xml(self, node: Element) -> None:
        self.id = node.attrib["id"]

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["id"] = self.id
        return node


class TagIdContainer(Container[TagId]):
    entity_name = "TAGS"
    entity_class = TagId
