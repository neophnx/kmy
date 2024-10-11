from kmy.xml_storage.common.attribute.date_attribute import DateAttribute
from kmy.xml_storage.common.entity import Entity


class CreationDate(Entity):
    entity_name = "CREATION_DATE"

    date: DateAttribute = DateAttribute("date")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}@{id(self)}({self.date})"
