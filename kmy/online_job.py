from xml.etree.ElementTree import Element

from .entity import Entity
from .container import Container


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
