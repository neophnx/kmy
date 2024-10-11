from typing import TypeVar, Generic, Type
from xml.etree.ElementTree import Element

from kmy.xml_storage.common.entity import Entity

E = TypeVar("E", bound=Entity)


class Container(Entity, Generic[E]):
    C = TypeVar("C", bound="Container[E]")
    FLAT = "<FLAT>"

    entity_class: "Type[E]"
    include_if_empty = False
    export_counts = True
    entities: "list[E]"

    @classmethod
    def from_xml(cls, node: Element) -> "Container[E]":
        self = cls()
        self.entities = []

        if node is not None:
            if self.entity_name == Container.FLAT:
                for entity in node.findall(self.entity_class.entity_name):
                    self.entities.append(self.entity_class.from_xml(entity))

            else:
                for entity in node:
                    self.entities.append(self.entity_class.from_xml(entity))
        return self

    def to_xml(self, parent: "Element | None") -> "Element|None":
        if self.entity_name == Container.FLAT:
            assert parent is not None
        if self.include_if_empty or len(self.entities) > 0:
            node = Element(self.entity_name)
            if self.export_counts:
                node.attrib["count"] = str(len(self.entities))
            for entity in self.entities:
                entity.to_xml(node)

            if parent is not None:
                parent.append(node)
                return None
            return node

        return None

    def __len__(self) -> int:
        return len(self.entities)

    def __getitem__(self, index: int) -> E:
        return self.entities[index]

    def __repr__(self) -> str:
        return f"Container[{self.entity_class}]"
