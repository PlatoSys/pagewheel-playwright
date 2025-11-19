import pytest
import allure
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.book_page import BookPage
from pages.page_editor_page import BookPageEditorPage
from pages.book_branding_page import BookBrandingPage
from config.config import Config
import logging

logger = logging.getLogger(__name__)


@allure.feature("Book Management")
@allure.story("Book Creation")
class TestBook:
    """Test cases for login functionality."""

    @pytest.mark.smoke
    @allure.title("Create Book")
    @allure.description("Verify that the book creates successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_book(self, page: Page, config: Config):
        """Test that the login page opens successfully."""
        with allure.step("Initialize login page"):
            login_page = LoginPage(page, config.BASE_URL)
            login_page.navigate()

            login_page.login(config.TEST_USER_EMAIL, config.TEST_USER_PASSWORD)

            book_page = BookPage(page, config.BASE_URL)
            book_page.click_element(book_page.CLOSE_ONBOARDING_MODAL_BTN)
            book_page.click_element(book_page.CREATE_DIGITA_PRODUCT_BTN)

            book_page.is_page_loader_visible()

            book_page.click_element(book_page.READY_TO_EDIT_CARD)

            book_page.wait_for_element(book_page.BATCH_CARD_CLASS, 25000)

            book_page.click_nth_child_element(
                book_page.BATCH_CARD_CLASS, ".checkMark", 1
            )

            book_page.click_element(book_page.BATCHES_READY_TO_EDIT_BUTTON)

            book_page.is_page_loader_visible()

            book_branding_page = BookBrandingPage(page, config.BASE_URL)
            book_branding_page.wait_and_click_element(
                book_branding_page.BRANDING_LOOKS_GOOD_NEXT_BUTTON
            )

            book_branding_page.is_page_loader_visible()
            book_branding_page.wait_and_click_element(
                book_branding_page.COVER_ASSEMBLER_LOOKS_GOOD_NEXT_BUTTON
            )

            page_editor_page = BookPageEditorPage(page, config.BASE_URL)
            page_editor_page.is_page_loader_visible()
            page_editor_page.wait_and_click_element(
                page_editor_page.PUBLISH_LOOKS_GOOD_NEXT_BUTTON
            )

            page_editor_page.is_page_loader_visible()
            page_editor_page.wait_and_click_element(
                page_editor_page.PUBLISH_APPROVE_BUTTON
            )

            page_editor_page.wait_and_click_element(
                page_editor_page.CREATE_WEBSITE_LOOKS_GOOD_NEXT_BUTTON, 30000
            )

            page_editor_page.wait_for_url_contains("/website", timeout=30000)

        allure.attach(
            page.url,
            name="Book Creation URL",
            attachment_type=allure.attachment_type.TEXT,
        )
