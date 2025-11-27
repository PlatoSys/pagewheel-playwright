import pytest
import allure
from playwright.sync_api import Page, Browser, BrowserContext
from config.config import Config


@pytest.fixture(scope="session")
def config():
    """Provide configuration for tests."""
    return Config()


@pytest.fixture(scope="function")
def page(page: Page, config: Config):
    """Provide a page instance with base configuration."""
    page.set_default_timeout(config.default_timeout)
    yield page


@pytest.fixture(scope="function")
def context(context: BrowserContext, config: Config):
    """Provide a browser context with base configuration."""
    yield context


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach screenshot and additional debug info to Allure report on test failure."""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Get the page fixture if it exists
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            try:
                # Capture screenshot
                screenshot = page.screenshot(full_page=True)
                allure.attach(
                    screenshot,
                    name="Screenshot on failure",
                    attachment_type=allure.attachment_type.PNG
                )
                
                # Capture page URL
                allure.attach(
                    page.url,
                    name="Page URL",
                    attachment_type=allure.attachment_type.TEXT
                )
                
                # Capture HTML content
                html_content = page.content()
                allure.attach(
                    html_content,
                    name="Page HTML",
                    attachment_type=allure.attachment_type.HTML
                )
                
            except Exception as e:
                print(f"Failed to capture debug information: {e}")
