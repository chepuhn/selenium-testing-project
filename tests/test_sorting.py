from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_sort_products_z_to_a(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.sort_by_name_z_to_a()
    driver.save_screenshot("screenshots/09_sorting_z_to_a.png")

    product_names = inventory_page.get_product_names()
    assert product_names == sorted(product_names, reverse=True)