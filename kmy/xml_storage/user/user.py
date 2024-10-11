from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.user.useraddress import UserAddress


class User(Entity):
    entity_name = "USER"

    name: StrAttribute = StrAttribute("name")
    email: StrAttribute = StrAttribute("email")

    address: UserAddress

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
