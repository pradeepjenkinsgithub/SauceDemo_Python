from playwright.sync_api import Page
import pytest

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
    
    @pytest.mark.regression
    def proceed_to_checkout(self):
        self.checkout_button.click()
