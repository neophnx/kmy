from xml.etree.ElementTree import Element

from .entity import Entity
from .container import Container


class Report(Entity):
    entity_name = "REPORT"

    def init_from_xml(self, node: Element) -> None:
        raise NotImplementedError()

    def to_xml(self) -> Element:
        raise NotImplementedError()

    def __repr__(self) -> str:
        raise NotImplementedError()


class ReportContainer(Container[Report]):
    entity_name = "REPORTS"
    entity_class = Report
