import json
from pathlib import Path

import pytest
from jsonschema import validate


pytestmark = pytest.mark.orders


def test_create_order_returns_created_order(api_client, auth_headers, test_data):
    response = api_client.create_order(test_data["valid_order"], headers=auth_headers)

    assert response.status_code == 201
    body = response.json()
    assert body["customer"] == test_data["valid_order"]["customer"]
    assert body["product_id"] == test_data["valid_order"]["product_id"]
    assert body["quantity"] == test_data["valid_order"]["quantity"]
    assert body["status"] == "created"
    assert "id" in body
    assert "created_at" in body


@pytest.mark.parametrize(
    "payload, expected_field",
    [
        ({"customer": "A", "product_id": 1, "quantity": 1}, "customer"),
        ({"customer": "Robert Joyce", "product_id": 1, "quantity": 0}, "quantity"),
        ({"customer": "Robert Joyce", "product_id": 1, "quantity": 101}, "quantity"),
    ],
)
def test_create_order_rejects_invalid_payloads(api_client, auth_headers, payload, expected_field):
    response = api_client.create_order(payload, headers=auth_headers)

    assert response.status_code == 422
    assert expected_field in str(response.json()["detail"])


def test_create_order_rejects_out_of_stock_product(api_client, auth_headers, test_data):
    response = api_client.create_order(test_data["out_of_stock_order"], headers=auth_headers)

    assert response.status_code == 409
    assert response.json()["detail"] == "Product is out of stock"


def test_order_status_can_be_updated_and_filtered(api_client, auth_headers, test_data):
    created = api_client.create_order(test_data["valid_order"], headers=auth_headers).json()
    api_client.create_order(test_data["second_order"], headers=auth_headers)

    paid_response = api_client.update_order_status(created["id"], "paid", headers=auth_headers)
    filtered_response = api_client.list_orders(auth_headers, status="paid")

    assert paid_response.status_code == 200
    assert paid_response.json()["status"] == "paid"
    assert [order["id"] for order in filtered_response.json()] == [created["id"]]


def test_unknown_order_returns_404(api_client, auth_headers):
    response = api_client.get_order("00000000-0000-0000-0000-000000000000", headers=auth_headers)

    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"


@pytest.mark.schema
def test_order_response_matches_schema(api_client, auth_headers, test_data):
    schema_path = Path(__file__).parent / "schemas" / "order.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))

    response = api_client.create_order(test_data["valid_order"], headers=auth_headers)

    assert response.status_code == 201
    validate(instance=response.json(), schema=schema)
