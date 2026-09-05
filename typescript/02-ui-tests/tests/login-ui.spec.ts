import { test, expect } from './fixtures';

test('successful login shows welcome message', async ({ page, loginPage }) => {
  await loginPage.login('qa@example.com', 'correct-password');

  await expect(page.getByRole('status')).toHaveText('Welcome back');
});

test('invalid login shows error message', async ({ page, loginPage }) => {
  await loginPage.login('qa@example.com', 'wrong-password');

  await expect(page.getByRole('status')).toHaveText('Invalid credentials');
});
