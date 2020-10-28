from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # initialize Page Object, giving browser and url as parameters to constructor
    page.open()
    page.should_be_login_link()
