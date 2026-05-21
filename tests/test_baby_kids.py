from playwright.sync_api import Page, expect
from pages.baby_kids_page import PostBabyKidsPage


def test_post_baby_kids(authenticated_page: Page):
    post_ad = PostBabyKidsPage(authenticated_page)

    # Navigate
    post_ad.go_to_post_ad()

    # Upload + AI
    post_ad.upload_image(
        "/Users/apple1/Downloads/toy.jpeg"
    )
    post_ad.wait_for_ai_processing()

    # Category
    post_ad.select_category()
    post_ad.select_subcategory("Toys")

    # Matrix fields
    post_ad.select_age_group("2 5y")
    post_ad.select_gender("Unisex")
    post_ad.select_type("Toy")
    post_ad.select_condition("New")

    # Common fields
    post_ad.fill_title("Kids Toy Set 2-5 Years")
    post_ad.fill_price("3500")
    post_ad.set_negotiable()

    # Location
    post_ad.select_wilaya("16")
    post_ad.fill_commune("Alger Centre")

    # Description
    post_ad.fill_description("Brand new toy set for kids aged 2-5 years, educational and fun.")

    # Publish
    post_ad.publish_listing()

    # Assert
    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)