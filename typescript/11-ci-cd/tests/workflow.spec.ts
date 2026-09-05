import { test, expect } from './fixtures';

test('workflow installs dependencies before running tests', async ({ workflowText }) => {
  expect(workflowText.indexOf('npm ci')).toBeLessThan(workflowText.indexOf('npm test'));
});
