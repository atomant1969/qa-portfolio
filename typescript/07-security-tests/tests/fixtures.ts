import { test as base, expect } from '@playwright/test';

export const test = base.extend<{ maliciousPayloads: string[] }>({
  maliciousPayloads: async ({}, use) => {
    await use(['<script>alert(1)</script>', "' OR 1=1 --", 'DROP TABLE users']);
  },
});

export { expect };
