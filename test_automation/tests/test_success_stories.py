from pages.success_stories_page import SuccessStoriesPage

def test_get_in_touch_button_visible(driver):
    success_stories_page = SuccessStoriesPage(driver)
    success_stories_page.wait_for_page_to_load()
    success_stories_page.go_to_success_stories()
    assert success_stories_page.is_get_in_touch_button_visible(), "Get in touch button is not visible"