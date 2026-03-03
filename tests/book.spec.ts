import { test } from '@playwright/test';
import { LoginPage } from '../pages/login-page';
import { BookPage } from '../pages/book-page';
import { BookPageEditorPage } from '../pages/page-editor-page';
import { BookBrandingPage } from '../pages/book-branding-page';
import { config } from '../config/config';

test.describe('Book Management - Book Creation', () => {
  test('Create Book @smoke', async ({ page }) => {
    const loginPage = new LoginPage(page, config.BASE_URL);
    await loginPage.navigate();
    await loginPage.login(config.TEST_USER_EMAIL, config.TEST_USER_PASSWORD);

    const bookPage = new BookPage(page, config.BASE_URL);
    await bookPage.clickElement(BookPage.CLOSE_ONBOARDING_MODAL_BTN);
    await bookPage.clickElement(BookPage.CREATE_DIGITAL_PRODUCT_BTN);

    await bookPage.isPageLoaderVisible();

    await bookPage.clickElement(BookPage.READY_TO_EDIT_CARD);

    await bookPage.waitForElement(BookPage.BATCH_CARD_CLASS, 25000);

    await bookPage.clickNthChildElement(BookPage.BATCH_CARD_CLASS, '.checkMark', 1);

    await bookPage.clickElement(BookPage.BATCHES_READY_TO_EDIT_BUTTON);

    await bookPage.isPageLoaderVisible();

    const bookBrandingPage = new BookBrandingPage(page, config.BASE_URL);
    await bookBrandingPage.waitAndClickElement(
      BookBrandingPage.BRANDING_LOOKS_GOOD_NEXT_BUTTON,
    );

    await bookBrandingPage.isPageLoaderVisible();
    await bookBrandingPage.waitAndClickElement(
      BookBrandingPage.COVER_ASSEMBLER_LOOKS_GOOD_NEXT_BUTTON,
    );

    const pageEditorPage = new BookPageEditorPage(page, config.BASE_URL);
    await pageEditorPage.isPageLoaderVisible();
    await pageEditorPage.waitAndClickElement(
      BookPageEditorPage.PUBLISH_LOOKS_GOOD_NEXT_BUTTON,
    );

    await pageEditorPage.isPageLoaderVisible();
    await pageEditorPage.waitAndClickElement(
      BookPageEditorPage.PUBLISH_APPROVE_BUTTON,
    );

    await pageEditorPage.waitAndClickElement(
      BookPageEditorPage.CREATE_WEBSITE_LOOKS_GOOD_NEXT_BUTTON,
      30000,
    );

    await pageEditorPage.waitForUrlContains('/website', 30000);
  });

  test('Create Book Page-by-Page @smoke', async ({ page }) => {
    const loginPage = new LoginPage(page, config.BASE_URL);
    await loginPage.navigate();
    await loginPage.login(config.TEST_USER_EMAIL, config.TEST_USER_PASSWORD);

    const bookPage = new BookPage(page, config.BASE_URL);
    await bookPage.clickElement(BookPage.CLOSE_ONBOARDING_MODAL_BTN);
    await bookPage.clickElement(BookPage.CREATE_DIGITAL_PRODUCT_BTN);

    await bookPage.isPageLoaderVisible();

    await bookPage.clickElement(BookPage.PAGE_BY_PAGE_CARD);

    await bookPage.isPageLoaderVisible();

    const bookBrandingPage = new BookBrandingPage(page, config.BASE_URL);
    await bookBrandingPage.waitAndClickElement(
      BookBrandingPage.BRANDING_LOOKS_GOOD_NEXT_BUTTON,
    );

    await bookBrandingPage.isPageLoaderVisible();
    await bookBrandingPage.waitAndClickElement(
      BookBrandingPage.COVER_ASSEMBLER_LOOKS_GOOD_NEXT_BUTTON,
    );

    await bookBrandingPage.isPageLoaderVisible();

    await bookBrandingPage.fillBookTitle();
    await bookBrandingPage.fillBookSubtitle();

    await bookBrandingPage.waitAndClickElement(
      BookBrandingPage.COVER_ASSEMBLER_LOOKS_GOOD_NEXT_BUTTON,
    );
  });
});
