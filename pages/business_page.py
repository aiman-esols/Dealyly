from playwright.sync_api import Page
from pages.base_page import BaseListingPage


class PostBusinessPage(BaseListingPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.upload_input = page.locator("#sec-photos input[type='file']")
        self.item_type = page.locator("input[type='text']").first
        self.brand = page.locator("input[type='text']").nth(1)

    def go_to_post_ad(self):
        self.page.goto("https://dealyly.com/en/deposer")
        self.page.wait_for_load_state("domcontentloaded")

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

    def select_category(self):
        btn = self.page.locator("button[title='Business & Industrial']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    def select_subcategory(self, subcategory: str):
        btn = self.page.locator(f"button.px-4:has-text('{subcategory}')").first
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()
        self.page.wait_for_timeout(500)

    def fill_type(self, item_type: str):
        self.item_type.wait_for(state="visible", timeout=8000)
        self.item_type.fill(item_type)

    def fill_brand(self, brand: str):
        self.brand.wait_for(state="visible", timeout=8000)
        self.brand.fill(brand)

    def select_condition(self, condition: str):
        btn = self.page.locator(f"button[aria-pressed]:has-text('{condition}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()