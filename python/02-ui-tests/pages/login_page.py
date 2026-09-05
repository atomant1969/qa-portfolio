from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        self.page.set_content(
            """
            <main>
              <h1>QA Store Login</h1>
              <label>Email <input id="email" type="email"></label>
              <label>Password <input id="password" type="password"></label>
              <button id="login">Sign in</button>
              <p id="message" role="status"></p>
              <script>
                document.querySelector('#login').addEventListener('click', () => {
                  const email = document.querySelector('#email').value;
                  const password = document.querySelector('#password').value;
                  document.querySelector('#message').textContent =
                    email === 'qa@example.com' && password === 'correct-password'
                      ? 'Welcome back'
                      : 'Invalid credentials';
                });
              </script>
            </main>
            """
        )

    def login(self, email: str, password: str) -> None:
        self.page.locator("#email").fill(email)
        self.page.locator("#password").fill(password)
        self.page.locator("#login").click()

    def expect_message(self, text: str) -> None:
        expect(self.page.get_by_role("status")).to_have_text(text)
