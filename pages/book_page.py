from playwright.sync_api import Page
from pages.base_page import BasePage


class BookPage(BasePage):
    """Page object for the Login page."""

    CREATE_DIGITA_PRODUCT_BTN = "#create-digital-product-button"
    CLOSE_ONBOARDING_MODAL_BTN = "#onboarding-modal-close"

    # Book Cards
    READY_TO_EDIT_CARD = "#ready-to-edit-card"
    PAGE_BY_PAGE_CARD = "#page-by-page-card"

    BATCH_CARD_CLASS = ".batchCard"

    BATCHES_READY_TO_EDIT_BUTTON = "#ready-to-edit-batches-button"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page)
        self.base_url = base_url
