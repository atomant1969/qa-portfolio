import { test, expect } from './fixtures';

test('builds authenticated order API request', async ({ storeApi }) => {
  const token = await storeApi.login();
  const response = await storeApi.createOrder(token, {
    customer: 'Robert Joyce',
    productId: 1,
    quantity: 2,
  });

  expect(response.status()).toBe(201);
  await expect(response).toBeOK();
  expect(await response.json()).toEqual({ status: 'created' });
});
