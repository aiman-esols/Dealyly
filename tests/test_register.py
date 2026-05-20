from playwright.sync_api import Page

from pages.register_page import RegisterPage


def test_register(page: Page):
    register = RegisterPage(page)

    register.goto()
    register.open_login_modal()
    register.open_register_form()

    register.fill_details(
        full_name="Test User",
        email="dummy.esols@gmail.com",
        password="Test@2025"
    )

    register.click_next()
    register.click_get_started()
    register.verify_account_created()