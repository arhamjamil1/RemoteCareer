import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        yield page

        browser.close()

@pytest.fixture
def logged_in_page(page):
    from pages.login_page import LoginPage

    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    return page