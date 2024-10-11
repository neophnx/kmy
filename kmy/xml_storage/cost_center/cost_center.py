from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class CostCenter(Entity):
    entity_name = "COSTCENTER"

    def __repr__(self) -> str:
        raise NotImplementedError()


class CostCenterContainer(Container[CostCenter]):
    entity_name = "COSTCENTERS"
    entity_class = CostCenter
    include_if_empty = True
