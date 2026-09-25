from config import Config


class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"
        self.menu_button = "#react-burger-menu-btn"
        self.logout_link = "#logout_sidebar_link"
        self.error_message = "[data-test='error']"

    def open(self):
        self.page.goto(Config.BASE_URL)

    def login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.login_button)

    def logout(self):
        self.page.click(self.menu_button)
        self.page.click(self.logout_link)

    def is_error_visible(self):
        return self.page.locator(self.error_message).is_visible()