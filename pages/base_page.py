from playwright.sync_api import Page, expect


class BaseListingPage:

    def __init__(self, page: Page):
        self.page = page

        self.wilaya = page.locator("select:has(option[value='2'])")
        self.commune = page.locator("input[placeholder*='Commencez']")
        self.title = page.locator("input[placeholder='Or type your own…']")
        self.price = page.locator("input[placeholder='0']")
        self.description = page.locator("textarea[placeholder*='Decrivez']")
        self.ai_description_btn = page.locator("button:has(.lucide-sparkles)")
        self.publish_btn = page.locator("button:has-text('Publish listing')")
        self.draft_btn = page.locator("button:has-text('Save as draft')")

    def fill_title(self, title: str):
        self.title.wait_for(state="visible", timeout=8000)
        self.title.fill(title)

    def fill_price(self, price: str):
        self.price.wait_for(state="visible", timeout=8000)
        self.price.fill(price)

    def set_negotiable(self):
        self.page.locator("button.rounded-full:has-text('Negotiable')").click()

    def select_wilaya(self, wilaya_value: str):
        self.wilaya.wait_for(state="visible", timeout=8000)
        self.wilaya.select_option(value=wilaya_value)
        self.page.wait_for_timeout(500)

    def fill_commune(self, commune: str):
        self.commune.wait_for(state="visible", timeout=8000)
        self.commune.fill(commune)
        self.page.locator(f"button.text-start:has-text('{commune}')").first.wait_for(state="visible", timeout=8000)
        self.page.locator(f"button.text-start:has-text('{commune}')").first.click()

    def fill_description(self, text: str):
        self.description.wait_for(state="visible", timeout=8000)
        self.description.fill(text)

    def generate_ai_description(self):
        self.ai_description_btn.wait_for(state="visible", timeout=8000)
        self.ai_description_btn.click()
        self.page.wait_for_timeout(5000)
        expect(self.description).not_to_be_empty(timeout=15000)

    def publish_listing(self):
        self.publish_btn.wait_for(state="visible", timeout=8000)
        self.publish_btn.click()

    def save_as_draft(self):
        self.draft_btn.wait_for(state="visible", timeout=8000)
        self.draft_btn.click()