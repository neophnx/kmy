from xml.etree.ElementTree import Element

from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


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
