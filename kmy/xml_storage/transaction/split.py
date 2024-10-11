from kmy.xml_storage.common.attribute.amount_attribute import AmountAttribute
from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.transaction.tag_id import TagIdContainer


class Split(Entity):
    entity_name = "SPLIT"

    payee: StrAttribute = StrAttribute("payee")
    memo: StrAttribute = StrAttribute("memo")
    shares: AmountAttribute = AmountAttribute("shares")
    number: StrAttribute = StrAttribute("number")
    action: StrAttribute = StrAttribute("action")
    price: AmountAttribute = AmountAttribute("price")
    account: StrAttribute = StrAttribute("account")
    reconcile_flag: StrAttribute = StrAttribute("reconcileflag")
    bank_id: StrAttribute = StrAttribute("bankid")
    value: StrAttribute = StrAttribute("value")
    reconcile_date: StrAttribute = StrAttribute("reconciledate")
    id: StrAttribute = StrAttribute("id")

    tag_ids: TagIdContainer

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(payee='{self.payee}', value='{self.value}')"


class SplitContainer(Container[Split]):
    entity_name = "SPLITS"
    entity_class = Split
    export_counts = False
