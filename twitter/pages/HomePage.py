from twitter.pages.LogoutPage import LogoutPage
from utils.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class HomePage(BasePage):

    TWEET_TXTAREA = (By.CSS_SELECTOR, "div.public-DraftEditor-content")
    SUBMIT_TWEET_BTN = (By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[data-testid='AccountSwitcher_Logout_Button']")
    ACCOUNT_MENU_BTN = (By.CSS_SELECTOR, "div[data-testid='SideNav_AccountSwitcher_Button']")

    def tweet(self, content):
        txt_area = self.driver.find_element(*self.TWEET_TXTAREA)

        # Click on text area to enable send keys
        actions = ActionChains(self.driver)
        actions.move_to_element(txt_area).click(txt_area).perform()
        txt_area.send_keys(content)

        # Send tweet
        submit_btn = self.driver.find_element(*self.SUBMIT_TWEET_BTN)
        submit_btn.click()

    def logout(self):
        account_menu = self.driver.find_element(*self.ACCOUNT_MENU_BTN)
        account_menu.click()
        logout_btn = self.driver.find_element(*self.LOGOUT_BUTTON)
        logout_btn.click()
        return LogoutPage(self.driver)
