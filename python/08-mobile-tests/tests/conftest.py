import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def mobile_page():
    with sync_playwright() as playwright:
        iphone = playwright.devices["iPhone 13"]
        browser = playwright.chromium.launch()
        context = browser.new_context(**iphone)
        page = context.new_page()
        yield page
        browser.close()
