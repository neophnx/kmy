from xml.etree.ElementTree import Element

from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class Tag(Entity):
    entity_name = "TAG"

    def __init__(self) -> None:
        self.closed: bool = False
        self.tag_color: str = ""
        self.name: str = ""
        self.id: str = ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"

    def init_from_xml(self, node: Element) -> None:
        self.closed = node.attrib["closed"] != "0"
        self.tag_color = node.attrib["tagcolor"]
        self.name = node.attrib["name"]
        self.id = node.attrib["id"]

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["closed"] = str(int(self.closed))
        node.attrib["tagcolor"] = self.tag_color
        node.attrib["name"] = self.name
        node.attrib["id"] = self.id
        return node


class TagContainer(Container[Tag]):
    entity_name = "TAGS"
    entity_class = Tag
