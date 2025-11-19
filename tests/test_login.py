import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from config.config import Config


class TestLogin:
    """Test cases for login functionality."""

    @pytest.mark.smoke
    def test_open_login_page(self, page: Page, config: Config):
        """Test that the login page opens successfully."""
        # Arrange
        login_page = LoginPage(page, config.BASE_URL)

        # Act
        login_page.navigate()

        # Assert
        assert login_page.is_loaded(), "Login page failed to load"
        assert page.title(), "Page title should not be empty"
        login_page.login(config.TEST_USER_EMAIL, config.TEST_USER_PASSWORD)
