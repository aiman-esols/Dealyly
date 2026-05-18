import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.goto()
    return lp


def test_login(login_page: LoginPage):
    login_page.open_login_modal()
    login_page.login("aiman.esols@gmail.com", "Aiman@2025")
    login_page.verify_login_success()