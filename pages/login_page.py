from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the Login page."""

    EMAIL_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#signin_button"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page)
        self.base_url = base_url
        self.login_url = f"{base_url}/sign-in"

    def navigate(self):
        """Navigate to the login page."""
        self.navigate_to(self.login_url)
        self.wait_for_load_state()

    def is_loaded(self) -> bool:
        """Check if login page is loaded."""
        return self.page.url.endswith("/sign-in") or "/sign-in" in self.page.url

    def enter_email(self, email: str):
        """Enter email in the email field."""
        self.page.fill(self.EMAIL_INPUT, email)

    def enter_password(self, password: str):
        """Enter password in the password field."""
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click the login button."""
        self.page.click(self.LOGIN_BUTTON)

    def login(self, email: str, password: str):
        """Perform complete login action."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
