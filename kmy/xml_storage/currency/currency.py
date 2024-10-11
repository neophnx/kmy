from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class Currency(Entity):
    entity_name = "CURRENCY"

    rounding_method: StrAttribute = StrAttribute("rounding-method")
    saf: StrAttribute = StrAttribute("saf")
    pp: StrAttribute = StrAttribute("pp")
    name: StrAttribute = StrAttribute("name")
    scf: StrAttribute = StrAttribute("scf")
    symbol: StrAttribute = StrAttribute("symbol")
    type: StrAttribute = StrAttribute("type")
    id: StrAttribute = StrAttribute("id")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"


class CurrencyContainer(Container[Currency]):
    entity_name = "CURRENCIES"
    entity_class = Currency
