from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item_name")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def wait_for_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.INVENTORY_CONTAINER)
        )

    def add_backpack_to_cart(self):
        self.wait_for_page()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_BACKPACK_BUTTON)
        )
        self.click(self.ADD_BACKPACK_BUTTON)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.REMOVE_BACKPACK_BUTTON)
        )

    def open_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        self.click(self.CART_LINK)

    def sort_by_name_z_to_a(self):
        self.wait_for_page()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SORT_SELECT)
        )
        select = Select(self.find(self.SORT_SELECT))
        select.select_by_value("za")

    def get_product_names(self):
        self.wait_for_page()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.INVENTORY_ITEMS)
        )
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return [item.text for item in items]

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )
        self.click(self.MENU_BUTTON)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        )
        self.click(self.LOGOUT_LINK)