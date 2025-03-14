from selenium.webdriver.common.by import By

from locators.locators import Locators
import time
from selenium.webdriver.support import expected_conditions as EC

from pages.order_pre_check import OrderPreCheck


class DateSelection:
    def __init__(self, driver, wait):
        self.locators = Locators()
        self.locator = self.locators.locator()
        self.driver = driver
        self.wait = wait
        self.locator_verify_date_selection = self.locator['CHEQ-LOCATOR']['date_selection']

    def select_date(self, date, suite):
        pre_check = OrderPreCheck(self.driver, self.wait)
        pre_check.pre_check_order(suite)
        locator = "//button[text()='{date}']".format(date=date)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        self.driver.find_element(By.XPATH, locator).click()

    def verify_date_selection(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_verify_date_selection)))
        elem = self.driver.find_element(By.XPATH, self.locator_verify_date_selection).is_displayed()
        return elem



