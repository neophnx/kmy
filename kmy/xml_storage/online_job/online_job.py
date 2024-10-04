from xml.etree.ElementTree import Element

from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class OnlineJob(Entity):
    entity_name = "ONLINEJOB"

    def init_from_xml(self, node: Element) -> None:
        raise NotImplementedError()

    def to_xml(self) -> Element:
        raise NotImplementedError()

    def __repr__(self) -> str:
        raise NotImplementedError()


class OnlineJobContainer(Container[OnlineJob]):
    entity_name = "ONLINEJOBS"
    entity_class = OnlineJob
