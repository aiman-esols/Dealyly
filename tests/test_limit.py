from playwright.sync_api import Page, expect
from pages.post_ad_page import PostAdPage


def test_publish_limit_reached(authenticated_page: Page):
    post_ad = PostAdPage(authenticated_page)

    post_ad.go_to_post_ad()
    post_ad.upload_image(
        "/Users/apple1/Downloads/A-Guide-to-Electric-Cars-in-Pakistan-Featured-Image.png"
    )
    post_ad.wait_for_ai_processing()

    post_ad.select_category("Vehicles")
    post_ad.select_subcategory("Cars")
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

    post_ad.fill_title("Audi E-Tron GT 2023")
    post_ad.fill_price("25000")
    post_ad.set_negotiable()

    post_ad.select_wilaya("2")
    post_ad.fill_commune("Ain Merane")
    post_ad.fill_description("Well maintained car, single owner, no accidents.")

    # Assert limit message appears instead of successful publish
    expect(authenticated_page.locator(
        "text=Daily publish limit reached"
    )).to_be_visible(timeout=10000)