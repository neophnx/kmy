from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity


class Payment(Entity):
    entity_name = "PAYMENT"


class PaymentContainer(Container[Payment]):
    entity_name = "PAYMENTS"
    entity_class = Payment
    include_if_empty = True
    export_counts = False
