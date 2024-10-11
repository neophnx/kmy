from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.attribute.date_attribute import DateAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class Period(Entity):
    entity_name = "PERIOD"

    start: DateAttribute = DateAttribute("start")
    amount: StrAttribute = StrAttribute("amount")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.start}, {self.amount})"


class PeriodContainer(Container[Period]):
    entity_name = Container.FLAT
    entity_class = Period
