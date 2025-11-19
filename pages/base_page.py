from playwright.sync_api import Page


class BasePage:
    """Base page class that all page objects inherit from."""
    
    def __init__(self, page: Page):
        self.page = page
    
    def navigate_to(self, url: str):
        """Navigate to a specific URL."""
        self.page.goto(url)
    
    def get_title(self) -> str:
        """Get the page title."""
        return self.page.title()
    
    def get_url(self) -> str:
        """Get the current URL."""
        return self.page.url
    
    def wait_for_load_state(self, state: str = "load"):
        """Wait for page to reach a specific load state."""
        self.page.wait_for_load_state(state)

