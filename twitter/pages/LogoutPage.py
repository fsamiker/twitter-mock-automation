from utils.BasePage import BasePage
from selenium.webdriver.common.by import By
import twitter.pages.LandingPage


class LogoutPage(BasePage):

    LOGOUT_BTN = (By.CSS_SELECTOR, "div[data-testid='confirmationSheetConfirm']")

    def confirm_logout(self):
        logout_btn = self.driver.find_element(*self.LOGOUT_BTN)
        logout_btn.click()
        return twitter.pages.LandingPage.LandingPage(self.driver)
