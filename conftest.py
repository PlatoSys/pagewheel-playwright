import pytest
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

