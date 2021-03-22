from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CHROME_DRIVER = os.getenv("CHROME_DRIVER") or "./webdrivers/chromedriver_v89"
    TEST_URL = 'https://twitter.com/'
    HEADLESS_TEST = False  # Run browser tests headless (no UI)

    # Credentials
    TEST_USER = os.getenv("TEST_USER")
    PASSWORD = os.getenv("PASSWORD")
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_SECRET_KEY= os.getenv("TWITTER_API_SECRET")
    TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
