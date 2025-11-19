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

## Project Structure

```
playwright-fe/
├── config/           # Configuration files
├── pages/            # Page Object Models
├── tests/            # Test cases
├── conftest.py       # Pytest fixtures
├── pytest.ini        # Pytest configuration
├── requirements.txt  # Python dependencies
└── README.md         # This file
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

