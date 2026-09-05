import { test, expect } from './fixtures';

test('orders query returns expected paid revenue aggregate', async ({ orderRows }) => {
  const paidRevenue = orderRows.filter((row) => row.status === 'paid').reduce((sum, row) => sum + row.total, 0);

  expect(paidRevenue).toBe(250);
});
