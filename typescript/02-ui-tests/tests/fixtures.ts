import { test as base, expect, type Page } from '@playwright/test';

class LoginPage {
  constructor(private readonly page: Page) {}

  async open(): Promise<void> {
    await this.page.setContent(`
      <label>Email <input id="email"></label>
      <label>Password <input id="password" type="password"></label>
      <button id="login">Sign in</button>
      <p role="status"></p>
      <script>
        document.querySelector('#login').addEventListener('click', () => {
          const email = document.querySelector('#email').value;
          const password = document.querySelector('#password').value;
          document.querySelector('[role=status]').textContent =
          email === 'qa@example.com' && password === 'correct-password'
            ? 'Welcome back'
            : 'Invalid credentials';
        });
      </script>
    `);
  }

  async login(email: string, password: string): Promise<void> {
    await this.page.locator('#email').fill(email);
    await this.page.locator('#password').fill(password);
    await this.page.locator('#login').click();
  }
}

type Fixtures = {
  loginPage: LoginPage;
};

export const test = base.extend<Fixtures>({
  loginPage: async ({ page }, use) => {
    // EN: The page object fixture centralizes setup for UI tests.
    // RU: Фикстура Page Object централизует подготовку UI-тестов.
    const loginPage = new LoginPage(page);
    await loginPage.open();
    await use(loginPage);
  },
});

export { expect };
