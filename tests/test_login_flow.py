from utils.BaseTest import BaseTest
from twitter.pages.LandingPage import LandingPage
import time


class TestAuth(BaseTest):

    def test_auth_flow(self, twitter_api, twitter_test_user):

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
        time.sleep(15)  # Wait 15 seconds for twitter api to update with latest tweet
        user = twitter_api.get_user(twitter_test_user['username'])
        user_id = user['id']
        latest_tweet = twitter_api.get_latest_tweet(user_id)
        assert latest_tweet['text'] == TEST_PHRASE

        # Logout
        logout_page = home_page.logout()
        logout_page.confirm_logout()