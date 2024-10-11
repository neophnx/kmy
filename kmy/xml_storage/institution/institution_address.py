from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.entity import Entity


class InstitutionAddress(Entity):
    entity_name = "ADDRESS"
    telephone: StrAttribute = StrAttribute("telephone")
    city: StrAttribute = StrAttribute("city")
    zip: StrAttribute = StrAttribute("zip")
    street: StrAttribute = StrAttribute("street")

    def __repr__(self) -> str:
        return f"InstitutionAddress({self.city=}, {self.street=}, {self.telephone=}, {self.zip=})"
