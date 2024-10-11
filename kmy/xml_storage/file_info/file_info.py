from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.file_info.creation_date import CreationDate
from kmy.xml_storage.file_info.fix_version import FixVersion
from kmy.xml_storage.file_info.last_modified_date import LastModifiedDate
from kmy.xml_storage.file_info.version import Version


class FileInfo(Entity):
    entity_name = "FILEINFO"

    creation_date: CreationDate
    last_modified_date: LastModifiedDate
    version: Version
    fix_version: FixVersion

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(creationDate='{self.creation_date}',"
            f" lastModifiedDate={self.last_modified_date})"
        )
