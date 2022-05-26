from tests.base_test import BaseTest
from pages.home_page import HomePage
from tests.test_data import TestData
from pages.contact_us_page import ContactUsPage
from time import sleep
import unittest



class SendMessage(BaseTest, ContactUsPage, HomePage):
    """
    Send message test
    """


    def send_message(self):
        """
        TC 005: Wysyłanie wiadomości
        """
        home_page = self.home_page
        # 1. Kliknij Sign In
        contact_us_page = home_page.click_contact_us()
        # 2. wybierz
        contact_us_page.subject_heading(self)

        #3. wpisz maila
        contact_us_page.put_email

        #create_an_account_page.enter_first_name(self.test_data.first_name)
        #create_an_account_page.choose_birthdate(self.test_data.birthdate)


