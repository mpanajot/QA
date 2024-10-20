from pages.contact_page import ContactPage

def test_send_message_without_tc(driver):
    contact_page = ContactPage(driver)
    contact_page.load_contact_page()
    contact_page.send_message("Martin", "Panajotov", "martin.panajotov@yahoo.com", "Test message", accept_tc=False)

    assert "Please complete this required field." in contact_page.get_terms_and_conditions_error_message()
    assert "Please complete all required fields." in contact_page.get_missing_required_fields_error_message()
