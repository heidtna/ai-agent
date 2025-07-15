import unittest
from functions.get_files_info import get_files_info


class TestGetFileInfo(unittest.TestCase):
    def test_get_calculator_files(self):
        result = get_files_info("calculator", ".")
        print("Result for current directory:")
        print(result)

    def test_get_pkg_files(self):
        result = get_files_info("calculator", "pkg")
        print("Result for 'pkg' directory:")
        print(result)

    def test_get_bin_files(self):
        result = get_files_info("calculator", "/bin")
        print("Result for '/bin' directory:")
        print(result)

    def test_get_parent_files(self):
        result = get_files_info("calculator", "../")
        print("Result for '../' directory:")
        print(result)

if __name__ == "__main__":
    unittest.main()