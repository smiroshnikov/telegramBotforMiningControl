import unittest
from selenium import webdriver
from .page import MainPage, Search_Results_Page


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        MAC_PATH = "/Users/smiroshn/work/chromedriver/chromedriver"
        WIN_PATH = 'H:\\Webdrivers\\geckodriver.exe'
        self.driver = webdriver.Firefox(executable_path=WIN_PATH)
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        # Load the main page. In this case the home page of Python.org.
        main_page = MainPage(self.driver)
        # Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."
        # Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pythonth"
        main_page.click_go_button()
        search_results_page = Search_Results_Page(self.driver)
        # Verifies that the results page is not empty
        assert search_results_page.is_result_found(), "No results found."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
