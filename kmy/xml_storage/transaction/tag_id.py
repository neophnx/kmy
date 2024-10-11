from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class TagId(Entity):
    entity_name = "TAG"

    id: StrAttribute = StrAttribute("id")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id='{self.id}')"


class TagIdContainer(Container[TagId]):
    entity_name = Container.FLAT
    entity_class = TagId
