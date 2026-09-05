FORBIDDEN_PATTERNS = ["<script", "drop table", "--", " or 1=1"]


def is_safe_search_query(value: str) -> bool:
    normalized = value.lower()
    return all(pattern not in normalized for pattern in FORBIDDEN_PATTERNS)


def can_access_order(user_id: str, order_owner_id: str, role: str) -> bool:
    return role == "admin" or user_id == order_owner_id
