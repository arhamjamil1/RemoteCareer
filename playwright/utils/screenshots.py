import os


def save_screenshot(page, test_name):
    os.makedirs("test-results", exist_ok=True)

    path = f"test-results/{test_name}.png"

    page.screenshot(path=path)

    return path