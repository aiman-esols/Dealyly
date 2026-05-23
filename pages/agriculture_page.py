from playwright.sync_api import Page, expect
from pages.base_page import BaseListingPage


class PostAgriculturePage(BaseListingPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.upload_input = page.locator("#sec-photos input[type='file']")
        self.product = page.locator("input[placeholder*='Dates, Olives']")
        self.quantity = page.locator("input[inputmode='numeric'][min='0'][max='1000000']")
        self.origin = page.locator("input[placeholder*='Biskra']")

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
        btn = self.page.locator("button[title='Agriculture & Food']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(1000)

    def select_subcategory(self, subcategory: str):
        btn = self.page.locator(f"button.px-4:has-text('{subcategory}')").first
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()
        self.page.wait_for_timeout(500)

    def fill_product(self, product: str):
        self.product.wait_for(state="visible", timeout=8000)
        self.product.fill(product)

    def fill_quantity(self, quantity: str):
        self.quantity.wait_for(state="visible", timeout=8000)
        self.quantity.fill(quantity)

    def select_unit(self, unit: str):
        btn = self.page.locator(f"button[aria-pressed]:has-text('{unit}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def set_bio(self, bio: bool = True):
        toggle = self.page.locator("button[aria-pressed]:has-text('Bio')")
        toggle.wait_for(state="visible", timeout=8000)
        is_pressed = toggle.get_attribute("aria-pressed")
        if bio and is_pressed == "false":
            toggle.click()
        elif not bio and is_pressed == "true":
            toggle.click()

    def fill_origin(self, origin: str):
        self.origin.wait_for(state="visible", timeout=8000)
        self.origin.fill(origin)

    def go_to_price_step(self):
        self.page.locator("a[href='#sec-price']").click()
        self.page.wait_for_timeout(500)