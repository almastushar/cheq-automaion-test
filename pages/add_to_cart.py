import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class AddToCart:
    def __init__(self, driver, wait):
        self.locators = Locators()
        self.locator = self.locators.locator()
        self.driver = driver
        self.wait = wait
        self.locator_category = self.locator['CHEQ-LOCATOR']['category']
        self.locator_add_to_order_button = self.locator['CHEQ-LOCATOR']['add_to_order_button']
        self.locator_view_cart_button = self.locator['CHEQ-LOCATOR']['view_cart_button']
        self.locator_save_pre_order_button = self.locator['CHEQ-LOCATOR']['save_pre_order_button']
        self.locator_verify_add_to_cart = self.locator['CHEQ-LOCATOR']['verify_title']
        self.locator_order_amount = self.locator['CHEQ-LOCATOR']['order_amount']

    def add_items_to_cart(self):
        elements = self.driver.find_elements(By.XPATH, self.locator_category)
        total_category = len(elements)
        for i in range(total_category):
            locator = "(//h2/following::button[1])[{count}]".format(
                count=i+1)
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//h2)[{count}]".format(
                count=i+1))))
            self.driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top + "
                                       "window.pageYOffset);", element)
            self.driver.find_element(By.XPATH, locator).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_add_to_order_button)))
            self.driver.find_element(By.XPATH, self.locator_add_to_order_button).click()
            time.sleep(3)

    def view_cart(self):
        self.driver.find_element(By.XPATH, self.locator_view_cart_button).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator_save_pre_order_button)))
        order_total = self.driver.find_element(By.XPATH, self.locator_order_amount).text
        return order_total

    def verify_view_cart(self, verify_add_to_cart_text):
        elem = self.driver.find_element(By.XPATH, self.locator_verify_add_to_cart).text == verify_add_to_cart_text
        return elem



