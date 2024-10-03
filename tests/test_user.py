import unittest
from pathlib import Path

from kmy.kmy import Kmy

file_name = Path(__file__).parent / "Test.kmy"


class TestUser(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.user = mm.user

    def test_read_name(self):
        self.assertEqual("Your name", self.user.name)

    def test_read_email(self):
        self.assertEqual("Email", self.user.email)


if __name__ == "__main__":
    unittest.main()
