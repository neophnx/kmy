from typing import List
from xml.etree.ElementTree import Element

from .entity import Entity
from .container import Container
from .split import Split, SplitContainer


class Transaction(Entity):
    entity_name = "TRANSACTION"

    def __init__(self) -> None:
        self.postDate: str = ""
        self.memo: str = ""
        self.commodity: str = ""
        self.entryDate: str = ""
        self.id: str = ""
        self.splits: SplitContainer = SplitContainer()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(postDate='{self.postDate}', memo='{self.memo}')"
        )

    def init_from_xml(self, node: Element) -> None:
        self.postDate = node.attrib["postdate"]
        self.memo = node.attrib["memo"]
        self.commodity = node.attrib["commodity"]
        self.entryDate = node.attrib["entrydate"]
        self.id = node.attrib["id"]
        self.splits = SplitContainer.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["postdate"] = self.postDate
        node.attrib["memo"] = self.memo
        node.attrib["commodity"] = self.commodity
        node.attrib["entrydate"] = self.entryDate
        node.attrib["id"] = self.id
        node.append(self.splits.to_xml())
        return node


class TransactionContainer(Container[Transaction]):
    entity_name = "TRANSACTIONS"
    entity_class = Transaction
