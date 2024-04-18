from time import sleep
from pages.authorization_page import AuthorizationPage
import allure


@allure.feature('Authorization')
@allure.story('Authorization to the system')
@allure.description('This test will run test of website authorization')
def test_authorization(browser):
    with allure.step('Open browser'):
        authorization_page = AuthorizationPage(browser)
    with allure.step('Go to site'):
        authorization_page.open()
    with allure.step('Write username'):
        authorization_page.username_send()
        sleep(1)
    with allure.step('Write password'):
        authorization_page.password_send()
        sleep(1)
    with allure.step('Click button'):
        authorization_page.login_button().click()
        sleep(1)


def test_button_check(browser):
    with allure.step('Open browser'):
        authorization_page = AuthorizationPage(browser)
    with allure.step('Go to site'):
        authorization_page.open()
    with allure.step('Click button'):
        assert authorization_page.login_button().is_displayed()
        sleep(1)
