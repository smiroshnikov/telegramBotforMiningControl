from selenium import webdriver
from selenium.webdriver.common.keys import Keys

MAC_PATH = "/Users/smiroshn/work/chromedriver/chromedriver"
WIN_PATH = "H:\Webdrivers\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(WIN_PATH)
# add OS selection dialogue

driver.get("http://python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Krokakokapuchila!")
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
assert "No results found." in driver.page_source
if "No results found" in driver.page_source:
    print("No result found as expected !")
news_button = driver.find_element_by_xpath("//li[contains(@id,'news')]/a")
news_button.click()

# print (type(driver.page_source), driver.page_source)
# driver.close()
