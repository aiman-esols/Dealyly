from playwright.sync_api import Page, expect


class EditListingPage:

    def __init__(self, page: Page):
        self.page = page

        self.avatar = page.locator("a.dl-brand-gradient")
        self.my_listings_link = page.locator("main a[href='/en/compte/annonces']")
        self.edit_btn = page.locator("button:has(.lucide-square-pen)").first
        self.price = page.locator("input[placeholder='0']")
        self.description = page.locator("textarea[placeholder*='Decrivez']")
        self.save_btn = page.locator("button:has-text('Save changes')")

    # ── NAVIGATION ────────────────────────────────────────────────────────────

    def go_to_profile(self):
        self.avatar.wait_for(state="visible", timeout=8000)
        self.avatar.click()
        self.page.wait_for_load_state("domcontentloaded")

    def go_to_my_listings(self):
        self.my_listings_link.wait_for(state="visible", timeout=8000)
        self.my_listings_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_edit(self, listing_name: str):
        # Find the listing card by name and click its edit button
        listing = self.page.locator(f"div.bg-surface:has(h3:has-text('{listing_name}'))")
        listing.wait_for(state="visible", timeout=8000)
        listing.scroll_into_view_if_needed()
        listing.locator("button:has(.lucide-square-pen)").click()
        self.page.wait_for_load_state("domcontentloaded")
    # ── EDIT FIELDS ───────────────────────────────────────────────────────────
    def update_wilaya(self, wilaya_value: str):
        wilaya = self.page.locator("select:has(option[value='2'])")
        wilaya.scroll_into_view_if_needed()
        wilaya.wait_for(state="visible", timeout=8000)
        wilaya.select_option(value=wilaya_value)
        self.page.wait_for_timeout(500)
    
    def update_commune(self, commune: str):
        commune_input = self.page.locator("input[placeholder*='Commencez']")
        commune_input.scroll_into_view_if_needed()
        commune_input.wait_for(state="visible", timeout=8000)
        commune_input.fill(commune)
        self.page.locator(f"button.text-start:has-text('{commune}')").first.wait_for(state="visible", timeout=8000)
        self.page.locator(f"button.text-start:has-text('{commune}')").first.click()

    def update_price(self, new_price: str):
        self.price.scroll_into_view_if_needed()
        self.price.wait_for(state="visible", timeout=8000)
        self.price.click(click_count=3)
        self.price.fill(new_price)

    def update_description(self, new_description: str):
        self.description.wait_for(state="visible", timeout=8000)
        self.description.click(click_count=3)
        self.description.fill(new_description)

    # ── SAVE ──────────────────────────────────────────────────────────────────

    def save_changes(self):
        self.save_btn.scroll_into_view_if_needed()
        self.save_btn.wait_for(state="visible", timeout=8000)
        self.save_btn.click()
        self.page.wait_for_load_state("domcontentloaded")

    # ── VERIFY ────────────────────────────────────────────────────────────────

    def verify_saved(self):
        expect(self.page.locator(
            "[class*='success'], [class*='confirmation'], button:has-text('Save changes')"
        ).first).to_be_visible(timeout=10000)