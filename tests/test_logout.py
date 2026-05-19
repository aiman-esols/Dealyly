import pytest
from playwright.sync_api import Page, expect

from pages.logout_page import LogoutPage

def test_logout(authenticated_page: Page):
    logout = LogoutPage(authenticated_page)

    logout.go_to_profile()
    logout.logout()
    logout.verify_logout()