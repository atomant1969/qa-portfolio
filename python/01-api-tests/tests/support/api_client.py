from __future__ import annotations

from typing import Any

from fastapi.testclient import TestClient
from httpx import Response


class StoreApiClient:
    def __init__(self, client: TestClient) -> None:
        self.client = client

    def login(self, username: str, password: str) -> Response:
        return self.client.post(
            "/auth/login",
            json={"username": username, "password": password},
        )

    def list_products(self, **params: Any) -> Response:
        return self.client.get("/products", params=params)

    def get_product(self, product_id: int) -> Response:
        return self.client.get(f"/products/{product_id}")

    def create_order(self, payload: dict[str, Any], headers: dict[str, str] | None = None) -> Response:
        return self.client.post("/orders", json=payload, headers=headers)

    def list_orders(self, headers: dict[str, str], **params: Any) -> Response:
        return self.client.get("/orders", params=params, headers=headers)

    def get_order(self, order_id: str, headers: dict[str, str]) -> Response:
        return self.client.get(f"/orders/{order_id}", headers=headers)

    def update_order_status(self, order_id: str, new_status: str, headers: dict[str, str]) -> Response:
        return self.client.patch(
            f"/orders/{order_id}/status",
            params={"new_status": new_status},
            headers=headers,
        )
