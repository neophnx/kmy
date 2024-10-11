from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.entity import Entity


class PayeeAddress(Entity):
    entity_name = "ADDRESS"
    telephone: StrAttribute = StrAttribute("telephone")
    state: StrAttribute = StrAttribute("state")
    city: StrAttribute = StrAttribute("city")
    street: StrAttribute = StrAttribute("street")
    post_code: StrAttribute = StrAttribute("postcode")

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.city=}, {self.street=},"
            f" {self.telephone=}, {self.post_code=}, {self.state=})"
        )
