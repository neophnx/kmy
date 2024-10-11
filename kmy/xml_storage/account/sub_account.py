from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity_id import EntityId


class SubAccount(EntityId):
    entity_name = "SUBACCOUNT"


class SubAccountContainer(Container[SubAccount]):
    entity_name = "SUBACCOUNTS"
    entity_class = SubAccount
    export_counts = False
