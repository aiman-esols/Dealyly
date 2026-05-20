from playwright.sync_api import Page, expect
from pages.base_page import BaseListingPage
import re

class PostRealEstatePage(BaseListingPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.post_ad_btn = page.locator("a[href='/en/deposer']")
        self.upload_input = page.locator("#sec-photos input[type='file']")

        self.wilaya = page.locator("select:has(option[value='2'])")
        self.commune = page.locator("input[placeholder*='Commencez']")

        self.title = page.locator("input[placeholder='Or type your own…']")
        self.price = page.locator("input[placeholder='0']")

        self.bathrooms = page.locator("input[inputmode='numeric'][min='1'][max='10']")
        self.surface = page.locator("input[inputmode='numeric'][min='1'][max='100000']").first
        self.built_surface = page.locator("input[inputmode='numeric'][min='1'][max='100000']").nth(1)
        self.floor = page.locator("input[min='-2'][max='60']")

        self.description = page.locator("textarea[placeholder*='Decrivez']")
        self.ai_description_btn = page.locator("button:has(.lucide-sparkles)")

        self.draft_btn = page.locator("button:has-text('Save as draft')")
        self.publish_btn = page.locator("button:has-text('Publish listing')")

    # ── NAVIGATION ────────────────────────────────────────────────────────────

    def go_to_post_ad(self):
        self.post_ad_btn.wait_for(state="visible", timeout=8000)
        self.post_ad_btn.click()
        self.page.wait_for_load_state("networkidle")

    # ── IMAGE UPLOAD ──────────────────────────────────────────────────────────

    def upload_image(self, image_path: str):
        self.upload_input.wait_for(state="attached", timeout=10000)
        self.upload_input.set_input_files(image_path)

    def wait_for_ai_processing(self):
        try:
            self.page.locator("[class*='loading'], [class*='spinner'], [class*='loader']").first.wait_for(
                state="hidden", timeout=20000
            )
        except Exception:
            pass
        self.page.wait_for_timeout(3000)

    # ── CATEGORY ──────────────────────────────────────────────────────────────

    def select_category(self):
        btn = self.page.locator("button[title='Real Estate']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    def select_subcategory(self):
        btn = self.page.get_by_role("button", name="Vacation Rentals", exact=True)
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(1500)
        # Verify it's selected
        btn_class = btn.get_attribute("class")
        if "border-primary" not in btn_class:
            btn.click()  # click again if not selected
            self.page.wait_for_timeout(1000)

    # ── REAL ESTATE MATRIX FIELDS ─────────────────────────────────────────────

    def select_usage(self, usage: str):
        # e.g. "Rent", "Sale"
        self.page.locator(f"button.rounded-full:has-text('{usage}')").first.click()
        self.page.wait_for_timeout(300)

    def select_use_type(self, use_type: str):
        # e.g. "Residential", "Commercial"
        self.page.locator(f"button.rounded-full:has-text('{use_type}')").first.click()
        self.page.wait_for_timeout(300)

    def select_property_type(self, property_type: str):
        # e.g. "Villa", "Apartment"
        self.page.locator(f"button.rounded-full:has-text('{property_type}')").first.click()
        self.page.wait_for_timeout(300)

    def select_rooms(self, rooms: str):
        # e.g. "F4", "F3", "F2"
        self.page.locator(f"button.rounded-full:has-text('{rooms}')").first.click()

    def fill_bathrooms(self, bathrooms: str):
        self.bathrooms.wait_for(state="visible", timeout=8000)
        self.bathrooms.fill(bathrooms)

    def fill_surface(self, surface: str):
        self.surface.wait_for(state="visible", timeout=8000)
        self.surface.fill(surface)

    def fill_built_surface(self, built_surface: str):
        self.built_surface.wait_for(state="visible", timeout=8000)
        self.built_surface.fill(built_surface)

    def fill_floor(self, floor: str):
        self.floor.wait_for(state="visible", timeout=8000)
        self.floor.fill(floor)
        self.page.keyboard.press("Tab")
        self.page.wait_for_timeout(500)

    def set_furnished(self, furnished: bool = True):
        toggle = self.page.locator("button[aria-pressed]:has-text('Furnished')")
        is_pressed = toggle.get_attribute("aria-pressed")
        if furnished and is_pressed == "false":
            toggle.click()
        elif not furnished and is_pressed == "true":
            toggle.click()

    def select_rental_period(self, period: str):
        # e.g. "Monthly", "Daily", "Weekly"
        self.page.locator(f"button.rounded-full:has-text('{period}')").first.click()

    def select_condition(self, condition: str):
        # e.g. "New", "Good", "To renovate"
        self.page.locator(f"button.rounded-full:has-text('{condition}')").first.click()

    def select_features(self, features: list):
        # e.g. ["Parking", "Elevator", "Pool", "Balcony"]
        for feature in features:
            self.page.locator(f"button.rounded-full:has-text('{feature}')").first.click()
            self.page.wait_for_timeout(200)

