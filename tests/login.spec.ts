import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/login-page';
import { config } from '../config/config';

test.describe('Authentication - Login Page', () => {
  test('Open Login Page @smoke', async ({ page }) => {
    const loginPage = new LoginPage(page, config.BASE_URL);
    await loginPage.navigate();

    expect(loginPage.isLoaded()).toBeTruthy();

    const title = await loginPage.getTitle();
    expect(title).toBeTruthy();

    await loginPage.login(config.TEST_USER_EMAIL, config.TEST_USER_PASSWORD);
  });
});
