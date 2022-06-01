from tests.base_test import BaseTest




class SendMessage(BaseTest):
    """
    Send message test
    """


    def test_send_message(self):
        """
        TC 005: Wysyłanie wiadomości
        """
        home_page = self.home_page
        # 1. Kliknij Contact us
        contact_us_page = home_page.click_contact_us()

        # 2. wybierz
        contact_us_page.subject_heading(self.test_data.cus_ser)

        #3. wpisz maila
        contact_us_page.put_email(self.test_data.email)

        #4. wpisz nr zamówinia
        contact_us_page.order_reference(self.test_data.order_no)

        #5. wpisz tekst wiadomosci
        contact_us_page.message_text(self.test_data.text_message)

        # 6. Klikni przycisk wyslij
        contact_us_page.send_msg_btn()

        # 7.Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „Your message has been successfully sent to our team.”
        correct = "Your message has been successfully sent to our team."

        self.assertCountEqual(contact_us_page.verify_page(), correct)