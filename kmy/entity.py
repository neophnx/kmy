from abc import ABC, abstractmethod
from typing import TypeVar, Type
from xml.etree.ElementTree import Element


C = TypeVar("C", bound="Entity")


class Entity(ABC):
    entity_name: str

    @classmethod
    def from_xml(cls: Type[C], node: Element) -> C:
        instance = cls()
        instance.init_from_xml(node)
        return instance

    @classmethod
    def from_parent_xml(cls: Type[C], node: Element) -> C:
        sub_nodes = node.findall(cls.entity_name)
        if len(sub_nodes) == 1:
            return cls.from_xml(sub_nodes[0])
        raise ValueError(f"from_parent_xml requires a single {cls.entity_name} entity")

    @abstractmethod
    def init_from_xml(self, node: Element) -> None:
        raise NotImplementedError(self.__class__)

    @abstractmethod
    def to_xml(self) -> Element:
        raise NotImplementedError(self.__class__)

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError(self.__class__)
