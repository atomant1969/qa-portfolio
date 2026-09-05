import { test as base, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

export const test = base.extend<{ testPlan: string; bugReport: string }>({
  testPlan: async ({}, use) => {
    await use(fs.readFileSync(path.join(__dirname, '..', 'test-plan.md'), 'utf-8'));
  },
  bugReport: async ({}, use) => {
    await use(fs.readFileSync(path.join(__dirname, '..', 'bug-report.md'), 'utf-8'));
  },
});

export { expect };
