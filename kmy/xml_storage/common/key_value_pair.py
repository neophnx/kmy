from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class KeyValuePair(Entity):
    entity_name = "PAIR"

    key: StrAttribute = StrAttribute("key")
    value: StrAttribute = StrAttribute("value")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.key!r}, {self.value!r})"


class KeyValuePairContainer(Container[KeyValuePair]):
    entity_name = "KEYVALUEPAIRS"
    entity_class = KeyValuePair
    export_counts = False
