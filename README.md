# Playwright Frontend Testing

Basic Playwright testing framework for frontend automation testing.

## Setup

1. **Create and activate virtual environment:**
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
playwright install chromium
```

3. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run with different browsers:
```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

### Run in headless mode:
```bash
pytest --headed=false
```

### Run specific test:
```bash
pytest tests/test_login.py::TestLogin::test_open_login_page
```

### Run with markers:
```bash
pytest -m smoke
```

## Allure Reports

### Quick start - Run tests and view report:
```bash
./run_with_allure.sh
```

### Manual commands:
```bash
# Run tests (generates allure-results)
pytest

# Generate and open HTML report
allure serve allure-results
```

### Generate static HTML report:
```bash
allure generate allure-results -o allure-report --clean
```

**Note:** You need to install Allure command-line tool first:
- **macOS:** `brew install allure`
- **Linux:** Download from [Allure releases](https://github.com/allure-framework/allure2/releases)
- **Windows:** `scoop install allure`

### Allure Features Included:
- ✅ Test steps with `@allure.step()`
- ✅ Test categorization with `@allure.feature()` and `@allure.story()`
- ✅ Automatic screenshot capture on test failure
- ✅ Test severity levels
- ✅ Custom attachments (URLs, logs, etc.)

## Project Structure

```
playwright-fe/
├── config/               # Configuration files
├── pages/                # Page Object Models
├── tests/                # Test cases
├── conftest.py           # Pytest fixtures with Allure integration
├── pytest.ini            # Pytest configuration
├── allure.properties     # Allure configuration
├── run_with_allure.sh    # Helper script to run tests and view report
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Writing Tests

Tests follow the Page Object Model pattern. Create page objects in `pages/` and test cases in `tests/`.

Example test:
```python
def test_example(page: Page, config: Config):
    login_page = LoginPage(page, config.BASE_URL)
    login_page.navigate()
    assert login_page.is_loaded()
```

