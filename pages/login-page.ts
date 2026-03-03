import { type Page } from '@playwright/test';
import { BasePage } from './base-page';

export class LoginPage extends BasePage {
  static readonly EMAIL_INPUT = '#username';
  static readonly PASSWORD_INPUT = '#password';
  static readonly LOGIN_BUTTON = '#signin_button';

  private readonly loginUrl: string;

  constructor(page: Page, private baseUrl: string) {
    super(page);
    this.loginUrl = `${baseUrl}/sign-in`;
  }

  async navigate() {
    await this.navigateTo(this.loginUrl);
    await this.waitForLoadState();
  }

  isLoaded(): boolean {
    const url = this.page.url();
    return url.endsWith('/sign-in') || url.includes('/sign-in');
  }

  async enterEmail(email: string) {
    await this.page.fill(LoginPage.EMAIL_INPUT, email);
  }

  async enterPassword(password: string) {
    await this.page.fill(LoginPage.PASSWORD_INPUT, password);
  }

  async clickLogin() {
    await this.page.click(LoginPage.LOGIN_BUTTON);
  }

  async login(email: string, password: string) {
    await this.enterEmail(email);
    await this.enterPassword(password);
    await this.clickLogin();
  }
}
