import pytest
from playwright.sync_api import expect

from src.order_service import OrderService


pytestmark = pytest.mark.e2e


def test_order_created_by_service_is_visible_in_ui(page):
    service = OrderService()
    order = service.pay_order(service.create_order("Robert Joyce", 199.0).id)

    page.set_content(
        f"""
        <h1>Order details</h1>
        <dl>
          <dt>Customer</dt><dd>{order.customer}</dd>
          <dt>Status</dt><dd>{order.status}</dd>
          <dt>Total</dt><dd>${order.total}</dd>
        </dl>
        """
    )

    expect(page.get_by_text("Robert Joyce")).to_be_visible()
    expect(page.get_by_text("paid")).to_be_visible()
    expect(page.get_by_text("$199.0")).to_be_visible()
