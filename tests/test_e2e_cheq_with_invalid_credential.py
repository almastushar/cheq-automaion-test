import ast

from loguru import logger

from pages.add_to_cart import AddToCart
from pages.choose_event import ChooseEvent
from pages.date_selection import DateSelection
from pages.input_credit_card_details import CreditCardDetails
from pages.login import LOGIN
from pages.pre_order import PreOrder
from pages.suite_preferences import SuitePreferences
from pages.suite_selection import SuiteSelection
from utils.datareader import Data
import sys
import pytest


class TestCheqInvalidCredential:
    td = Data()
    testdata = td.data()
    data = ast.literal_eval(testdata['CHEQ-DATA']['invalid_data_credential'])

    @pytest.mark.order(2)
    @pytest.mark.regression
    @logger.catch(onerror=lambda _: sys.exit(1))
    def test_e2e_with_invalid_credential(self, driver, config, wait):
        # Unsuccessful Login
        login = LOGIN(driver, config, wait)
        print("Navigate to login page")
        login.navigate_to_login_page()
        login.login(email=self.data['email'], password=self.data['password'])
        assert login.verify_unsuccessful_login_for_invalid_credential(self.data['verify_login_invalid_credential']) is True, \
            "User logged in."

    @pytest.mark.order(3)
    @pytest.mark.regression
    @logger.catch(onerror=lambda _: sys.exit(1))
    def test_e2e_with_invalid_pass_least_characters(self, driver, config, wait):
        # Unsuccessful Login
        login = LOGIN(driver, config, wait)
        print("Navigate to login page")
        login.navigate_to_login_page()
        login.login(email=self.data['email'], password=self.data['least_password'])
        assert login.verify_unsuccessful_login_for_least_pass_character(self.data['verify_login_invalid_pass_characters']) is True, \
            "User logged in."

    @pytest.mark.order(4)
    @pytest.mark.regression
    @logger.catch(onerror=lambda _: sys.exit(1))
    def test_e2e_with_blank_email_pass(self, driver, config, wait):
        # Unsuccessful Login
        login = LOGIN(driver, config, wait)
        print("Navigate to login page")
        login.navigate_to_login_page()
        login.login(email=self.data['blank_email'], password=self.data['blank_password'])
        assert login.verify_unsuccessful_login_for_blank_credential(
            self.data['verify_login_blank_email'], self.data['verify_login_blank_password']) is True, \
            "User logged in."