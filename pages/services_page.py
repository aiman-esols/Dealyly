from playwright.sync_api import Page
from pages.base_page import BaseListingPage


class PostServicesPage(BaseListingPage):

    def __init__(self, page: Page):
        super().__init__(page)

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
        btn = self.page.locator("button[title='Services']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    def select_subcategory(self, subcategory: str):
        btn = self.page.locator(f"button.px-4:has-text('{subcategory}')").first
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()
        self.page.wait_for_timeout(500)

    def select_service_type(self, service_type: str):
        # e.g. "Tutoring", "Cleaning", "Transport", "Home Repair", "Beauty", "IT", "Event", "Other"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{service_type}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def select_service_area(self, area: str):
        # e.g. "Area Local", "Area Wilaya", "Area Nationwide"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{area}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def select_availability(self, availability: str):
        # e.g. "Anytime", "Weekdays", "Weekends", "By appointment"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{availability}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)
    
    def fill_price(self, price: str):
        field = self.page.locator("input[placeholder='Tarif']")
        field.wait_for(state="visible", timeout=8000)
        field.fill(price)
        field.press("Tab")
        self.page.wait_for_timeout(500)