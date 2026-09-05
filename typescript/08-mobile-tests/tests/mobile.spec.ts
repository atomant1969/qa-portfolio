import { test, expect } from './fixtures';

test('mobile checkout button is visible in phone viewport', async ({ page }) => {
  await page.setContent('<main><h1>Cart</h1><button aria-label="Checkout">Checkout</button></main>');

  await expect(page.getByLabel('Checkout')).toBeVisible();
});
