import pytest

from pages.products_page import ProductsPage
from test_data.login_data import LOGIN_TEST_DATA


def test_open_login_page(login_page):
    login_page.open()

    assert login_page.get_page_title() == "Swag Labs"

    login_page.login()

    assert login_page.get_current_url().endswith("/inventory.html")

    products_page = ProductsPage(login_page.page)
    assert products_page.get_title() == "Products"


def test_logout(logged_in_page):
    logged_in_page.logout()

    assert logged_in_page.get_current_url() == "https://www.saucedemo.com/"


@pytest.mark.parametrize(
    "username,password,should_login",
    LOGIN_TEST_DATA
)
def test_login_scenarios(login_page, username, password, should_login):

    login_page.open()
    login_page.login(username, password)

    if should_login:
        assert login_page.get_current_url().endswith("/inventory.html")
    else:
        assert login_page.is_error_visible()