from kmy.xml_storage.common.attribute.bool_attribute import BoolAttribute
from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.payee.payee_address import PayeeAddress


class Payee(Entity):
    entity_name = "PAYEE"
    reference: StrAttribute = StrAttribute("reference")
    name: StrAttribute = StrAttribute("name")
    email: StrAttribute = StrAttribute("email")
    notes: StrAttribute = StrAttribute("notes", None)
    id: StrAttribute = StrAttribute("id")
    matching_enabled: BoolAttribute = BoolAttribute("matchingenabled")
    using_match_key: BoolAttribute = BoolAttribute("usingmatchkey", None)
    match_key: StrAttribute = StrAttribute("matchkey", None)
    match_ignore_case: BoolAttribute = BoolAttribute("matchignorecase", None)
    address: PayeeAddress

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"


class PayeeContainer(Container[Payee]):
    entity_name = "PAYEES"
    entity_class = Payee
