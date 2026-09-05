import { test, expect } from './fixtures';

test('test plan documents scope and evidence', async ({ testPlan }) => {
  expect(testPlan).toContain('## Scope');
  expect(testPlan).toContain('## Evidence');
});

test('bug report documents expected and actual behavior', async ({ bugReport }) => {
  expect(bugReport).toContain('## Expected');
  expect(bugReport).toContain('## Actual');
});
