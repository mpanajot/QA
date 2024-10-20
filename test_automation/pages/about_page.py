from pages.base_page import BasePage
from pages.locators import Locators

class AboutPage(BasePage):
    def go_to_about_page(self):
        self.click(*Locators.ABOUT_ICT_GROUP)
        self.scroll_to_element(Locators.GO_TO_ICT_GROUP_SITE)

    def is_go_to_ict_group_link_visible(self):
        return self.is_element_visible(*Locators.GO_TO_ICT_GROUP_SITE)

    def scroll_to_element(self, locator):
        """Scroll to the element specified by the locator."""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)