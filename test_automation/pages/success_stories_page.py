from pages.base_page import BasePage
from pages.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SuccessStoriesPage(BasePage):
    def go_to_success_stories(self):
        self.wait_for_page_to_load()
        resources_menu = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(Locators.RESOURCES_MENU)
        )
        resources_menu.click()
        time.sleep(2)
        success_stories_link = None
        try:
            success_stories_link = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(Locators.SUCCESS_STORIES)
            )
            success_stories_link.click()
        except:
            if success_stories_link:
                ActionChains(self.driver).click(success_stories_link).perform()
            else:
                print("Success Stories link could not be located.")

    def is_get_in_touch_button_visible(self):
        time.sleep(2)
        try:
            get_in_touch_button = WebDriverWait(self.driver, self.timeout + 30).until(
                EC.visibility_of_element_located(Locators.GET_IN_TOUCH_BUTTON)
            )
            ActionChains(self.driver).scroll_to_element(get_in_touch_button).perform()
            time.sleep(2)  # Give time for scroll
            return get_in_touch_button.is_displayed()
        except Exception as e:
            print(f"Exception in locating 'Get in Touch' button: {str(e)}")
            return False