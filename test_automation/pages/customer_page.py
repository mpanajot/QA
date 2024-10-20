from pages.base_page import BasePage
from pages.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CustomerPage(BasePage):
    def open_asml_customer(self):
        customer_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(Locators.CUSTOMER_PAGE)
        )
        customer_button.click()

        asml_image = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.ASML_IMAGE)
        )
        action = ActionChains(self.driver)
        action.move_to_element(asml_image).perform()
        asml_customer_link = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(Locators.ASML_CUSTOMER)
        )
        asml_customer_link.click()

    def is_asml_page_loaded(self):
        WebDriverWait(self.driver, self.timeout).until(lambda driver: "ASML" in driver.title)
        return "ASML" in self.driver.title
