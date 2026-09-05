import pytest


@pytest.fixture
def failure_log() -> str:
    return "Timeout while waiting for order status"
