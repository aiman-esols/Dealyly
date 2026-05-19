import pytest
from playwright.sync_api import Page, expect

from pages.edit_listing_page import EditListingPage


def test_edit_listing(authenticated_page: Page):
    edit = EditListingPage(authenticated_page)

    # Go to profile → my listings
    edit.go_to_profile()
    edit.go_to_my_listings()

    # Click edit on first listing
    edit.click_edit("yanmar")

    # Update price and description
    edit.update_wilaya("11")   # Tamanrasset
    edit.update_commune("Idles")
    edit.update_price("35000")
    edit.update_description("Updated description — price reduced, still in perfect condition.")

    # Save
    edit.save_changes()

    # Verify
    edit.verify_saved()