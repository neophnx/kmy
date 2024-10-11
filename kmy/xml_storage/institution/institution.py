from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.common.key_value_pair import KeyValuePairContainer
from kmy.xml_storage.institution.account_id import AccountIdContainer
from kmy.xml_storage.institution.institution_address import InstitutionAddress


class Institution(Entity):
    entity_name = "INSTITUTION"

    sort_code: StrAttribute = StrAttribute("sortcode")
    manager: StrAttribute = StrAttribute("manager")
    name: StrAttribute = StrAttribute("name")
    id: StrAttribute = StrAttribute("id")
    address: InstitutionAddress
    account_ids: AccountIdContainer
    key_value_pairs: KeyValuePairContainer

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"


class InstitutionContainer(Container[Institution]):
    entity_name = "INSTITUTIONS"
    entity_class = Institution

    include_if_empty = True
