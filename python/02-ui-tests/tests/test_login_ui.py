import pytest

from pages.login_page import LoginPage


pytestmark = pytest.mark.ui


def test_successful_login_shows_welcome_message(page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login("qa@example.com", "correct-password")

    login_page.expect_message("Welcome back")


def test_invalid_login_shows_error_message(page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login("qa@example.com", "wrong-password")

    login_page.expect_message("Invalid credentials")
