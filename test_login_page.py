from .pages.login_page import LoginPage


link = 'http://selenium1py.pythonanywhere.com/accounts/login/'

def test_login_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()