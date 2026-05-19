from playwright.sync_api import Page

from pages.profile_page import ProfilePage


def test_update_profile(authenticated_page: Page):
    profile = ProfilePage(authenticated_page)

    # Navigate to settings
    profile.go_to_profile()
    profile.go_to_settings()

    # Update fields
    profile.update_full_name("Hassan Esols Updated")
    profile.select_province("16 - Alger")

    # Save
    profile.save_changes()

    # Verify
    profile.verify_saved("Hassan Esols Updated")