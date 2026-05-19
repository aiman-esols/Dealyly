import pytest
from playwright.sync_api import Page, expect

from pages.search_page import SearchPage


def test_search(page: Page):
    search = SearchPage(page)

    search.goto()
    search.search("car")
    search.verify_results("car")