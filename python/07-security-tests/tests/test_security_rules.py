import pytest

from src.security_rules import can_access_order, is_safe_search_query


pytestmark = pytest.mark.security


def test_malicious_search_payloads_are_rejected(malicious_payloads):
    for payload in malicious_payloads:
        assert is_safe_search_query(payload) is False


def test_user_cannot_access_another_users_order():
    assert can_access_order(user_id="user-1", order_owner_id="user-2", role="customer") is False


def test_admin_can_access_any_order():
    assert can_access_order(user_id="admin-1", order_owner_id="user-2", role="admin") is True
