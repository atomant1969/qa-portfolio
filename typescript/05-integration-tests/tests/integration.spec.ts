import { test, expect } from './fixtures';

test('service update is persisted in repository', async ({ repository }) => {
  repository.save('order-1', 'paid');

  expect(repository.get('order-1')).toBe('paid');
});
