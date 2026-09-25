import os

import pytest
from playwright.sync_api import sync_playwright

from config import Config


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        yield page

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            os.makedirs("test-results", exist_ok=True)
            screenshot_path = f"test-results/{request.node.name}.png"
            page.screenshot(path=screenshot_path)

        browser.close()


@pytest.fixture
def logged_in_page(page):
    from pages.login_page import LoginPage

    username = Config.TEST_USERNAME
    password = Config.TEST_PASSWORD

    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    return page