import pytest


@pytest.mark.usefixtures("browser", "twitter_test_user")
class BaseTest:
    """
    This class contains functionality to be shared by any test class created.
    Pytest Fixtures are configured to automatically run
    """
    pass