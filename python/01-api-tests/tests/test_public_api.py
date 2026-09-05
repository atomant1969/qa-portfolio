import os

import pytest
import requests


pytestmark = pytest.mark.external


def public_api_enabled() -> bool:
    return os.getenv("RUN_PUBLIC_API_TESTS") == "1"


@pytest.mark.skipif(
    not public_api_enabled(),
    reason="Set RUN_PUBLIC_API_TESTS=1 to run third-party API checks.",
)
def test_jsonplaceholder_post_contract():
    """Validate a stable public API contract without making CI depend on it.

    EN: External API tests are useful portfolio evidence, but should be opt-in.
    RU: Тесты внешних API полезны для портфолио, но должны запускаться явно.
    """
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10,
    )

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["userId"] == 1
    assert isinstance(body["title"], str)
    assert isinstance(body["body"], str)
