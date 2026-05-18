from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_success_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    driver.save_screenshot("screenshots/01_login_page.png")

    login_page.login("standard_user", "secret_sauce")
    driver.save_screenshot("screenshots/02_success_login.png")

    assert "inventory" in driver.current_url


def test_failed_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("wrong_user", "wrong_password")

    driver.save_screenshot("screenshots/03_failed_login.png")

    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text


def test_logout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.logout()
    driver.save_screenshot("screenshots/10_logout.png")

    assert "saucedemo.com" in driver.current_url