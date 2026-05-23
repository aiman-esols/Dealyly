from playwright.sync_api import Page, expect
from pages.agriculture_page import PostAgriculturePage


def test_post_agriculture_ad(authenticated_page: Page):
    post_ad = PostAgriculturePage(authenticated_page)

    post_ad.go_to_post_ad()

    post_ad.upload_image(
        "/Users/apple1/Downloads/date.jpeg"
    )
    post_ad.wait_for_ai_processing()

    # Force correct category regardless of AI detection
    post_ad.select_category()
    post_ad.select_subcategory("Dates (Deglet Nour)")

    post_ad.fill_product("Deglet Nour Dates")
    post_ad.fill_quantity("100")
    post_ad.select_unit("Kilogram (kg)")
    post_ad.set_bio(True)
    post_ad.fill_origin("Biskra")

    post_ad.fill_title("Premium Deglet Nour Dates from Biskra")
    post_ad.go_to_price_step()
    post_ad.fill_price("5000")
    

    post_ad.select_wilaya("7")
    post_ad.fill_commune("Chetma")

    post_ad.fill_description("Fresh premium quality Deglet Nour dates directly from Biskra farms.")

    post_ad.publish_listing()

    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)