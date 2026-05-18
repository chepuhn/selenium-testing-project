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
        # ВАЖНО — ждём, что точно попали на страницу checkout
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-one")
        )

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )

        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)

        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", continue_button)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FINISH_BUTTON)
        )

    def finish_order(self):
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", finish_button)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.COMPLETE_HEADER)
        )

    def get_complete_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.COMPLETE_HEADER)
        ).text