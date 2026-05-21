from playwright.sync_api import Page, expect
from pages.pet_page import PostPetsPage


def test_post_pets_ad(authenticated_page: Page):
    post_ad = PostPetsPage(authenticated_page)

    # Navigate
    post_ad.go_to_post_ad()

    # Upload + AI
    post_ad.upload_image(
        "/Users/apple1/Downloads/golden.jpeg"
    )
    post_ad.wait_for_ai_processing()

    # Category
    post_ad.select_category()
    post_ad.select_subcategory("Dogs")

    # Matrix fields
    post_ad.select_species("Dog")
    post_ad.fill_breed("Golden Retriever")
    post_ad.fill_age_months("6")
    post_ad.select_gender("Male")
    post_ad.set_vaccinated(True)
    post_ad.set_papers(True)

    # Common fields
    post_ad.fill_title("Golden Retriever Puppy 6 Months")
    post_ad.fill_price("25000")
    post_ad.set_negotiable()

    # Location
    post_ad.select_wilaya("16")
    post_ad.fill_commune("Alger Centre")

    # Description
    post_ad.fill_description("Healthy Golden Retriever puppy, vaccinated, with papers.")

    # Publish
    post_ad.publish_listing()

    # Assert
    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)