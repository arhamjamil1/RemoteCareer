from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_products_page(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert products_page.get_title() == "Products"
    assert products_page.get_product_count() > 0