import gzip
import xml.etree.ElementTree as elementTree
from os import PathLike  # pylint: disable=unused-import

from .account import AccountContainer
from .budget import BudgetContainer
from .costcenter import CostCenterContainer
from .currency import CurrencyContainer
from .fileinfo import FileInfo
from .institution import InstitutionContainer
from .key_value_pair import KeyValuePairContainer
from .online_job import OnlineJobContainer
from .payee import PayeeContainer
from .price import PriceContainer
from .report import ReportContainer
from .schedule import ScheduledTxContainer
from .security import SecurityContainer
from .tag import TagContainer
from .transaction import TransactionContainer
from .user import User


class Kmy:
    def __init__(self) -> None:
        self.file_info: FileInfo = FileInfo()
        self.user: User = User()
        self.institutions: InstitutionContainer = InstitutionContainer()
        self.payees: PayeeContainer = PayeeContainer()
        self.cost_centers: CostCenterContainer = CostCenterContainer()
        self.tags: TagContainer = TagContainer()
        self.accounts: AccountContainer = AccountContainer()
        self.transactions: TransactionContainer = TransactionContainer()
        self.key_value_pairs: KeyValuePairContainer = KeyValuePairContainer()
        self.schedules: ScheduledTxContainer = ScheduledTxContainer()
        self.securities: SecurityContainer = SecurityContainer()
        self.currencies: CurrencyContainer = CurrencyContainer()
        self.prices: PriceContainer = PriceContainer()
        self.reports: ReportContainer = ReportContainer()
        self.budgets: BudgetContainer = BudgetContainer()
        self.online_jobs: OnlineJobContainer = OnlineJobContainer()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(fileInfo='{self.file_info}', user={self.user})"
        )

    @classmethod
    def from_xml(cls, node: elementTree.Element) -> "Kmy":
        kmy: Kmy = cls()
        kmy.init_from_xml(node)
        return kmy

    def to_xml(self) -> elementTree.ElementTree:
        root = elementTree.Element("KMYMONEY-FILE")
        root.append(self.file_info.to_xml())
        root.append(self.user.to_xml())

        root.append(self.institutions.to_xml())
        root.append(self.payees.to_xml())
        root.append(self.cost_centers.to_xml())
        root.append(self.tags.to_xml())
        root.append(self.accounts.to_xml())
        root.append(self.transactions.to_xml())
        root.append(self.key_value_pairs.to_xml())
        root.append(self.schedules.to_xml())
        root.append(self.securities.to_xml())
        root.append(self.currencies.to_xml())
        root.append(self.prices.to_xml())
        root.append(self.reports.to_xml())
        root.append(self.budgets.to_xml())
        root.append(self.online_jobs.to_xml())

        return elementTree.ElementTree(root)

    def init_from_xml(self, node: elementTree.Element) -> None:
        self.file_info = FileInfo.from_parent_xml(node)
        self.user = User.from_parent_xml(node)

        self.institutions = InstitutionContainer.from_parent_xml(node)
        self.payees = PayeeContainer.from_parent_xml(node)
        self.cost_centers = CostCenterContainer.from_parent_xml(node)
        self.tags = TagContainer.from_parent_xml(node)
        self.accounts = AccountContainer.from_parent_xml(node)
        self.transactions = TransactionContainer.from_parent_xml(node)
        self.key_value_pairs = KeyValuePairContainer.from_parent_xml(node)
        self.schedules = ScheduledTxContainer.from_parent_xml(node)
        self.securities = SecurityContainer.from_parent_xml(node)
        self.currencies = CurrencyContainer.from_parent_xml(node)
        self.prices = PriceContainer.from_parent_xml(node)
        self.reports = ReportContainer.from_parent_xml(node)
        self.budgets = BudgetContainer.from_parent_xml(node)
        self.online_jobs = OnlineJobContainer.from_parent_xml(node)

    @classmethod
    def from_kmy_file(cls, file_name: "PathLike[str] | str") -> "Kmy":
        with gzip.open(file_name, "rb") as file:
            tree = elementTree.parse(file)
        root = tree.getroot()
        kmm = Kmy.from_xml(root)
        return kmm
