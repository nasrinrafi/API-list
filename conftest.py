import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def api_request_context(playwright: Playwright):
    """ساخت یک کانتکست اختصاصی برای درخواست‌های API"""
    request_context = playwright.request.new_context(
        base_url="https://automationexercise.com"
    )
    yield request_context
    request_context.dispose()