import unittest
from pathlib import Path

from kmy.kmy import Kmy

file_name = Path(__file__).parent / "Test.kmy"


class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        mm = Kmy.from_kmy_file(file_name)
        self.accounts = mm.accounts
        self.account0 = self.accounts[0]

    def test_read_accounts_count(self) -> None:
        self.assertEqual(11, len(self.accounts))

    def test_read_number(self) -> None:
        self.assertEqual("", self.account0.number)

    def test_read_lastmodified(self) -> None:
        self.assertEqual("", self.account0.lastModified)

    def test_read_institution(self) -> None:
        self.assertEqual("", self.account0.institution)

    def test_read_name(self) -> None:
        self.assertEqual("Asset", self.account0.name)

    def test_read_currency(self) -> None:
        self.assertEqual("USD", self.account0.currency)

    def test_read_parentaccount(self) -> None:
        self.assertEqual("", self.account0.parentAccount)

    def test_read_lastreconciled(self) -> None:
        self.assertEqual("", self.account0.lastReconciled)

    def test_read_description(self) -> None:
        self.assertEqual("", self.account0.description)

    def test_read_type(self) -> None:
        self.assertEqual("9", self.account0.type)

    def test_read_opened(self) -> None:
        self.assertEqual("", self.account0.opened)

    def test_read_id(self) -> None:
        self.assertEqual("AStd::Asset", self.account0.id)

    def test_read_subaccounts(self) -> None:
        self.assertEqual(1, len(self.account0.subAccounts))

    def test_read_subaccount_id(self) -> None:
        self.assertEqual("A000001", self.account0.subAccounts[0].id)


if __name__ == "__main__":
    unittest.main()
