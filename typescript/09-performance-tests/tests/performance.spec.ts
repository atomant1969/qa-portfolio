import { test, expect } from './fixtures';

function percentile(values: number[], rank: number) {
  const ordered = [...values].sort((a, b) => a - b);
  const index = Math.ceil((rank / 100) * ordered.length) - 1;
  return ordered[index];
}

test('response time p95 stays under threshold', async ({ responseTimesMs }) => {
  expect(percentile(responseTimesMs, 95)).toBeLessThanOrEqual(260);
});
