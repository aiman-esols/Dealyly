from playwright.sync_api import Page
from pages.base_page import BaseListingPage


class PostTraditionalPage(BaseListingPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.upload_input = page.locator("#sec-photos input[type='file']")
        self.material = page.locator("input[placeholder*='Wool']")

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
        btn = self.page.locator("button[title='Traditional & Artisanal']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    def select_subcategory(self, subcategory: str):
        btn = self.page.locator(f"button.px-4:has-text('{subcategory}')").first
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()
        self.page.wait_for_timeout(500)

    def set_handmade(self, handmade: bool = True):
        toggle = self.page.locator("button[aria-pressed]:has-text('Handmade')")
        toggle.wait_for(state="visible", timeout=8000)
        is_pressed = toggle.get_attribute("aria-pressed")
        if handmade and is_pressed == "false":
            toggle.click()
        elif not handmade and is_pressed == "true":
            toggle.click()

    def fill_material(self, material: str):
        self.material.wait_for(state="visible", timeout=8000)
        self.material.fill(material)

    def select_condition(self, condition: str):
        btn = self.page.locator(f"button[aria-pressed]:has-text('{condition}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()