from playwright.sync_api import sync_playwright


def test_products_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        assert page.locator(".title").inner_text() == "Products"

        products = page.locator(".inventory_item")

        assert products.count() > 0

        browser.close()