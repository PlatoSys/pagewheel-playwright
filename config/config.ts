import dotenv from 'dotenv';

dotenv.config();

export const config = {
  BASE_URL: process.env.BASE_URL || 'http://localhost:3000',
  DEFAULT_TIMEOUT: parseInt(process.env.DEFAULT_TIMEOUT || '30000', 10),
  TEST_USER_EMAIL: process.env.TEST_USERNAME || 'selenium_user@gmail.com',
  TEST_USER_PASSWORD: process.env.TEST_PASSWORD || 'Selenium_user$1',
  HEADLESS: (process.env.HEADLESS || 'false').toLowerCase() === 'true',
  SLOW_MO: parseInt(process.env.SLOW_MO || '0', 10),
};
