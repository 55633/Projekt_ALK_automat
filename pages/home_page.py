from pages.base_page import BasePage
from pages.locators import HomePageLocators
from pages.authentication_page import AuthenticationPage
from pages.contact_us_page import ContactUsPage


class HomePage(BasePage):
    """
    Landing Page Object
    """
    def click_sign_in(self):
        """
        Clicks Sign In link and returns AuthenticationPage instance
        """
        # Zlokalizuj Sign In
        el = self.driver.find_element(*HomePageLocators.SIGN_IN_LINK)
        # Kliknij
        el.click()
        # Zwróć kolejną stronę (Authentication Page)
        return AuthenticationPage(self.driver)


    def search_area(self, item):
        """
          wejdźw pole wyszukiwania i wklej produkt
        """
        sa = self.driver.find_element(*HomePageLocators.SEARCH_POINT)
        sa.click()
        sa.send_keys(item)

    def clc_search(self):
        """
         kliknij szukaj
        """
        clk = self.driver.find_element(*HomePageLocators.SEARCH_BTN)
        clk.click()


    def click_contact_us(self):
        """
        Clicks Sign In link and returns AuthenticationPage instance
        """
        # Zlokalizuj contact us
        el = self.driver.find_element(*HomePageLocators.CONTACT_US_LINK)
        # Kliknij
        el.click()
        # Zwróć kolejną stronę (Authentication Page)
        return ContactUsPage(self.driver)



