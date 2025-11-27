from playwright.sync_api import Page
from pages.base_page import BasePage


class BookBrandingPage(BasePage):
    """Page object for the BookBranding page."""

    BRANDING_LOOKS_GOOD_NEXT_BUTTON = "#branding-looks-good-next-button"
    COVER_ASSEMBLER_LOOKS_GOOD_NEXT_BUTTON = "#cover-assembler-looks-good-next-button"

    BOOK_TITLE_INPUT = "#book_title"
    BOOK_SUBTITLE_INPUT = "#book_subtitle"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page)
        self.base_url = base_url

    def fill_book_title(self, title: str = "Gym Membership for begginers"):
        """Fill in the book title field."""
        self.page.fill(self.BOOK_TITLE_INPUT, title)

    def fill_book_subtitle(self, subtitle: str = "A Comprehensive Guide"):
        """Fill in the book subtitle field."""
        self.page.fill(self.BOOK_SUBTITLE_INPUT, subtitle)
