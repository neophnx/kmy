from kmy.xml_storage.budget.budget_account import BudgetAccountContainer
from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.attribute.date_attribute import DateAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class Budget(Entity):
    entity_name = "BUDGET"

    start: DateAttribute = DateAttribute("start")
    version: StrAttribute = StrAttribute("version")
    name: StrAttribute = StrAttribute("name")
    id: StrAttribute = StrAttribute("id")

    accounts: BudgetAccountContainer = BudgetAccountContainer()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.start}, {self.version}, {self.name}, {self.id})"


class BudgetContainer(Container[Budget]):
    entity_name = "BUDGETS"
    entity_class = Budget
    include_if_empty = True
