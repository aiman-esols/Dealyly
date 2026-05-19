from playwright.sync_api import Page

from pages.favorites_page import FavouritesPage


def test_favorites(authenticated_page: Page):
    fav = FavouritesPage(authenticated_page)

    # Go to home and add first listing to favourites
    fav.goto_home()
    fav.add_to_favourites()
    fav.verify_favourite_added()

    # Go to favourites page and verify listing appears
    fav.goto_favourites()
    fav.verify_favourites_page()