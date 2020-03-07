from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main>h1')
    MESSAGE_PRODUCT_TITLE = (By.CSS_SELECTOR, '#messages .alertinner>strong')
    MESSAGE_COST_BASKET = (By.CSS_SELECTOR, '#messages .alertinner>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success')
