from xml.etree.ElementTree import Element

from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.common.key_value_pair import KeyValuePairContainer


class Security(Entity):
    entity_name = "SECURITY"

    def __init__(self) -> None:
        self.rounding_method: str = ""
        self.symbol: str = ""
        self.saf: str = ""
        self.type: str = ""
        self.name: str = ""
        self.pp: str = ""
        self.trading_currency: str = ""
        self.trading_market: str = ""
        self.id: str = ""

        self.key_palue_pairs: KeyValuePairContainer = KeyValuePairContainer()

    def init_from_xml(self, node: Element) -> None:
        self.rounding_method = node.get("rounding-method", "")
        self.symbol = node.get("symbol", "")
        self.saf = node.get("saf", "")
        self.type = node.get("type", "")
        self.name = node.get("name", "")
        self.pp = node.get("pp", "")
        self.trading_currency = node.get("trading-currency", "")
        self.trading_market = node.get("trading-market", "")
        self.id = node.get("id", "")
        self.key_palue_pairs = KeyValuePairContainer.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["rounding-method"] = self.rounding_method
        node.attrib["symbol"] = self.symbol
        node.attrib["saf"] = self.saf
        node.attrib["type"] = self.type
        node.attrib["name"] = self.name
        node.attrib["pp"] = self.pp
        node.attrib["trading-currency"] = self.trading_currency
        node.attrib["trading-market"] = self.trading_market
        node.attrib["id"] = self.id
        if self.key_palue_pairs.entities:
            node.append(self.key_palue_pairs.to_xml())
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class SecurityContainer(Container[Security]):
    entity_name = "SECURITIES"
    entity_class = Security
