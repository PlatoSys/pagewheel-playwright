import { defineConfig } from '@playwright/test';
import dotenv from 'dotenv';

dotenv.config();

const BASE_URL = process.env.BASE_URL || 'http://localhost:3000';
const DEFAULT_TIMEOUT = parseInt(process.env.DEFAULT_TIMEOUT || '30000', 10);
const HEADLESS = (process.env.HEADLESS || 'false').toLowerCase() === 'true';
const SLOW_MO = parseInt(process.env.SLOW_MO || '0', 10);

export default defineConfig({
  testDir: './tests',
  timeout: DEFAULT_TIMEOUT,
  fullyParallel: false,
  forbidOnly: !!process.env.CI,
  retries: 0,
  reporter: [
    ['list'],
    ['allure-playwright'],
  ],
  use: {
    baseURL: BASE_URL,
    headless: HEADLESS,
    launchOptions: {
      slowMo: SLOW_MO,
    },
    screenshot: 'only-on-failure',
    trace: 'retain-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { browserName: 'chromium' },
    },
  ],
});
