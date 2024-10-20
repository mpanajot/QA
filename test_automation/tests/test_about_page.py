from pages.about_page import AboutPage

def test_go_to_ict_group_link_visible(driver):
    about_page = AboutPage(driver)
    about_page.go_to_about_page()
    assert about_page.is_go_to_ict_group_link_visible(), "Go to ICT Group link is not visible"
