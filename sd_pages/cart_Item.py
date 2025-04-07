from playwright.sync_api import Page
import pytest

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_buttons = page.locator(".btn_inventory")
        self.cart_icon = page.locator(".shopping_cart_link")
        
    @pytest.mark.smoke
    def add_first_item_to_cart(self):
        self.add_to_cart_buttons.first.click()

    def go_to_cart(self):
        self.cart_icon.click()
