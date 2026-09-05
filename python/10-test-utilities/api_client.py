from __future__ import annotations

from typing import Any

import httpx


class ApiClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    def get(self, path: str, **kwargs: Any) -> httpx.Response:
        return httpx.get(f"{self.base_url}{path}", **kwargs)

    def post(self, path: str, json: dict[str, Any], **kwargs: Any) -> httpx.Response:
        return httpx.post(f"{self.base_url}{path}", json=json, **kwargs)
