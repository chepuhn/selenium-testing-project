from unittest.mock import patch
from pages import checkout_page


def fake_failed_payment():
    return False


@patch("pages.checkout_page.process_payment", side_effect=fake_failed_payment)
def test_payment_should_be_successful(mock_payment):
    result = checkout_page.process_payment()

    # намеренно неправильная проверка для демонстрации ошибки
    assert result is True