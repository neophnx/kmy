from xml.etree.ElementTree import Element

from .entity import Entity


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


class Version(Entity):
    entity_name = "VERSION"

    def __init__(
        self,
    ) -> None:
        self.id: str = ""

    def init_from_xml(self, node: Element) -> None:
        self.id = node.attrib.get("id", "")

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["id"] = self.id
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id=})"


class FixVersion(Version):
    entity_name = "FIXVERSION"


class FileInfo(Entity):
    entity_name = "FILEINFO"

    def __init__(self) -> None:
        self.creationDate: CreationDate = CreationDate()
        self.lastModifiedDate: LastModifiedDate = LastModifiedDate()
        self.version: Version = Version()
        self.fixVersion: FixVersion = FixVersion()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(creationDate='{self.creationDate}', lastModifiedDate={self.lastModifiedDate})"

    def init_from_xml(self, node: Element) -> None:
        self.creationDate = CreationDate.from_parent_xml(node)
        self.lastModifiedDate = LastModifiedDate.from_parent_xml(node)
        self.version = Version.from_parent_xml(node)
        self.fixVersion = FixVersion.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element("FILEINFO")

        node.append(self.creationDate.to_xml())
        node.append(self.lastModifiedDate.to_xml())
        node.append(self.version.to_xml())
        node.append(self.fixVersion.to_xml())
        return node
