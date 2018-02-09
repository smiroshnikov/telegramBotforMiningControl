from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys

# constants
MAC_PATH = "/Users/smiroshn/work/chromedriver/chromedriver"
WIN_PATH = "H:\Webdrivers\chromedriver_win32\chromedriver.exe"
CREEDENTIALS = ["automation@gmail.com", "rhrDBWT78iwU"]
USER_ACC_URL = "https://chorus.ai/blueprint/205426"
DRIVER = webdriver.WebDriver(WIN_PATH)


class ChorusHW:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.chorus.ai/login'

    def navigate_to_test_page(self):
        self.driver.get(self.url)

    def quit(self):
        """
        Close the browser
        """
        self.driver.quit()

    def login_into_chorus(self, credentials):
        # email_box = "//div[contains(@class, 'email-field')]"
        email_box = "//input[@name='email']"
        email_box_element = self.driver.find_element_by_xpath(email_box)
        email_box_element.click()
        email_box_element.clear()  # just in case
        email_box_element.send_keys(credentials[0])
        email_box_element.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)  # not too elegant
        password_box = "//input[@name='password']"
        password_box_element = self.driver.find_element_by_xpath(password_box)
        password_box_element.click()
        password_box_element.send_keys(credentials[1])
        password_box_element.send_keys(Keys.RETURN)


# def click_toggle_all(self):
#     """
#     The first click will mark all todos as completed.
#     The second click will mark all todos as active.
#     """
#     self.driver.find_element_by_id('toggle-all').click()


if __name__ == "__main__":
    chorus = ChorusHW(DRIVER)
    chorus.navigate_to_test_page()
    chorus.login_into_chorus(CREEDENTIALS)
    # chorus.quit()

#
#
#
# def find_new_todo_input(self):
#     """
#     Find new todo field
#     """
#     return self.driver.find_element_by_id('new-todo')
#
# def click_toggle_all(self):
#     """
#     The first click will mark all todos as completed.
#     The second click will mark all todos as active.
#     """
#     self.driver.find_element_by_id('toggle-all').click()
#
# def count_active_todos(self):
#     """
#     Get the count of active todos
#     """
#     return self.driver.find_element_by_id('todo-count').text
#
# def filter_all(self):
#     """
#     Displaying all todos
#     """
#     self.find_filters().find_element_by_xpath("//li/a[contains(text(), 'All')]").click()
#
# def filter_active(self):
#     """
#     Displaying only active todos
#     """
#     self.find_filters().find_element_by_xpath("//li/a[contains(text(), 'Active')]").click()
#
# def filter_completed(self):
#     """
#     Displaying only completed todos
#     """
#     self.find_filters().find_element_by_xpath("//li/a[contains(text(), 'Completed')]").click()
#
# def clear_completed(self):
#     """
#     Delete all completed todos
#     """
#     self.driver.find_element_by_id('clear-completed').click()
#
# def find_todo_list(self):
#     """
#     Get the todo list
#     """
#     return self.driver.find_element_by_id('todo-list')
#
# def toggle_todo(self, text):
#     """
#     Mark a todo that has value 'text' as complete or active
#     """
#     todo = self.find_todo(text)
#     todo.find_element_by_class_name('toggle').click()
#
# def toggle_todos(self, text):
#     """
#     Mark all todos that has value 'text' as complete or active
#     """
#     todos = self.find_todos(text)
#     for todo in todos:
#         todo.find_element_by_id('toggle').click()
#
# def delete_todo(self, text):
#     """
#     Delete a todo by the value
#     """
#     todo = self.find_todo(text)
#     todo_view = todo.find_element_by_class_name('view')
#     destroy_button = todo.find_element_by_class_name('destroy')
#     hover = ActionChains(self.driver).move_to_element(todo_view)
#     hover.perform()
#     if destroy_button.is_displayed():
#         destroy_button.click()
#
# def delete_todos(self, text):
#     """
#     Delete all todos by the value
#     """
#     todos = self.find_todos(text)
#     for todo in todos:
#         todo_view = todo.find_element_by_class_name('view')
#         destroy_button = todo.find_element_by_class_name('destroy')
#         hover = ActionChains(self.driver).move_to_element(todo_view)
#         hover.perform()
#         if destroy_button.is_displayed():
#             destroy_button.click()
#
# def find_active_todos(self):
#     """
#     Get the active todo list
#     """
#     todoList = self.find_todo_list()
#     return todoList.find_elements_by_xpath("//li[@class='ng-scope']")
#
# def find_completed_todos(self):
#     """
#     Get the completed todo list
#     """
#     todoList = self.find_todo_list()
#     return todoList.find_elements_by_xpath("//li[@class='ng-scope completed']")
#
# def update_todo(self, current_text, new_text):
#     """
#     Update a todo from 'current_text' to 'new_text'
#     """
#     todo = self.find_todo(current_text)
#     todo_view = todo.find_element_by_class_name('view')
#     todo_edit = todo.find_element_by_class_name('edit')
#     ActionChains(self.driver).double_click(todo_view).perform()
#     if todo_edit.is_displayed():
#         todo_edit.clear()
#         todo_edit.send_keys(new_text, Keys.ENTER)
#
# def update_todos(self, current_text, new_text):
#     """
#     Update all todos that have value 'current_text' to 'new_text'
#     """
#     todos = self.find_todos(text)
#     for todo in todos:
#         todo_view = todo.find_element_by_class_name('view')
#         todo_edit = todo.find_element_by_class_name('edit')
#         ActionChains(self.driver).double_click(todo_view).perform()
#         if todo_edit.is_displayed():
#             todo_edit.clear()
#             todo_edit.send_keys(text, Keys.ENTER)
#
# def find_todo(self, text):
#     """
#     Get a todo by the value
#     """
#     todoList = self.find_todo_list()
#     todo = todoList.find_element_by_xpath(
#         "//li/div[@class='view']/label[contains(text(), %s)]" % self.toXPathStringLiteral(text))
#     return todo.find_element_by_xpath('../..')
#
# def find_todos(self, text):
#     """
#     Get all todos by the value
#     """
#     result = []
#     todoList = self.find_todo_list()
#     todos = todoList.find_elements_by_xpath(
#         "//li/div[@class='view']/label[contains(text(), %s)]" % self.toXPathStringLiteral(text))
#     for todo in todos:
#         result.append(todo.find_element_by_xpath('../..'))
#     return result
#
# def find_filters(self):
#     """
#     Get filters panel
#     """
#     return self.driver.find_element_by_id('filters')
#
# def is_active_todo(self, todo):
#     """
#     Check wheter the specified todo is active or complete
#     """
#     return todo.get_attribute("class") == 'ng-scope'
#
# def toXPathStringLiteral(self, s):
#     """
#     Sanitize the string s to be used in the XPath
#     """
#     if "'" not in s: return "'%s'" % s
#     if '"' not in s: return '"%s"' % s
#     return "concat('%s')" % s.replace("'", "',\"'\",'")
