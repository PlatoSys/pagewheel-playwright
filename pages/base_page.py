from playwright.sync_api import Page, expect
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """Base page class that all page objects inherit from."""

    LOADER_SELECTOR = "#page-loader"

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

    def verify_url_contains(self, text: str):
        """Verify that the current URL contains the specified text."""
        expect(self.page).to_have_url(text, timeout=10000)

    def wait_for_url_contains(self, text: str, timeout: int = 10000):
        """Wait for the URL to contain the specified text."""
        self.page.wait_for_url(f"**/*{text}*", timeout=timeout)

    def wait_for_load_state(self, state: str = "load"):
        """Wait for page to reach a specific load state."""
        self.page.wait_for_load_state(state)

    def click_element(self, selector: str):
        """Click an element specified by the selector."""
        self.page.click(selector)

    def fill_input(self, selector: str, text: str):
        """Fill an input field with the specified text."""
        self.page.fill(selector, text)

    def get_element_text(self, selector: str) -> str:
        """Get the text content of an element."""
        return self.page.text_content(selector)

    def is_element_visible(self, selector: str) -> bool:
        """Check if an element is visible on the page."""
        return self.page.is_visible(selector)

    def is_element_enabled(self, selector: str) -> bool:
        """Check if an element is enabled."""
        return self.page.is_enabled(selector)

    def wait_for_element(self, selector: str, timeout: int = 10000):
        """Wait for an element to be visible."""
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)

    def wait_for_element_hidden(self, selector: str, timeout: int = 10000):
        """Wait for an element to be hidden."""
        self.page.wait_for_selector(selector, state="hidden", timeout=timeout)

    def hover_element(self, selector: str):
        """Hover over an element."""
        self.page.hover(selector)

    def select_option(self, selector: str, value: str):
        """Select an option from a dropdown."""
        self.page.select_option(selector, value)

    def check_checkbox(self, selector: str):
        """Check a checkbox."""
        self.page.check(selector)

    def uncheck_checkbox(self, selector: str):
        """Uncheck a checkbox."""
        self.page.uncheck(selector)

    def reload_page(self):
        """Reload the current page."""
        self.page.reload()

    def go_back(self):
        """Go back in browser history."""
        self.page.go_back()

    def screenshot(self, path: str):
        """Take a screenshot and save it to the specified path."""
        self.page.screenshot(path=path)

    def get_element_attribute(self, selector: str, attribute: str) -> str:
        """Get an attribute value from an element."""
        return self.page.get_attribute(selector, attribute)

    def press_key(self, key: str):
        """Press a keyboard key."""
        self.page.keyboard.press(key)

    def type_text(self, selector: str, text: str, delay: int = 0):
        """Type text into an element with optional delay between keystrokes."""
        self.page.type(selector, text, delay=delay)

    def wait_for_timeout(self, timeout: int):
        """Wait for a specified timeout in milliseconds."""
        self.page.wait_for_timeout(timeout)

    def execute_script(self, script: str, *args):
        """Execute JavaScript on the page."""
        return self.page.evaluate(script, *args)

    def scroll_to_element(self, selector: str):
        """Scroll to an element."""
        self.page.locator(selector).scroll_into_view_if_needed()

    def get_elements_count(self, selector: str) -> int:
        """Get the count of elements matching the selector."""
        return self.page.locator(selector).count()

    def is_page_loader_visible(self, loader_selector: str = LOADER_SELECTOR) -> bool:
        """Wait for the page loader to show up and then disappear within 20 seconds each."""
        try:
            self.page.wait_for_selector(loader_selector, state="visible", timeout=5000)
            self.page.wait_for_selector(loader_selector, state="hidden", timeout=20000)
            return True
        except Exception:
            return False

    def wait_and_click_element(self, selector: str, timeout: int = 10000):
        """Wait for an element to be visible and then click it."""
        self.wait_for_element(selector, timeout)
        self.click_element(selector)

    def find_child_element(self, parent_selector: str, child_selector: str):
        """Find a child element within a parent element."""
        parent = self.page.locator(parent_selector)
        return parent.locator(child_selector)

    def click_child_element(self, parent_selector: str, child_selector: str):
        """Click a child element within a parent element."""
        child = self.find_child_element(parent_selector, child_selector)
        child.click()

    def get_child_element_text(self, parent_selector: str, child_selector: str) -> str:
        """Get text content from a child element within a parent element."""
        child = self.find_child_element(parent_selector, child_selector)
        return child.text_content()

    def is_child_element_visible(
        self, parent_selector: str, child_selector: str
    ) -> bool:
        """Check if a child element within a parent element is visible."""
        child = self.find_child_element(parent_selector, child_selector)
        return child.is_visible()

    def wait_for_child_element(
        self, parent_selector: str, child_selector: str, timeout: int = 10000
    ):
        """Wait for a child element within a parent element to be visible."""
        child = self.find_child_element(parent_selector, child_selector)
        child.wait_for(state="visible", timeout=timeout)

    def get_child_elements_count(
        self, parent_selector: str, child_selector: str
    ) -> int:
        """Get the count of child elements within a parent element."""
        child = self.find_child_element(parent_selector, child_selector)
        return child.count()

    def click_first_child_element(self, parent_selector: str, child_selector: str):
        """Click the first matching child element within a parent element."""
        child = self.find_child_element(parent_selector, child_selector)
        child.first.click()

    def click_last_child_element(self, parent_selector: str, child_selector: str):
        """Click the last matching child element within a parent element."""
        child = self.find_child_element(parent_selector, child_selector)
        child.last.click()

    def click_nth_child_element(
        self, parent_selector: str, child_selector: str, index: int
    ):
        """Click the nth matching child element within a parent element (0-based index)."""
        child = self.find_child_element(parent_selector, child_selector)
        child.nth(index).click()

    def click_all_child_elements(self, parent_selector: str, child_selector: str):
        """Click all matching child elements within a parent element."""
        children = self.find_child_element(parent_selector, child_selector)
        count = children.count()
        for i in range(count):
            children.nth(i).click()

    def get_first_child_element_text(
        self, parent_selector: str, child_selector: str
    ) -> str:
        """Get text from the first matching child element."""
        child = self.find_child_element(parent_selector, child_selector)
        return child.first.text_content()

    def get_last_child_element_text(
        self, parent_selector: str, child_selector: str
    ) -> str:
        """Get text from the last matching child element."""
        child = self.find_child_element(parent_selector, child_selector)
        return child.last.text_content()

    def get_nth_child_element_text(
        self, parent_selector: str, child_selector: str, index: int
    ) -> str:
        """Get text from the nth matching child element (0-based index)."""
        child = self.find_child_element(parent_selector, child_selector)
        return child.nth(index).text_content()

    def get_all_child_elements_text(
        self, parent_selector: str, child_selector: str
    ) -> list:
        """Get text from all matching child elements."""
        children = self.find_child_element(parent_selector, child_selector)
        count = children.count()
        return [children.nth(i).text_content() for i in range(count)]

    def is_first_child_element_visible(
        self, parent_selector: str, child_selector: str
    ) -> bool:
        """Check if the first matching child element is visible."""
        child = self.find_child_element(parent_selector, child_selector)
        return child.first.is_visible()

    def is_last_child_element_visible(
        self, parent_selector: str, child_selector: str
    ) -> bool:
        """Check if the last matching child element is visible."""
        child = self.find_child_element(parent_selector, child_selector)
        return child.last.is_visible()

    def is_nth_child_element_visible(
        self, parent_selector: str, child_selector: str, index: int
    ) -> bool:
        """Check if the nth matching child element is visible (0-based index)."""
        child = self.find_child_element(parent_selector, child_selector)
        return child.nth(index).is_visible()

    def wait_for_first_child_element(
        self, parent_selector: str, child_selector: str, timeout: int = 10000
    ):
        """Wait for the first matching child element to be visible."""
        child = self.find_child_element(parent_selector, child_selector)
        child.first.wait_for(state="visible", timeout=timeout)

    def wait_for_last_child_element(
        self, parent_selector: str, child_selector: str, timeout: int = 10000
    ):
        """Wait for the last matching child element to be visible."""
        child = self.find_child_element(parent_selector, child_selector)
        child.last.wait_for(state="visible", timeout=timeout)

    def wait_for_nth_child_element(
        self,
        parent_selector: str,
        child_selector: str,
        index: int,
        timeout: int = 10000,
    ):
        """Wait for the nth matching child element to be visible (0-based index)."""
        child = self.find_child_element(parent_selector, child_selector)
        child.nth(index).wait_for(state="visible", timeout=timeout)

    def hover_child_element(self, parent_selector: str, child_selector: str):
        """Hover over the first matching child element within a parent element."""
        child = self.find_child_element(parent_selector, child_selector)
        child.first.hover()

    def hover_nth_child_element(
        self, parent_selector: str, child_selector: str, index: int
    ):
        """Hover over the nth matching child element (0-based index)."""
        child = self.find_child_element(parent_selector, child_selector)
        child.nth(index).hover()

    def fill_child_input(self, parent_selector: str, child_selector: str, text: str):
        """Fill the first matching child input element with text."""
        child = self.find_child_element(parent_selector, child_selector)
        child.first.fill(text)

    def fill_nth_child_input(
        self, parent_selector: str, child_selector: str, index: int, text: str
    ):
        """Fill the nth matching child input element with text (0-based index)."""
        child = self.find_child_element(parent_selector, child_selector)
        child.nth(index).fill(text)

    def get_child_element_attribute(
        self, parent_selector: str, child_selector: str, attribute: str
    ) -> str:
        """Get an attribute value from the first matching child element."""
        child = self.find_child_element(parent_selector, child_selector)
        return child.first.get_attribute(attribute)

    def get_nth_child_element_attribute(
        self, parent_selector: str, child_selector: str, index: int, attribute: str
    ) -> str:
        """Get an attribute value from the nth matching child element (0-based index)."""
        child = self.find_child_element(parent_selector, child_selector)
        return child.nth(index).get_attribute(attribute)
