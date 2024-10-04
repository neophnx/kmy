from xml.etree.ElementTree import Element

from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.transaction.tag_id import TagId


class Split(Entity):
    entity_name = "SPLIT"

    def __init__(self) -> None:
        self.payee: str = ""
        self.memo: str = ""
        self.shares: str = ""
        self.number: str = ""
        self.action: str = ""
        self.price: str = ""
        self.account: str = ""
        self.reconcile_flag: str = ""
        self.bank_id: str = ""
        self.value: str = ""
        self.reconcile_date: str = ""
        self.id: str = ""
        self.tag_ids: list[TagId] = []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(payee='{self.payee}', value='{self.value}')"

    def init_from_xml(self, node: Element) -> None:
        self.payee = node.attrib["payee"]
        self.memo = node.attrib["memo"]
        self.shares = node.attrib["shares"]
        self.number = node.attrib["number"]
        self.action = node.attrib["action"]
        self.price = node.attrib["price"]
        self.account = node.attrib["account"]
        self.reconcile_flag = node.attrib["reconcileflag"]
        self.bank_id = node.attrib["bankid"]
        self.value = node.attrib["value"]
        self.reconcile_date = node.attrib["reconciledate"]
        self.id = node.attrib["id"]

        for sub_node in node.findall(TagId.entity_name):
            self.tag_ids.append(TagId.from_xml(sub_node))

    def to_xml(self) -> Element:
        node = Element("SPLIT")
        node.attrib["payee"] = self.payee
        node.attrib["memo"] = self.memo
        node.attrib["shares"] = self.shares
        node.attrib["number"] = self.number
        node.attrib["action"] = self.action
        node.attrib["price"] = self.price
        node.attrib["account"] = self.account
        node.attrib["reconcileflag"] = self.reconcile_flag
        node.attrib["bankid"] = self.bank_id
        node.attrib["value"] = self.value
        node.attrib["reconciledate"] = self.reconcile_date
        node.attrib["id"] = self.id

        for tag in self.tag_ids:
            node.append(tag.to_xml())
        return node


class SplitContainer(Container[Split]):
    entity_name = "SPLITS"
    entity_class = Split

    def __init__(self) -> None:
        super().__init__(export_counts=False)
