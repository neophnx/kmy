from xml.etree.ElementTree import Element

from .entity import Entity
from .container import Container


class Price(Entity):
    entity_name = "PRICE"

    def init_from_xml(self, node: Element) -> None:
        raise NotImplementedError()

    def to_xml(self) -> Element:
        raise NotImplementedError()

    def __repr__(self) -> str:
        raise NotImplementedError()


class PriceContainer(Container[Price]):
    entity_name = "PRICES"
    entity_class = Price
