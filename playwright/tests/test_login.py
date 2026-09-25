from pages.login_page import LoginPage


def test_open_login_page(page):
    login_page = LoginPage(page)

    login_page.open()

    assert page.title() == "Swag Labs"

    login_page.login("standard_user", "secret_sauce")

    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert page.locator(".title").inner_text() == "Products"


def test_logout(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    login_page.logout()

    assert page.url == "https://www.saucedemo.com/"