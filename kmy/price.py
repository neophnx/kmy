from xml.etree.ElementTree import Element

from .entity import Entity
from .container import Container


class Price(Entity):
    entity_name = "PRICE"

    def __init__(self) -> None:
        self.date: str = ""
        self.source: str = ""
        self.price: str = ""

    def init_from_xml(self, node: Element) -> None:

        self.date = node.attrib.get("date", "")
        self.source = node.attrib.get("source", "")
        self.price = node.attrib.get("price", "")

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.set("date", self.date)
        node.set("source", self.source)
        node.set("price", self.price)
        return node

    def __repr__(self) -> str:
        raise NotImplementedError()


class PricePair(Entity):
    entity_name = "PRICEPAIR"

    def __init__(self) -> None:
        self.to_id: str = ""
        self.from_id: str = ""
        self.prices: list[Price] = []

    def init_from_xml(self, node: Element) -> None:
        self.to_id = node.attrib.get("to", "")
        self.from_id = node.attrib.get("from", "")
        for sub_node in node:
            self.prices.append(Price.from_xml(sub_node))

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.set("to", self.to_id)
        node.set("from", self.from_id)
        for price in self.prices:
            node.append(price.to_xml())
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_id}, {self.from_id})"


class PriceContainer(Container[PricePair]):
    entity_name = "PRICES"
    entity_class = PricePair
