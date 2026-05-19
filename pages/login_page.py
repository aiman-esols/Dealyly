import pytest
from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.login_btn = page.locator("button:has(span:text-is('Log in')), button:has-text('Log in')").first
        self.email = page.locator("input[type='email']")
        self.password = page.locator("input[type='password']")
        self.submit_btn = page.locator("[role='dialog'] button[type='submit']")
        self.avatar = page.locator("[class*='avatar'], [class*='user'], button:has(.lucide-user)").first
        self.avatar = page.locator("a.dl-brand-gradient")  # ← must be here

    def goto(self):
        self.page.goto("https://dealyly.com/en")
        self.page.wait_for_load_state("networkidle")

    def open_login_modal(self):
        self.page.wait_for_load_state("networkidle")
        self.login_btn.wait_for(state="visible", timeout=1000)
        self.login_btn.click()
        self.page.wait_for_timeout(1000)  # wait for modal animation

    def login(self, email: str, password: str):
        self.email.wait_for(state="visible", timeout=10000)
        self.email.fill(email)
        self.password.fill(password)
        self.submit_btn.click()

    def verify_login_success(self):
        expect(self.avatar).to_be_visible(timeout=10000)