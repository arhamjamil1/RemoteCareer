from playwright.sync_api import expect


def test_file_upload(page):
    page.goto("https://the-internet.herokuapp.com/upload")

    file_input = page.locator("#file-upload")

    file_input.set_input_files(
        "tests/test_file.txt"
    )

    page.get_by_role("button", name="Upload").click()

    expect(page.locator("#uploaded-files")).to_have_text(
        "test_file.txt"
    )