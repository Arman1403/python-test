from time import sleep
from pages.authorization_page import AuthorizationPage
import allure


def test_authorization(browser):
    authorization_page = AuthorizationPage(browser)
    authorization_page.open()

    authorization_page.username_send()
    sleep(5)
    authorization_page.password_send()
    sleep(5)
    authorization_page.login_button().click()
    sleep(5)
