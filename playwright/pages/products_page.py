class ProductsPage:

    def __init__(self, page):
        self.page = page

        self.page_title = ".title"
        self.products = ".inventory_item"

    def get_title(self):
        return self.page.locator(self.page_title).inner_text()

    def get_product_count(self):
        return self.page.locator(self.products).count()