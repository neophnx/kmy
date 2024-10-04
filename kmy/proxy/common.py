from datetime import date, datetime
from typing import Generic, TypeVar


from kmy.xml_storage.common.entity import Entity

E = TypeVar("E", bound=Entity)
T = TypeVar("T")


class EntityProxy(Generic[E]):

    @property
    def _dirty(self) -> bool:
        for attr in dir(self):
            if attr[0] != "_" and isinstance(
                getattr(self, attr), (EntityProxy, AttributeProxy)
            ):
                print(
                    attr, isinstance(getattr(self, attr), (EntityProxy, AttributeProxy))
                )
                if getattr(self, attr)._dirty:
                    print(attr, "dirty")
                    return True
        return False

    def __setattr__(self, key: str, value: "EntityProxy[E]|AttributeProxy[T]") -> None:
        try:
            getattr(self, key).set(value)
        except AttributeError:
            # initialization time
            self.__dict__[key] = value


class AttributeProxy(Generic[T]):

    def __init__(self, value: T) -> None:
        self.value = value
        self._dirty = False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self.value)):
            return False
        return other == self.value

    def __repr__(self) -> str:
        return repr(self.value)

    def set(self, value: T) -> None:
        if self.value != value:
            self._dirty = True
            self.value = value


class DateProxy(AttributeProxy[date]):
    def __init__(self, value: str) -> None:
        _value = datetime.strptime(value, "%Y-%m-%d").date()
        super().__init__(_value)
