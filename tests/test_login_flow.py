from utils.BaseTest import BaseTest
from twitter.pages.LandingPage import LandingPage
import time


class TestAuth(BaseTest):

    def test_auth_flow(self, twitter_test_user):

        # Login
        landing_page = LandingPage(self.driver)
        login_page = landing_page.click_login()
        login_page.enter_username(twitter_test_user['username'])
        login_page.enter_password(twitter_test_user['password'])
        home_page = login_page.click_login()

        # Tweet something
        TEST_PHRASE = "Test Tweet. Hello World!"
        home_page.tweet(TEST_PHRASE)

        # Check API for tweet

        # Delete tweet

        # Logout

        time.sleep(5)