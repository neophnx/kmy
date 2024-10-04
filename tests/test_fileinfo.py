import unittest
from pathlib import Path

from kmy.kmy import Kmy

file_name = Path(__file__).parent / "Test.kmy"


class TestFileInfo(unittest.TestCase):
    def setUp(self) -> None:
        mm = Kmy.from_kmy_file(file_name)
        self.file_info = mm.file_info

    def test_read_creation_date(self) -> None:
        self.assertEqual("2020-12-13", self.file_info.creation_date.date)

    def test_read_last_modified_date(self) -> None:
        self.assertEqual("2020-12-13", self.file_info.last_modified_date.date)

    def test_read_version(self) -> None:
        self.assertEqual("1", self.file_info.version.id)

    def test_read_fix_version(self) -> None:
        self.assertEqual("5", self.file_info.fix_version.id)


if __name__ == "__main__":
    unittest.main()
