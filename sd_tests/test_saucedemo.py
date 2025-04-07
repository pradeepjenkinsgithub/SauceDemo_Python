import pytest
from playwright.sync_api import sync_playwright
from sd_pages.login import LoginPage
from sd_pages.cart_Item import InventoryPage
from sd_pages.checkout_cart import CartPage
from sd_pages.checkout_data import CheckoutPage
from sd_pages.logout import LogoutPage
import json

with open('testdata.json') as rfile:
    test_data = json.load(rfile)

@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def test_saucedemo_flow(setup):
    page = setup
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login(test_data["user"]["username"], test_data["user"]["password"])

    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_information(
        test_data["checkout"]["first_name"],
        test_data["checkout"]["last_name"],
        test_data["checkout"]["postal_code"]
    )
    checkout_page.finish_checkout()

    logout_page = LogoutPage(page)
    logout_page.logout()
