from playwright.sync_api import sync_playwright


def test_open_login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        assert page.title() == "Swag Labs"

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        
        assert page.url == "https://www.saucedemo.com/inventory.html"
        assert page.locator(".title").inner_text() == "Products"

        browser.close()

def test_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        page.click("#react-burger-menu-btn")
        page.click("#logout_sidebar_link")

        assert page.url == "https://www.saucedemo.com/"

        browser.close()