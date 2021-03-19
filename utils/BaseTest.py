import pytest


@pytest.mark.usefixtures("browser", "twitter_test_user")
class BaseTest:
    pass