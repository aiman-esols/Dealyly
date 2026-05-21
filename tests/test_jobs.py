from playwright.sync_api import Page, expect
from pages.jobs_page import PostJobsPage


def test_post_jobs_ad(authenticated_page: Page):
    post_ad = PostJobsPage(authenticated_page)

    # Navigate
    post_ad.go_to_post_ad()

    # Upload + AI
    post_ad.upload_image(
        "/Users/apple1/Downloads/job.png"
    )
    post_ad.wait_for_ai_processing()

    # Category
    post_ad.select_category()
    post_ad.select_subcategory("IT & Tech")

    # Matrix fields
    post_ad.select_job_mode("Jobs Hiring")
    post_ad.select_job_type("Full-time")
    post_ad.select_experience("Junior (1–3 yr)")
    post_ad.select_sector("IT & Tech")
    post_ad.set_remote_ok(True)

    # Common fields
    post_ad.fill_title("Senior Python Developer")
    post_ad.fill_salary("150000")

    # Location
    post_ad.select_wilaya("16")
    post_ad.fill_commune("Alger Centre")

    # Description
    post_ad.fill_description("Looking for a Senior Python Developer with 3-5 years experience.")

    # Publish
    post_ad.publish_listing()

    # Assert
    expect(authenticated_page.locator(
        "[class*='success'], [class*='confirmation'], h1:has-text('published')"
    ).first).to_be_visible(timeout=10000)