from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self):
        email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email.send_keys(str(time.time()) + "@fakemail.org")
        password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password.send_keys("VSRATIYPASSWORD13")
        password1 = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        password1.send_keys("VSRATIYPASSWORD13")
        submit = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        submit.click()
