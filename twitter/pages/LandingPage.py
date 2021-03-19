from twitter.pages.LoginPage import LoginPage
from utils.BasePage import BasePage
from selenium.webdriver.common.by import By

class LandingPage(BasePage):

    LOGIN_BTN_CSS = (By.CSS_SELECTOR, "a[data-testid='loginButton']")

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN_CSS).click()
        return LoginPage(self.driver)