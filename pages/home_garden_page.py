from playwright.sync_api import Page, expect


class PostHomeGardenPage:

    def __init__(self, page: Page):
        self.page = page

        self.post_ad_btn = page.locator("a[href='/en/deposer']")
        self.upload_input = page.locator("#sec-photos input[type='file']")

        self.wilaya = page.locator("select:has(option[value='2'])")
        self.commune = page.locator("input[placeholder*='Commencez']")

        self.title = page.locator("input[placeholder='Or type your own…']")
        self.price = page.locator("input[placeholder='0']")
        self.brand = page.locator("input[placeholder*='Condor']")

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
        btn = self.page.locator("button[title='Home & Garden']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    def select_subcategory(self, subcategory: str):
        # e.g. "Appliances", "Furniture", "Kitchen & Utensils"
        btn = self.page.get_by_role("button", name=subcategory, exact=True)
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()
        self.page.wait_for_timeout(500)

    # ── HOME & GARDEN MATRIX FIELDS ───────────────────────────────────────────

    def select_type(self, item_type: str):
        # e.g. "Refrigerator", "Washing Machine", "Oven", "AC"
        btn = self.page.locator(f"button.rounded-full:has-text('{item_type}')").first
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()
        self.page.wait_for_timeout(300)

    def fill_brand(self, brand: str):
        self.brand.wait_for(state="visible", timeout=8000)
        self.brand.fill(brand)

    def select_condition(self, condition: str):
        # e.g. "New", "Like new", "Good", "Fair", "Needs repair"
        btn = self.page.locator(f"button.rounded-full:has-text('{condition}')").first
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()

    # ── COMMON FIELDS ─────────────────────────────────────────────────────────

    def fill_title(self, title: str):
        self.title.wait_for(state="visible", timeout=8000)
        self.title.fill(title)

    def fill_price(self, price: str):
        self.price.wait_for(state="visible", timeout=8000)
        self.price.fill(price)

    def set_negotiable(self):
        self.page.locator("button.rounded-full:has-text('Negotiable')").click()

    # ── LOCATION ──────────────────────────────────────────────────────────────

    def select_wilaya(self, wilaya_value: str):
        self.wilaya.wait_for(state="visible", timeout=8000)
        self.wilaya.select_option(value=wilaya_value)
        self.page.wait_for_timeout(500)

    def fill_commune(self, commune: str):
        self.commune.wait_for(state="visible", timeout=8000)
        self.commune.fill(commune)
        self.page.locator(f"button.text-start:has-text('{commune}')").first.wait_for(state="visible", timeout=8000)
        self.page.locator(f"button.text-start:has-text('{commune}')").first.click()

    # ── DESCRIPTION ───────────────────────────────────────────────────────────

    def fill_description(self, text: str):
        self.description.wait_for(state="visible", timeout=8000)
        self.description.fill(text)

    def generate_ai_description(self):
        self.ai_description_btn.wait_for(state="visible", timeout=8000)
        self.ai_description_btn.click()
        self.page.wait_for_timeout(5000)
        expect(self.description).not_to_be_empty(timeout=15000)

    # ── SUBMIT ────────────────────────────────────────────────────────────────

    def publish_listing(self):
        self.publish_btn.wait_for(state="visible", timeout=8000)
        self.publish_btn.click()

    def save_as_draft(self):
        self.draft_btn.wait_for(state="visible", timeout=8000)
        self.draft_btn.click()