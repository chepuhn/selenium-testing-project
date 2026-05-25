from unittest.mock import patch
from pages import checkout_page


def fake_success_payment():
    return True


def fake_failed_payment():
    return False


@patch("pages.checkout_page.process_payment", side_effect=fake_success_payment)
def test_payment_success(mock_payment):
    result = checkout_page.process_payment()
    assert result is True


@patch("pages.checkout_page.process_payment", side_effect=fake_failed_payment)
def test_payment_failed(mock_payment):
    result = checkout_page.process_payment()
    assert result is False