from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class Price(Entity):
    entity_name = "PRICE"

    date: StrAttribute = StrAttribute("date")
    source: StrAttribute = StrAttribute("source")
    price: StrAttribute = StrAttribute("price")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.date}, {self.source}, {self.price})"


class InnerPriceContainer(Container[Price]):
    entity_name = Container.FLAT
    entity_class = Price


class PricePair(Entity):
    entity_name = "PRICEPAIR"
    to_id: StrAttribute = StrAttribute("to")
    from_id: StrAttribute = StrAttribute("from")
    prices: InnerPriceContainer

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_id}, {self.from_id})"


class PriceContainer(Container[PricePair]):
    entity_name = "PRICES"
    entity_class = PricePair
    include_if_empty = True
