from selenium.webdriver.common.by import By

class Locators:
    # Scenario 1
    FIRST_NAME = (By.NAME, "firstname")
    LAST_NAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    MESSAGE = (By.NAME, "message")
    ACCEPT_TC = (By.ID, "accept-terms-checkbox")
    SEND_BUTTON = (By.XPATH, "//input[@value='SEND']")
    TERMS_ERROR_MESSAGE = (By.XPATH, "//div[@class='legal-consent-container']//label[contains(@class, 'hs-error-msg')]")
    MISSING_REQ_FIELDS_ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'hs_error_rollup')]//label")

    # Scenario 2
    CUSTOMER_PAGE = (By.LINK_TEXT, "Customers")
    ASML_IMAGE = (By.XPATH, "//img[@alt='ASML logo small']")
    ASML_CUSTOMER = (By.XPATH, "//div[contains(text(), 'ASML')]")

    # Scenario 3
    RESOURCES_MENU = (By.XPATH, "//a[text()='Resources']")
    SUCCESS_STORIES = (By.XPATH, "//a[text()='Success Stories']")
    GET_IN_TOUCH_BUTTON = (By.XPATH, "//span[text()='Get in touch']")

    # Scenario 4
    CAREERS_BUTTON = (By.LINK_TEXT, "Careers")
    TECHNOLOGY_DROPDOWN = (By.XPATH, "//select[@class='facetwp-dropdown']")
    QA_OPTION = (By.XPATH, "//option[contains(text(), 'Quality Assurance')]")
    QA_POSITIONS = (By.XPATH, "//a[contains(text(), 'Automation Quality Assurance Engineer')]")

    # Scenario 5
    ABOUT_ICT_GROUP = (By.LINK_TEXT, "About ICT Group")
    GO_TO_ICT_GROUP_SITE = (By.LINK_TEXT, "GO TO ICT GROUP WEBSITE")
