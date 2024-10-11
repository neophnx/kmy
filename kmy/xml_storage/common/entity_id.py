from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.entity import Entity


class EntityId(Entity):
    entity_name = "ENTITY_ID"

    id: StrAttribute = StrAttribute("id")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id=})"
