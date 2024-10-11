from kmy.xml_storage.account.sub_account import SubAccountContainer
from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.attribute.date_attribute import DateAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.common.key_value_pair import KeyValuePairContainer


class Account(Entity):
    entity_name = "ACCOUNT"

    number: StrAttribute = StrAttribute("number")
    last_modified: DateAttribute = DateAttribute("lastmodified")
    institution: StrAttribute = StrAttribute("institution")
    name: StrAttribute = StrAttribute("name")
    currency: StrAttribute = StrAttribute("currency")
    parent_account: StrAttribute = StrAttribute("parentaccount")
    last_reconciled: DateAttribute = DateAttribute("lastreconciled")
    description: StrAttribute = StrAttribute("description")
    type: StrAttribute = StrAttribute("type")
    opened: DateAttribute = DateAttribute("opened")
    id: StrAttribute = StrAttribute("id")

    sub_accounts: SubAccountContainer
    key_value_pair: KeyValuePairContainer

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(name={self.name!r}, currency={self.currency!r})"
        )


class AccountContainer(Container[Account]):
    entity_name = "ACCOUNTS"
    entity_class = Account
