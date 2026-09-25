class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.page_title = self.page.locator(".title")
        self.products = self.page.locator(".inventory_item")

    def get_title(self):
        return self.page_title.inner_text()

    def get_product_count(self):
        return self.products.count()