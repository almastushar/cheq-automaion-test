import ast
import configparser

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


class TestCheqValidData:
    td = Data()
    testdata = td.data()
    data = ast.literal_eval(testdata['CHEQ-DATA']['valid_data'])

    @pytest.mark.order(1)
    @pytest.mark.regression
    @pytest.mark.sanity
    @logger.catch(onerror=lambda _: sys.exit(1))
    def test_e2e_with_valid_data(self, driver, config, wait):
        # Successful Login
        login = LOGIN(driver, config, wait)
        print("Navigate to login page")
        login.navigate_to_login_page()
        login.login(email=self.data['email'], password=self.data['password'])
        assert login.verify_successful_login(self.data['verify_login']) is True, \
            "User unable to logged In."

        # Event Date selection
        date_selection = DateSelection(driver, wait)
        print("Select Date")
        date_selection.select_date(date=self.data['date'], suite=self.data['suite_name'])
        assert date_selection.verify_date_selection() is True, \
            "Date is not selected."

        # Choose Event
        choose_event = ChooseEvent(driver, wait)
        print("Choose event and continue")
        choose_event.choose_event(self.data['event_name'])
        assert choose_event.verify_chosen_event(self.data['verify_chosen_event']) is True, \
            "Failed to choose event."

        # Suite Selection
        suite_selection = SuiteSelection(driver, wait)
        print("Select Suite and continue")
        suite_selection.select_suite(self.data['suite_name'])
        assert suite_selection.verify_suite_selection(self.data['verify_suite_selection']) is True, \
            "Failed to select Suite."

        # Save Suite Preferences
        suite_preferences = SuitePreferences(driver, wait)
        print("Save default Suite Preferences")
        suite_preferences.save_suite_preferences()
        assert suite_preferences.verify_suite_preferences(self.data['verify_suite_preferences']) is True, \
            "Failed to save Suite Preferences."

        # Add to Cart and View Cart
        add_to_cart = AddToCart(driver, wait)
        print("Add items to Cart")
        add_to_cart.add_items_to_cart()
        print("View items in Cart")
        order_total = add_to_cart.view_cart()
        assert add_to_cart.verify_view_cart(self.data['verify_add_to_cart']) is True, \
            "Failed to add items in Cart."

        # Pre Order using Credit Card
        pre_order = PreOrder(driver, wait)
        print("Save Pre Order")
        pre_order.save_pre_order()
        print("Select Credit Card")
        pre_order.select_credit_card()
        assert pre_order.verify_credit_card_selection(self.data['verify_sub_total'], order_total) is True, \
            "Failed to select credit card."

        # Complete the order
        complete_order = CreditCardDetails(driver, wait)
        print("Input Credit Card Details")
        complete_order.input_cc_details(card_number=self.data['card_number'], expiry_date=self.data['expiry_date'], cvc=self.data['cvc'], name_on_card=self.data['name_on_card'])
        assert complete_order.verify_completed_order(self.data['verify_order_completed']) is True, \
            "Failed to complete the order."
