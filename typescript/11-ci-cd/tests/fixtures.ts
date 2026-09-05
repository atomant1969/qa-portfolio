import { test as base, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

export const test = base.extend<{ workflowText: string }>({
  workflowText: async ({}, use) => {
    await use(fs.readFileSync(path.join(__dirname, '..', 'workflows', 'playwright-tests.yml'), 'utf-8'));
  },
});

export { expect };
