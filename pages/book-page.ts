import { type Page } from '@playwright/test';
import { BasePage } from './base-page';

export class BookPage extends BasePage {
  static readonly CREATE_DIGITAL_PRODUCT_BTN = '#create-digital-product-button';
  static readonly CLOSE_ONBOARDING_MODAL_BTN = '#onboarding-modal-close';

  static readonly READY_TO_EDIT_CARD = '#ready-to-edit-card';
  static readonly PAGE_BY_PAGE_CARD = '#page-by-page-card';

  static readonly BATCH_CARD_CLASS = '.batchCard';

  static readonly BATCHES_READY_TO_EDIT_BUTTON = '#ready-to-edit-batches-button';

  constructor(page: Page, private baseUrl: string) {
    super(page);
  }
}
