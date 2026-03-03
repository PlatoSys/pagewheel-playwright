import { type Page, expect } from '@playwright/test';

export class BasePage {
  static readonly LOADER_SELECTOR = '#page-loader';
  static readonly ALERT_SELECTOR = '.MuiSnackbar-root';

  constructor(protected page: Page) {}

  async navigateTo(url: string) {
    await this.page.goto(url);
  }

  async getTitle(): Promise<string> {
    return this.page.title();
  }

  getUrl(): string {
    return this.page.url();
  }

  async verifyUrlContains(text: string) {
    await expect(this.page).toHaveURL(text, { timeout: 10000 });
  }

  async waitForUrlContains(text: string, timeout = 10000) {
    await this.page.waitForURL(`**/*${text}*`, { timeout });
  }

  async waitForLoadState(state: 'load' | 'domcontentloaded' | 'networkidle' = 'load') {
    await this.page.waitForLoadState(state);
  }

  async clickElement(selector: string) {
    await this.page.click(selector);
  }

  async fillInput(selector: string, text: string) {
    await this.page.fill(selector, text);
  }

  async getElementText(selector: string): Promise<string | null> {
    return this.page.textContent(selector);
  }

  async isElementVisible(selector: string): Promise<boolean> {
    return this.page.isVisible(selector);
  }

  async isElementEnabled(selector: string): Promise<boolean> {
    return this.page.isEnabled(selector);
  }

  async waitForElement(selector: string, timeout = 10000) {
    await this.page.waitForSelector(selector, { state: 'visible', timeout });
  }

  async waitForElementHidden(selector: string, timeout = 10000) {
    await this.page.waitForSelector(selector, { state: 'hidden', timeout });
  }

  async hoverElement(selector: string) {
    await this.page.hover(selector);
  }

  async selectOption(selector: string, value: string) {
    await this.page.selectOption(selector, value);
  }

  async checkCheckbox(selector: string) {
    await this.page.check(selector);
  }

  async uncheckCheckbox(selector: string) {
    await this.page.uncheck(selector);
  }

  async reloadPage() {
    await this.page.reload();
  }

  async goBack() {
    await this.page.goBack();
  }

  async screenshot(path: string) {
    await this.page.screenshot({ path });
  }

  async getElementAttribute(selector: string, attribute: string): Promise<string | null> {
    return this.page.getAttribute(selector, attribute);
  }

  async pressKey(key: string) {
    await this.page.keyboard.press(key);
  }

  async typeText(selector: string, text: string, delay = 0) {
    await this.page.type(selector, text, { delay });
  }

  async waitForTimeout(timeout: number) {
    await this.page.waitForTimeout(timeout);
  }

  async executeScript<T>(script: string, ...args: unknown[]): Promise<T> {
    return this.page.evaluate(script, ...args);
  }

  async scrollToElement(selector: string) {
    await this.page.locator(selector).scrollIntoViewIfNeeded();
  }

  async getElementsCount(selector: string): Promise<number> {
    return this.page.locator(selector).count();
  }

  async isPageLoaderVisible(loaderSelector = BasePage.LOADER_SELECTOR): Promise<boolean> {
    try {
      await this.page.waitForSelector(loaderSelector, { state: 'visible', timeout: 5000 });
      await this.page.waitForSelector(loaderSelector, { state: 'hidden', timeout: 20000 });
      return true;
    } catch {
      return false;
    }
  }

  async waitAndClickElement(selector: string, timeout = 10000) {
    await this.waitForElement(selector, timeout);
    await this.clickElement(selector);
  }

  findChildElement(parentSelector: string, childSelector: string) {
    return this.page.locator(parentSelector).locator(childSelector);
  }

  async clickChildElement(parentSelector: string, childSelector: string) {
    await this.findChildElement(parentSelector, childSelector).click();
  }

  async getChildElementText(parentSelector: string, childSelector: string): Promise<string | null> {
    return this.findChildElement(parentSelector, childSelector).textContent();
  }

  async isChildElementVisible(parentSelector: string, childSelector: string): Promise<boolean> {
    return this.findChildElement(parentSelector, childSelector).isVisible();
  }

  async waitForChildElement(parentSelector: string, childSelector: string, timeout = 10000) {
    await this.findChildElement(parentSelector, childSelector).waitFor({ state: 'visible', timeout });
  }

