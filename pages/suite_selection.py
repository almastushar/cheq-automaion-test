import time

from selenium.webdriver.common.by import By

from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class SuiteSelection:
    def __init__(self, driver, wait):
        self.locators = Locators()
        self.locator = self.locators.locator()
        self.driver = driver
        self.wait = wait
        self.locator_continue_button = self.locator['CHEQ-LOCATOR']['continue_button']
        self.locator_pop_continue_button = self.locator['CHEQ-LOCATOR']['pop_continue_button']
        self.locator_save_button = self.locator['CHEQ-LOCATOR']['save_button']
        self.locator_verify_suite_selection = self.locator['CHEQ-LOCATOR']['verify_title']

    def select_suite(self, suite_name):
        locator = "//span[text()='{suite_name}']/ancestor::label/span/input[@type='radio']".format(suite_name=suite_name)
        self.driver.find_element(By.XPATH, locator).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_continue_button)))
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.locator_continue_button).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_pop_continue_button)))
        self.driver.find_element(By.XPATH, self.locator_pop_continue_button).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_save_button)))

    def verify_suite_selection(self, verify_suite_selection_text):
        elem = self.driver.find_element(By.XPATH, self.locator_verify_suite_selection).text == verify_suite_selection_text
        return elem



