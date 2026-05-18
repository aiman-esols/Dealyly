from playwright.sync_api import Page, expect


class PostAdPage:

    def __init__(self, page: Page):
        self.page = page

        self.post_ad_btn = page.locator("a[href='/en/deposer']")
        self.upload_input = page.locator("#sec-photos input[type='file']")

        # Wilaya is a real <select>, commune is a text input
        self.wilaya = page.locator("select:has(option[value='2'])")
        self.commune = page.locator("input[placeholder*='Commencez']")

        # Title manual input
        self.title = page.locator("input[placeholder='Or type your own…']")

        # Price input
        self.price = page.locator("input[placeholder='0']")

        # Description textarea
        self.description = page.locator("textarea[placeholder*='Decrivez']")

        # AI description generate button
        self.ai_description_btn = page.locator("button:has(.lucide-sparkles)")

        # Submit buttons
        self.publish_btn = page.locator("button:has-text('Publish listing')")
        self.draft_btn = page.locator("button:has-text('Save as draft')")

    # ── NAVIGATION ────────────────────────────────────────────────────────────

    def go_to_post_ad(self):
        self.post_ad_btn.wait_for(state="visible", timeout=8000)
        self.post_ad_btn.click()
        self.page.wait_for_load_state("networkidle")

    # ── IMAGE UPLOAD ──────────────────────────────────────────────────────────

    def upload_image(self, image_path: str):
        self.upload_input.wait_for(state="attached", timeout=10000)
        self.upload_input.set_input_files(image_path)

    def wait_for_ai_processing(self):
        # Wait for spinner/loader to disappear after image upload
        try:
            self.page.locator("[class*='loading'], [class*='spinner'], [class*='loader']").first.wait_for(
                state="hidden", timeout=20000
            )
        except Exception:
            pass
        self.page.wait_for_timeout(3000)

    # ── CATEGORY — pill buttons, not <select> ─────────────────────────────────

    def select_category(self, category_name: str):
        btn = self.page.locator(f"button[title='{category_name}']")
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    def select_subcategory(self, subcategory_name: str):
        btn = self.page.locator(f"button.rounded-full:has-text('{subcategory_name}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()
        self.page.wait_for_timeout(500)

    # ── CAR MATRIX FIELDS — all pill buttons or text inputs ──────────────────

    def select_brand(self, brand: str):
        btn = self.page.locator(f"button.rounded-full:has-text('{brand}')").first
        btn.wait_for(state="visible", timeout=8000)
        btn.click()

    def fill_model(self, model: str):
        # First plain text input with no placeholder (model field)
        field = self.page.locator("input[type='text'][value='']").first
        field.wait_for(state="visible", timeout=8000)
        field.fill(model)

    def fill_version(self, version: str):
        self.page.locator("input[placeholder*='GTI']").fill(version)

    def fill_engine(self, engine: str):
        self.page.locator("input[placeholder*='1.6 TDI']").fill(engine)

    def fill_year(self, year: str):
        self.page.locator("input[aria-label='Year']").fill(year)

    def select_condition(self, condition: str):
        # e.g. "New", "Used"
        self.page.locator(f"button.rounded-full:has-text('{condition}')").first.click()

    def select_fuel(self, fuel: str):
        # e.g. "Petrol", "Diesel", "Electric"
        self.page.locator(f"button.rounded-full:has-text('{fuel}')").first.click()

    def select_transmission(self, transmission: str):
        # e.g. "Manual", "Automatic"
        self.page.locator(f"button.rounded-full:has-text('{transmission}')").first.click()

    def select_color(self, color: str):
        # e.g. "Grey", "Black", "White"
        self.page.locator(f"button.rounded-full:has-text('{color}')").first.click()

    def fill_mileage(self, mileage: str):
        self.page.locator("input[type='number']").first.fill(mileage)

    # ── COMMON FIELDS ─────────────────────────────────────────────────────────

    def fill_title(self, title: str):
        self.title.wait_for(state="visible", timeout=8000)
        self.title.fill(title)

    def fill_price(self, price: str):
        self.price.wait_for(state="visible", timeout=8000)
        self.price.fill(price)

    def set_negotiable(self):
        self.page.locator("button.rounded-full:has-text('Negotiable')").click()

    # ── LOCATION ──────────────────────────────────────────────────────────────

    def select_wilaya(self, wilaya_value: str):
        # Pass the option value e.g. "2" for Chlef
        self.wilaya.wait_for(state="visible", timeout=8000)
        self.wilaya.select_option(value=wilaya_value)
        self.page.wait_for_timeout(500)  # wait for commune input to enable

    def fill_commune(self, commune: str):
        self.commune.wait_for(state="visible", timeout=8000)
        self.commune.fill(commune)
        # Dropdown items are buttons
        self.page.locator(f"button.text-start:has-text('{commune}')").first.wait_for(state="visible", timeout=8000)
        self.page.locator(f"button.text-start:has-text('{commune}')").first.click()

    # ── DESCRIPTION ───────────────────────────────────────────────────────────

    def fill_description(self, text: str):
        self.description.wait_for(state="visible", timeout=8000)
        self.description.fill(text)

    def generate_ai_description(self):
        self.ai_description_btn.wait_for(state="visible", timeout=8000)
        self.ai_description_btn.click()
        # Wait until textarea has content
        self.page.wait_for_function(
            "document.querySelector('textarea') && document.querySelector('textarea').value.length > 0",
            timeout=20000
        )

    # ── SUBMIT ────────────────────────────────────────────────────────────────

    def publish_listing(self):
        # Wait for publish button to become enabled
        self.page.wait_for_function(
            "!document.querySelector('button:disabled') || "
            "Array.from(document.querySelectorAll('button')).some(b => b.textContent.includes('Publish') && !b.disabled)",
            timeout=10000
        )
        self.publish_btn.wait_for(state="visible", timeout=8000)
        self.publish_btn.click()

    def save_as_draft(self):
        self.draft_btn.wait_for(state="visible", timeout=8000)
        self.draft_btn.click()