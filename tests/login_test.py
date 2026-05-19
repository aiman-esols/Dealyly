from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_login(authenticated_page: Page):
    # If authenticated_page works, login was successful
    login = LoginPage(authenticated_page)
    login.verify_login_success()