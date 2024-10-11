from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.common.key_value_pair import KeyValuePairContainer


class Security(Entity):
    entity_name = "SECURITY"

    rounding_method: StrAttribute = StrAttribute("rounding-method")
    symbol: StrAttribute = StrAttribute("symbol")
    saf: StrAttribute = StrAttribute("saf")
    type: StrAttribute = StrAttribute("type")
    name: StrAttribute = StrAttribute("name")
    pp: StrAttribute = StrAttribute("pp")
    trading_currency: StrAttribute = StrAttribute("trading-currency")
    trading_market: StrAttribute = StrAttribute("trading-market")
    id: StrAttribute = StrAttribute("id")

    key_palue_pairs: KeyValuePairContainer

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class SecurityContainer(Container[Security]):
    entity_name = "SECURITIES"
    entity_class = Security

    include_if_empty = True
