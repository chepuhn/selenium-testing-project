from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items_count(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.CART_ITEMS)
        )
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        self.click(self.CHECKOUT_BUTTON)