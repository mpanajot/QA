from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators


class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def load_contact_page(self):
        self.driver.get("https://ict-strypes.com/contact")

    def send_message(self, first_name, last_name, email, message, accept_tc=False):
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(Locators.FIRST_NAME))

        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*Locators.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*Locators.EMAIL).send_keys(email)
        self.driver.find_element(*Locators.MESSAGE).send_keys(message)

        if accept_tc:
            self.driver.find_element(*Locators.ACCEPT_TC).click()
        self.driver.find_element(*Locators.SEND_BUTTON).click()

    def get_terms_and_conditions_error_message(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(Locators.TERMS_ERROR_MESSAGE)
        ).text
        
    def get_missing_required_fields_error_message(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(Locators.MISSING_REQ_FIELDS_ERROR_MESSAGE)
        ).text