from xml.etree.ElementTree import Element

from .entity import Entity
from .container import Container


class Budget(Entity):
    entity_name = "BUDGET"

    def init_from_xml(self, node: Element) -> None:
        raise NotImplementedError()

    def to_xml(self) -> Element:
        raise NotImplementedError()

    def __repr__(self) -> str:
        raise NotImplementedError()


class BudgetContainer(Container[Budget]):
    entity_name = "BUDGETS"
    entity_class = Budget
