from kmy.xml_storage.common.attribute.attribute import Attribute


class StrAttribute(Attribute[str]):
    @property
    def value(self) -> str:
        if self.raw_value is not None:
            return self.raw_value
        raise ValueError(f"StrAttribute expects str, got {self.raw_value}")

    @value.setter
    def value(self, value: str) -> None:
        self.raw_value = value
