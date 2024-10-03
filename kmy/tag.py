from xml.etree.ElementTree import Element

from .entity import Entity
from .container import Container


class Tag(Entity):
    entity_name = "TAG"

    def __init__(self) -> None:
        self.closed: bool = False
        self.tagColor: str = ""
        self.name: str = ""
        self.id: str = ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"

    def init_from_xml(self, node: Element) -> None:
        self.closed = node.attrib["closed"] != "0"
        self.tagColor = node.attrib["tagcolor"]
        self.name = node.attrib["name"]
        self.id = node.attrib["id"]

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["closed"] = str(int(self.closed))
        node.attrib["tagcolor"] = self.tagColor
        node.attrib["name"] = self.name
        node.attrib["id"] = self.id
        return node


class TagContainer(Container[Tag]):
    entity_name = "TAGS"
    entity_class = Tag


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
