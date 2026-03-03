# Playwright Frontend Testing

Playwright testing framework for frontend automation testing using TypeScript.

## Setup

1. **Install dependencies:**
```bash
npm install
```

2. **Install Playwright browsers:**
```bash
npx playwright install chromium
```

3. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Running Tests

### Run all tests:
```bash
npm test
```

### Run smoke tests:
```bash
npm run test:smoke
```

### Run with specific browser:
```bash
npm run test:chromium
npm run test:firefox
npm run test:webkit
```

### Run in headed mode:
```bash
npm run test:headed
```

### Run with Playwright UI:
```bash
npm run test:ui
```

### Run a specific test file:
```bash
npx playwright test tests/login.spec.ts
```

### View HTML report:
```bash
npm run report
```

## Allure Reports

### Generate and view report:
```bash
npm run allure:serve
```

### Generate static HTML report:
```bash
npm run allure:generate
```

**Note:** You need to install Allure command-line tool first:
- **macOS:** `brew install allure`
- **Linux:** Download from [Allure releases](https://github.com/allure-framework/allure2/releases)
- **Windows:** `scoop install allure`

## Project Structure

```
pagewheel-playwright/
├── config/               # Configuration
├── pages/                # Page Object Models
├── tests/                # Test specs
├── playwright.config.ts  # Playwright configuration
├── package.json          # Node.js dependencies
└── README.md             # This file
```

## Writing Tests

Tests follow the Page Object Model pattern. Create page objects in `pages/` and test specs in `tests/`.

Example test:
```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/login-page';
import { config } from '../config/config';

test('example test', async ({ page }) => {
  const loginPage = new LoginPage(page, config.BASE_URL);
  await loginPage.navigate();
  expect(loginPage.isLoaded()).toBeTruthy();
});
```
