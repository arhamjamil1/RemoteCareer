from config import Config


class LoginPage:
    def __init__(self, page):
        self.page = page

        self.username = self.page.get_by_placeholder("Username")
        self.password = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.menu_button = self.page.get_by_role("button", name="Open Menu")
        self.logout_link = self.page.locator("#logout_sidebar_link")
        self.error_message = self.page.locator("[data-test='error']")

    def open(self):
        self.page.goto(Config.BASE_URL)

    def login(self, username=None, password=None):
        username = username or Config.TEST_USERNAME
        password = password or Config.TEST_PASSWORD

        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()

    def is_error_visible(self):
        return self.error_message.is_visible()

    def get_page_title(self):
        return self.page.title()

    def get_current_url(self):
        return self.page.url