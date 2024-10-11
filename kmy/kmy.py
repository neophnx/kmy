import gzip
import xml.etree.ElementTree as elementTree
from os import PathLike  # pylint: disable=unused-import

from kmy.xml_storage.account.account import AccountContainer
from kmy.xml_storage.budget.budget import BudgetContainer
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.common.key_value_pair import KeyValuePairContainer
from kmy.xml_storage.cost_center.cost_center import CostCenterContainer
from kmy.xml_storage.currency.currency import CurrencyContainer
from kmy.xml_storage.file_info.file_info import FileInfo
from kmy.xml_storage.institution.institution import InstitutionContainer
from kmy.xml_storage.online_job.online_job import OnlineJobContainer
from kmy.xml_storage.payee.payee import PayeeContainer
from kmy.xml_storage.price.price import PriceContainer
from kmy.xml_storage.report.report import ReportContainer
from kmy.xml_storage.schedule.schedule import ScheduledTxContainer
from kmy.xml_storage.security.security import SecurityContainer
from kmy.xml_storage.tag.tag import TagContainer
from kmy.xml_storage.transaction.transaction import TransactionContainer
from kmy.xml_storage.user.user import User


class Kmy(Entity):
    entity_name = "KMYMONEY-FILE"

    file_info: FileInfo
    user: User
    institutions: InstitutionContainer
    payees: PayeeContainer
    cost_centers: CostCenterContainer
    tags: TagContainer
    accounts: AccountContainer
    transactions: TransactionContainer
    key_value_pairs: KeyValuePairContainer
    schedules: ScheduledTxContainer
    securities: SecurityContainer
    currencies: CurrencyContainer
    prices: PriceContainer
    reports: ReportContainer
    budgets: BudgetContainer
    online_jobs: OnlineJobContainer

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def to_xml_tree(self) -> elementTree.ElementTree:
        root = self.to_xml(None)
        return elementTree.ElementTree(root)

    @classmethod
    def from_kmy_file(cls, file_name: "PathLike[str] | str") -> "Kmy":
        with gzip.open(file_name, "rb") as file:
            tree = elementTree.parse(file)
        root = tree.getroot()
        kmm = Kmy.from_xml(root)
        return kmm
