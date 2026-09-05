import { test, expect } from './fixtures';
import { generateOrder } from '../src/dataGenerator';

test('order generator produces deterministic valid payload', async ({ orderIndex }) => {
  const order = generateOrder(orderIndex);

  expect(order).toEqual({ customer: 'Customer 007', productId: 2, quantity: 3 });
});
