from playwright.sync_api import Page
from pages.base_page import BaseListingPage


class PostFarmAnimalsPage(BaseListingPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.upload_input = page.locator("#sec-photos input[type='file']")
        self.breed = page.locator("input[placeholder*='Ouled']")
        self.age_months = page.locator("input[inputmode='numeric'][min='0'][max='360']")

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
        btn = self.page.locator("button[title='Farm Animals']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    def select_species(self, species: str):
        # e.g. "Sheep", "Goat", "Cattle", "Horse", "Donkey", "Camel", "Poultry"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{species}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def fill_breed(self, breed: str):
        self.breed.wait_for(state="visible", timeout=8000)
        self.breed.fill(breed)

    def fill_age_months(self, months: str):
        self.age_months.wait_for(state="visible", timeout=8000)
        self.age_months.fill(months)

    def select_gender(self, gender: str):
        btn = self.page.locator(f"button[aria-pressed]:has-text('{gender}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def set_vaccinated(self, vaccinated: bool = True):
        toggle = self.page.locator("button[aria-pressed]:has-text('Vaccinated')")
        toggle.wait_for(state="visible", timeout=8000)
        is_pressed = toggle.get_attribute("aria-pressed")
        if vaccinated and is_pressed == "false":
            toggle.click()
        elif not vaccinated and is_pressed == "true":
            toggle.click()