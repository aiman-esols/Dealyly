import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="function")
def page(request):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context()

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        try:
            yield page

        finally:
            context.tracing.stop()
            context.close()
            browser.close()

@pytest.fixture(scope="function")
def authenticated_page(page):
    login = LoginPage(page)
    login.goto()
    login.open_login_modal()
    login.login("h.esolspk@gmail.com", "hassanesols")
    login.verify_login_success()
    return page