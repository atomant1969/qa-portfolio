import { test, expect } from './fixtures';

test('created order is visible in the order details UI', async ({ page, order }) => {
  await page.setContent(`<h1>${order.customer}</h1><p>${order.status}</p><p>$${order.total}</p>`);

  await expect(page.getByText('Robert Joyce')).toBeVisible();
  await expect(page.getByText('paid')).toBeVisible();
  await expect(page.getByText('$199')).toBeVisible();
});
