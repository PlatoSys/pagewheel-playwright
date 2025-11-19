from playwright.sync_api import Page
from pages.base_page import BasePage


class BookPageEditorPage(BasePage):
    """Page object for the Login page."""

    PUBLISH_LOOKS_GOOD_NEXT_BUTTON = "#publish_looks_good_next"
    PUBLISH_APPROVE_BUTTON = "#publish_approve_button"
    CREATE_WEBSITE_LOOKS_GOOD_NEXT_BUTTON = "#create_website_looks_good_next"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page)
        self.base_url = base_url
