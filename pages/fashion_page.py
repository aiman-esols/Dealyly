from playwright.sync_api import Page, expect
from pages.base_page import BaseListingPage
import re

class PostFashionPage(BaseListingPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.post_ad_btn = page.locator("a[href='/en/deposer']")
        self.upload_input = page.locator("#sec-photos input[type='file']")

        self.wilaya = page.locator("select:has(option[value='2'])")
        self.commune = page.locator("input[placeholder*='Commencez']")

        self.title = page.locator("input[placeholder='Or type your own…']")
        self.price = page.locator("input[placeholder='0']")
        self.material = page.locator("input[placeholder='E.G. Cotton, Wool']")

        self.description = page.locator("textarea[placeholder*='Decrivez']")

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
        btn = self.page.locator("button[title='Fashion & Beauty']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(1500)

    def select_subcategory(self, subcategory: str):
        btn = self.page.get_by_role("button", name=subcategory, exact=True)
        btn.wait_for(state="visible", timeout=8000)
        # Only click if not already selected
        btn_class = btn.get_attribute("class") or ""
        if "border-primary" not in btn_class:
            btn.click()
            self.page.wait_for_timeout(1000)
            # Click again if still not selected
            btn_class = btn.get_attribute("class") or ""
            if "border-primary" not in btn_class:
                btn.click()
        self.page.wait_for_timeout(500)

    # ── FASHION MATRIX FIELDS ─────────────────────────────────────────────────

    def select_gender(self, gender: str):
        btn = self.page.locator(f"button[aria-pressed]:has-text('{gender}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def select_type(self, item_type: str):
        btn = self.page.locator(f"button[aria-pressed]:has-text('{item_type}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def select_size(self, size: str):
        btn = self.page.locator("button[aria-pressed]").filter(has_text=re.compile(f"^{size}$"))
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)   
    def select_condition(self, condition: str):
        # e.g. "New", "Like new", "Good", "Fair", "Needs repair"
        btn = self.page.locator(f"button.rounded-full:has-text('{condition}')").first
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()

    def fill_material(self, material: str):
        self.material.wait_for(state="visible", timeout=8000)
        self.material.fill(material)

