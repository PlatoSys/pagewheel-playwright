import { type Page } from '@playwright/test';
import { BasePage } from './base-page';

export class BookPageEditorPage extends BasePage {
  static readonly PUBLISH_LOOKS_GOOD_NEXT_BUTTON = '#publish_looks_good_next';
  static readonly PUBLISH_APPROVE_BUTTON = '#publish_approve_button';
  static readonly CREATE_WEBSITE_LOOKS_GOOD_NEXT_BUTTON = '#create_website_looks_good_next';

  constructor(page: Page, private baseUrl: string) {
    super(page);
  }
}
