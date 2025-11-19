import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class for test settings."""

    # Base URL
    BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")

    # Timeouts (in milliseconds)
    default_timeout = int(os.getenv("DEFAULT_TIMEOUT", "30000"))

    # Credentials
    TEST_USER_EMAIL = os.getenv("TEST_USERNAME", "selenium_user@gmail.com")
    TEST_USER_PASSWORD = os.getenv("TEST_PASSWORD", "Selenium_user$1")

    # Browser settings
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))
