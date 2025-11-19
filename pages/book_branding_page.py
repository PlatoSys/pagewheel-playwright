from playwright.sync_api import Page
from pages.base_page import BasePage


class BookBrandingPage(BasePage):
    """Page object for the BookBranding page."""

    BRANDING_LOOKS_GOOD_NEXT_BUTTON = "#branding-looks-good-next-button"
    COVER_ASSEMBLER_LOOKS_GOOD_NEXT_BUTTON = "#cover-assembler-looks-good-next-button"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page)
        self.base_url = base_url
