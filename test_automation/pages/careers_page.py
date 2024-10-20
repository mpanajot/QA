from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators
from selenium.webdriver.support.select import Select


class CareersPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_careers(self):
        careers_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(Locators.CAREERS_BUTTON)
        )
        careers_button.click()

    def select_qa_positions(self):
        self.driver.execute_script("window.scrollBy(0, 300);")
        technology_dropdown = Select(WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(Locators.TECHNOLOGY_DROPDOWN)
        ))
        technology_dropdown.select_by_value('quality-assurance')

    def is_single_qa_position_displayed(self):
        qa_positions = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located(Locators.QA_POSITIONS)
        )
        return len(qa_positions) == 1