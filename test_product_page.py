from .pages.product_page import ProductPage
import pytest

links = [
    f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10)
]
# Помечаю падающие страницы
links[7] = pytest.param(links[7], marks=pytest.mark.xfail)


@pytest.mark.parametrize("link", links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.test_add_to_basket()
