from playwright.sync_api import Page, expect
from pages.farm_animals_page import PostFarmAnimalsPage


def test_post_farm_animals(authenticated_page: Page):
    post_ad = PostFarmAnimalsPage(authenticated_page)

    post_ad.go_to_post_ad()

    post_ad.upload_image(
        "/Users/apple1/Downloads/camel.jpeg"
    )
    post_ad.wait_for_ai_processing()

    post_ad.select_category()
    post_ad.select_species("Camel")
    post_ad.fill_breed("Ouled Djellal")
    post_ad.fill_age_months("12")
    post_ad.select_gender("Male")
    post_ad.set_vaccinated(True)

    post_ad.fill_title("Healthy Camel for Sale")
    post_ad.fill_price("350000")
    post_ad.set_negotiable()

    post_ad.select_wilaya("16")
    post_ad.fill_commune("Alger Centre")

    post_ad.fill_description("Healthy vaccinated camel, 12 months old, good breed.")

    post_ad.publish_listing()

    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)