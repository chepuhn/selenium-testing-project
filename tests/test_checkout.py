from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_order(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.checkout()

    driver.save_screenshot("screenshots/06_checkout_form.png")

    checkout_page.fill_user_data("Ivan", "Ivanov", "443000")
    driver.save_screenshot("screenshots/07_checkout_overview.png")

    checkout_page.finish_order()
    driver.save_screenshot("screenshots/08_order_complete.png")

    assert checkout_page.get_complete_message() == "Thank you for your order!"