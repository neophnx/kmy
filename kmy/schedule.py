from xml.etree.ElementTree import Element

from kmy.container import Container
from kmy.entity import Entity
from kmy.payement import PaymentContainer
from kmy.transaction import TransactionContainer, Transaction


class ScheduledTx(Entity):
    entity_type = "SCHEDULED_TX"

    def __init__(self) -> None:
        self.lastDayInMonth: str = ""
        self.occurenceMultiplier: str = ""
        self.fixed: str = ""
        self.occurence: str = ""
        self.paymentType: str = ""
        self.endDate: str = ""
        self.startDate: str = ""
        self.autoEnter: str = ""
        self.name: str = ""
        self.type: str = ""
        self.weekendOption: str = ""
        self.id: str = ""
        self.lastPayment: str = ""

        self.payments: PaymentContainer = PaymentContainer()
        self.transaction: Transaction = Transaction()

    def init_from_xml(self, node: Element) -> None:
        self.lastDayInMonth = node.attrib.get("lastDayInMonth", "")
        self.occurenceMultiplier = node.attrib.get("occurenceMultiplier", "")
        self.fixed = node.attrib.get("fixed", "")
        self.occurence = node.attrib.get("occurence", "")
        self.paymentType = node.attrib.get("paymentType", "")
        self.endDate = node.attrib.get("endDate", "")
        self.startDate = node.attrib.get("startDate", "")
        self.autoEnter = node.attrib.get("autoEnter", "")
        self.name = node.attrib.get("name", "")
        self.type = node.attrib.get("type", "")
        self.weekendOption = node.attrib.get("weekendOption", "")
        self.id = node.attrib.get("id", "")
        self.lastPayment = node.attrib.get("lastPayment", "")

        self.payments = PaymentContainer.from_parent_xml(node)
        self.transaction = Transaction.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element(self.entity_type)
        node.attrib["lastDayInMonth"] = self.lastDayInMonth
        node.attrib["occurenceMultiplier"] = self.occurenceMultiplier
        node.attrib["fixed"] = self.fixed
        node.attrib["occurence"] = self.occurence
        node.attrib["paymentType"] = self.paymentType
        node.attrib["endDate"] = self.endDate
        node.attrib["startDate"] = self.startDate
        node.attrib["autoEnter"] = self.autoEnter
        node.attrib["name"] = self.name
        node.attrib["type"] = self.type
        node.attrib["weekendOption"] = self.weekendOption
        node.attrib["id"] = self.id
        node.attrib["lastPayment"] = self.lastPayment

        node.append(self.payments.to_xml())
        node.append(self.transaction.to_xml())
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.lastDayInMonth}...)"


class ScheduledTxContainer(Container[ScheduledTx]):
    entity_name = "SCHEDULES"
    entity_class = ScheduledTx
