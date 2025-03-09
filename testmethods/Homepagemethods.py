from selenium.webdriver.common.by import By
from locators.HomePage import HomePagelocators

locators = HomePagelocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_menu(self):
        """Click on the navigation menu button."""
        self.driver.find_element(By.ID, locators.menu_button_id).click()  # FIXED

    def close_menu(self):
        """Click on the close button in the navigation menu."""
        self.driver.find_element(By.ID, locators.menu_close_button_id).click()  # FIXED

    def is_menu_visible(self):
        """Check if the navigation menu is visible."""
        menu_content = self.driver.find_element(By.XPATH, locators.menu_trending_test_xpath)  # FIXED
        return menu_content.is_displayed()
