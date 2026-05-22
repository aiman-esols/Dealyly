from playwright.sync_api import Page, expect
from pages.services_page import PostServicesPage


def test_post_services_ad(authenticated_page: Page):
    post_ad = PostServicesPage(authenticated_page)

    post_ad.go_to_post_ad()

    post_ad.upload_image(
        "/Users/apple1/Downloads/tutoring.jpeg"
    )
    post_ad.wait_for_ai_processing()

    post_ad.select_category()
    post_ad.select_subcategory("Private Tutoring")

    post_ad.select_service_type("Tutoring")
    post_ad.select_service_area("Area Local")
    post_ad.select_availability("Weekends")

    post_ad.fill_title("Math Tutoring for High School Students")
    post_ad.fill_price("2000")
    
    post_ad.select_wilaya("16")
    post_ad.fill_commune("Alger Centre")

    post_ad.fill_description("Experienced math tutor available on weekends for high school students.")

    post_ad.publish_listing()

    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)