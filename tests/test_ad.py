import pytest
from playwright.sync_api import Page, expect

from pages.post_ad_page import PostAdPage
from pages.login_page import LoginPage


@pytest.fixture
def authenticated_page(page: Page):
    login = LoginPage(page)
    login.goto()
    login.open_login_modal()
    login.login("aiman.esols@gmail.com", "Aiman@2025")
    login.verify_login_success()
    return page


def test_post_car_ad(authenticated_page: Page):
    post_ad = PostAdPage(authenticated_page)

    # Navigate
    post_ad.go_to_post_ad()

    # Upload image + wait for AI
    post_ad.upload_image(
        "/Users/apple1/Downloads/A-Guide-to-Electric-Cars-in-Pakistan-Featured-Image.png"
    )
    post_ad.wait_for_ai_processing()

    # Category
    post_ad.select_category("Vehicles")
    post_ad.select_subcategory("Cars")

    # Car matrix
    post_ad.select_brand("Audi")
    post_ad.fill_model("E-Tron GT")
    post_ad.fill_version("GT")
    post_ad.fill_engine("2.0 V6")
    post_ad.fill_year("2023")
    post_ad.select_condition("New")
    post_ad.select_fuel("Petrol")
    post_ad.select_transmission("Manual")
    post_ad.select_color("Grey")
    post_ad.fill_mileage("5000")

    # Title & price
    post_ad.fill_title("Audi E-Tron GT 2023")
    post_ad.fill_price("25000")
    post_ad.set_negotiable()

    # Location
    post_ad.select_wilaya("2")       # 02 — Chlef
    post_ad.fill_commune("Ain Merane")

    # Description
    post_ad.fill_description("Well maintained car, single owner, no accidents.")

    # Publish
    post_ad.publish_listing()

    # Assert success
    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)