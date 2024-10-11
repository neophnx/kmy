from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.entity import Entity


class UserAddress(Entity):
    entity_name = "ADDRESS"

    telephone: StrAttribute = StrAttribute("telephone")
    county: StrAttribute = StrAttribute("county")
    city: StrAttribute = StrAttribute("city")
    zip_code: StrAttribute = StrAttribute("zipcode")
    street: StrAttribute = StrAttribute("street")

    def __repr__(self) -> str:
        return (
            f"InstitutionAddress({self.city=}, {self.street=}, "
            f"{self.telephone=}, {self.zip_code=}, {self.county=})"
        )
