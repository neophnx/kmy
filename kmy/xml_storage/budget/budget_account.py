from xml.etree.ElementTree import Element

from kmy.xml_storage.budget.period import Period
from kmy.xml_storage.common.entity import Entity


class BudgetAccount(Entity):
    entity_name = "ACCOUNT"

    def __init__(self) -> None:
        self.budgetsubaccounts: str = ""
        self.budgetlevel: str = ""
        self.id: str = ""

        self.periods: list[Period] = []

    def init_from_xml(self, node: Element) -> None:
        self.budgetsubaccounts = node.attrib["budgetsubaccounts"]
        self.budgetlevel = node.attrib["budgetlevel"]
        self.id = node.attrib["id"]

        for sub_node in node.findall(Period.entity_name):
            self.periods.append(Period.from_xml(sub_node))

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["budgetsubaccounts"] = self.budgetsubaccounts
        node.attrib["budgetlevel"] = self.budgetlevel
        node.attrib["id"] = self.id
        for period in self.periods:
            node.append(period.to_xml())
        return node

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.budgetsubaccounts}, {self.budgetlevel})"
        )
