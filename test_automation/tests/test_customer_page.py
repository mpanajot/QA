from pages.customer_page import CustomerPage
import pytest

@pytest.mark.usefixtures("driver")
def test_validate_asml_customer_page_load(driver):
    customer_page = CustomerPage(driver)
    customer_page.open_asml_customer()
    assert customer_page.is_asml_page_loaded(), "ASML customer page not loaded correctly"
