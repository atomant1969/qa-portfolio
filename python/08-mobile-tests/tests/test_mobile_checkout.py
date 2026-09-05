import pytest
from playwright.sync_api import expect


pytestmark = pytest.mark.mobile


def test_mobile_checkout_button_remains_visible(mobile_page):
    mobile_page.set_content(
        """
        <main style="max-width: 390px">
          <h1>Cart</h1>
          <p>QA Automation Toolkit</p>
          <button aria-label="Checkout">Checkout</button>
        </main>
        """
    )

    expect(mobile_page.get_by_label("Checkout")).to_be_visible()
