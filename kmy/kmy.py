from pathlib import Path

from kmy import xml_storage
from kmy.proxy.common import EntityProxy
from kmy.proxy.file_info.file_info import FileInfoProxy


class Kmy(EntityProxy[xml_storage.Kmy]):

    def __init__(self, path: Path) -> None:
        self.path = path
        self._raw = xml_storage.Kmy.from_kmy_file(path)

        self.file_info: FileInfoProxy = FileInfoProxy(self._raw.file_info)
        # self.user: UserProxy = UserProxy(self._raw.user)
        # self.institutions: InstitutionContainerProxy = InstitutionContainerProxy(self._raw.institutions)
        # self.payees: PayeeContainerProxy = PayeeContainerProxy()
        # self.cost_centers: CostCenterContainerProxy = CostCenterContainerProxy()
        # self.tags: TagContainerProxy = TagContainerProxy()
        # self.accounts: AccountContainerProxy = AccountContainerProxy()
        # self.transactions: TransactionContainerProxy = TransactionContainerProxy()
        # self.key_value_pairs: KeyValuePairContainerProxy = KeyValuePairContainerProxy()
        # self.schedules: ScheduledTxContainerProxy = ScheduledTxContainerProxy()
        # self.securities: SecurityContainerProxy = SecurityContainerProxy()
        # self.currencies: CurrencyContainerProxy = CurrencyContainerProxy()
        # self.prices: PriceContainerProxy = PriceContainerProxy()
        # self.reports: ReportContainerProxy = ReportContainerProxy()
        # self.budgets: BudgetContainerProxy = BudgetContainerProxy()
        # self.online_jobs: OnlineJobContainerProxy = OnlineJobContainerProxy()
