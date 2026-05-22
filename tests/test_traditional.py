from playwright.sync_api import Page, expect
from pages.traditional_page import PostTraditionalPage


def test_post_traditional(authenticated_page: Page):
    post_ad = PostTraditionalPage(authenticated_page)

    post_ad.go_to_post_ad()

    post_ad.upload_image(
        "/Users/apple1/Downloads/copper.jpeg"
    )
    post_ad.wait_for_ai_processing()

    post_ad.select_category()
    post_ad.select_subcategory("Copper & Brassware")

    post_ad.set_handmade(True)
    post_ad.fill_material("Brass")
    post_ad.select_condition("New")

    post_ad.fill_title("Handmade Brassware")
    post_ad.fill_price("45000")
    post_ad.set_negotiable()

    post_ad.select_wilaya("15")  # Tizi Ouzou
    post_ad.fill_commune("Tizi Ouzou")

    post_ad.fill_description("Authentic handmade Brassware, pure brass, traditional design.")

    post_ad.publish_listing()

    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)