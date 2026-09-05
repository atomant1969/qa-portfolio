import { test, expect } from './fixtures';

const forbiddenPatterns = ['<script', 'drop table', '--', ' or 1=1'];

function isSafeSearchQuery(value: string) {
  const normalized = value.toLowerCase();
  return forbiddenPatterns.every((pattern) => !normalized.includes(pattern));
}

test('common injection payloads are rejected by validation rule', async ({ maliciousPayloads }) => {
  for (const payload of maliciousPayloads) {
    expect(isSafeSearchQuery(payload)).toBe(false);
  }
});
