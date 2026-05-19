from playwright.sync_api import Page, expect


class FavouritesPage:

    def __init__(self, page: Page):
        self.page = page

        self.favourites_link = page.locator("header a[href='/en/compte/favoris']")
        # Heart button on first listing card
        self.heart_btn = page.locator("span:has(.lucide-heart)").first

    # ── NAVIGATION ────────────────────────────────────────────────────────────

    def goto_home(self):
        self.page.goto("https://dealyly.com/en")
        self.page.wait_for_load_state("domcontentloaded")

    def goto_favourites(self):
        self.favourites_link.wait_for(state="visible", timeout=8000)
        self.favourites_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    # ── ACTIONS ───────────────────────────────────────────────────────────────

    def add_to_favourites(self):
        listing = self.page.locator("div.bg-surface.rounded-3xl:has(a:has-text('huawei Honor 10'))")
        listing.scroll_into_view_if_needed()
        heart = listing.locator("span:has(.lucide-heart)").nth(2) #3rd lsiitng we can use .first for 1st lisitng
        heart.wait_for(state="visible", timeout=8000)
        heart.click()
        self.page.wait_for_timeout(1000)


    # ── VERIFY ────────────────────────────────────────────────────────────────

    def verify_favourite_added(self):
        # Heart should be filled/red after clicking
        expect(self.page.locator(
            "span:has(.lucide-heart) svg.text-red-500, span:has(.lucide-heart) svg[fill='red'], span:has(.lucide-heart) svg.text-error"
        ).first).to_be_visible(timeout=8000)

    def verify_favourites_page(self):
        expect(self.page).to_have_url("https://dealyly.com/en/compte/favoris", timeout=8000)
        expect(self.page.locator("img[alt*='- 1']").first).to_be_visible(timeout=8000)