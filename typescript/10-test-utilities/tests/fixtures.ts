import { test as base, expect } from '@playwright/test';

export const test = base.extend<{ orderIndex: number }>({
  orderIndex: async ({}, use) => {
    await use(7);
  },
});

export { expect };
