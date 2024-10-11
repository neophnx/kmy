from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity_id import EntityId


class AccountId(EntityId):
    entity_name = "ACCOUNTID"


class AccountIdContainer(Container[AccountId]):
    entity_name = "ACCOUNTIDS"
    entity_class = AccountId
    export_counts = False
