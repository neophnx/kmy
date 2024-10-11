from abc import ABC, abstractmethod
from typing import Generic, Any, TypeVar
from xml.etree.ElementTree import Element


T = TypeVar("T")


class Attribute(ABC, Generic[T]):
    A = TypeVar("A", bound="Attribute[T]")

    def __init__(self, name: str, value: "str | None" = "") -> None:
        self.name: str = name
        self.raw_value: str | None = value

    def from_xml(self: A, node: Element) -> A:
        new = self.__class__(name=self.name, value=self.raw_value)

        new.raw_value = node.attrib.get(new.name, new.raw_value)
        return new

    def to_xml(self, node: Element) -> None:
        if self.raw_value is not None:
            assert isinstance(self.raw_value, str)
            node.attrib[self.name] = self.raw_value

    @property
    @abstractmethod
    def value(self) -> T:  # pragma: no cover
        raise NotImplementedError

    @value.setter
    def value(self, value: T) -> None:  # pragma: no cover
        raise NotImplementedError

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, str):
            return self.raw_value == other
        if isinstance(other, Attribute):
            return self.raw_value == other.raw_value

        return bool(self.value == other)

    def __repr__(self) -> str:
        return repr(self.raw_value)
