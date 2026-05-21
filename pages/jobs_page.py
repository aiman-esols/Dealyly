from playwright.sync_api import Page
from pages.base_page import BaseListingPage


class PostJobsPage(BaseListingPage):

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
        btn = self.page.locator("button[title='Jobs']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)


    def select_subcategory(self, subcategory: str):
        btn = self.page.locator(f"button.px-4:has-text('{subcategory}')").first
        btn.wait_for(state="visible", timeout=8000)
        if "border-primary" not in (btn.get_attribute("class") or ""):
            btn.click()
        self.page.wait_for_timeout(500)

    def select_job_mode(self, mode: str):
        # e.g. "Jobs Hiring", "Jobs Seeking"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{mode}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def select_job_type(self, job_type: str):
        # e.g. "Full-time", "Part-time", "Internship", "Remote"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{job_type}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def select_experience(self, experience: str):
        # e.g. "Entry (0–1 yr)", "Junior (1-3yr)", "Mid (3-5yr)", "Senior (5-10yrs)", "Expert (10+yrs)"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{experience}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def select_sector(self, sector: str):
        # e.g. "IT & Tech", "Healthcare", "Education", "Construction"
        btn = self.page.locator(f"button[aria-pressed]:has-text('{sector}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(300)

    def set_remote_ok(self, remote: bool = True):
        toggle = self.page.locator("button[aria-pressed]:has-text('Remote Ok')")
        toggle.wait_for(state="visible", timeout=8000)
        is_pressed = toggle.get_attribute("aria-pressed")
        if remote and is_pressed == "false":
            toggle.click()
        elif not remote and is_pressed == "true":
            toggle.click()
    

    def fill_salary(self, salary: str):
        field = self.page.locator("input[placeholder*='Salaire']")
        field.wait_for(state="visible", timeout=8000)
        field.fill(salary)
        field.press("Tab")
        self.page.wait_for_timeout(500)