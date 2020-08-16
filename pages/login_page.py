from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_login_page()
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        input_password.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        submit_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),\
            "Register form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL),\
            "Registration email textbox is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD),\
            "Registration password textbox is not presented"
        assert self.is_element_present(*LoginPageLocators.CONFIRM_PASSWORD),\
            "Confirmation password textbox is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUBMIT_BUTTON),\
            "Registration submit button is not presented"
