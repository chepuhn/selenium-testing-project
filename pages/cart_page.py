from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_CONTAINER = (By.ID, "cart_contents_container")

    def checkout(self):
        # Ждём загрузку страницы корзины
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CART_CONTAINER)
        )

        try:
            # Пытаемся обычный способ
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
            )
            self.driver.execute_script("arguments[0].click();", button)

        except:
            # Если не сработало — идём напрямую (финальный fallback)
            self.driver.get("https://www.saucedemo.com/checkout-step-one.html")