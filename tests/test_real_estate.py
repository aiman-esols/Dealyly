import pytest
from playwright.sync_api import Page, expect

from pages.real_estate_ad_page import PostRealEstatePage
from pages.login_page import LoginPage



def test_post_vacation_rental(authenticated_page: Page):
    post_ad = PostRealEstatePage(authenticated_page)

    # Navigate
    post_ad.go_to_post_ad()

    # Upload image + wait for AI
    post_ad.upload_image(
        "/Users/apple1/Documents/Screenshot 2026-05-18 at 4.40.48 PM.png"
    )
    post_ad.wait_for_ai_processing()

    # Category
    post_ad.select_category()
    #post_ad.select_subcategory()

    # Real estate matrix
    post_ad.select_usage("Rent")
    post_ad.select_use_type("Residential")
    post_ad.select_property_type("Villa")
    post_ad.select_rooms("F4")
    post_ad.fill_bathrooms("2")
    post_ad.fill_surface("180")
    post_ad.fill_built_surface("160")
    post_ad.fill_floor("3")
    #post_ad.set_furnished(True)
    #post_ad.select_rental_period("Monthly")
    post_ad.select_condition("New")
    post_ad.select_features(["Parking", "Elevator", "Balcony", "Pool"])

    # Title & price
    post_ad.fill_title("Luxury Villa for Sale")
    post_ad.fill_price("50000")
    post_ad.set_negotiable()

    # Location
    post_ad.select_wilaya("16")  # Alger
    post_ad.fill_commune("Alger Centre")

    # AI description
    post_ad.generate_ai_description()

    # Save as draft
    post_ad.publish_listing()

# Assert published
    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published'), h1:has-text('success')"
        ).first).to_be_visible(timeout=10000)