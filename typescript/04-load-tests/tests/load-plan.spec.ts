import { test, expect } from './fixtures';

test('load profile contains ramp-up and steady-state phases', async ({ loadProfile }) => {
  expect(loadProfile.protocol).toBe('tcp');
  expect(loadProfile.rampUpSeconds).toBeGreaterThan(0);
  expect(loadProfile.steadyStateSeconds).toBeGreaterThan(loadProfile.rampUpSeconds);
});
