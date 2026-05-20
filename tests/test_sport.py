from playwright.sync_api import Page, expect

from pages.sports_page import PostSportsPage


def test_sports(authenticated_page: Page):
    post_ad = PostSportsPage(authenticated_page)

    # Navigate
    post_ad.go_to_post_ad()

    # Upload + AI
    post_ad.upload_image(
        "/Users/apple1/Downloads/nikee.jpeg"
    )
    post_ad.wait_for_ai_processing()

    # Category
    post_ad.select_category()
    post_ad.select_subcategory("Fitness Equipment")

    # Matrix fields
    post_ad.select_type("Fitness")
    post_ad.fill_brand("Nike")
    post_ad.select_condition("New")

    # Common fields — from BaseListingPage
    post_ad.fill_title("Nike Fitness Equipment")
    post_ad.fill_price("15000")
    post_ad.set_negotiable()

    # Location
    post_ad.select_wilaya("14")
    post_ad.fill_commune("Sebt")

    # Description
    post_ad.fill_description("Brand new Nike fitness equipment, never used.")

    # Publish
    post_ad.publish_listing()

    # Assert
    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)