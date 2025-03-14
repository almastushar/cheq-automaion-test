import time

from selenium.webdriver.common.by import By

from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class LOGIN:
    def __init__(self, driver, config, wait):
        self.locators = Locators()
        self.locator = self.locators.locator()
        self.driver = driver
        self.wait = wait
        self.url = config['CHEQ-UAT']['host'] + config['CHEQ-UAT']['login']
        self.locator_email = self.locator['CHEQ-LOCATOR']['email']
        self.locator_password = self.locator['CHEQ-LOCATOR']['password']
        self.locator_btn_login = self.locator['CHEQ-LOCATOR']['btn_login']
        self.locator_verify_successful_login = self.locator['CHEQ-LOCATOR']['verify_header']
        self.locator_verify_unsuccessful_login_for_invalid_credential = self.locator['CHEQ-LOCATOR']['verify_unsuccessful_login_for_invalid_credential']
        self.locator_verify_unsuccessful_login_for_pass_less_than_least_characters = self.locator['CHEQ-LOCATOR']['verify_unsuccessful_login_for_pass']
        self.locator_verify_unsuccessful_login_for_blank_credential_email = self.locator['CHEQ-LOCATOR']['verify_unsuccessful_login_for_email']
        self.locator_verify_unsuccessful_login_for_blank_credential_pass = self.locator['CHEQ-LOCATOR']['verify_unsuccessful_login_for_pass']

    def navigate_to_login_page(self):
        self.driver.get(url=self.url)

    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_email)))
        self.driver.find_element(By.XPATH, self.locator_email).send_keys(email)
        self.driver.find_element(By.XPATH, self.locator_password).send_keys(password)
        self.driver.find_element(By.XPATH, self.locator_btn_login).click()

    def verify_successful_login(self, verify_login_text):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_verify_successful_login)))
        elem = self.driver.find_element(By.XPATH, self.locator_verify_successful_login).text == verify_login_text
        return elem

    def verify_unsuccessful_login_for_invalid_credential(self, verify_login_text):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_verify_unsuccessful_login_for_invalid_credential)))
        elem = self.driver.find_element(By.XPATH, self.locator_verify_unsuccessful_login_for_invalid_credential).text.splitlines()[-1] == verify_login_text
        return elem

    def verify_unsuccessful_login_for_least_pass_character(self, verify_login_text):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_verify_unsuccessful_login_for_pass_less_than_least_characters)))
        elem = self.driver.find_element(By.XPATH, self.locator_verify_unsuccessful_login_for_pass_less_than_least_characters).text == verify_login_text
        return elem

    def verify_unsuccessful_login_for_blank_credential(self, verify_login_text_email, verify_login_text_pass):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_verify_unsuccessful_login_for_blank_credential_email)))
        elem1 = self.driver.find_element(By.XPATH, self.locator_verify_unsuccessful_login_for_blank_credential_email).text == verify_login_text_email
        elem2 = self.driver.find_element(By.XPATH, self.locator_verify_unsuccessful_login_for_blank_credential_pass).text == verify_login_text_pass
        if elem1 and elem2 is True:
            return True
        else:
            return False


