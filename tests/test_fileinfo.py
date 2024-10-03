import unittest
from pathlib import Path

from kmy.kmy import Kmy

file_name = Path(__file__).parent / "Test.kmy"


class TestFileInfo(unittest.TestCase):
    def setUp(self) -> None:
        mm = Kmy.from_kmy_file(file_name)
        self.fileInfo = mm.fileInfo

    def test_read_creationDate(self) -> None:
        self.assertEqual("2020-12-13", self.fileInfo.creationDate.date)

    def test_read_lastModifiedDate(self) -> None:
        self.assertEqual("2020-12-13", self.fileInfo.lastModifiedDate.date)

    def test_read_version(self) -> None:
        self.assertEqual("1", self.fileInfo.version.id)

    def test_read_fixVersion(self) -> None:
        self.assertEqual("5", self.fileInfo.fixVersion.id)


if __name__ == "__main__":
    unittest.main()
