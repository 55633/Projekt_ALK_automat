from tests.base_test import BaseTest
from time import sleep
import unittest

class SingInTest(BaseTest):
    """
    Sing In Tests
    """
    def verify_error_messages(self, errors):
        """
        weryfikacja błędu wyświetlanego użytkownikowi(["firstname is required"])
        """
        pass

    def test_no_name(self):
        """
        TC 004 : Użytkownik wpisuje złe hasło przy logowaniu
        """
        home_page = self.home_page
        # 1. Kliknij Sign In
        authentication_page = home_page.click_sign_in()
        # 2. Wpisz e-mail
        # 3. Kliknij przycisk „sing in”
        create_an_account_page = authentication_page.log_in(self.test_data.logemail, self.test_data.fakpassword)

        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „Authentication failed.”
        errors = ["Authentication failed."]
        self.assertCountEqual(authentication_page.error_messages_authe_texts(), errors)

        sleep(5)








