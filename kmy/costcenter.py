from xml.etree.ElementTree import Element

from .entity import Entity
from .container import Container


class CostCenter(Entity):
    entity_name = "COSTCENTER"

    def init_from_xml(self, node: Element) -> None:
        raise NotImplementedError()

    def to_xml(self) -> Element:
        raise NotImplementedError()

    def __repr__(self) -> str:
        raise NotImplementedError()


class CostCenterContainer(Container[CostCenter]):
    entity_name = "COSTCENTERS"
    entity_class = CostCenter
