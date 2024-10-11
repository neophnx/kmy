from kmy.xml_storage.common.attribute.bool_attribute import BoolAttribute
from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class Tag(Entity):
    entity_name = "TAG"

    closed: BoolAttribute = BoolAttribute("closed")
    tag_color: StrAttribute = StrAttribute("tagcolor")
    name: StrAttribute = StrAttribute("name")
    id: StrAttribute = StrAttribute("id")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"


class TagContainer(Container[Tag]):
    entity_name = "TAGS"
    entity_class = Tag
    include_if_empty = True