  async getChildElementsCount(parentSelector: string, childSelector: string): Promise<number> {
    return this.findChildElement(parentSelector, childSelector).count();
  }

  async clickFirstChildElement(parentSelector: string, childSelector: string) {
    await this.findChildElement(parentSelector, childSelector).first().click();
  }

  async clickLastChildElement(parentSelector: string, childSelector: string) {
    await this.findChildElement(parentSelector, childSelector).last().click();
  }

  async clickNthChildElement(parentSelector: string, childSelector: string, index: number) {
    await this.findChildElement(parentSelector, childSelector).nth(index).click();
  }

  async clickAllChildElements(parentSelector: string, childSelector: string) {
    const children = this.findChildElement(parentSelector, childSelector);
    const count = await children.count();
    for (let i = 0; i < count; i++) {
      await children.nth(i).click();
    }
  }

  async getFirstChildElementText(parentSelector: string, childSelector: string): Promise<string | null> {
    return this.findChildElement(parentSelector, childSelector).first().textContent();
  }

  async getLastChildElementText(parentSelector: string, childSelector: string): Promise<string | null> {
    return this.findChildElement(parentSelector, childSelector).last().textContent();
  }

  async getNthChildElementText(parentSelector: string, childSelector: string, index: number): Promise<string | null> {
    return this.findChildElement(parentSelector, childSelector).nth(index).textContent();
  }

  async getAllChildElementsText(parentSelector: string, childSelector: string): Promise<(string | null)[]> {
    const children = this.findChildElement(parentSelector, childSelector);
    const count = await children.count();
    const texts: (string | null)[] = [];
    for (let i = 0; i < count; i++) {
      texts.push(await children.nth(i).textContent());
    }
    return texts;
  }

  async isFirstChildElementVisible(parentSelector: string, childSelector: string): Promise<boolean> {
    return this.findChildElement(parentSelector, childSelector).first().isVisible();
  }

  async isLastChildElementVisible(parentSelector: string, childSelector: string): Promise<boolean> {
    return this.findChildElement(parentSelector, childSelector).last().isVisible();
  }

  async isNthChildElementVisible(parentSelector: string, childSelector: string, index: number): Promise<boolean> {
    return this.findChildElement(parentSelector, childSelector).nth(index).isVisible();
  }

  async waitForFirstChildElement(parentSelector: string, childSelector: string, timeout = 10000) {
    await this.findChildElement(parentSelector, childSelector).first().waitFor({ state: 'visible', timeout });
  }

  async waitForLastChildElement(parentSelector: string, childSelector: string, timeout = 10000) {
    await this.findChildElement(parentSelector, childSelector).last().waitFor({ state: 'visible', timeout });
  }

  async waitForNthChildElement(parentSelector: string, childSelector: string, index: number, timeout = 10000) {
    await this.findChildElement(parentSelector, childSelector).nth(index).waitFor({ state: 'visible', timeout });
  }

  async hoverChildElement(parentSelector: string, childSelector: string) {
    await this.findChildElement(parentSelector, childSelector).first().hover();
  }

  async hoverNthChildElement(parentSelector: string, childSelector: string, index: number) {
    await this.findChildElement(parentSelector, childSelector).nth(index).hover();
  }

  async fillChildInput(parentSelector: string, childSelector: string, text: string) {
    await this.findChildElement(parentSelector, childSelector).first().fill(text);
  }

  async fillNthChildInput(parentSelector: string, childSelector: string, index: number, text: string) {
    await this.findChildElement(parentSelector, childSelector).nth(index).fill(text);
  }

  async getChildElementAttribute(parentSelector: string, childSelector: string, attribute: string): Promise<string | null> {
    return this.findChildElement(parentSelector, childSelector).first().getAttribute(attribute);
  }

  async getNthChildElementAttribute(parentSelector: string, childSelector: string, index: number, attribute: string): Promise<string | null> {
    return this.findChildElement(parentSelector, childSelector).nth(index).getAttribute(attribute);
  }

  async isAlertDisplayed(alertSelector = BasePage.ALERT_SELECTOR): Promise<boolean> {
    try {
      await this.page.waitForSelector(alertSelector, { state: 'visible', timeout: 5000 });
      await this.page.waitForSelector(alertSelector, { state: 'hidden', timeout: 20000 });
      return true;
    } catch {
      return false;
    }
  }
}
