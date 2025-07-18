import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


class TestGetFileInfo(unittest.TestCase):
    def test_get_calculator_files(self):
        contents = ["main.py", "tests.py", "pkg"]
        result = get_files_info("calculator", ".")
        for content in contents:
            self.assertIn(content, result, f"{content} not found in directory 'calculator'")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        # print("Result for current directory:")
        # print(result)

    def test_get_pkg_files(self):
        contents = ["calculator.py", "render.py"]
        result = get_files_info("calculator", "pkg")
        for content in contents:
            self.assertIn(content, result, f"{content} not found in directory 'calculator'")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        # print("Result for 'pkg' directory:")
        # print(result)

    def test_get_bin_files(self):
        result = get_files_info("calculator", "/bin")
        self.assertIn("outside the permitted working directory", result, "Method did not return expected error")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        # print("Result for '/bin' directory:")
        # print(result)

    def test_get_parent_files(self):
        result = get_files_info("calculator", "../")
        self.assertIn("outside the permitted working directory", result, "Method did not return expected error")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        # print("Result for '../' directory:")
        # print(result)

    def test_lorem_ipsum_shouldMeetCharLimit(self):
        result = get_file_content("calculator", "lorem.txt")
        self.assertLess(len(result), 10100)

        # Print for course assignments
        # TODO: Remove after completing scripted project
        # print(result)

    def test_get_file_contents_main_shouldSucceed(self):
        result = get_file_content("calculator", "main.py")
        self.assertIn("def main():", result, "File did not contain expected contents")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    def test_get_file_contents_pkgcalculator_shouldSucceed(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        self.assertIn("def _apply_operator", result, "File did not contain expected contents")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    def test_get_file_contents_bin_shouldError(self):
        result = get_file_content("calculator", "/bin")
        self.assertIn("outside the permitted working directory", result, "Method did not return expected error")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    def test_get_file_contents_pkg_shouldError(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        self.assertIn("No such file or directory", result, "Method did not return expected error")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

if __name__ == "__main__":
    unittest.main()