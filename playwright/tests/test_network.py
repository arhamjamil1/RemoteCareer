from playwright.sync_api import expect


def test_mock_api_response(page):
    page.route(
        "https://jsonplaceholder.typicode.com/todos/1",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body='{"userId":1,"id":1,"title":"Mocked Task","completed":true}'
        )
    )

    page.goto("https://jsonplaceholder.typicode.com/todos/1")

    expect(page.locator("body")).to_contain_text("Mocked Task")
    expect(page.locator("body")).to_contain_text('"completed":true')