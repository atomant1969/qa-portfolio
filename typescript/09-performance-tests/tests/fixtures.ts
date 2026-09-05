import { test as base, expect } from '@playwright/test';

export const test = base.extend<{ responseTimesMs: number[] }>({
  responseTimesMs: async ({}, use) => {
    await use([120, 130, 125, 140, 155, 160, 180, 220, 240, 260]);
  },
});

export { expect };
