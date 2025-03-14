from selenium.webdriver.common.by import By

from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class SuitePreferences:
    def __init__(self, driver, wait):
        self.locators = Locators()
        self.locator = self.locators.locator()
        self.driver = driver
        self.wait = wait
        self.locator_save_button = self.locator['CHEQ-LOCATOR']['save_button']
        self.locator_view_cart_button = self.locator['CHEQ-LOCATOR']['view_cart_button']
        self.locator_verify_suite_preferences = self.locator['CHEQ-LOCATOR']['verify_title']

    def save_suite_preferences(self):
        self.driver.find_element(By.XPATH, self.locator_save_button).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_view_cart_button)))

    def verify_suite_preferences(self, verify_suite_preferences_text):
        elem = self.driver.find_element(By.XPATH, self.locator_verify_suite_preferences).text == verify_suite_preferences_text
        return elem



