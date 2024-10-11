from kmy.xml_storage.budget.period import PeriodContainer
from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class BudgetAccount(Entity):
    entity_name = "ACCOUNT"

    budgetsubaccounts: StrAttribute = StrAttribute("budgetsubaccounts")
    budgetlevel: StrAttribute = StrAttribute("budgetlevel")
    id: StrAttribute = StrAttribute("id")

    periods: PeriodContainer = PeriodContainer()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.budgetsubaccounts}, {self.budgetlevel})"
        )


class BudgetAccountContainer(Container[BudgetAccount]):
    entity_name = Container.FLAT
    entity_class = BudgetAccount
