import { test as base, expect } from '@playwright/test';

type OrderRow = { status: 'paid' | 'cancelled'; total: number };

export const test = base.extend<{ orderRows: OrderRow[] }>({
  orderRows: async ({}, use) => {
    await use([
      { status: 'paid', total: 100 },
      { status: 'paid', total: 150 },
      { status: 'cancelled', total: 40 },
    ]);
  },
});

export { expect };
