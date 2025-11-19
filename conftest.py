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
    """Attach screenshot to Allure report on test failure."""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Get the page fixture if it exists
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            try:
                screenshot = page.screenshot()
                allure.attach(
                    screenshot,
                    name="Screenshot on failure",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")
