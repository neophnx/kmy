from xml.etree.ElementTree import Element

from .budget_account import BudgetAccount
from .entity import Entity
from .container import Container


class Budget(Entity):
    entity_name = "BUDGET"

    def __init__(self) -> None:
        self.start: str = ""
        self.version: str = ""
        self.name: str = ""
        self.id: str = ""
        self.accounts: list[BudgetAccount] = []

    def init_from_xml(self, node: Element) -> None:
        self.start = node.attrib.get("start", "")
        self.version = node.attrib.get("version", "")
        self.name = node.attrib.get("name", "")
        self.id = node.attrib.get("id", "")
        for sub_node in node.findall(BudgetAccount.entity_name):
            self.accounts.append(BudgetAccount.from_xml(sub_node))

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.set("start", self.start)
        node.set("version", self.version)
        node.set("name", self.name)
        node.set("id", self.id)
        for budget_account in self.accounts:
            node.append(budget_account.to_xml())
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.start}, {self.version}, {self.name}, {self.id})"


class BudgetContainer(Container[Budget]):
    entity_name = "BUDGETS"
    entity_class = Budget
