from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    BACKPACK_ITEM = (By.XPATH, "//div[text()='Sauce Labs Backpack']")

    def is_backpack_in_cart(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.BACKPACK_ITEM)
        ).is_displayed()

    def checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        self.click(self.CHECKOUT_BUTTON)