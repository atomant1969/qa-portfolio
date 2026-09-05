import { test as base, expect } from '@playwright/test';

export const test = base.extend<{ failureNotes: string }>({
  failureNotes: async ({}, use) => {
    await use('Checkout returns 500 after payment confirmation.');
  },
});

export { expect };
