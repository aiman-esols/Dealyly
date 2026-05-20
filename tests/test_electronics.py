import pytest
from playwright.sync_api import Page, expect

from pages.electronics_ad_page import PostElectronicsPage
from pages.login_page import LoginPage


@pytest.mark.parametrize("subcategory, kind, brand, model, condition, storage, screen_size, warranty, title, price, wilaya, commune", [
    ("Audio & Headphones", "Audio", "Sony", "WH-1000XM5", "Like new", "N/A", "N/A", True, "Sony WH-1000XM5 Headphones", "45000", "16", "Alger Centre"),
])
def test_post_electronics_ad(authenticated_page: Page, subcategory, kind, brand, model, condition, storage, screen_size, warranty, title, price, wilaya, commune):
    post_ad = PostElectronicsPage(authenticated_page)

    # Navigate
    post_ad.go_to_post_ad()

    # Upload + AI
    post_ad.upload_image(
        "/Users/apple1/Downloads/headphones.jpg"
    )
    post_ad.wait_for_ai_processing()

    # Category
    post_ad.select_category()
    post_ad.select_subcategory(subcategory)

    # Electronics matrix
    post_ad.select_kind(kind)
    post_ad.select_brand(brand)
    post_ad.fill_model(model)
    post_ad.select_condition(condition)
    post_ad.fill_storage(storage)
    post_ad.fill_screen_size(screen_size)
    post_ad.set_warranty(warranty)

    # Common fields
    post_ad.fill_title(title)
    post_ad.fill_price(price)
    post_ad.set_negotiable()

    # Location
    post_ad.select_wilaya(wilaya)
    post_ad.fill_commune(commune)

    # Description
    post_ad.generate_ai_description()

    # Publish
    post_ad.publish_listing()

    # Assert
    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)