import { test as base, expect } from '@playwright/test';

type Order = { customer: string; status: string; total: number };

export const test = base.extend<{ order: Order }>({
  order: async ({}, use) => {
    // EN: API-style setup prepares state before UI validation.
    // RU: Подготовка в стиле API создает состояние перед проверкой UI.
    await use({ customer: 'Robert Joyce', status: 'paid', total: 199 });
  },
});

export { expect };
