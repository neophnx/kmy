from kmy.proxy.common import EntityProxy
from kmy.proxy.file_info.creation_date import CreationDateProxy
from kmy.xml_storage.file_info.file_info import FileInfo


class FileInfoProxy(EntityProxy[FileInfo]):

    def __init__(self, file_info: FileInfo):
        self.creation_date: CreationDateProxy = CreationDateProxy(
            file_info.creation_date
        )
        # self.last_modified_date: LastModifiedDateProxy = LastModifiedDateProxy(file_info.last_modified_date)
        # self.version: VersionProxy = VersionProxy(file_info.version)
        # self.fix_version: FixVersionProxy = FixVersionProxy(file_info.fix_version)
