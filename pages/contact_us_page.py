from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from pages.locators import MessageLocators

class ContactUsPage(BasePage):
    """
    Create an account Page Object
    """

    def subject_heading(self, subject):

        el = Select(self.driver.find_element(*MessageLocators.SUBJECT_HEADING))
        el.select_by_visible_text(subject)

    def put_email(self, email):

        """
        Enter email
        """
        el = self.driver.find_element(*MessageLocators.MESSAGE_EMAIL)
        el.click()
        el.send_keys(email)

        #el = self.driver.find_element(*MessageLocators.MESSAGE_EMAIL)

        #return el.get_attribute("value")

    def order_reference(self, order_no):
        """
        Enters order number
        """
        el = self.driver.find_element(*MessageLocators.ID_ORDER)
        el.click()
        el.send_keys(order_no)

    def message_text(self, words):
        """
        Enters text
        """
        el = self.driver.find_element(*MessageLocators.MESSAGE_AREA)
        el.click()
        el.send_keys(words)

    def send_msg_btn(self):
        # znajdź przycisk SEND
        el5 = self.driver.find_element(*MessageLocators.SEND_MESSAGE_BTN)
        # Click this button
        el5.click()


    def verify_page(self):
        """
        Verifies Send Message
        """
        success = self.driver.find_element(*MessageLocators.SUCCESS_MESSAGE)
        #print(success.text)
        return success.text
