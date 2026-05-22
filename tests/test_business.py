from playwright.sync_api import Page, expect
from pages.business_page import PostBusinessPage


def test_post_business_ad(authenticated_page: Page):
    post_ad = PostBusinessPage(authenticated_page)

    post_ad.go_to_post_ad()

    post_ad.upload_image(
        "/Users/apple1/Downloads/office.jpeg"
    )
    post_ad.wait_for_ai_processing()

    post_ad.select_category()
    post_ad.select_subcategory("Office Furniture & Supplies")

    post_ad.fill_type("Office Chair")
    post_ad.fill_brand("Ikea")
    post_ad.select_condition("New")

    post_ad.fill_title("Ikea Office Chair Brand New")
    post_ad.fill_price("25000")
    post_ad.set_negotiable()

    post_ad.select_wilaya("16")
    post_ad.fill_commune("Alger Centre")

    post_ad.fill_description("Brand new Ikea office chair, ergonomic design, never used.")

    post_ad.publish_listing()

    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)