from xml.etree.ElementTree import Element

from kmy.container import Container
from kmy.entity import Entity
from kmy.payement import PaymentContainer
from kmy.transaction import Transaction


class ScheduledTx(Entity):
    entity_type = "SCHEDULED_TX"

    def __init__(self) -> None:
        self.last_day_in_month: str = ""
        self.occurence_multiplier: str = ""
        self.fixed: str = ""
        self.occurence: str = ""
        self.payment_type: str = ""
        self.end_date: str = ""
        self.start_date: str = ""
        self.auto_enter: str = ""
        self.name: str = ""
        self.type: str = ""
        self.weekend_option: str = ""
        self.id: str = ""
        self.last_payment: str = ""

        self.payments: PaymentContainer = PaymentContainer()
        self.transaction: Transaction = Transaction()

    def init_from_xml(self, node: Element) -> None:
        self.last_day_in_month = node.attrib.get("lastDayInMonth", "")
        self.occurence_multiplier = node.attrib.get("occurenceMultiplier", "")
        self.fixed = node.attrib.get("fixed", "")
        self.occurence = node.attrib.get("occurence", "")
        self.payment_type = node.attrib.get("paymentType", "")
        self.end_date = node.attrib.get("endDate", "")
        self.start_date = node.attrib.get("startDate", "")
        self.auto_enter = node.attrib.get("autoEnter", "")
        self.name = node.attrib.get("name", "")
        self.type = node.attrib.get("type", "")
        self.weekend_option = node.attrib.get("weekendOption", "")
        self.id = node.attrib.get("id", "")
        self.last_payment = node.attrib.get("lastPayment", "")

        self.payments = PaymentContainer.from_parent_xml(node)
        self.transaction = Transaction.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element(self.entity_type)
        node.attrib["lastDayInMonth"] = self.last_day_in_month
        node.attrib["occurenceMultiplier"] = self.occurence_multiplier
        node.attrib["fixed"] = self.fixed
        node.attrib["occurence"] = self.occurence
        node.attrib["paymentType"] = self.payment_type
        node.attrib["endDate"] = self.end_date
        node.attrib["startDate"] = self.start_date
        node.attrib["autoEnter"] = self.auto_enter
        node.attrib["name"] = self.name
        node.attrib["type"] = self.type
        node.attrib["weekendOption"] = self.weekend_option
        node.attrib["id"] = self.id
        node.attrib["lastPayment"] = self.last_payment

        node.append(self.payments.to_xml())
        node.append(self.transaction.to_xml())
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.last_day_in_month}...)"


class ScheduledTxContainer(Container[ScheduledTx]):
    entity_name = "SCHEDULES"
    entity_class = ScheduledTx
