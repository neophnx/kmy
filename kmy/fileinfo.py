from xml.etree.ElementTree import Element

from .entity import Entity
from .entity_id import EntityId


class CreationDate(Entity):
    entity_name = "CREATION_DATE"

    def __init__(
        self,
    ) -> None:
        self.date: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.date = node.attrib.get("date", "")

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["date"] = self.date
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.date})"


class LastModifiedDate(CreationDate):
    entity_name = "LAST_MODIFIED_DATE"


class Version(EntityId):
    entity_name = "VERSION"


class FixVersion(EntityId):
    entity_name = "FIXVERSION"


class FileInfo(Entity):
    entity_name = "FILEINFO"

    def __init__(self) -> None:
        self.creation_date: CreationDate = CreationDate()
        self.last_modified_date: LastModifiedDate = LastModifiedDate()
        self.version: Version = Version()
        self.fix_version: FixVersion = FixVersion()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(creationDate='{self.creation_date}',"
            f" lastModifiedDate={self.last_modified_date})"
        )

    def init_from_xml(self, node: Element) -> None:
        self.creation_date = CreationDate.from_parent_xml(node)
        self.last_modified_date = LastModifiedDate.from_parent_xml(node)
        self.version = Version.from_parent_xml(node)
        self.fix_version = FixVersion.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element("FILEINFO")

        node.append(self.creation_date.to_xml())
        node.append(self.last_modified_date.to_xml())
        node.append(self.version.to_xml())
        node.append(self.fix_version.to_xml())
        return node
