from tests.base_test import BaseTest

from time import sleep
import unittest

class SingInTest(BaseTest):
    """
    Sing In Tests
    """

    def test_negativ_log(self):
        """
        TC 004 : Użytkownik wpisuje złe hasło przy logowaniu
        """
        home_page = self.home_page
        # 1. Kliknij Sign In
        authentication_page = home_page.click_sign_in()
        # 2. Wpisz e-mail
        # 3. Kliknij przycisk „sing in”
        log_an_account_page = authentication_page.log_in(self.test_data.logemail, self.test_data.fakpassword)
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „Authentication failed.”
        errors = ["Authentication failed."]
        self.assertCountEqual(authentication_page.error_messages_authe_texts(), errors)

        """
        TC 004.1 : Użytkownik wpisuje poprawne hasło przy logowaniu
        """
        # kliknij w pole hasłoi wpisz poprawne hasło
        log_an_account_page = authentication_page.log_in_pass(self.test_data.goodpassword)

        # Oczekiwany rezultat:
        # 1. Użytkownik zalogowany na formatce "My account"
        correct1 = 'MY ACCOUNT'
        self.assertEqual(create_an_account_page.verify_page(), correct1)

        sleep(12)








