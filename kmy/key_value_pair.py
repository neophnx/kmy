from xml.etree.ElementTree import Element

from .container import Container
from .entity import Entity


class KeyValuePair(Entity):
    entity_name = "PAIR"

    def __init__(self) -> None:
        self.key: str = ""
        self.value: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.key = node.attrib.get("key", "")
        self.value = node.attrib.get("value", "")

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.set("key", self.key)
        node.set("value", self.value)
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.key!r}, {self.value!r})"


class KeyValuePairContainer(Container[KeyValuePair]):
    entity_name = "KEYVALUEPAIRS"
    entity_class = KeyValuePair

    def __init__(self) -> None:
        super().__init__(export_counts=False)
