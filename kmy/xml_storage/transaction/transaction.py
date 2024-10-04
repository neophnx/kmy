from xml.etree.ElementTree import Element

from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.transaction.split import SplitContainer


class Transaction(Entity):
    entity_name = "TRANSACTION"

    def __init__(self) -> None:
        self.post_date: str = ""
        self.memo: str = ""
        self.commodity: str = ""
        self.entry_date: str = ""
        self.id: str = ""
        self.splits: SplitContainer = SplitContainer()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(postDate='{self.post_date}', memo='{self.memo}')"

    def init_from_xml(self, node: Element) -> None:
        self.post_date = node.attrib["postdate"]
        self.memo = node.attrib["memo"]
        self.commodity = node.attrib["commodity"]
        self.entry_date = node.attrib["entrydate"]
        self.id = node.attrib["id"]
        self.splits = SplitContainer.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["postdate"] = self.post_date
        node.attrib["memo"] = self.memo
        node.attrib["commodity"] = self.commodity
        node.attrib["entrydate"] = self.entry_date
        node.attrib["id"] = self.id
        node.append(self.splits.to_xml())
        return node


class TransactionContainer(Container[Transaction]):
    entity_name = "TRANSACTIONS"
    entity_class = Transaction
