from tests.base_test import BaseTest


class RegistrationTest(BaseTest):
    """
    Registration Tests
    """


    def test_registration_no_firstname(self):
        """
        TC 001 : Użytkowmnik nie uzupełnia pola:First name
        """
        home_page = self.home_page
        # 1. Kliknij Sign In
        authentication_page = home_page.click_sign_in()
        # 2. Wpisz e-mail
        # 3. Kliknij przycisk „Create account”
        create_an_account_page = authentication_page.create_account_with_email(self.test_data.email)
        # 4. Wybierz płeć
        create_an_account_page.choose_gender(self.test_data.gender)
        # 5. Wpisz nazwisko
        create_an_account_page.enter_last_name(self.test_data.last_name)
        # 6. Sprawdź poprawność e-maila
        self.assertEqual(create_an_account_page.get_email(), self.test_data.email, "Mail differs from entered previously!")
        # 7. Wpisz hasło
        create_an_account_page.enter_password(self.test_data.password)
        # 8. Wybierz datę urodzenia
        create_an_account_page.choose_birthdate(self.test_data.birthdate)
        # 9. Sprawdź pole „First name”
        self.assertEqual(create_an_account_page.get_first_name(), "")
        # 10. Sprawdź pole „Last name”
        self.assertEqual(create_an_account_page.get_last_name(), self.test_data.last_name)
        # 11. Wpisz adres
        create_an_account_page.enter_address(self.test_data.address)
        # 12. Wpisz miasto
        create_an_account_page.enter_city(self.test_data.city)
        # 13. Wpisz kod pocztowy
        create_an_account_page.enter_postal_code(self.test_data.postal_code)
        # 14. Wybierz stan
        create_an_account_page.choose_state(self.test_data.state)
        # 15. Wpisz nr telefonu komórkowego
        create_an_account_page.enter_mobile_phone(self.test_data.phone)
        # 16. Wpisz alias adresu
        create_an_account_page.enter_address_alias(self.test_data.alias)
        # 17. Kliknij Register
        create_an_account_page.click_register_btn()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „firstname is required”
        errors = ["firstname is required."]
        self.assertCountEqual(create_an_account_page.get_error_messages_visible_texts(), errors)