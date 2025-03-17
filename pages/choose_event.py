import configparser

from selenium.webdriver.common.by import By

from locators.locators import Locators
import time
from selenium.webdriver.support import expected_conditions as EC


class ChooseEvent:
    def __init__(self, driver, wait):
        self.locators = Locators()
        self.locator = self.locators.locator()
        self.driver = driver
        self.wait = wait
        self.locator_continue_button = self.locator['CHEQ-LOCATOR']['continue_button']
        self.locator_verify_chosen_event = self.locator['CHEQ-LOCATOR']['verify_header']

    def choose_event(self, event_name):
        locators = "//span[text()='{event_name}']/ancestor::label/span/input[@type='radio']".format(event_name=event_name)
        self.driver.find_element(By.XPATH, locators).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_continue_button)))
        self.driver.find_element(By.XPATH, self.locator_continue_button).click()
        time.sleep(2)

    def verify_chosen_event(self, verify_chosen_event_text):
        elem = self.driver.find_element(By.XPATH, self.locator_verify_chosen_event).text == verify_chosen_event_text
        return elem



