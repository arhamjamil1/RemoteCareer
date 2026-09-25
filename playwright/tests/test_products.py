from pages.products_page import ProductsPage


def test_products_page(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    assert products_page.get_title() == "Products"
    assert products_page.get_product_count() > 0