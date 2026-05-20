from playwright.sync_api import Page
from pages.base_page import BaseListingPage


class PostAdPage(BaseListingPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.post_ad_btn = page.locator("a[href='/en/deposer']")
        self.upload_input = page.locator("#sec-photos input[type='file']")

    # ── NAVIGATION ────────────────────────────────────────────────────────────

    def go_to_post_ad(self):
        self.page.goto("https://dealyly.com/en")
        self.page.wait_for_load_state("domcontentloaded")
        self.post_ad_btn.wait_for(state="visible", timeout=8000)
        self.post_ad_btn.click()
        self.page.wait_for_load_state("domcontentloaded")

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

    def select_category(self, category_name: str):
        btn = self.page.locator(f"button[title='{category_name}']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    def select_subcategory(self, subcategory_name: str):
        btn = self.page.locator(f"button.rounded-full:has-text('{subcategory_name}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    # ── CAR MATRIX FIELDS ─────────────────────────────────────────────────────

    def select_brand(self, brand: str, brand_name: str = ""):
        btn = self.page.locator(f"button.rounded-full:has-text('{brand}')").first
        try:
            btn.wait_for(state="visible", timeout=3000)
            if "border-primary" not in (btn.get_attribute("class") or ""):
                btn.click()
        except Exception:
            other_btn = self.page.locator("button.rounded-full:has-text('Other')").first
            other_btn.wait_for(state="visible", timeout=8000)
            other_btn.click()
            self.page.wait_for_timeout(500)
            brand_input = self.page.locator("input[placeholder*='brand'], input[placeholder*='Brand'], input[placeholder*='marque']").first
            brand_input.wait_for(state="visible", timeout=8000)
            brand_input.fill(brand_name)

    def fill_model(self, model: str):
        field = self.page.locator("input[type='text'][value='']").first
        field.wait_for(state="visible", timeout=8000)
        field.fill(model)

    def fill_version(self, version: str):
        self.page.locator("input[placeholder*='GTI']").fill(version)

    def fill_engine(self, engine: str):
        self.page.locator("input[placeholder*='1.6 TDI']").fill(engine)

    def fill_year(self, year: str):
        self.page.locator("input[aria-label='Year']").fill(year)
        self.page.wait_for_timeout(500)
        self.page.locator("body").click(position={"x": 10, "y": 10})
        self.page.wait_for_timeout(1500)

    def select_condition(self, condition: str):
        btn = self.page.locator(f"button[aria-pressed]:has-text('{condition}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn_class = btn.get_attribute("class") or ""
        if "border-primary" not in btn_class:
            btn.click()
        self.page.wait_for_timeout(300)

    def select_fuel(self, fuel: str):
        self.page.locator(f"button.rounded-full:has-text('{fuel}')").first.click()

    def select_transmission(self, transmission: str):
        self.page.locator(f"button.rounded-full:has-text('{transmission}')").first.click()

    def select_color(self, color: str):
        self.page.locator(f"button.rounded-full:has-text('{color}')").first.click()

    def fill_mileage(self, mileage: str):
        self.page.locator("input[type='number']").first.fill(mileage)