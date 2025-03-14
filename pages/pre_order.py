import configparser
import time

from selenium.webdriver.common.by import By

from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC

locator = configparser.ConfigParser()
locator.read("locators.ini")


class PreOrder:
    def __init__(self, driver, wait):
        # self.locators = Locators()
        # self.locator = self.locators.locator()
        self.driver = driver
        self.wait = wait
        self.locator_save_pre_order_button = locator['CHEQ-LOCATOR']['save_pre_order_button']
        self.locator_credit_card_button = locator['CHEQ-LOCATOR']['credit_card_button']
        self.locator_verify_subtotal_button = locator['CHEQ-LOCATOR']['verify_subtotal_button']
        self.locator_verify_credit_card = locator['CHEQ-LOCATOR']['verify_credit_card']

    def save_pre_order(self):
        self.driver.find_element(By.XPATH, self.locator_save_pre_order_button).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_credit_card_button)))

    def select_credit_card(self):
        self.driver.find_element(By.XPATH, self.locator_credit_card_button).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_verify_subtotal_button)))
        time.sleep(2)

    def verify_credit_card_selection(self, verify_sub_total_text, total_order):
        elem = self.driver.find_element(By.XPATH,
                                        self.locator_verify_credit_card).text == verify_sub_total_text + " " + total_order
        return elem
