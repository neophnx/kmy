from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class Payment(Entity):
    entity_name = "PAYMENT"


class PaymentContainer(Container[Payment]):
    entity_name = "PAYMENTS"
    entity_class = Payment

    def __init__(self) -> None:
        super().__init__(export_counts=False)
