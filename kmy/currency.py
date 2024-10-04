from xml.etree.ElementTree import Element

from kmy.container import Container
from kmy.entity import Entity


class Currency(Entity):
    entity_name = "CURRENCY"

    def __init__(self) -> None:
        self.rounding_method: str = ""
        self.saf: str = ""
        self.pp: str = ""
        self.name: str = ""
        self.scf: str = ""
        self.symbol: str = ""
        self.type: str = ""
        self.id: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.rounding_method = node.attrib.get("rounding-method", "")
        self.saf = node.attrib.get("saf", "")
        self.pp = node.attrib.get("pp", "")
        self.name = node.attrib.get("name", "")
        self.scf = node.attrib.get("scf", "")
        self.symbol = node.attrib.get("symbol", "")
        self.type = node.attrib.get("type", "")
        self.id = node.attrib.get("id", "")

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["rounding-method"] = self.rounding_method
        node.attrib["saf"] = self.saf
        node.attrib["pp"] = self.pp
        node.attrib["name"] = self.name
        node.attrib["scf"] = self.scf
        node.attrib["symbol"] = self.symbol
        node.attrib["type"] = self.type
        node.attrib["id"] = self.id
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"


class CurrencyContainer(Container[Currency]):
    entity_name = "CURRENCIES"
    entity_class = Currency
