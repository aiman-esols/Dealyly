import pytest
from playwright.sync_api import Page, expect

from pages.home_garden_page import PostHomeGardenPage
from pages.login_page import LoginPage



def test_post_home_garden(authenticated_page: Page):
    post_ad = PostHomeGardenPage(authenticated_page)

    # Navigate
    post_ad.go_to_post_ad()

    # Upload + AI
    post_ad.upload_image(
        "/Users/apple1/Downloads/fridge.jpg"
    )
    post_ad.wait_for_ai_processing()

    # Category
    post_ad.select_category()
    post_ad.select_subcategory("Appliances")

    # Matrix fields
    post_ad.select_type("Refrigerator")
    post_ad.fill_brand("Samsung")
    post_ad.select_condition("New")

    # Common fields
    post_ad.fill_title("Samsung Refrigerator 400L")
    post_ad.fill_price("85000")
    post_ad.set_negotiable()

    # Location
    post_ad.select_wilaya("5")
    post_ad.fill_commune("Arris")

    # Description
    # Description
    post_ad.fill_description("Brand new Samsung refrigerator 400L, never used, perfect condition.")

    # Publish
    post_ad.publish_listing()

    # Assert
    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)