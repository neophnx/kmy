from kmy.xml_storage.common.attribute.date_attribute import DateAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class Dates(Entity):
    entity_name = "DATES"
    from_date: DateAttribute = DateAttribute("from")
    to_date: DateAttribute = DateAttribute("to")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.from_date!r}, {self.to_date!r})"


class DatesContainer(Container[Dates]):
    entity_name = Container.FLAT
    entity_class = Dates
