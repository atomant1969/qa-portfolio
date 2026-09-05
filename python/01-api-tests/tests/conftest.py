import json
from pathlib import Path
from typing import Any

import pytest
from fastapi.testclient import TestClient

from qa_store_api.main import app, orders
from support.api_client import StoreApiClient


@pytest.fixture
def raw_client() -> TestClient:
    # EN: Reset in-memory state so tests stay independent.
    # RU: Сбрасываем состояние в памяти, чтобы тесты были независимыми.
    orders.clear()
    return TestClient(app)


@pytest.fixture
def api_client(raw_client: TestClient) -> StoreApiClient:
    return StoreApiClient(raw_client)


@pytest.fixture
def auth_headers(api_client: StoreApiClient) -> dict[str, str]:
    token = api_client.login("qa.engineer", "correct-password").json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def test_data() -> dict[str, Any]:
    path = Path(__file__).parent / "data" / "orders.json"
    return json.loads(path.read_text(encoding="utf-8"))
