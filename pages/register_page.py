from playwright.sync_api import Page, expect


class RegisterPage:

    def __init__(self, page: Page):
        self.page = page

        self.login_btn = page.locator("button:has(span:text-is('Log in')), button:has-text('Log in')").first
        self.create_account_btn = page.locator("button:has-text('Create account')")

        self.full_name = page.locator("#full-name")
        self.email = page.locator("#email")
        self.password = page.locator("#new-password")

        self.next_btn = page.locator("button[type='submit']:has-text('Next')")
        self.get_started_btn = page.locator("button[type='submit']:has-text('Get started')")

        self.avatar = page.locator("a.dl-brand-gradient")

    def goto(self):
        self.page.goto("https://dealyly.com/en")
        self.page.wait_for_load_state("domcontentloaded")

    def open_login_modal(self):
        self.login_btn.wait_for(state="visible", timeout=8000)
        self.login_btn.click()
        self.page.wait_for_timeout(500)

    def open_register_form(self):
        self.create_account_btn.wait_for(state="visible", timeout=8000)
        self.create_account_btn.click()
        self.page.wait_for_timeout(500)

    def fill_details(self, full_name: str, email: str, password: str):
        self.full_name.wait_for(state="visible", timeout=8000)
        self.full_name.fill(full_name)
        self.email.fill(email)
        self.password.fill(password)

    def click_next(self):
        self.next_btn.wait_for(state="visible", timeout=8000)
        self.next_btn.click()
        self.page.wait_for_timeout(1000)

    def click_get_started(self):
        self.get_started_btn.wait_for(state="visible", timeout=8000)
        self.get_started_btn.click()
        self.page.wait_for_load_state("domcontentloaded")

    def verify_account_created(self):
        expect(self.avatar).to_be_visible(timeout=10000)