from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage(object):
    username_locator = By.ID("username")
    password_locator = By.ID("passwd")
    login_button_locator = By.ID("login")

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="H:\\Webdrivers\\geckodriver.exe")



