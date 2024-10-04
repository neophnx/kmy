from kmy.proxy.common import EntityProxy, DateProxy
from kmy.xml_storage.file_info.creation_date import CreationDate


class CreationDateProxy(EntityProxy[CreationDate]):

    def __init__(self, creation_date: CreationDate) -> None:
        self.date = DateProxy(creation_date.date)
