from playwright.sync_api import expect

from pages.products_page import ProductsPage


def test_products_page(logged_in_page):
    products_page = ProductsPage(logged_in_page.page)

    expect(products_page.page_title).to_have_text("Products")
    expect(products_page.products.first).to_be_visible()

    assert products_page.get_product_count() > 0


def test_sort_products(logged_in_page):
    products_page = ProductsPage(logged_in_page.page)

    products_page.sort_products("za")

    first_product = products_page.get_first_product_name()

    assert first_product == "Test.allTheThings() T-Shirt (Red)"