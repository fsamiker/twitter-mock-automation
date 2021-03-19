from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CHROME_DRIVER = os.getenv("CHROME_DRIVER") or os.path.join(ROOT_DIR, "webdrivers/chromedriver_v89")
    TEST_URL = 'https://twitter.com/'
    HEADLESS_TEST = False  # Run browser tests headless (no UI)

    # Credentials
    TEST_USER = os.getenv("TEST_USER")
    PASSWORD = os.getenv("PASSWORD")