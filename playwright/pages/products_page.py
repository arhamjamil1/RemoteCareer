from utils.logger import logger


class ProductsPage:
    def __init__(self, page):
        self.page = page

        self.page_title = self.page.locator(".title")
        self.products = self.page.locator(".inventory_item")
        self.sort_dropdown = self.page.locator(".product_sort_container")

    def get_title(self):
        logger.info("Getting products page title")
        return self.page_title.inner_text()

    def get_product_count(self):
        count = self.products.count()
        logger.info(f"Product count: {count}")
        return count

    def sort_products(self, option):
        logger.info(f"Sorting products: {option}")
        self.sort_dropdown.select_option(option)

    def get_first_product_name(self):
        name = self.products.first.locator(
            ".inventory_item_name"
        ).inner_text()

        logger.info(f"First product: {name}")

        return name