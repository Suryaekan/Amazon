import pytest
from selenium import webdriver
import time
from testmethods.Homepagemethods import HomePage


@pytest.fixture(scope="class")
def setup(request):
    """Fixture to initialize and quit the WebDriver once per test session."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver  # Attach driver to test class
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestHomePage:
    base_url = "https://www.amazon.in/"

    @pytest.fixture(autouse=True)
    def setup_test(self):
        """Setup method to initialize HomePage for all tests."""
        self.hp = HomePage(self.driver)  # ✅ Initialize hp for all tests

    def test_open_nav_menu(self):
        """Test if clicking the menu button opens the navigation menu."""
        self.driver.get(self.base_url)
        self.hp.click_menu()
        time.sleep(2)

        # Verify if the menu is opened
        assert self.hp.is_menu_visible(), "Navigation menu did not open."
        print("[PASS] Navigation menu opened successfully.")

    def test_close_nav_menu(self):
        """Test if clicking the close button closes the navigation menu."""
        self.driver.get(self.base_url)

        # Open the menu first
        self.hp.click_menu()
        time.sleep(2)

        # Click on the close button
        self.hp.close_menu()
        time.sleep(2)

        # Verify if the menu is closed
        assert not self.hp.is_menu_visible(), "Navigation menu did not close."
        print("[PASS] Navigation menu closed successfully.")