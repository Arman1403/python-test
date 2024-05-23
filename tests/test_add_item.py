from time import sleep

import pytest

from pages.main_page import MainPage
from tests.test_authorization import authorization
import allure


def test_add_item(browser, authorization):
    main_page = MainPage(browser)
    print("THis is/n" + main_page.backpack_add_button().text)
    main_page.backpack_add_button_click()
    main_page.cart_button_click()
