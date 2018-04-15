from .element import BasePageElement
from .locators import MainPageLocators


class SearchTextElement(BasePageElement):
    """class retreives search text from the provided locator """

    # locator from searchbox
    locator = 'q'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON) # interesting....
        element.click()

class Search_Results_Page(BasePage):
    """ """
    def is_result_found(self):
        return "No results found" not in self.driver.page_source