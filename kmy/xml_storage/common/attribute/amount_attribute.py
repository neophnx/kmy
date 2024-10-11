from decimal import Decimal
from fractions import Fraction

from kmy.xml_storage.common.attribute.attribute import Attribute


class AmountAttribute(Attribute[Decimal]):
    @property
    def value(self) -> Decimal:
        if self.raw_value is not None and "/" in self.raw_value:
            numerator, denominator = self.raw_value.split("/", 1)
            return Decimal(int(numerator)) / Decimal(int(denominator))
        raise ValueError(f"AmountAttribute expects fraction, got {self.raw_value}")

    @value.setter
    def value(self, value: Decimal) -> None:
        num, denom = Fraction.from_decimal(value).as_integer_ratio()
        self.raw_value = f"{num}/{denom}"
