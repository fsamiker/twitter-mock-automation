from twitter.pages.HomePage import HomePage
from utils.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    USERNAME_TXTBOX = (By.CSS_SELECTOR, "input[type=text]")
    PASSWORD_TXTBOX = (By.CSS_SELECTOR, "input[type=password]")
    LOGIN_BTN = (By.CSS_SELECTOR, "div[data-testid='LoginForm_Login_Button']")

    def enter_username(self, username):
        input = self.driver.find_element(*self.USERNAME_TXTBOX)
        input.clear()
        input.send_keys(username)

    def enter_password(self, password):
        input = self.driver.find_element(*self.PASSWORD_TXTBOX)
        input.clear()
        input.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
        return HomePage(self.driver)
