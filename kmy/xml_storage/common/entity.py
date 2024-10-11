from abc import ABC, abstractmethod

from typing import TypeVar, Type
from xml.etree.ElementTree import Element

C = TypeVar("C", bound="Entity")


class Entity(ABC):
    entity_name: str

    @classmethod
    def _all_annotations(cls) -> dict[str, Type[object]]:
        res = {}
        for cls0 in reversed(cls.mro()):
            if issubclass(cls0, Entity) and cls0 != Entity:
                res.update(cls0.__annotations__)

        return res

    @classmethod
    def from_xml(cls: Type[C], node: Element) -> C:
        from kmy.xml_storage.common.attribute.attribute import Attribute
        from kmy.xml_storage.common.container import Container

        assert (
            node.tag == cls.entity_name
        ), f"Actual tag {node.tag} expected {cls.__name__}"

        self = cls()

        for attr, entity_class in cls._all_annotations().items():
            if attr in ["entity_class"]:
                continue
            if issubclass(entity_class, Attribute):
                value = getattr(cls, attr)
                setattr(self, attr, value.from_xml(node))

            elif (
                issubclass(entity_class, Container)
                and entity_class.entity_name == Container.FLAT
            ):
                value = entity_class()
                value.entities = []
                for sub_node in node.findall(value.entity_class.entity_name):
                    value.entities.append(value.entity_class.from_xml(sub_node))

                setattr(self, attr, value)

            elif issubclass(entity_class, Entity):

                sub_nodes = node.findall(entity_class.entity_name)
                if len(sub_nodes) == 1:
                    value = entity_class.from_xml(sub_nodes[0])
                    setattr(self, attr, value)
                elif len(sub_nodes) > 1:
                    raise ValueError(
                        "{type(self)} has multiple children {type(entity_class)}, expected one"
                    )
            else:
                raise NotImplementedError(cls, attr, entity_class)
        return self

    def to_xml(self, parent: "Element|None") -> "Element|None":
        from kmy.xml_storage.common.attribute.attribute import Attribute
        from kmy.xml_storage.common.container import Container

        node = Element(self.entity_name)

        for attr, value in self.__dict__.items():
            if issubclass(getattr(self, attr).__class__, Attribute):
                value.to_xml(node)
            elif (
                issubclass(getattr(self, attr).__class__, Container)
                and getattr(self, attr).entity_name == Container.FLAT
            ):
                for sub_value in value.entities:
                    sub_value.to_xml(node)

            elif issubclass(getattr(self, attr).__class__, Entity):
                value.to_xml(node)

            else:
                raise NotImplementedError(attr, value, getattr(self, attr).__class__)
        if parent is not None:
            parent.append(node)
            return None
        return node

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError(self.__class__)
