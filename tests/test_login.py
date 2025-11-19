import pytest
import allure
from playwright.sync_api import Page
from pages.login_page import LoginPage
from config.config import Config


@allure.feature("Authentication")
@allure.story("Login Page")
class TestLogin:
    """Test cases for login functionality."""

    @pytest.mark.smoke
    @allure.title("Open Login Page")
    @allure.description("Verify that the login page loads successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_login_page(self, page: Page, config: Config):
        """Test that the login page opens successfully."""
        with allure.step("Initialize login page"):
            login_page = LoginPage(page, config.BASE_URL)
            login_page.navigate()

            assert login_page.is_loaded(), "Login page failed to load"
            assert page.title(), "Page title should not be empty"

            login_page.login(config.TEST_USER_EMAIL, config.TEST_USER_PASSWORD)

        allure.attach(
            page.url, name="Login Page URL", attachment_type=allure.attachment_type.TEXT
        )
