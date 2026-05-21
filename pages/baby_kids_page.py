from playwright.sync_api import Page
from pages.base_page import BaseListingPage


class PostBabyKidsPage(BaseListingPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.post_ad_btn = page.locator("a[href='/en/deposer']")
        self.upload_input = page.locator("#sec-photos input[type='file']")

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
        btn = self.page.locator("button[title='Baby & Kids']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    def select_subcategory(self, subcategory: str):
        btn = self.page.get_by_role("button", name=subcategory, exact=True)
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()
        self.page.wait_for_timeout(500)

    def select_age_group(self, age: str):
        # e.g. "0 6m", "6 12m", "1 2y", "2 5y", "5 10y", "10plus"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{age}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def select_gender(self, gender: str):
        # e.g. "Boy", "Girl", "Unisex"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{gender}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def select_type(self, item_type: str):
        # e.g. "Stroller", "Crib", "Car seat", "Toy", "Clothing", "Other"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{item_type}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def select_condition(self, condition: str):
        # e.g. "New", "Like new", "Good", "Fair", "Needs repair"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{condition}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        