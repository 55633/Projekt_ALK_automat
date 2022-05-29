from selenium.webdriver.common.by import By

class HomePageLocators():
    """
    Locators used on Home Page
    """
    SIGN_IN_LINK = (By.CLASS_NAME, "login")
    SEARCH_POINT = (By.ID, "search_query_top")
    SEARCH_BTN = (By.NAME, "submit_search")
    CONTACT_US_LINK = (By.ID, "contact-link")

class AuthenticationPageLocators():
    """
    Locators used on Authentication Page
    """
    CREATE_AN_ACCOUNT_EMAIL = (By.ID, "email_create")
    CREATE_AN_ACCOUNT_BTN = (By.ID, "SubmitCreate")
    SING_IN_EMAIL = (By.ID, "email")
    SING_IN_PASSWORD = (By.ID, "passwd")
    SING_IN_BTN = (By.ID, "SubmitLogin")
    ERROR_MESSAGES1 = (By.XPATH, "//li[contains(text(), 'Authentication failed.')]")

class CreateAnAccountPageLocators():
    """
    Locators used on Create an Account Page
    """
    GENDER_MALE = (By.ID, "id_gender1")
    GENDER_FEMALE = (By.ID, "id_gender2")
    FIRST_NAME = (By.ID, "customer_firstname")
    LAST_NAME = (By.ID, "customer_lastname")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    BIRTHDATE_DAY = (By.ID, "days")
    BIRTHDATE_MONTH = (By.ID, "months")
    BIRTHDATE_YEAR = (By.ID, "years")
    ADDRESS_FIRST_NAME = (By.ID, "firstname")
    ADDRESS_LAST_NAME = (By.ID, "lastname")
    ADDRESS = (By.ID, "address1")
    CITY = (By.ID, "city")
    STATE = (By.ID, "id_state")
    POSTAL_CODE = (By.ID, "postcode")
    MOBILE_PHONE = (By.ID, "phone_mobile")
    ADDRESS_ALIAS = (By.ID, "alias")
    REGISTER_BTN = (By.ID, "submitAccount")
    NUMBER_OF_ERRORS_MESSAGE = (By.XPATH, '//div[@class="alert alert-danger"]/p')
    ERROR_MESSAGES = (By.XPATH, '//div[@class="alert alert-danger"]/ol/li')
    #MY_ACCOUNT_MESSAGE = (BY.XPATH, '//p[@class="info-account"]')
    MY_ACCOUNT_MESSAGE = (By.XPATH, "//h1[contains(text(),'My account')]")


class ProduktsLocators():
    FIRST_PROD = (By.XPATH, "//span[contains(text(),'More')]")
    PROD_NAME_P = (By.XPATH, "//body/div[@id='page']/div[2]/div[1]/div[3]/div[2]/ul[1]/li[1]/div[1]/div[2]/h5[1]/a[1]")
    ADD_BTN = (By.XPATH, "//span[contains(text(),'Add to cart')]")
    BASKET_BTN = (By.XPATH, "//body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[4]/div[1]/div[2]/div[4]/a[1]/span[1]")
    IN_BASKET_PROD_NAME = (By.XPATH, "//h1[contains(text(),'Faded Short Sleeve T-shirts')]")

class MessageLocators():
    SUBJECT_HEADING = (By.ID, "id_contact")
    MESSAGE_EMAIL = (By.XPATH, "//input[@id='email']")
    ID_ORDER = (By.ID, "id_order")
    SEND_MESSAGE_BTN = (By.ID, "submitMessage")
    MESSAGE_AREA = (By.XPATH, "//textarea[@id='message']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
