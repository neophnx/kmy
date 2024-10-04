import unittest
from pathlib import Path

from kmy.kmy import Kmy

file_name = Path(__file__).parent / "Test.kmy"


class TestInstitution(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.institutions = mm.institutions
        self.institution0 = self.institutions[0]

    def test_read_institutions_count(self):
        self.assertEqual(1, len(self.institutions))

    def test_read_institution_sortcode(self):
        self.assertEqual("Routing number", self.institution0.sort_code)

    def test_read_institution_manager(self):
        self.assertEqual("", self.institution0.manager)

    def test_read_institution_name(self):
        self.assertEqual("Name of the institution", self.institution0.name)

    def test_read_institution_id(self):
        self.assertEqual("I000001", self.institution0.id)

    def test_read_institution_accountids(self):
        self.assertEqual(2, len(self.institution0.account_ids))
        self.assertEqual("A000001", self.institution0.account_ids[0].id)
        self.assertEqual("A000003", self.institution0.account_ids[1].id)


if __name__ == "__main__":
    unittest.main()
