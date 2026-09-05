import { test as base, expect } from '@playwright/test';

type LoadProfile = {
  virtualUsers: number;
  rampUpSeconds: number;
  steadyStateSeconds: number;
  protocol: 'tcp' | 'jdbc';
};

export const test = base.extend<{ loadProfile: LoadProfile }>({
  loadProfile: async ({}, use) => {
    await use({ virtualUsers: 50, rampUpSeconds: 120, steadyStateSeconds: 300, protocol: 'tcp' });
  },
});

export { expect };
