import configparser

from selenium.webdriver.common.by import By

from locators.locators import Locators
import time
from selenium.webdriver.support import expected_conditions as EC


class OrderPreCheck:
    def __init__(self, driver, wait):
        self.locators = Locators()
        self.locator = self.locators.locator()
        self.driver = driver
        self.wait = wait
        self.locator_orders_tab = self.locator['CHEQ-LOCATOR']['orders_tab']
        self.locator_edit_order_button = self.locator['CHEQ-LOCATOR']['edit_order_button']
        self.locator_cancel_order_button = self.locator['CHEQ-LOCATOR']['cancel_order_button']
        self.locator_cancel_confirmation_button = self.locator['CHEQ-LOCATOR']['cancel_confirmation_button']
        self.locator_start_order_button = self.locator['CHEQ-LOCATOR']['start_order_button']

    def pre_check_order(self, suite):
        self.driver.find_element(By.XPATH, self.locator_orders_tab).click()
        time.sleep(3)
        locators = "//h6[contains(text(), '{suite}')]/following-sibling::div/p[contains(text(), 'New')]".format(suite=suite)
        elements = self.driver.find_elements(By.XPATH, locators)
        total_new_order = len(elements)
        print(total_new_order)
        if total_new_order is not None:
            for i in range(total_new_order):
                locators = "((//h6[contains(text(), 'Suite (South)')]/following-sibling::div/p[contains(text(), " \
                          "'New')])[{count}]/parent::div/preceding-sibling::div/button[text()='View Details'])[1]".format(
                    count=i+1)
                element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators)))
                self.driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top + "
                                           "window.pageYOffset);", element)
                self.driver.find_element(By.XPATH, locators).click()
                self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_edit_order_button)))
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.locator_edit_order_button).click()
                self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_cancel_order_button)))
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.locator_cancel_order_button).click()
                self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_cancel_confirmation_button)))
                self.driver.find_element(By.XPATH, self.locator_cancel_confirmation_button).click()
                self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_start_order_button)))
            time.sleep(4)
            self.driver.find_element(By.XPATH, self.locator_start_order_button).click()
            time.sleep(2)
        else:
            self.driver.find_element(By.XPATH, self.locator_start_order_button).click()
            time.sleep(2)






