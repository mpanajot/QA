from pages.careers_page import CareersPage

def test_single_qa_position_displayed(driver):
    careers_page = CareersPage(driver)
    careers_page.navigate_to_careers()
    careers_page.select_qa_positions()
    assert careers_page.is_single_qa_position_displayed(), "More than one QA position is displayed"




