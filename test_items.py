def test_store_page(browser):
    length_text_of_the_button = len(browser.find_element_by_css_selector(".btn-add-to-basket").text)
    assert length_text_of_the_button > 0, "The button is not present"
