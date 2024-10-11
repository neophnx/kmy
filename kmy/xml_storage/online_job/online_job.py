from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class OnlineJob(Entity):
    entity_name = "ONLINEJOB"

    def __repr__(self) -> str:
        raise NotImplementedError()


class OnlineJobContainer(Container[OnlineJob]):
    entity_name = "ONLINEJOBS"
    entity_class = OnlineJob
    include_if_empty = True
