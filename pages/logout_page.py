from playwright.sync_api import Page, expect


class LogoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.avatar = page.locator("a.dl-brand-gradient")
        self.logout_btn = page.locator("button:has(.lucide-log-out)")
        self.login_btn = page.locator("button:has(span:text-is('Log in')), button:has-text('Log in')").first

    def go_to_profile(self):
        self.avatar.wait_for(state="visible", timeout=8000)
        self.avatar.click()
        self.page.wait_for_load_state("domcontentloaded")

    def logout(self):
        # Scroll down to find logout button
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.page.wait_for_timeout(500)
        self.logout_btn.wait_for(state="visible", timeout=8000)
        self.logout_btn.click()
        self.page.wait_for_load_state("domcontentloaded")

    def verify_logout(self):
        # Should be back on home page
        expect(self.page).to_have_url("https://dealyly.com/en", timeout=10000)
        # Login button should be visible again
        expect(self.login_btn).to_be_visible(timeout=8000)