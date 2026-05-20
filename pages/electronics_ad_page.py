import re
from playwright.sync_api import Page, expect
from pages.base_page import BaseListingPage


class PostElectronicsPage(BaseListingPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.post_ad_btn = page.locator("a[href='/en/deposer']")
        self.upload_input = page.locator("#sec-photos input[type='file']")

        self.wilaya = page.locator("select:has(option[value='2'])")
        self.commune = page.locator("input[placeholder*='Commencez']")

        self.title = page.locator("input[placeholder='Or type your own…']")
        self.price = page.locator("input[placeholder='0']")

        self.model = page.locator("input[type='text'][value='']").first
        self.storage = page.locator("input[placeholder*='256 GB']")
        self.screen_size = page.locator("input[placeholder*='6.7']")

        self.description = page.locator("textarea[placeholder*='Decrivez']")
        self.ai_description_btn = page.locator("button:has(.lucide-sparkles)")

        self.publish_btn = page.locator("button:has-text('Publish listing')")
        self.draft_btn = page.locator("button:has-text('Save as draft')")

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
        btn = self.page.locator("button[title='Electronics']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    def select_subcategory(self, subcategory: str):
        # e.g. "Phones", "Tablets", "TVs"
        btn = self.page.get_by_role("button", name=subcategory, exact=True)
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()
        self.page.wait_for_timeout(500)

    # ── ELECTRONICS MATRIX FIELDS ─────────────────────────────────────────────

    def select_kind(self, kind: str):
        # e.g. "Phone", "Laptop", "Tablet", "Television"
        btn = self.page.locator(f"button.rounded-full:has-text('{kind}')").first
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()
        self.page.wait_for_timeout(300)

    def select_brand(self, brand: str):
        # e.g. "Apple", "Samsung", "Xiaomi"
        btn = self.page.locator(f"button.rounded-full:has-text('{brand}')").first
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()

    def fill_model(self, model: str):
        self.model.wait_for(state="visible", timeout=8000)
        self.model.fill(model)

    def select_condition(self, condition: str):
        # e.g. "New", "Like new", "Good", "Fair", "Needs repair"
        btn = self.page.locator(f"button.rounded-full:has-text('{condition}')").first
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()

    def fill_storage(self, storage: str):
        if storage == "N/A":
            return
        self.storage.wait_for(state="visible", timeout=8000)
        self.storage.fill(storage)

    def fill_screen_size(self, size: str):
        if size == "N/A":
            return
        self.screen_size.wait_for(state="visible", timeout=8000)
        self.screen_size.fill(size)

    def set_warranty(self, warranty: bool = True):
        toggle = self.page.locator("button[aria-pressed]:has-text('Warranty')")
        toggle.wait_for(state="visible", timeout=8000)
        is_pressed = toggle.get_attribute("aria-pressed")
        if warranty and is_pressed == "false":
            toggle.click()
        elif not warranty and is_pressed == "true":
            toggle.click()

