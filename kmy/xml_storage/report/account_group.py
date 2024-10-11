from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class AccountGroup(Entity):
    entity_name = "ACCOUNTGROUP"
    group: StrAttribute = StrAttribute("group")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.group!r})"


class AccountGroupContainer(Container[AccountGroup]):
    entity_name = Container.FLAT
    entity_class = AccountGroup
