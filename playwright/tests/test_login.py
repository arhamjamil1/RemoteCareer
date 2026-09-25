import pytest
from pages.login_page import LoginPage


def test_open_login_page(page):
    login_page = LoginPage(page)

    login_page.open()

    assert page.title() == "Swag Labs"

    login_page.login("standard_user", "secret_sauce")

    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert page.locator(".title").inner_text() == "Products"


def test_logout(logged_in_page):
    login_page = LoginPage(logged_in_page)

    login_page.logout()

    assert logged_in_page.url == "https://www.saucedemo.com/"

import pytest


@pytest.mark.parametrize(
    "username,password,should_login",
    [
        ("standard_user", "secret_sauce", True),
        ("standard_user", "wrong_password", False),
    ]
)
def test_login_scenarios(page, username, password, should_login):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    if should_login:
        assert page.url.endswith("/inventory.html")
    else:
        assert login_page.is_error_visible()