from datetime import date, datetime

from kmy.xml_storage.common.attribute.attribute import Attribute


class DateAttribute(Attribute[date]):

    @property
    def value(self) -> date:
        if self.raw_value is not None and self.raw_value != "":
            return datetime.strptime(self.raw_value, "%Y-%m-%d").date()
        raise ValueError(
            f"DateAttribute expects date formated as YYYY-MM-DD, got {self.raw_value!r} instead"
        )

    @value.setter
    def value(self, value: date) -> None:
        self.raw_value = value.strftime("%Y-%m-%d")
