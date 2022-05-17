from pages.base_page import BasePage
from pages.locators import AuthenticationPageLocators
from pages.create_an_account_page import CreateAnAccountPage


class AuthenticationPage(BasePage):
    """
    Authentication Page Object
    """
    def create_account_with_email(self, email):
        """
        Creates an account with email and returns CreateAnAccountPage instance
        """
        # Find Create an Account E-mail input
        el = self.driver.find_element(*AuthenticationPageLocators.CREATE_AN_ACCOUNT_EMAIL)
        # Fill this input with email
        el.send_keys(email)
        # Find Create an Account button
        el2 = self.driver.find_element(*AuthenticationPageLocators.CREATE_AN_ACCOUNT_BTN)
        # Click this button
        el2.click()
        # return CreateAnAccountPage instance
        return CreateAnAccountPage(self.driver)

    def log_in(self, email, password1):
        """
     Logowanie za pomocą wcześniej utworzonego loginu i hasła
        """
        # Znajdź pole Email Adress w sekcji logowania
        el3 = self.driver.find_element(*AuthenticationPageLocators.SING_IN_EMAIL)
        # Fill this input with email
        el3.send_keys(email)
        # Znajdź pole Hasło  w sekcji logowania
        el4 = self.driver.find_element(*AuthenticationPageLocators.SING_IN_PASSWORD)
        # Fill this input with email
        el4.send_keys(password1)
        # znajdź przycisk Sing IN
        el5 = self.driver.find_element(*AuthenticationPageLocators.SING_IN_BTN)
        # Click this button
        el5.click()
        # return CreateAnAccountPage instance
        #return CreateAnAccountPage(self.driver)


    def error_messages_authe_texts(self):
        """
        Returns all user errors
        """
        # Znajduję wszystkie błędy - lista WebElementów
        errors = self.driver.find_elements(*AuthenticationPageLocators.ERROR_MESSAGES1)
        error_texts = []
        # Iteruję po liście webelementów
        for e in errors:
            # Dodaję do listy widoczny tekst
            error_texts.append(e.text)
        return error_texts

    def log_in_pass(self, password2):
        """
     Logowanie za pomocą wcześniej utworzonego loginu i hasła poprawne
        """
        # Znajdź pole Email Adress w sekcji logowania
        #el3 = self.driver.find_element(*AuthenticationPageLocators.SING_IN_EMAIL)
        # Fill this input with email
        #el3.send_keys(email)
        # Znajdź pole Hasło  w sekcji logowania
        el4 = self.driver.find_element(*AuthenticationPageLocators.SING_IN_PASSWORD)
        # wyczyść pole hasło  dopisać

        # Fill this input with email
        el4.send_keys(password2)
        # znajdź przycisk Sing IN
        el5 = self.driver.find_element(*AuthenticationPageLocators.SING_IN_BTN)
        # Click this button
        el5.click()
        # return CreateAnAccountPage instance
        #return CreateAnAccountPage(self.driver)







    def input_email_in_create_account(self, email):
        pass

    def click_create_an_account(self):
        pass



    def _verify_page(self):
        """
        Verifies Authentication Page
        """
        pass