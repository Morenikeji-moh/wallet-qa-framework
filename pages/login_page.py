from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("[data-test='username']")
        self.password = page.locator("[data-test='password']")
        self.submit = page.locator("[data-test='login-button']")
        self.error = page.locator("[data-test='error']")

    def open(self):
        self.page.goto("/", wait_until="domcontentloaded")

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.submit.click()

    def expect_error(self, text: str):
        expect(self.error).to_contain_text(text)