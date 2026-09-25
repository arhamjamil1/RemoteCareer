from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def test_open_login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        assert page.title() == "Swag Labs"

        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")
        
        assert page.url == "https://www.saucedemo.com/inventory.html"
        assert page.locator(".title").inner_text() == "Products"

        browser.close()

def test_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        login_page.logout()

        assert page.url == "https://www.saucedemo.com/"

        browser.close()