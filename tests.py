import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


class TestGetFileInfo(unittest.TestCase):
    def test_get_calculator_files(self):
        contents = ["main.py", "tests.py", "pkg"]
        result = get_files_info("calculator", ".")
        for content in contents:
            self.assertIn(content, result, f"{content} not found in directory 'calculator'.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        # print("Result for current directory:")
        # print(result)

    def test_get_pkg_files(self):
        contents = ["calculator.py", "render.py"]
        result = get_files_info("calculator", "pkg")
        for content in contents:
            self.assertIn(content, result, f"{content} not found in directory 'calculator'.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        # print("Result for 'pkg' directory:")
        # print(result)

    def test_get_bin_files(self):
        result = get_files_info("calculator", "/bin")
        self.assertIn("outside the permitted working directory", result, "Method did not return expected error.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        # print("Result for '/bin' directory:")
        # print(result)

    def test_get_parent_files(self):
        result = get_files_info("calculator", "../")
        self.assertIn("outside the permitted working directory", result, "Method did not return expected error.")

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
        self.assertIn("def main():", result, "File did not contain expected contents.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    def test_get_file_contents_pkgcalculator_shouldSucceed(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        self.assertIn("def _apply_operator", result, "File did not contain expected contents.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    def test_get_file_contents_bin_shouldError(self):
        result = get_file_content("calculator", "/bin")
        self.assertIn("outside the permitted working directory", result, "Method did not return expected error.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    def test_get_file_contents_pkg_shouldError(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        self.assertIn("No such file or directory", result, "Method did not return expected error.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    @unittest.skip("Skip this test because it will permanently change file contents.")
    #TODO: Update this test later to reset file and verify new contents.
    def test_write_to_exiting_file_shouldSucceed(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        self.assertIn("File successfully overwritten", result, "Method did not return expected result.")
        
        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    @unittest.skip("Skip this test because it will fail successive runs if file isn't first deleted.")
    #TODO: Update this test later to handle successive runs.
    def test_create_and_write_new_file_shouldSucceed(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        self.assertIn("File successfully created", result, "Method did not return expected result.")
        
        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    def test_write_to_file_outside_working_directory_shouldError(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        self.assertIn("outside the permitted working directory", result, "Method did not return expected error.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    def test_run_calculator_file_shouldPrintUsageInstructions(self):
        result = run_python_file("calculator", "main.py")
        self.assertIn("Usage", result, "Method did not produce usage instructions.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    def test_run_calculator_with_arguments_shouldOutputResult(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        self.assertIn("8", result, "Method did not produce expected result.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    #@unittest.skip("Skip this test because it does not currently produce output that can be verified.")
    #TODO: Update this test later fix output for verification.
    def test_run_calculator_tests_shouldSucceed(self):
        result = run_python_file("calculator", "tests.py")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    def test_run_agent_main_file_shouldError(self):
        result = run_python_file("calculator", "../main.py")
        self.assertIn("outside the permitted working directory", result, "Method did not produce expected error.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

    def test_run_nonexisting_file_shouldError(self):
        result = run_python_file("calculator", "nonexistent.py")
        self.assertIn("File \"nonexistent.py\" not found", result, "Method did not produce expected error.")

        # Print for course assignments
        # TODO: Remove after completing scripted project
        #print(result)

if __name__ == "__main__":
    unittest.main()