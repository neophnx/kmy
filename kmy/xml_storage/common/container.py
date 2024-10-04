from typing import TypeVar, Generic, Type
from xml.etree.ElementTree import Element

from kmy.xml_storage.common.entity import Entity

E = TypeVar("E", bound=Entity)


class Container(Entity, Generic[E]):
    C = TypeVar("C", bound="Container[E]")

    entity_class: Type[E]

    def __init__(self, export_counts: bool = True) -> None:
        self.entities: list[E] = []
        self.export_counts = export_counts
        super().__init__()

    def init_from_xml(self, node: Element) -> None:
        if node is not None:
            for entity in node:
                self.entities.append(self.entity_class.from_xml(entity))

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        if self.export_counts:
            node.attrib["count"] = str(len(self.entities))
        for entity in self.entities:
            node.append(entity.to_xml())
        return node

    @classmethod
    def from_parent_xml(cls: "Type[C]", node: Element) -> "C":
        nodes = node.findall(cls.entity_name)
        if len(nodes) == 0:
            return cls()
        return super().from_parent_xml(node)

    def __len__(self) -> int:
        return len(self.entities)

    def __getitem__(self, index: int) -> E:
        return self.entities[index]

    def __repr__(self) -> str:
        return f"Container[{self.entity_class}]"
