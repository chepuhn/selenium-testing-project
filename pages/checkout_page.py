from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_user_data(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )

        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)

        self.click(self.CONTINUE_BUTTON)

        # ВАЖНО — ждём следующую страницу
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-two")
        )

    def finish_order(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )

        self.driver.execute_script("arguments[0].click();", button)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.COMPLETE_HEADER)
        )