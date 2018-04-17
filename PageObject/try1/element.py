from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """
    Used for base page
    """

    def __set__(self, instance, value):
        """ sets text for element to be located """
        driver = instance.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, instance, owner):
        """ Get text out of element """
        driver = instance.driver
        WebDriverWait(driver,100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
