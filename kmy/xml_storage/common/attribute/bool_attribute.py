from kmy.xml_storage.common.attribute.attribute import Attribute


class BoolAttribute(Attribute[bool]):
    @property
    def value(self) -> bool:
        if self.raw_value is not None:
            if self.raw_value != "":
                return bool(int(self.raw_value))

        raise ValueError(f"BoolAttribute expects 0 or 1, got {self.raw_value}")

    @value.setter
    def value(self, value: bool) -> None:
        self.raw_value = str(int(value))

    def __bool__(self) -> bool:
        return self.value
