from playwright.sync_api import Page, expect


class SearchPage:

    def __init__(self, page: Page):
        self.page = page

        self.search_input = page.locator("input[aria-label='Search on Dealyly']")
        self.search_btn = page.locator("button[aria-label='Search']")
        self.results = page.locator("img[alt*='- 1']")

    def goto(self):
        self.page.goto("https://dealyly.com/en")
        self.page.wait_for_load_state("domcontentloaded")

    def search(self, query: str):
        self.search_input.wait_for(state="visible", timeout=8000)
        self.search_input.fill(query)
        self.search_btn.click()
        self.page.wait_for_load_state("domcontentloaded")

    def verify_results(self, query: str):
        # Verify search chip appears
        expect(self.page.locator(f"span:has-text('{query}')").first).to_be_visible(timeout=8000)
        # Verify at least one result image appears
        expect(self.results.first).to_be_visible(timeout=8000)