import pytest


@pytest.fixture
def malicious_payloads() -> list[str]:
    return ["<script>alert(1)</script>", "' OR 1=1 --", "DROP TABLE users"]
