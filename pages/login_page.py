from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_register_form()
        email_field = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        password1_field = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD1)
        password1_field.send_keys(password)
        password2_field = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD2)
        password2_field.send_keys(password)
        password1_field = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_BUTTON)
        password1_field.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализована проверка на корректный url адрес
        assert "login" in self.browser.current_url, "This is not a login URL"

    def should_be_login_form(self):
        # реализована проверка, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализована проверка, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"
