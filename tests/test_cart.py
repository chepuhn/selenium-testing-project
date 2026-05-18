from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    driver.save_screenshot("screenshots/04_product_added.png")

    inventory_page.open_cart()
    driver.save_screenshot("screenshots/05_cart_page.png")

    assert cart_page.get_cart_items_count() == 1