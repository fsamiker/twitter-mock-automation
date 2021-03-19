from selenium.webdriver.chrome.options import Options
from config import Config
import pytest
from selenium import webdriver

# Add base directory path to PYTHONPATH
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture
def config():
    return Config()

@pytest.fixture(scope="function")
def browser(request, config):
    options = Options()
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    if config.HEADLESS_TEST:
        options.headless = True
    driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER, options=options)
    driver.get(config.TEST_URL)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture
def twitter_test_user(config):
    if not (config.TEST_USER and config.PASSWORD):
        pytest.fail('Incomplete credentials. Kindly add twitter credentials to config.py')
    credentials = {'username': config.TEST_USER, 'password': config.PASSWORD}
    return credentials