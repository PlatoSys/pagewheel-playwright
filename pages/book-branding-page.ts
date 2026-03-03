import { type Page } from '@playwright/test';
import { BasePage } from './base-page';

export class BookBrandingPage extends BasePage {
  static readonly BRANDING_LOOKS_GOOD_NEXT_BUTTON = '#branding-looks-good-next-button';
  static readonly COVER_ASSEMBLER_LOOKS_GOOD_NEXT_BUTTON = '#cover-assembler-looks-good-next-button';

  static readonly BOOK_TITLE_INPUT = '#book_title';
  static readonly BOOK_SUBTITLE_INPUT = '#book_subtitle';

  constructor(page: Page, private baseUrl: string) {
    super(page);
  }

  async fillBookTitle(title = 'Gym Membership for begginers') {
    await this.page.fill(BookBrandingPage.BOOK_TITLE_INPUT, title);
  }

  async fillBookSubtitle(subtitle = 'A Comprehensive Guide') {
    await this.page.fill(BookBrandingPage.BOOK_SUBTITLE_INPUT, subtitle);
  }
}
