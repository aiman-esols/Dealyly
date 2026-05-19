from playwright.sync_api import Page, expect


class ProfilePage:

    def __init__(self, page: Page):
        self.page = page

        self.avatar = page.locator("a.dl-brand-gradient")
        self.settings_link = page.locator("a[href='/en/compte/profil']")
        self.full_name = page.locator("#full-name")
        self.province_btn = page.locator("button[aria-haspopup='listbox']")
        self.save_btn = page.locator("button:has(.lucide-save)")

    # ── NAVIGATION ────────────────────────────────────────────────────────────

    def go_to_profile(self):
        self.avatar.wait_for(state="visible", timeout=8000)
        self.avatar.click()
        self.page.wait_for_load_state("domcontentloaded")

    def go_to_settings(self):
        self.settings_link.wait_for(state="visible", timeout=8000)
        self.settings_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    # ── EDIT FIELDS ───────────────────────────────────────────────────────────

    def update_full_name(self, name: str):
        self.full_name.wait_for(state="visible", timeout=8000)
        self.full_name.click(click_count=3)
        self.full_name.fill(name)

    def select_province(self, province: str):
        # Open the province dropdown
        self.province_btn.wait_for(state="visible", timeout=8000)
        self.province_btn.click()
        self.page.wait_for_timeout(500)
        # Click the matching option
        option = self.page.locator(f"[role='option']:has-text('{province}'), li:has-text('{province}')").first
        option.wait_for(state="visible", timeout=8000)
        option.click()

    # ── SAVE ──────────────────────────────────────────────────────────────────

    def save_changes(self):
        self.save_btn.wait_for(state="visible", timeout=8000)
        self.save_btn.click()
        self.page.wait_for_timeout(1000)

    # ── VERIFY ────────────────────────────────────────────────────────────────

    def verify_saved(self, expected_name: str):
        expect(self.full_name).to_have_value(expected_name, timeout=8000)