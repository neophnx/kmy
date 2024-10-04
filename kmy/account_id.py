from .container import Container
from .entity_id import EntityId


class AccountId(EntityId):
    entity_name = "ACCOUNTID"


class AccountIdContainer(Container[AccountId]):
    entity_name = "ACCOUNTIDS"
    entity_class = AccountId

    def __init__(self) -> None:
        super().__init__(export_counts=False)
