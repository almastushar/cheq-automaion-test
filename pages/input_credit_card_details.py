import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class CreditCardDetails:
    def __init__(self, driver, wait):
        self.locators = Locators()
        self.locator = self.locators.locator()
        self.driver = driver
        self.wait = wait
        self.locator_iframe_card_number = self.locator['CHEQ-LOCATOR']['iframe_card_number']
        self.locator_iframe_expiry_date = self.locator['CHEQ-LOCATOR']['iframe_expiry_date']
        self.locator_iframe_cvc = self.locator['CHEQ-LOCATOR']['iframe_cvc']
        self.locator_card_number = self.locator['CHEQ-LOCATOR']['card_number']
        self.locator_expiry_date = self.locator['CHEQ-LOCATOR']['expiry_date']
        self.locator_cvc = self.locator['CHEQ-LOCATOR']['cvc']
        self.locator_name_on_card = self.locator['CHEQ-LOCATOR']['name_on_card']
        self.locator_verify_subtotal_button = self.locator['CHEQ-LOCATOR']['verify_subtotal_button']
        self.locator_start_order_button = self.locator['CHEQ-LOCATOR']['start_order_button']
        self.locator_verify_order_completed = self.locator['CHEQ-LOCATOR']['verify_order_completed']
        self.locator_verify_purchase_failed_with_cc = self.locator['CHEQ-LOCATOR']['verify_purchase_failed_with_cc']

    def input_cc_details(self, card_number, expiry_date, cvc, name_on_card):
        iframe = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_iframe_card_number)))
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.XPATH, self.locator_card_number).send_keys(card_number)
        self.driver.switch_to.default_content()
        iframe = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_iframe_expiry_date)))
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.XPATH, self.locator_expiry_date).send_keys(expiry_date)
        self.driver.switch_to.default_content()
        iframe = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_iframe_cvc)))
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.XPATH, self.locator_cvc).send_keys(cvc)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, self.locator_name_on_card).send_keys(name_on_card)
        self.driver.find_element(By.XPATH, self.locator_verify_subtotal_button).click()

    def verify_completed_order(self, verify_order_completed_text):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_start_order_button)))
        time.sleep(2)
        elem = verify_order_completed_text in self.driver.find_element(By.XPATH, self.locator_verify_order_completed).text
        return elem

    def verify_failed_to_complete_order(self, verify_order_completed_text):
        time.sleep(2)
        elem = verify_order_completed_text in self.driver.find_element(By.XPATH, self.locator_verify_purchase_failed_with_cc).text
        return elem
