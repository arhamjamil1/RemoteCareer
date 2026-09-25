from playwright.sync_api import expect


def test_open_new_tab(page):
    page.goto("https://www.saucedemo.com/")

    with page.expect_popup() as popup_info:
        page.evaluate("""
            window.open('https://example.com', '_blank')
        """)

    new_page = popup_info.value

    expect(new_page).to_have_url("https://example.com/")
    expect(new_page).to_have_title("Example Domain")

    new_page.close()