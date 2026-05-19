import pytest
from playwright.sync_api import Page, expect

from pages.fashion_page import PostFashionPage
from pages.login_page import LoginPage


def test_post_fashion(authenticated_page: Page):
    post_ad = PostFashionPage(authenticated_page)

    # Navigate
    post_ad.go_to_post_ad()

    # Upload + AI
    post_ad.upload_image(
        "/Users/apple1/Downloads/top.jpeg"
    )
    post_ad.wait_for_ai_processing()

    # Category
    post_ad.select_category()
    post_ad.select_subcategory("Women's Clothing")

    # Fashion matrix
    post_ad.select_gender("Women")
    post_ad.select_type("Top")
    post_ad.select_size("M")
    post_ad.select_condition("New")
    post_ad.fill_material("Cotton")

    # Common fields
    post_ad.fill_title("Cotton Women Top Medium")
    post_ad.fill_price("2500")
    post_ad.set_negotiable()

    # Location
    post_ad.select_wilaya("16")
    post_ad.fill_commune("Alger Centre")

    # Description
    post_ad.fill_description("Brand new cotton top, never worn, perfect condition.")

    # Publish
    post_ad.publish_listing()

    # Assert
    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)