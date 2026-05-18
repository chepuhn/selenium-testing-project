from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item_name")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BUTTON)

    def open_cart(self):
        self.click(self.CART_LINK)

    def sort_by_name_z_to_a(self):
        select = Select(self.find(self.SORT_SELECT))
        select.select_by_value("za")

    def get_product_names(self):
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return [item.text for item in items]

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)