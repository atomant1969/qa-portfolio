import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  projects: [{ name: 'Mobile Chrome', use: devices['Pixel 5'] }],
});
