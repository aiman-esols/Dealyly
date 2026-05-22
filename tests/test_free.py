from playwright.sync_api import Page, expect
from pages.free_page import PostGiveawayPage


def test_post_giveaway_ad(authenticated_page: Page):
    post_ad = PostGiveawayPage(authenticated_page)

    post_ad.go_to_post_ad()

    post_ad.upload_image(
        "/Users/apple1/Downloads/random.jpeg"
    )
    post_ad.wait_for_ai_processing()

    post_ad.select_category()
    post_ad.select_condition("Good")

    # No price — giveaway is free
    post_ad.fill_title("Free Books Collection")

    post_ad.select_wilaya("16")
    post_ad.fill_commune("Alger Centre")

    post_ad.fill_description("Giving away a collection of books for free, good condition.")

    post_ad.publish_listing()

    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)