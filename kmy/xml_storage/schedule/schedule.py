from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.attribute.date_attribute import DateAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.schedule.payement import PaymentContainer
from kmy.xml_storage.transaction.transaction import Transaction


class ScheduledTx(Entity):
    entity_name = "SCHEDULED_TX"

    last_day_in_month: StrAttribute = StrAttribute("lastDayInMonth")
    occurence_multiplier: StrAttribute = StrAttribute("occurenceMultiplier")
    fixed: StrAttribute = StrAttribute("fixed")
    occurence: StrAttribute = StrAttribute("occurence")
    payment_type: StrAttribute = StrAttribute("paymentType")
    end_date: StrAttribute = StrAttribute("endDate")
    start_date: DateAttribute = DateAttribute("startDate")
    auto_enter: StrAttribute = StrAttribute("autoEnter")
    name: StrAttribute = StrAttribute("name")
    type: StrAttribute = StrAttribute("type")
    weekend_option: StrAttribute = StrAttribute("weekendOption")
    id: StrAttribute = StrAttribute("id")
    last_payment: StrAttribute = StrAttribute("lastPayment")

    payments: PaymentContainer = PaymentContainer()
    transaction: Transaction = Transaction()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.last_day_in_month}...)"


class ScheduledTxContainer(Container[ScheduledTx]):
    entity_name = "SCHEDULES"
    entity_class = ScheduledTx
