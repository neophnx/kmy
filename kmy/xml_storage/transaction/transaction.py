from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.transaction.split import SplitContainer


class Transaction(Entity):
    entity_name = "TRANSACTION"

    post_date: StrAttribute = StrAttribute("postdate")
    memo: StrAttribute = StrAttribute("memo")
    commodity: StrAttribute = StrAttribute("commodity")
    entry_date: StrAttribute = StrAttribute("entrydate")
    id: StrAttribute = StrAttribute("id")

    splits: SplitContainer = SplitContainer()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(postDate='{self.post_date}', memo='{self.memo}')"


class TransactionContainer(Container[Transaction]):
    entity_name = "TRANSACTIONS"
    entity_class = Transaction
