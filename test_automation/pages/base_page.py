from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20  # Increased timeout to 20 seconds

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click(self, *locator):
        self.find_element(*locator).click()

    def enter_text(self, text, *locator):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def is_element_visible(self, *locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return True if element.is_displayed() else False
        except:
            return False

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )