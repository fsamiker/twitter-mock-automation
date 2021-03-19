class BasePage:

    DEFAULT_PAGE_LOAD = 5  # seconds

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.DEFAULT_PAGE_LOAD)