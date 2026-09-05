import { test as base, expect, devices, type BrowserContext } from '@playwright/test';

type Fixtures = {
  context: BrowserContext;
};

export const test = base.extend<Fixtures>({
  context: async ({ browser }, use) => {
    // EN: Device fixture keeps mobile configuration in one place.
    // RU: Фикстура устройства хранит мобильную конфигурацию в одном месте.
    const context = await browser.newContext(devices['Pixel 5']);
    await use(context);
    await context.close();
  },
});

export { expect };
