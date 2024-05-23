from selenium.webdriver.common.by import By
from pages.base_page import BasePage

backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
cart = (By.XPATH, '//a[@class="shopping_cart_link"]')


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def backpack_add_button(self):
        return self.find(backpack)

    def backpack_add_button_click(self):
        return self.find(backpack).click()

    def cart_button(self):
        return self.find(cart)

    def cart_button_click(self):
        return self.find(cart).click()